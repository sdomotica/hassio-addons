ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base-debian:trixie
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
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Libreria lgpio copiata dal sistema di build (non disponibile nei repo Debian)
COPY liblgpio.so.1* /usr/lib/aarch64-linux-gnu/
RUN ldconfig

# Copia l'eseguibile e gli script
COPY OpenSprinklerDE /app/OpenSprinklerDE
RUN chmod a+x /app/OpenSprinklerDE

# Verifica che tutte le librerie dinamiche siano risolte: se manca qualcosa la build fallisce
RUN if ldd /app/OpenSprinklerDE | grep "not found"; then \
        echo "ERRORE: librerie mancanti nel container" && exit 1; \
    fi

COPY run.sh /app/run.sh
RUN chmod a+x /app/run.sh

# Assicuriamoci che la directory /data sia pronta (verrà poi sovrascritta dal mount di HassOS)
RUN mkdir -p /data

CMD [ "/app/run.sh" ]