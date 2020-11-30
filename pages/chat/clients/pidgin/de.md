@title = 'Pidgin'

## Über Pidgin

![logopidgin](logo.pidgin.png)

Pidgin ist das bekannteste Direktnachrichten-Programm für GNU/Linux, Windows und macOS. Du kannst es hier herunterladen: https://pidgin.im/download. Für Mac gibt es [[Adium]], die Alternative zu Pidgin für Mac.

## Konto erstellen

Um ein Konto zu erstellen, drücke beim ersten Start `Strg+A` (alternativ im Menü `Konten` - `Konten verwalten`) und `Hinzufügen ...`, .

(1) Im Reiter `Einfach` stelle folgendes ein:

![newaccountbasictab](new-account-basic-tab.png)

- `Protokoll`: XMPP
- `Benutzer`: dein Riseup-Name
- `Domain`: riseup.net
- `Passwort`: Dein [[riseup-password]]

Optional kannst du einen lokalen Alias einstellen und ein Bild hinzufügen. Andere Menschen werden dieses Bild in ihrer Liste sehen.

## Benutzung von OTR

Siehe die [[otr]]-Anleitung für Details zu Ende-zu-Ende-Verschlüsselung mit Pidgin.

## Absichern von Pidgin unter GNU/Linux mit ["Apparmor"](https://gitlab.com/apparmor/apparmor/wikis/home/)

Für zusätzliche Sicherheit empfehlen wir, Pidgin mit folgenden Schritten abzusichern:

- Kopiere usr.bin.pidgin nach `/etc/apparmor.d/usr.bin.pidgin`
  * [usr.bin.pidgin für Ubuntu 14.04](https://bazaar.launchpad.net/~apparmor-dev/apparmor-profiles/master/view/head:/ubuntu/14.04/usr.bin.pidgin)
- starte apparmor neu
`sudo /etc/init.d/apparmor restart`
- starte Pidgin neu

## Tor mit Pidgin

Um Pidgin über Tor zu benutzen, gehe zu `Kontoeinstellungen`.

![pidginmodifyaccount](pidgin-modify-account.png)

Klicke auf `Erweitert` und setze folgende Werte:

- `Verbindungssicherheit`: Verschlüsselung fordern
- `Verbindungsport`: 5222
- `Verbindungsserver`: suche auf der [[Seite von Riseups .onion-Diensten->tor#riseups-tor-hidden-services]] nach `xmpp.*.onion`
- `Proxys für Dateiübertragungen`: `proxy.riseup.net`

![pidginmodifyaccount](pidgin-modify-account.png)

Danach im Reiter `Proxy` ...

![piginmodifyaccountproxy](pidgin-modify-account-proxy.png)

Setze den `Proxy-Typ` auf `SOCKS5`, den Host und Port, so wie im Bild zu sehen ist, sowie deinen Nutzernamen und Passwort.
