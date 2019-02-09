"""Support for MyHome Audio Settopboxes."""
import asyncio
import logging
from datetime import timedelta
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
import voluptuous as vol
import time

import requests

from homeassistant.util import Throttle
from homeassistant.components.media_player import (
    SUPPORT_SELECT_SOURCE, MediaPlayerDevice, PLATFORM_SCHEMA,
    SUPPORT_PREVIOUS_TRACK, SUPPORT_TURN_OFF, SUPPORT_TURN_ON,
    SUPPORT_VOLUME_STEP, MEDIA_TYPE_MUSIC,
    SUPPORT_NEXT_TRACK, SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET)
from homeassistant.const import (
    CONF_HOST, STATE_OFF, STATE_ON, STATE_UNKNOWN, CONF_NAME, CONF_PORT,
    CONF_USERNAME, CONF_PASSWORD, CONF_TIMEOUT, CONF_ADDRESS)
import homeassistant.helpers.config_validation as cv

#REQUIREMENTS = ['beautifulsoup4==4.6.0']

# Return cached results if last scan was less then this time ago.
MIN_TIME_BETWEEN_SCANS = timedelta(seconds=10)

DEFAULT_HOST = '127.0.0.1'
DEFAULT_NAME = 'BTicino Sound'
DEFAULT_PORT = '3000'
DEFAULT_TIMEOUT = None
DEFAULT_USERNAME = 'root'
DEFAULT_PASSWORD = 'dreambox'
DEFAULT_ADDRESS = '11'
DEFAULT_SOURCEA = 'Source 1'
DEFAULT_SOURCEB = 'Source 2'
DEFAULT_SOURCEC = 'Source 3'
DEFAULT_SOURCED = 'Source 4'
DEFAULT_RADIO = '1'



_LOGGER = logging.getLogger(__name__)

SUPPORT_MYHOMEAUDIO = SUPPORT_VOLUME_SET |  \
                 SUPPORT_PREVIOUS_TRACK | SUPPORT_NEXT_TRACK | \
                 SUPPORT_TURN_ON | SUPPORT_TURN_OFF | \
                 SUPPORT_SELECT_SOURCE | SUPPORT_VOLUME_STEP

MAX_VOLUME = 31

CONF_SOURCEA = 'source1'
CONF_SOURCEB = 'source2'
CONF_SOURCEC = 'source3'
CONF_SOURCED = 'source4'
CONF_RADIO = 'radio'


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST, default=DEFAULT_HOST): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_USERNAME, default=DEFAULT_USERNAME): cv.string,
    vol.Optional(CONF_PASSWORD, default=DEFAULT_PASSWORD): cv.string,
    vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.string,
    vol.Optional(CONF_TIMEOUT, default=DEFAULT_TIMEOUT): cv.socket_timeout,
    vol.Optional(CONF_ADDRESS, default=DEFAULT_ADDRESS): cv.string,
    vol.Optional(CONF_SOURCEA, default=DEFAULT_SOURCEA): cv.string,
    vol.Optional(CONF_SOURCEB, default=DEFAULT_SOURCEB): cv.string,
    vol.Optional(CONF_SOURCEC, default=DEFAULT_SOURCEC): cv.string,
    vol.Optional(CONF_SOURCED, default=DEFAULT_SOURCED): cv.string,
    vol.Optional(CONF_RADIO, default=DEFAULT_RADIO): cv.string,
    
})

@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    """Setup the MyHome Audio platform."""
    myhomeaudio = MyHomeAudio(config.get(CONF_NAME),
                          config.get(CONF_HOST),
                          config.get(CONF_PORT),
                          config.get(CONF_USERNAME),
                          config.get(CONF_PASSWORD),
                          config.get(CONF_TIMEOUT),
                          config.get(CONF_ADDRESS),
                          config.get(CONF_SOURCEA),
                          config.get(CONF_SOURCEB),
                          config.get(CONF_SOURCEC),
                          config.get(CONF_SOURCED),
                          config.get(CONF_RADIO))
                          
    if myhomeaudio.update():
        async_add_devices([myhomeaudio])
        return True
    return False


class MyHomeAudio(MediaPlayerDevice):
    """Representation of a MyHome Audio device."""

    def __init__(self, name, host, port, username, password, timeout, address, sourcea , sourceb , sourcec , sourced, radio ):
        """Initialize the MyHome Audio device."""
        self._name = name
        self._host = host
        self._port = port
        self._address = address
        self._username = username
        self._password = password
        self._timeout = timeout
        self._pwstate = True
        self._volume = 0
        self._muted = False
        self._selected_source = ''
        self._radio = int(radio)
        self._currentsong = ''
        #self._source_names = {}
        self._source_names = [sourcea, sourceb, sourcec,sourced]        
        self._sources = {}
        if self._password != DEFAULT_PASSWORD:
            self.handle_base_auth()
        #self.load_sources()

    def handle_base_auth(self):
        """Handle HTTP Auth."""
        mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        mgr.add_password(None, self._host, self._username, self._password)
        handler = urllib.request.HTTPBasicAuthHandler(mgr)
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)

    def request_call(self, url):
        """Call web API request."""
        uri = 'http://' + self._host + ':' + self._port +  url
        try:
            return urllib.request.urlopen(uri, timeout=10).read().decode('UTF8')
        except (HTTPError, URLError, ConnectionRefusedError):
            return False
            
    def send_rest_msg(self, Command):
        """Send message."""
        try:
            url = "http://{}:{}{}".format(self._host, self._port, Command)    
            response = requests.get(url).text
            #print(response)    
            return response
        except AttributeError:
            print(response)
            return False

    def async_ask_volume(self):
        """Select input source."""
        time.sleep(1)
        response = self.send_rest_msg('/status/volume/' + self._address )
        if response :
            self._volume = int(response) / MAX_VOLUME if response else None

    def async_ask_power(self):
        """Select input source."""
        time.sleep(1)
        response = self.send_rest_msg('/status/audio/' + self._address )
        if response == '0':
            self._pwstate = 'true'
        else:
            self._pwstate = 'false'
            self.async_ask_source()

    def async_ask_source(self):
        """Select input source."""
        time.sleep(2)
        response = self.send_rest_msg('/status/source/' + self._address )
        if response :
            if int(response) == self._radio:
                frequence = self.send_rest_msg('/status/radio/frequenza/1')
                rds = self.send_rest_msg('/status/radio/rds/1')
                self._currentsong = (frequence + " " + rds)
                self._selected_source = (self._source_names[int(response)-1]) if response else None
            else:
                self._currentsong = ('')
                self._selected_source = (self._source_names[int(response)-1]) if response else None

            
    @Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self):
        """Recupera se acceso o meno"""
        self._pwstate = 'false'
        response = self.send_rest_msg('/status/audio/' + self._address )
        if response == '0':
            self._pwstate = 'true'         
        else:
            self._pwstate = 'false'       


        sources = ['1','2','3','4']
        self._sources = dict(zip(self._source_names, sources))


        if self._name == 'BTicino Sound':
            name = 'BTicino Sound Ampli: ' + self._address
            if name:
                self._name = name


        if self._pwstate == 'false':
            #volcurrent = '85'
            response = self.send_rest_msg('/status/volume/' + self._address )
            if response :
                self._volume = int(response) / MAX_VOLUME if response else None
            #self._volume = int(volcurrent) / MAX_VOLUME if volcurrent else None
            
            volmuted = 'False'
            self._muted = (volmuted == 'True') if volmuted else None

            response = self.send_rest_msg('/status/source/' + self._address )
            if response :
            #self._selected_source = ('Source 1')
                if int(response) == self._radio:
                   frequence = self.send_rest_msg('/status/radio/frequenza/1')
                   rds = self.send_rest_msg('/status/radio/rds/1')
                   self._currentsong = (frequence + " " + rds)
                   self._selected_source = (self._source_names[int(response)-1]) if response else None
                else:
                   self._currentsong = ('')
                   self._selected_source = (self._source_names[int(response)-1]) if response else None

            
            
            

        return True

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def media_content_type(self):
        """Content type of current playing media."""
        return MEDIA_TYPE_MUSIC
        
    @property
    def state(self):
        """Return the state of the device."""
        if self._pwstate == 'true':
            return STATE_OFF
        if self._pwstate == 'false':
            return STATE_ON

        return STATE_UNKNOWN
    


    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._volume

    @property
    def is_volume_muted(self):
        """Boolean if volume is currently muted."""
        return self._muted

    @property
    def supported_features(self):
        """Flag of media commands that are supported."""
        return SUPPORT_MYHOMEAUDIO

    @property
    def media_title(self):
        """Title of current playing media."""
        return self._selected_source

    @property
    def media_artist(self):
        """Title of current playing media."""
        return self._currentsong
        
    @property
    def source(self):
        """Return the current input source."""
        return self._selected_source

    @property
    def source_list(self):
        """List of available input sources."""
        return self._source_names
             
        
    @asyncio.coroutine
    def async_select_source(self, source):
        """Select input source."""
        _LOGGER.error(source)
        _LOGGER.error(self._sources[source])
        self.request_call('/source/' + self._address + '/' + self._sources[source])
        self.async_ask_source()


    @asyncio.coroutine
    def async_media_next_track(self):
        """Send next track command """
        #if int(response) == self._radio:
        self.request_call('/station/' + str(self._radio) +  '/up')
        self.async_ask_source()

    @asyncio.coroutine
    def async_media_previous_track(self):
        self.request_call('/station/' + str(self._radio) + '/down')
        self.async_ask_source()
        
    @asyncio.coroutine
    def async_set_volume_level(self, volume):
        """Set volume level, range 0..1."""
        volset = str(round(volume * MAX_VOLUME))
        response = self.send_rest_msg('/volume/' + self._address + '/' + volset )
        if response :
            self._volume = int(response) / MAX_VOLUME if response else None

    
    @asyncio.coroutine
    def volume_up(self):
        """Service to send the MPD the command for volume up."""
        self.request_call('/vol/' + self._address + '/up')
        self.async_ask_volume()

    
    @asyncio.coroutine
    def volume_down(self):
        """Service to send the MPD the command for volume down."""
        self.request_call('/vol/' + self._address + '/down')
        self.async_ask_volume()
        
    @asyncio.coroutine
    def async_mute_volume(self, mute):
        """Mute or unmute media player."""
        #self.request_call('/web/vol?set=mute')
        print ("Mute")
    
    @asyncio.coroutine
    def async_turn_on(self):
        """Turn the media player on.""" 
        self.request_call('/audio/' + self._address + '/1')
        self.async_ask_power()

    @asyncio.coroutine
    def async_turn_off(self):
        """Turn off media player."""
        self.request_call('/audio/' + self._address + '/0')
        self.async_ask_power()
