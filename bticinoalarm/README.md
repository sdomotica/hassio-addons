# Sdomotica Gateway for BTicino Alarm 4200/4201/4202

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

![Tastierino][tastiera]

Integrate your BTicino Alarm alarm system into Home Assistant

![WebInterface][webinterface]

## English
Sdomotica is a gateway using no official API to integrate BTicino alarm
system to Home Assistant.

The integration expose as mqtt services all the alarm functions as
zones, partitions, scenarios, arm and disarm.

This addon could decrease the security level of your alarm system.

For this reason you have to sign to Sdomotica a specific disclaimer and
discharge before use it.

Here the [manual][manuale] for configure the addon

## Italiano
Sdomotica è un gateway che utilizza API non ufficiali per integrare la
centrale di allarme di BTicino a Home Assistant.

L'integrazione espone come servizi mqtt tutte le funzioni della centrale
dall'allarme come zone, partizioni, scenari, inserimenti e
disinserimenti.

Questo addon riduce il livello di sicurezza del vostro sistema di
allarme.

Per questo motivo per utilizzare l'addon dovete firmare una informativa
e scarico di responsabilità prima di utilizarlo

Qui [il manuale][manuale] per configurare l'addon.


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
[manuale]: http://www.sdomotica.com/gateway2/KseniaIP_Sdomotica.pdf
[webinterface]: http://www.sdomotica.com/gateway2/kseniaipweb.png
[tastiera]: http://www.sdomotica.com/gateway2/kseniatastierino.png
