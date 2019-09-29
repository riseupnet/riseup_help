@title = "Geräteverschlüsselung"
@toc = true
@summary = "Warum und wie Speichermedien verschlüsseln"

# Warum Geräteverschlüsselung verwenden?

Mit Geräteverschlüsselung werden Inhalte Deiner Speichermedien wie Betriebssystem, installierte Programme und persönliche Daten in unlesbarer Form gespeichert, sodass darauf nicht zugegriffen werden kann, wenn das Gerät ausgeschaltet ist.

Ohne Geräteverschlüsselung können Dateien einfach gelesen oder kopiert werden, oder auf Onlinekonten zugegriffen werden, um Identitäten zu stehlen, wenn das Gerät gestohlen oder gefunden wird. Noch schlimmer: ein Angreifer kann Schadprogramme installieren, um von Ferne deine Aktivitäten zu überwachen oder steuern.

# Wie kann Geräteverschlüsselung aktiviert werden

Obwohl vollständige Festplattenverschlüsselung auf einigen Geräten standardmäßig aktiviert ist, muss es auf Laptops und Desktop-Computern und vielen Handys und Tablets manuell aktiviert werden.

Desktop-Anleitungen:

- **Windows**: [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  - WICHTIG: Standardmäßig speichert Windows Schlüssel für Geräteverschlüsselung online (cloud storage). Das bedeutet, dass Microsoft und Regierungen mit denen es kooperiert in der Lage sind, das Gerät zu entschlüsseln. Falls Dich diese Möglichkeit beunruhigt, solltest Du jetzt diese "Funktion" deaktivieren und [[neue Schlüssel generieren => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]].
- **macOS**: [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
- **Linux**: Fast jede Linux-Distribution ermöglicht es, Geräteverschlüsselung bei der Installation zu deaktivieren. Es gibt verschiedene Arten:
  - vollständige Festplattenverschlüsselung ("Full Disk" encryption): Diese Methode verschlüsselt alles auf der primären Festplatte, inklusive des Betriebssystems. Bei jedem Start muss dafür ein separates Kennwort eingegeben werden.
  - verschlüsselter "Home"-Ordner: Hierbei **wird nicht** das Betriebssystem verschlüsselt. Zwar sind persönliche Daten geschützt, aber es ist einfacher für Angreifer, Schadprogramme zu installieren.

Mobile-Anleitung:

- **iOS**: [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
- **Android**: [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Vorsichtsmaßnahmen für Festplattenverschlüsselung

**Limitatierungen** Festplattenverschlüsselung funkioniert nicht immer! Wenn Dein [[Passwort -> passwords]] nicht komplex ist, kann es ein Computer erraten und die Daten entschlüsseln. Auch schützt Verschlüsselung nicht gegen Viren und Schadsoftware. Wenn die Daten auf einen Cloud-Dienst übertragen werden und dieser kompromittiert wird, oder mit einer Regierung kooperiert, kann Festplattenverschlüsselung Deine Daten nicht schützen (sofern der Dienst keine Ende-zu-Ende-Verschlüsselung unterstützt).

**Authentifizierung muss aktiviert werden** Geräteverschlüsselung ist nicht effektiv solange das Gerät keine Authentifizierung benutzt, wie z.B. das Eingeben von Login-Daten für Laptops, oder einer PIN für Mobilgeräte.

**Verhindert Wiederherstellung** Vollständige Festplattenverschlüsselung kann das Risiko erhöhen, Zugriff auf Deine Daten zu verlieren, sofern keine robuste Passwort- oder PIN-Verwaltung verwendet wird. Ein verlorenes Passwort, oder Ausfall des Speicherbereichs, welcher die Schlüssel enthält, bedeutet in der Regel, dass Daten nicht wiederhergestellt werden können. Erstelle daher regelmäßig Backups, um diese Gefahr zu minimieren.

**Gerät muss ausgeschaltet oder blockiert werden** Geräteverschlüsselung schützt nur, wenn der Computer ausgeschaltet ist, oder die Eingabe eines Passworts erfordert. Nach dem Entschlüsseln wird der Schlüssel im RAM gespeichert, sodass selbst mit gesperrtem Bildschirm oder im Ruhezustand- / Bereitschaftsmodus das Risiko besteht, dass Daten ausgelesen werden. Allerdings ist das Umgehen dieser Lockmechanismen im Allgemeinen ein recht technischer Angriff und sollte Dich nicht davon abhalten, den Computer angeschaltet zu lassen, wenn Du damit arbeitest. Es ist jedoch am besten, Geräte in einer feindlichen Umgebung auszuschalten, wenn Du Dich davon entfernst. Sofern Du befürchtest Ziel eines Angriffs zu sein, ist es beste Praxis, das Gerät immer in physischer Reichweite zu behalten.

# Weitere Literatur

- [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
- [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
- [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
- [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
- [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
- [Security Self-defense / How to: Encrypt Your iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
