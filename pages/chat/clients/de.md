@title = "XMPP Clients"
@summary = "Konfiguration von XMPP-Clients für die Verwendung mit dem Riseup XMPP-Chat-Dienst."

<p class=“alert alert-info”>Please help us update this page by trying out different clients.</p>

## Wichtige Funktionen, nach denen eine Beurteilung des Clients erfolgen kann:

- **[[OTR]]?** Falls verfügbar, hat dieser Client eine eingebaute Unterstützung für _off-the-record_-messaging, was eine Ende-zu-Ende Verschlüsselung von Chat-Nachrichten mit PFS (perfect-forward-secrecy / dt. etwa perfekte vorwärts gerichtete Geheimhaltung) vereint.
- **[OMEMO](https://conversations.im/omemo/)?** Wenn Ja, unterstützt dieses Programm Ende-zu-Ende-Verschlüsselung für verschiedene Programme und Offline-Gespräche.
- **<a href="https://en.wikipedia.org/wiki/Jingle_(protocol)">Jingle</a>?** Falls verfügbar, kann dieser Client für Sprach- und Videochat verwendet werden.
- **[Proxy](https://en.wikipedia.org/wiki/Proxy_server)?** Falls verfügbar, kann dieser Client Proxys verwenden bzw. hält sich dieser Client strikt an die Proxy-Einstellungen.
- **[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)** Falls verfügbar, unterstützt dieser Client verschlüsselte Verbindungen mit dem Chat-Server.
- **[[Tor]]?** Falls verfügbar, kann dieser Client Verbindungen korrekt durch Tor leiten, um Zensur zu umgehen und auf Dienste anonym zuzugreifen. Falls nein, sollte der Client **nicht mit Tor verwendet werden**.
- **[[MUC]]?** If yes, this client can be used for Multi-User Chat (chatrooms XEP-0045)

## Empfohlene Clients

| Client                                           | Unterstütztes Betriebssystem              | OTR? | OMEMO? | Jingle?      | Proxy? | TLS? | Tor? | MUC? | Kommentare                                                                                        |
|--------------------------------------------------|-------------------------------------------|------|--------|--------------|--------|------|------|------|---------------------------------------------------------------------------------------------------|
| [Gajim](https://gajim.org)                       | GNU/Linux, Windows, FreeBSD               | Nein | *Ja*   | *Ja*         | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Guter XMPP-Client, der in Python und GTK+ programmiert wurde.                         |
| [Gajim 0.16.x](https://gajim.org)                | GNU/Linux, Windows, FreeBSD               | *Ja* | Nein   | *Ja*         | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Guter XMPP-Client, der in Python und GTK+ programmiert wurde.                         |
| [Psi](https://psi-im.org)                        | GNU/Linux, Windows, macOS                 | *Ja* | *Ja*   | *Ja* (Linux) | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Guter XMPP-Client, der in C ++ und Qt programmiert wurde.                             |
| [Psi+](https://psi-plus.com)                     | GNU/Linux, Windows, macOS, Haiku, FreeBSD | *Ja* | *Ja*   | *Ja* (Linux) | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Guter XMPP-Client, der in C ++ und Qt programmiert wurde.                             |
| [CoyIM](https://coy.im)                          | GNU/Linux, Windows, macOS                 | *Ja* | Nein   | Nein         | *Ja*   | *Ja* | *Ja* | Nein | Quelloffen. Per Standard sicher in GNOME.                                                         |
| [ChatSecure](https://chatsecure.org)             | Android, F-Droid, iOS                     | *Ja* | *Ja*   | Nein         | *Ja*   | *Ja* | *Ja* | ?    | Quelloffen, Tor-Unterstützung.                                                                    |
| [Conversations](https://conversations.im)        | Android                                   | Nein | *Ja*   | Nein         | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Ein sehr gutes Chatprogramm für Android. Unterstützt verschlüsselte Gruppengespräche! |
| [Conversations Legacy](https://conversations.im) | Android                                   | *Ja* | Nein   | Nein         | *Ja*   | *Ja* | *Ja* | *Ja* | Quelloffen. Ein sehr gutes Chatprogramm für Android. Unterstützt verschlüsselte Gruppengespräche! |


## Andere Clients

| Client                                              | Unterstützte Betriebssysteme | OTR?          | OMEMO?        | Jingle?      | Proxy? | TLS? | Tor?      | MUC? | Kommentare                                                                                                                                   |
|-----------------------------------------------------|------------------------------|---------------|---------------|--------------|--------|------|-----------|------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [[Adium]]                                               | macOS                        | *Ja*          | *Ja* (Plugin) | Nein         | *Ja*   | *Ja* | Teilweise | ?    | Quelloffen. Gute native Version von Pidgin für Mac, jedoch wird libpurple nur selten aktualisiert. DNS- und URL-Informationen dringen durch. |
| [Jitsi](https://jitsi.org)                          | GNU/Linux, Windows, macOS    | *Ja*          | Nein          | *Ja*         | ?      | ?    | ?         | ?    | Quelloffen. Programmiert in Java.                                                                                                            |
| [Miranda](https://miranda-im.org)                   | Windows                      | *Ja*          | Nein          | Nein         | ?      | ?    | ?         | ?    | Quelloffen. Stabiler Client mit vielen Plugins.                                                                                              |
| [Miranda NG](https://miranda-ng.org)                | Windows                      | *Ja*          | Nein          | Nein         | ?      | ?    | ?         | ?    | Quelloffen. Stabiler Client mit vielen Plugins.                                                                                              |
| [[Pidgin]]                                           | GNU/Linux, Windows, macOS    | *Ja* (Plugin) | *Ja* (Plugin) | *Ja* (Linux) | *Ja*   | *Ja* | *Ja*      | ?    | Quelloffen. Läuft Stabil und bringt viele Funktionen mit. Verwende die aktuellste Version.                                                   |
| [Spark](https://igniterealtime.org/projects/spark/) | GNU/Linux, Windows, macOS    | *Ja*          | Nein          | *Ja*         | ?      | ?    | ?         | ?    | Quelloffen. Programmiert in Java, derzeit leider noch nicht getestet.                                                                        |

## Andere Clients

| Client                                    | OS supportés | OTR? | OMEMO? | Jingle? | Proxy?       | SSL/TLS?     | Tor? | MUC? | Kommentare                                                                                                   |
|-------------------------------------------|--------------|------|--------|---------|--------------|--------------|------|------|--------------------------------------------------------------------------------------------------------------|
| [Beem](https://beem-project.com)          | Android      | Nein | Nein   | Nein    | ?            | ?            | ?    | ?    | Quelloffen. Stabile Android-App. Unterstützt keine Gruppenchats.                                             |
| [Empathy](https://live.gnome.org/Empathy) | GNU/Linux    | Nein | Nein   | *Ja*    | *Ja* (GNOME) | *Ja* (GNOME) | ?    | ?    | Quelloffen. Läuft stabil und ist einfach zu verwenden.                                                       |
| [iChat](https://www.apple.com)            | macOS        | Nein | Nein   | Nein    | ?            | ?            | ?    | ?    | Apples eingebaute Chat-Software unterstützt XMPP, aber nur mit einer stark dezimierten Anzahl an Funktionen. |
| [Pandion](https://pandion.im)             | Windows      | Nein | Nein   | Nein    | ?            | ?            | ?    | ?    | Quelloffen. Guter stabiler Windows-XMPP-Client.                                                              |
