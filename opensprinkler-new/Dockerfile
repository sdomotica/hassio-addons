ARG BUILD_FROM=homeassistant/aarch64-base-debian:bookworm
FROM $BUILD_FROM

# Installazione di tutte le dipendenze hardware, strumenti gpiod e client MQTT
RUN apt-get update && apt-get install -y --no-install-recommends \
    libstdc++6 \
    libc6 \
    ca-certificates \
    mosquitto-clients \
    libi2c0 \
    libmodbus5 \
    libgpiod2 \
    gpiod \
    && rm -rf /var/lib/apt/lists/*



# Configurazione della cartella interna dell'applicazione
WORKDIR /app

# Copia il file che hai compilato sul Raspberry dentro il container
COPY OpenSprinkler /app/OpenSprinkler
RUN chmod a+x /app/OpenSprinkler

# Copia lo script di avvio dell'add-on
COPY run.sh /app/run.sh
RUN chmod a+x /app/run.sh

CMD [ "/app/run.sh" ]