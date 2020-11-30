@title = "Chat Sicherheit"

## Deine Nachrichten schützen

Wenn du den XMPP Dienst von Riseup nutzt, werden deine Nachrichten in den meisten Fällen verschlüsselt transportiert. Die verschlüsselte Verbindung kann aber nicht garantiert werden, wenn nicht beide Beteiligten den Dienst von Riseup verwenden.

Wenn du eine Ende-zu-Ende Verschlüsselung deiner Nachrichten sicher stellen möchtest, ist deine beste Option [[Off-the-Record Messaging (OTR) -> https://de.wikipedia.org/wiki/Off-the-Record_Messaging]]. Wenn du mehr darüber wissen möchtest kannst du unser [[OTR Tutorial -> otr]] lesen.

## Deine Online-Telefonate schützen

Als wir es das letzte Mal getestet haben, war Jitsi der einzige XMPP Client, der sichere (Video-)Telefonie unterstützt hat.

## IRC absichern

- **SSL** - siehe [[security/network-security/certificates]]. Für das Netzwerk IndyMedia, wo #riseup lebt, benutze Port 6697.
- **SASL EXTERNAL** und **CertFP** - verschiedene aber nicht verwandte Mechanismen, um sich gegenüber dem Dienst mit Zertifikaten zu authentifzieren. Wenn sie zusammen benutzt werden, kann ohne Passwort sichergestellt, dass Du authentifziziert bist, ehe der Verbindungsaufbau abgeschlossen ist.
  * Registriere Deinen Nicknamen: `/msg nickserv register <password> <email>`
  * Erstelle Dir ein Zertifikat: `openssl req -x509 -new -newkey rsa:4096 -sha256 -days 1000 -nodes -out riseup.pem -keyout riseup.pem`
  * Konfiguriere dein IRC-Programm, um dieses Zertifikat zu verwenden (SASL EXTERNAL): [[siehe die Anleitung für das Netzwerk OFTC -> https://www.oftc.net/NickServ/CertFP/]]
  * Baue eine Verbindung zum Netzwerk auf unter Verwendung des Zertifikats.
  * Verifziere deinen Fingerabdruck mit `/whois <your-nick>` und vergleiche ihne mit dem von Deinem Zertifikat. Weitere Info: [[security/network-security/certificates]]
  * Füge deinen CertFP (Fingerabdruck des Zertifikats) hinzu: `/msg nickserv cert add`
  * Schütze die Zertifikate wie Deine Passwörter.

