FROM raspbian/stretch

ENV LANG C.UTF-8

RUN mkdir /sdomotica
COPY sdomotica /sdomotica
COPY config_default.json /sdomotica
COPY sdomotica_js.cfg /sdomotica
#COPY sdomotica_js.cfg /data

RUN chmod a+x /sdomotica/sdomotica
#WORKDIR /sdomotica

#-- Logs and config information go into the volume on /data
#VOLUME /data
VOLUME /sdomotica

#-- OpenSprinkler interface is available on 8080
EXPOSE 3100 3000 3300

CMD [ "./sdomotica/sdomotica" ]
