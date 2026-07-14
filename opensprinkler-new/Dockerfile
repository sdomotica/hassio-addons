ARG BUILD_FROM=homeassistant/aarch64-base-debian:bookworm
FROM $BUILD_FROM
# Installazione dipendenze
RUN apt-get update && apt-get install -y --no-install-recommends \
    libstdc++6 \
    libc6 \
    ca-certificates \
    mosquitto-clients \
    libi2c0 \
    libmodbus5 \
    libbluetooth3 \
    libgpiod2 \
    gpiod \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
# Copia l'eseguibile e gli script
COPY OpenSprinkler /app/OpenSprinkler
RUN chmod a+x /app/OpenSprinkler
# Verifica che tutte le librerie dinamiche siano risolte: se manca qualcosa la build fallisce
RUN if ldd /app/OpenSprinkler | grep "not found"; then \
        echo "ERRORE: librerie mancanti nel container" && exit 1; \
    fi
COPY run.sh /app/run.sh
RUN chmod a+x /app/run.sh
# Assicuriamoci che la directory /data sia pronta (verrà poi sovrascritta dal mount di HassOS)
RUN mkdir -p /data
CMD [ "/app/run.sh" ]
