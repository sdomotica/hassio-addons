#!/usr/bin/with-contenv bashio

echo "====================================================="
echo " Avvio di OpenSprinkler (Pre-compilato Debian 64-bit)"
echo " Client MQTT integrato e pronto."
echo "====================================================="

# -d indica la cartella dei dati di configurazione (/data è persistente in HassOS)
# -s indica la cartella dei file statici web (se integrati nell'eseguibile, altrimenti punta a /app)
exec /app/OpenSprinkler -d /data
