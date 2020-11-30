@title = "Ändern der MAC-Adresse"

Diese Anleitung zeigt, wie Du bei jeder neuen Verbindung eine neue MAC-Adresse generierst.

h1. Was ist eine MAC-Adresse?

Eine [[MAC (Media Access Control, Medienzugriffskontroll) -Adresse->https://en.wikipedia.org/wiki/Mac_address]] ist eine einmalige Adresse, die in allen Netzwerkgeräten verwendet wird. Es identifiziert die spezifische Netzwerkkarte (und damit, wenn die Karte nicht oft gewechselt wird, Deinen Computer), mit der Du mit einem Computernetzwerk kommunizierst. Es ist ähnlich einer IP-Adresse zur eindeutigen Identifizierung geeignet, aber ist zudem direkt an Deine Hardware gekoppelt.

h1. Warum MAC-Adressen randomisieren?

Weil es ein eindeutiges Identifizierungsmerkmal ist, kann es benutzt werden, um Dich im Internet zu verfolgen. Das ist besonders wichtig für offene WLAN-Netze wie in öffentlichen Restaurants.
 *Wenn Du Dich mit freien Netzwerken verbindest, ist es stark empfohlen, generierte MAC-Adressen zu benutzen, so wie es weiter unten beschrieben ist, denn es ist einfach, ein ganzes Profil über Dich zu erstellen, nur anhand der MAC-Adresse*.

h1. Welche Limitierungen hat das?

Manche Router identifzieren Dich mit Deiner MAC-Adresse, um Dir eine spezielle IP-Adresse zuzuteilen, oder den Zugriff auf spezielle Dienste zu erlauben. Jeder Dienst, der an ein spezielles Netzwerkgerät gebunden ist, könnte nicht mehr funktionieren, wenn diese Methode benutzt wird. Wenn Du nicht verstehst, was das bedeutet, ist es allerdings sehr wahrscheinlich kein Problem. Wahrscheinlicher ist es notwendig, sich immer wieder duch Portale zu klicken, die beim ersten Mal erscheinen, wenn man sich mit einem Nutzernamen in einem Netzwerk registriert (wie zum Beispieil in freien WLAN-Netzwerken bei Unternehmen). Meist ist es bei jeder neuen Verbindung nötig, die Nutzungsbedingungen zu akzeptieren.

h1. Konfiguration automatischer zufälliger MAC-Adressen in Ubuntu 10.04 mit Network Manager

Ubuntu 10.04 (und seit dem 1. September 2010 und in naher Zukunft, alle Distributions mit Network Manager) kommt mit einer Version von Network Manager, die keine "pre-up"-Skripte für Netzwerkverbindungen unterstützt. Das bedeutet, dass es unfähig ist, Skripte vor jeder neuen Verbindung auszuführen. Damit wäre es einfach möglich, die MAC-Adresse mit einem automatisch ausgeführten Skript zu ändern. Daher wird in dieser Anleitung speziell bei jeder Verbindung eine neue MAC-Adresse generiert, wenn Network Manager gestartet wird und jedes Mal eine neue, wenn die Verbindung unterbrochen wird.

# Führe in einem Terminal aus:
<code>
sudo apt-get install macchanger
</code>
# Es ist empfohlen, die aktuelle MAC-Adresse zu notieren, um später sicher stellen zu können, dass diese geändert wurde. Für ein Kabelnetzwerk tippe:
<code>
macchanger eth0
</code>
das gleiche für ein WLAN-Gerät:
<code>
macchanger wlan0
</code>
Die Ausgabe wird ungefähr so aussehen:
<code>
Current MAC: 00:0c:1d:47:a4:0c (Mettler & Fuchs Ag)
</code>
**00:0c:1d:47:a4:0c** ist die MAC-Adresse dieser Instanz, immer in der Form **XX:XX:XX:XX:XX:XX**. Der Text in Klammern gibt den Hersteller an und wird sich ändern.
# Erstelle die Datei @/etc/init/macchanger.conf@.  Das geht mit:
<code>
sudo nano /etc/init/macchanger.conf
</code>
# Füge die folgenden Zeilen ein und speichere die Datei (STRG+X speichert und beendet den Texteditor nano):

<pre>
# macchanger - set MAC addresses
#
# Set the MAC addresses for the network interfaces.

description     "change mac addresses"

start on starting network-manager

pre-start script
        /usr/bin/macchanger -A wlan0
        /usr/bin/macchanger -A eth0
        /usr/bin/macchanger -A wmaster0
        /usr/bin/macchanger -A pan0
        #/usr/bin/logger wlan0 `/usr/bin/macchanger -s wlan0`
        #/usr/bin/logger eth0 `/usr/bin/macchanger -s eth0`
end script
</pre>
Dieses Skript wird ausgeführt, nachdem _network manager_ gestartet wurde (mittels Ubuntus Upstart-Dienst). Die Verwendung der @-A@-Option erstellt eine zufällige herstellergebundene MAC-Adresse. Das Programm @macchanger@ kann verschiedene Arten Adressen generieren.  Diese Methode mag seltsam aussehen bei aktiver Netzwerküberwachung, aber passive Netzwerküberwachung und Hintergrundüberwachung werden es wahrscheinlich nicht bemerken. Diese Methode sollte für die meisten Menschen gut funktionien.
# Erstelle die Datei @/etc/network/if-post-down.d/random-mac@ und füge folgende Zeilen ein:

<pre>
#!/bin/sh

MACCHANGER=/usr/bin/macchanger

[ "$IFACE" != "lo" ] || exit 0

# Bring down interface (for wireless cards that are up to scan for networks), change MAC address to a random vendor address, bring up the interface
/sbin/ifconfig "$IFACE" down
macchanger -A "$IFACE"
</pre>

This script changes the MAC address again when the network is disconnected.  It's possible if the network is never properly brought down and one never reboots that one can use the same address more than once.
# Make the **random-mac** script executable by typing:
<code>
sudo chmod +x /etc/network/if-post-down.d/random-mac
</code>
# Restart Network Manager to take effect:
<code>
sudo service network-manager restart
</code>

Dein Computer wird von nun an (ohne weitere Intervention) für jedes Netzwerkgerät bei neuen Verbindungen eine neue MAC-Adresse erstellen und damit Deine Verfolgbarkeit in öffentlichen Netzen reduzieren!

Diese Taktik kann einfach für verschiedene linux/BSD-Einstellungen angepasst werden und wahrscheinlich auch OS X und Windows (Bitte schickt uns neue Implementationen).
