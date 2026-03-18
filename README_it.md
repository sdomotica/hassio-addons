# Sdomotica Add-on per Home Assistant

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatibile-brightgreen.svg)](https://www.home-assistant.io/)
[![Stars](https://img.shields.io/github/stars/sdomotica/hassio-addons?style=social)](https://github.com/sdomotica/hassio-addons/stargazers)

> Una raccolta di add-on per Home Assistant per integrare i principali sistemi domotici e di sicurezza italiani — BTicino MyHome, Inim, Ksenia, Netatmo, Smarther e molto altro.

---

## 📦 Add-on Disponibili

### 🏠 BTicino MyHome SCS — Domotica

| Add-on | Descrizione |
|--------|-------------|
| **bticino2021** | Integra il sistema domotico **BTicino MyHome SCS** bus in Home Assistant. Supporta luci, tapparelle, termostati, monitoraggio energetico e scenari tramite il protocollo OpenWebNet. Compatibile con i gateway F454, MH200, MH201 e similari. |
| **bticino20212** | Versione aggiornata dell'integrazione BTicino MyHome, con miglioramenti e supporto per le versioni firmware più recenti dei gateway. |
| **f460** | Integrazione dedicata per il **server BTicino F460** — il server SCS DIN principale che supporta fino a 525 dispositivi. Permette il controllo completo del sistema MyHome: luci, tapparelle, climatizzazione e gestione energetica. |

---

### 🚨 Sistemi di Sicurezza e Allarme

| Add-on | Descrizione |
|--------|-------------|
| **bticinoalarm** | Integra il **sistema di allarme BTicino MyHome** in Home Assistant. Permette l'inserimento/disinserimento delle partizioni, il monitoraggio delle zone e la ricezione in tempo reale degli eventi di allarme. |
| **ksenia40** | Integrazione per **Ksenia Lares 4.0** — la centrale di sicurezza e domotica italiana all-in-one. Supporta inserimento/disinserimento, monitoraggio zone, controllo uscite e scenari domotici. |
| **kseniaip** | Integrazione per **Ksenia LaresIP** (serie pre-4.0, es. Lares 48IP). Si connette tramite l'interfaccia web locale per monitorare zone e partizioni e controllare il sistema di allarme. Compatibile con i sistemi di allarme BTicino. |
| **ksenia40BTicino** | Integrazione combinata per sistemi Ksenia utilizzati insieme a installazioni BTicino. Unifica gli eventi di sicurezza Ksenia con la domotica BTicino in un unico ambiente Home Assistant. |
| **inim** | Integra la **centrale di allarme Inim Prime** tramite la scheda Ethernet **PrimeLAN**. Supporta monitoraggio zone, inserimento/disinserimento partizioni, registro eventi e stato in tempo reale — direttamente in Home Assistant. |

---

### 🌡️ Climatizzazione e Termostati Smart

| Add-on | Descrizione |
|--------|-------------|
| **smarther** | Integra il **termostato connesso BTicino Smarther X8000 (Gen 1)** in Home Assistant. Fornisce monitoraggio della temperatura, controllo del setpoint e programmazione oraria tramite le API cloud Legrand/BTicino. |
| **netatmo** | Integra i dispositivi **BTicino Living Now Zigbee** e il termostato connesso **Smarther2** (basato su Netatmo). Collega l'ecosistema Netatmo con Home Assistant per il controllo climatico e la gestione energetica. |

---

### 💧 Irrigazione

| Add-on | Descrizione |
|--------|-------------|
| **opensprinkler** | Permette di utilizzare il software di irrigazione **OpenSprinkler** insieme agli **attuatori SCS BTicino**. Combina il motore di schedulazione di OpenSprinkler con il bus BTicino per controllare le zone di irrigazione tramite il cablaggio SCS esistente. |

---

### 🌐 Altre Integrazioni

| Add-on | Descrizione |
|--------|-------------|
| **telegea** | Integra il server di monitoraggio e gestione energetica **Telegea** in Home Assistant. Permette la visualizzazione e il controllo dei dati energetici delle installazioni Telegea. |

---

## 📖 Documentazione

Il manuale completo di installazione e configurazione è disponibile nel repository:

📄 [Hassio_Sdomotica_manual.pdf](https://github.com/sdomotica/hassio-addons/blob/master/Hassio_Sdomotica_manual.pdf)

---

## 🚀 Installazione

1. Apri Home Assistant e vai su **Impostazioni → Add-on → Store Add-on**
2. Clicca il menu (⋮) in alto a destra e seleziona **Repository**
3. Aggiungi il seguente URL:
   ```
   https://github.com/sdomotica/hassio-addons
   ```
4. Trova l'add-on desiderato nello store e clicca **Installa**

---

## 🔧 Hardware Supportato

- Gateway BTicino / Legrand MyHome SCS (F454, MH200, MH201, MH202, F460, F461)
- Sistemi di allarme BTicino
- Centrali di allarme Inim Prime (con scheda PrimeLAN)
- Centrali Ksenia Lares 4.0 e LaresIP (48IP)
- Termostato BTicino Smarther X8000
- BTicino Living Now Zigbee / Smarther2 (Netatmo)
- OpenSprinkler con attuatori BTicino SCS
- Server energetico Telegea

---

## 🤝 Contribuire

Segnalazioni e pull request sono benvenute. Se hai un'installazione BTicino, Inim o Ksenia e vuoi contribuire a migliorare queste integrazioni, apri pure una issue o invia una PR.

---

## 📝 Licenza

Questo progetto è distribuito sotto licenza MIT.

---

*Fatto con ❤️ in Italia — [sdomotica.com](http://www.sdomotica.com)*
