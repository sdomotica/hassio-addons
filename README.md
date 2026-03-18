# Sdomotica Add-ons for Home Assistant

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatible-brightgreen.svg)](https://www.home-assistant.io/)
[![Stars](https://img.shields.io/github/stars/sdomotica/hassio-addons?style=social)](https://github.com/sdomotica/hassio-addons/stargazers)

> A collection of Home Assistant add-ons to integrate Italian home automation and security systems — BTicino MyHome, Inim, Ksenia, Netatmo, Smarther and more.

---

## 📦 Available Add-ons

### 🏠 BTicino MyHome SCS — Home Automation

| Add-on | Description |
|--------|-------------|
| **bticino2021** | Integrates the **BTicino MyHome SCS** bus home automation system into Home Assistant. Supports lights, shutters, thermostats, energy monitoring and scenarios via the OpenWebNet protocol. Compatible with gateways F454, MH200, MH201 and similar. |
| **bticino20212** | Updated version of the BTicino MyHome integration, with improvements and support for newer gateway firmware versions. |
| **f460** | Dedicated integration for the **BTicino F460 server** — the main SCS DIN server supporting up to 525 devices. Enables full control of the MyHome system including lighting, shutters, climate and energy management. |

---

### 🚨 Security & Alarm Systems

| Add-on | Description |
|--------|-------------|
| **bticinoalarm** | Integrates the **BTicino MyHome alarm system** into Home Assistant. Allows arming/disarming partitions, monitoring zones and receiving real-time alarm events. |
| **ksenia40** | Integration for **Ksenia Lares 4.0** — the Italian all-in-one security and home automation control panel. Supports arming/disarming, zone monitoring, outputs control and home automation scenarios. |
| **kseniaip** | Integration for **Ksenia LaresIP** (pre-4.0 series, e.g. Lares 48IP). Connects via the local web interface to monitor zones and partitions and control the alarm system. Compatible with BTicino alarm systems. |
| **ksenia40BTicino** | Combined integration for Ksenia alarm systems used alongside BTicino installations. Bridges Ksenia security events with BTicino home automation in a unified Home Assistant environment. |
| **inim** | Integrates the **Inim Prime** alarm control panel via the **PrimeLAN** Ethernet board. Supports zone monitoring, partition arming/disarming, event log and real-time status — all directly in Home Assistant. |

---

### 🌡️ Climate & Smart Thermostat

| Add-on | Description |
|--------|-------------|
| **smarther** | Integrates the **BTicino Smarther X8000 (Gen 1)** connected thermostat into Home Assistant. Provides temperature monitoring, setpoint control and scheduling via the Legrand/BTicino cloud API. |
| **netatmo** | Integrates **BTicino Living Now Zigbee** devices and the **Smarther2** (Netatmo-based) connected thermostat. Bridges the Netatmo ecosystem with Home Assistant for climate control and energy management. |

---

### 💧 Irrigation

| Add-on | Description |
|--------|-------------|
| **opensprinkler** | Allows use of the **OpenSprinkler** irrigation software together with **BTicino SCS actuators**. Combines OpenSprinkler's scheduling engine with the BTicino bus to control irrigation zones via the existing SCS wiring. |

---

### 🌐 Other Integrations

| Add-on | Description |
|--------|-------------|
| **telegea** | Integrates the **Telegea** energy monitoring and management server into Home Assistant. Enables visualization and control of energy data from Telegea-connected installations. |

---

## 📖 Documentation

A full installation and configuration manual is available in the repository:

📄 [Hassio_Sdomotica_manual.pdf](https://github.com/sdomotica/hassio-addons/blob/master/Hassio_Sdomotica_manual.pdf)

---

## 🚀 Installation

1. Open Home Assistant and go to **Settings → Add-ons → Add-on Store**
2. Click the menu (⋮) in the top right and select **Repositories**
3. Add the following URL:
   ```
   https://github.com/sdomotica/hassio-addons
   ```
4. Find the desired add-on in the store and click **Install**

---

## 🔧 Supported Hardware

- BTicino / Legrand MyHome SCS gateways (F454, MH200, MH201, MH202, F460, F461)
- BTicino alarm systems
- Inim Prime control panels (with PrimeLAN board)
- Ksenia Lares 4.0 and LaresIP (48IP) control panels
- BTicino Smarther X8000 thermostat
- BTicino Living Now Zigbee / Smarther2 (Netatmo)
- OpenSprinkler with BTicino SCS actuators
- Telegea energy server

---

## 🤝 Contributing

Issues and pull requests are welcome. If you have a BTicino, Inim or Ksenia installation and want to help improve these integrations, feel free to open an issue or submit a PR.

---

## 📝 License

This project is licensed under the MIT License.

---

*Made with ❤️ in Italy — [sdomotica.com](http://www.sdomotica.com)*
