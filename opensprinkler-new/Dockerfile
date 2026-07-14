ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base-debian:trixie
FROM $BUILD_FROM

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

# Libreria lgpio: file reale copiato dal sistema di build (non esiste nei repo Debian)
COPY liblgpio.so.1 /usr/lib/aarch64-linux-gnu/liblgpio.so.1
RUN ldconfig

COPY OpenSprinkler /app/OpenSprinkler
RUN chmod a+x /app/OpenSprinkler

RUN if ldd /app/OpenSprinkler | grep "not found"; then \
        echo "ERRORE: librerie mancanti nel container" && exit 1; \
    fi

COPY run.sh /app/run.sh
RUN chmod a+x /app/run.sh

RUN mkdir -p /data

CMD [ "/app/run.sh" ]