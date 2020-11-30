@title = "Riseup Chat"
@nav_title = "Chat"

## Was ist XMPP?

XMPP ist ein offener Standard für Instant Messaging (Kurznachrichten) sowie für Sprach/Video-Chat. Mit XMPP kannst du Nachrichten zwischen Nutzern von tausenden verschiedenen Chat-Anbietern senden und empfangen.

## Riseup's XMPP Dienst verwenden

Deine riseup.net E-Mail Adresse entspricht deiner XMPP-Adresse. Jemand, der dir eine XMPP-Nachricht oder eine Freundschaftsanfrage senden möchte, muss diese nur an `username@riseup.net` senden.

Um einen [[XMPP-Client => chat/clients]] zu konfigurieren, benötigst du folgende Informationen:

- **Protokoll**: "xmpp"
- **Account**: `benutzername@riseup.net`
- **Passwort**: dein [[Riseup-Passwort -> human-security/riseup-password]]

Es ist sehr wichtig, dass du deinen Client so konfigurierst, dass er **Verschlüsselung immer erfordert**. Einige Clients haben die Einstellungsmöglichkeit "verschlüsseln, wenn möglich". Obwohl der riseup.net-Server eine Verschlüsselung erfordert, kann ein Angreifer dein Passwort leicht abfangen, falls dein Client so konfiguriert ist, dass er "verschlüsselt, wenn möglich".

Einige XMPP-Clients werden dich nach deinem Benutzernamen und der Domain seperat fragen. In diesem Fall verwende folgende Daten:

- **Benutzername**: `benutzername`
- **Domain/Domäne**: `riseup.net`

Anleitungen für einige Clients findest du unter [[XMPP Clients => chat/clients]].

## Verbindung mit multi-user Chatrooms (Gruppenchats) herstellen

Wenn du dich mit Chatrooms verbindest oder diese im Riseup XMPP-Netzwerk erstellst, sollte die Syntax so aussehen:

- `dein-raum-name@conference.riseup.net`

Wenn du den Raumnamen seperat definieren musst, verwende:

- Chatroom: `dein-raum-name`
- Domain/Domäne: `conference.riseup.net`

Verwende NICHT:

- `dein-raum-name@riseup.net`

### Pidgin-Räume

Wenn du über [[Pidgin => pidgin]] verbunden bist, klicke auf `Chat hinzufügen` im `Buddys`-Menü.

- Raum: `dein-raum-name`
- Server: `conference.riseup.net`
- Kürzel: `dein-nickname`
- Passwort: [optional]
- Alias: [optional]
- Gruppe: [optional]

Klicke auf `Hinzufügen` und schau in die Buddy-Liste. Du solltest jetzt in der Gruppe `Chats` deinen Raum sehen.
Klicke rechts auf den Raum und wähle `Betreten`.

Zum Testen kannst du `riseup.net` als Raumname verwenden und diesem beitreten.

## Für höhere Sicherheit

1. Um deine Sicherheit zu erhöhen, verbinde dich mit unserem XMPP-Server über das [[Riseup VPN => vpn]].
1. Benutze unseren [Tor .onion-Dienst](https://www.torproject.org/docs/hidden-services.html.en): suche nach `xmpp.*.onion` auf der Seite mit [[Riseups onion-Diensten->tor#riseups-tor-hidden-services]].
