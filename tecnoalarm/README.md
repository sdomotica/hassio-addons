# Sdomotica Gateway per Tecnoalarm

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

![Banner1][banner1]


# Integra il tuo sistema Tecnoalarm in Home Assistant


## Tecnoalarm

Tecnoalarm rappresenta da decenni un punto di riferimento nel panorama della sicurezza antintrusione italiana, con una gamma di centrali che coprono dalle piccole installazioni residenziali fino ai sistemi di grandi dimensioni. Le centrali della serie TP ed EV offrono funzionalità avanzate di gestione degli allarmi, automazione e integrazione con sistemi esterni.

La serie **TP (Top Performance)** include modelli come TP8-88 PLUS e TP20-440, progettati per installazioni che richiedono un'elevata capacità di gestione di zone e programmi. Queste centrali supportano espansioni modulari e dispongono di funzionalità avanzate come la gestione di programmi multipli, l'esclusione selettiva delle zone e la gestione di uscite telecomando.

La serie **EV (Evolution)** comprende modelli come EV 10-50 ed EV 12-150, che rappresentano l'evoluzione tecnologica delle centrali Tecnoalarm. Il modello EV 10-50 è una centrale ibrida espandibile da 10 a 50 zone, con comunicazione IP e 4G LTE integrata, tecnologie RDV® e RSC®, e gestione fino a 122 codici di accesso. La EV 12-150 estende queste capacità fino a 150 zone per installazioni di dimensioni maggiori.

Tutte le centrali supportate offrono il **protocollo Tecno Out**, un protocollo di comunicazione proprietario che consente l'integrazione con sistemi di supervisione esterni. La sicurezza delle comunicazioni è garantita dall'utilizzo di crittografia AES a 128 bit.

## Tecno Out

Il protocollo **Tecno Out** è il sistema di comunicazione proprietario Tecnoalarm che consente l'integrazione delle centrali con sistemi terzi. La sua attivazione richiede una **licenza opzionale** da richiedere al distributore Tecnoalarm, e il codice di abilitazione deve essere inserito tramite tastierino nella centrale.

La configurazione del protocollo Tecno Out avviene tramite il software **Tecnoalarm Centro** e prevede:
- Abilitazione della modalità **SERVER**
- Configurazione della porta di comunicazione (default: 10005)
- Impostazione di una **passphrase** di 16 caratteri (solo lettere e numeri) che funge da base per la crittografia AES a 128 bit
- Possibilità di limitare le connessioni tramite **whitelist** degli indirizzi IP autorizzati

Il programma **TecnoOut Monitor** versione 4.2, fornito da Tecnoalarm, permette di verificare la corretta comunicazione con la centrale, mostrando in tempo reale lo stato delle zone e dei programmi.

Le funzionalità principali rese disponibili dal protocollo Tecno Out includono:
- Visualizzazione dello stato delle zone in tempo reale
- Inserimento e disinserimento dei programmi definiti nella centrale
- Esclusione mirata di singole zone
- Gestione delle uscite di tipo telecomando
- Lettura del log eventi della centrale

## Compatibilità

| Modello | Versione Firmware Minima |
|---------|--------------------------|
| TP8-88 PLUS | 2.1.06 o superiore |
| TP20-440 | 2.1.06 o superiore |
| EV 10-50 | 1.2.04 o superiore |
| EV 12-150 | 1.0.00 o superiore |

## Note sull'installazione

1. Richiedere il **codice di abilitazione Tecno Out** al proprio distributore Tecnoalarm
2. Inserire il codice tramite tastierino nella centrale (menu "Opzioni > Abilitazioni")
3. Configurare il protocollo Tecno Out in modalità SERVER con porta **10005** e passphrase di 16 caratteri
4. Verificare la comunicazione con il programma **TecnoOut Monitor 4.2**
5. Gli attributi e i permessi descritti nella lista valgono per le centrali TP8-88 con Release 2.4.08 e EV10-50/12-150 con release 2.0

---

# Sdomotica Gateway for Tecnoalarm

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

![Banner1][banner1]


# Integrate your Tecnoalarm System into Home Assistant


## Tecnoalarm

Tecnoalarm has been a reference point in the Italian intrusion protection landscape for decades, offering a range of control panels that cover everything from small residential installations to large-scale systems. The TP and EV series panels provide advanced alarm management, automation, and integration capabilities with external systems.

The **TP (Top Performance)** series includes models such as TP8-88 PLUS and TP20-440, designed for installations requiring high capacity for managing zones and programs. These panels support modular expansions and feature advanced functionality including multiple program management, selective zone exclusion, and remote control output management.

The **EV (Evolution)** series comprises models such as EV 10-50 and EV 12-150, representing the technological evolution of Tecnoalarm panels. The EV 10-50 is a hybrid panel expandable from 10 to 50 zones, with integrated IP and 4G LTE communication, RDV® and RSC® technologies, and management of up to 122 access codes. The EV 12-150 extends these capabilities up to 150 zones for larger installations.

All supported panels offer the **Tecno Out** protocol, a proprietary communication protocol that enables integration with external supervision systems. Communication security is ensured through the use of AES 128-bit encryption.

## Tecno Out

The **Tecno Out** protocol is Tecnoalarm's proprietary communication system that enables panel integration with third-party systems. Its activation requires an **optional license** to be requested from the Tecnoalarm distributor, and the activation code must be entered via keypad on the panel.

Tecno Out protocol configuration is performed through **Tecnoalarm Centro** software and includes:
- Enabling **SERVER** mode
- Configuring the communication port (default: 10005)
- Setting a **passphrase** of 16 characters (letters and numbers only) that serves as the basis for AES 128-bit encryption
- Option to restrict connections via **whitelist** of authorized IP addresses

The **TecnoOut Monitor** version 4.2 program, provided by Tecnoalarm, allows verification of correct communication with the panel, showing real-time status of zones and programs.

The main functionalities made available by the Tecno Out protocol include:
- Real-time zone status visualization
- Arming and disarming of programs defined in the panel
- Targeted exclusion of individual zones
- Management of remote control type outputs
- Reading the panel event log

## Compatibility

| Model | Minimum Firmware Version |
|---------|--------------------------|
| TP8-88 PLUS | 2.1.06 or higher |
| TP20-440 | 2.1.06 or higher |
| EV 10-50 | 1.2.04 or higher |
| EV 12-150 | 1.0.00 or higher |

## Installation Notes

1. Request the **Tecno Out activation code** from your Tecnoalarm distributor
2. Enter the code via keypad on the panel (menu "Options > Enabling")
3. Configure the Tecno Out protocol in SERVER mode with port **10005** and a 16-character passphrase
4. Verify communication with the **TecnoOut Monitor 4.2** program
5. The attributes and permissions described in the list apply to TP8-88 panels with Release 2.4.08 and EV10-50/12-150 with release 2.0

## License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-no-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-no-green.svg
[banner1]: http://www.sdomotica.com/gateway2/tecnoalarmbanner.png