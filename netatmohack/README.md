# Sdomotica Classe 300EOS e 100X (Home + Security)

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

## 🔑 Apertura Cancelletto e Porte
Controlla direttamente da Home Assistant l'apertura dei cancelli e delle porte del tuo impianto videocitofonico con un semplice comando.

## 💡 Accensione Luci Scale
Attiva e disattiva l'illuminazione delle scale e delle aree comuni direttamente dall'interfaccia di Home Assistant.

## 📋 Visione di tutti gli ultimi eventi memorizzati
Visualizza cronologia completa degli eventi con:
- **Immagine** dell'evento
- **Data e ora** precisa
- **Messaggio evento** dettagliato

## 📞 Avviso tramite popup della chiamata in arrivo
Ricevi notifiche in tempo reale con **popup** che mostrano lo **screenshot del post esterno** quando qualcuno suona al tuo citofono.

### Integra i tuoi videocitofoni BTicino Class 300EOS e Class 100X in Home Assistant

![Scs5][scs5]

![Scs4][scs4]


## Descrizione del Progetto

Questo componente nasce da un'attività di **reverse engineering** della connessione utilizzata dall'applicazione ufficiale **Home + Security** di Netatmo / Legrand / BTicino, allo scopo di consentire l'integrazione dei videocitofoni **Class 300EOS** e **Class 100X** all'interno dell'ecosistema **Home Assistant**.

L'integrazione espone le funzioni del vostro impianto videocitofonico tramite servizi MQTT.

> ⚠️ **AVVERTENZA IMPORTANTE E LIMITAZIONI:**
> - Trattandosi di un'integrazione basata su reverse engineering della connessione e non su API/SDK ufficiali documentate per questi specifici dispositivi, il **supporto è limitato** e **non viene garantito il corretto funzionamento continuativo**.
> - L'uso di questo componente **potrebbe comportare malfunzionamenti o problemi sull'impianto videocitofonico** e sulla gestione delle chiamate.
> - L'utilizzo è a proprio rischio e pericolo.

---

## Consigliato: Utilizzare un Account Dedicato

L'API cloud di BTicino / Netatmo applica rigide limitazioni sul numero di sessioni e connessioni contemporanee. Se si utilizza lo **stesso account** sia sull'app mobile **Home + Security** che all'interno di **Home Assistant**, si potrebbero riscontrare i seguenti problemi:

- **Disconnessioni frequenti del WebSocket**
- **Notifiche in ritardo o perse** (es. avviso di chiamata citofonica)
- **Errori di API intermittenti o blocchi temporanei della sessione**

Si consiglia vivamente di creare e utilizzare un **account secondario/dedicato** da associare all'integrazione Home Assistant.

---

## Documentazione e Configurazione

Qui [il manuale][manuale] per configurare l'addon.

---

## Licenza

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
[manuale]: http://www.sdomotica.com/gateway2/Addon_Sdomotica_Netatmo.pdf
[webinterface]: http://www.sdomotica.com/gateway2/scswebinterface.png
[scs4]: http://www.sdomotica.com/gateway2/netatmo4.png
[scs5]: http://www.sdomotica.com/gateway2/netatmo5.png