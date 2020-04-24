@title = "Geräteverschlüsselung"
@toc = true
@summary = "Das Wie und Warum der Verschlüsselung deiner Geräte"

# Warum Geräteverschlüsselung nutzen?

Durch Geräteverschlüsselung werden die Inhalte des Speichers deines Gerätes--der Bereich, der das Betriebssystem, deine installierten Programme und deine persönlichen Daten enthält--verschlüsselt, so dass auf diese nicht zugegriffen werden kann, wenn das Gerät ausgeschaltet ist oder wenn du abgemeldet bist.

Ist keine Geräteverschlüsselung aktiviert, so kann eine Person, die dein Gerät stiehlt, es findet, wenn du es verloren hast oder auf einem anderen Weg Zugriff zu deiner Hardware erlangt, leicht deine Dateien lesen, Zugriff auf deine Online Konten erhalten und sich als deine Person ausgeben. Noch schlimmer, ein_e Angreifer_in kann Malware installieren, die es erlaubt ferngesteuert auf alle deine Aktivitäten zuzugreifen.

# Wie kann ich Geräteverschlüsselung aktivieren?

Obwohl eine vollständige Speicherverschlüsselung bei manchen mobilen Geräten standarmäßig aktiviert ist, muss sie auf allen Laptops und Desktop-Computern sowie bei vielen Smartphones und Tablets manuell eingerichtet werden.

Desktop How-Tos:

* **Windows**: [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  * WICHTIG: Standardmäßig macht Microsoft ein cloud-basiertes Backup des Schlüssels, der für die Verschlüsselung deines Gerätes verwendet wird. Das heißt, dass Microsoft und jede Regierung, mit der das Unternehmen kooperiert, in der Lage ist dein Gerät zu entschlüsseln. Wenn dich die Möglichkeit, dass eine nationale Regierung Zugriff auf die Inhalte deines Gerätes erlangen könnte, beunruhigt, solltest du dieses "Feature" deaktivieren und [[neue Schlüssel generieren => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]].
* **macOS**: [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* **Linux**: Beinahe jede Linux Distribution, ermöglicht es, die Geräteverschlüsselung bei der Installation des Betriebssystems zu aktivieren. Es gibt zwei verschiedene Möglichkeiten:
  * "Full Disk" Encryption: Dieser Ansatz verschlüsselt den gesamten primären Speicher deines Gerätes, inklusive des Betriebssytems. Beim einschalten des gerätes wirst du nach einem separaten Passwort gefragt.
  * "Home Directory" Encryption: Dieser Ansatz **verschlüsselt nicht** das Betriebssytem. So werden deine persönlichen Daten geschützt, aber für eine_n Angreifer_in mit Zugriff auf dein Gerät wird es leichter Malware zu installieren.

Smartphone How-Tos:

* **iOS**: [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* **Android**: [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Warnungen zur Geräteverschlüsselung

**Einschräkungen** Geräteverschlüsselung funktioniert nicht immer! Wenn dein [[Passwort => passwords]]  nicht komplex ist, kann ein Computer dieses sehr leicht erraten und dein Gerät entschlüsseln. Außerdem bietet Geräteverschlüsselung keinen Schutz gegen Viren und Malware. Wenn deine Daten in einen cloud-basierten Backup-Service kopiert werden und dieser Dienst wird kompromittiert oder kooperiert mit der Regierung, so wird Verschlüsselung nicht deine Daten schützen (solange du nicht einen Dienst verwendest, der ausdrücklich "clientseitige" Verschlüsselung unterstützt).

**Authentifikation muss aktiviert sein** Geräteverschlüsselung ist nicht wirksam, solange das Gerät keine Anmeldung fordert, um es zu benutzen. Zum Beispiel musst du dich für die Benutzung deines Laptops einloggen oder bei der Nutzung eines Smartphones eine PIN eingeben.

**Macht die Wiederherstellung des Speichers unmöglich** Eine vollständige Speicherverschlüsselung kann auch das Risiko erhöhen, den Zugriff auf einige deiner Daten zu verlieren, wenn keine ordentlichen Verfahren zum Passwort- oder PIN-Managment angewandt werden. Ein verlorenes Passwort, eine verlorene PIN oder auch ein Ausfall des Bereichs des Datenträgers, wo die Schlüssel gespeichert sind, führen dazu, dass du deine Daten nicht wiederherstellen kannst (und auch keine andere Person kann das). Stelle sicher, regelmäßige Sicherungen deiner Daten durchzuführen, um das Risiko eines Datenverlustes zu minimieren.

**Das Gerät muss ausgeschaltet oder gesperrt sein** Geräteverschlüsselung bietet nur dann Schutz, wenn dein Computer ausgeschaltetet ist oder angeschaltet, aber ein Passwort zum Entschlüsseln benötigt. Sobald du dich eingeloggt hast, befindet sich dein geheimer Schlüssel, der für die Entschlüsselung deiner Daten benötigt wird, im Arbeitsspeicher des Computers, so dass sogar bei gesperrtem Bildschirm das Risiko besteht, dass eine Person Zugriff auf die Inhalte deines Computers erlangen könnte, solange dieser eingeschaltet ist (oder sich im Schlafmodus befindet). Im allgemeinen ist es dennoch ein extrem technischer Angriff diese Kontrollen zu umgehen und dieses Risiko sollte dich nicht davon abhalten, deinen Computer eingeschaltet zu lassen und angemeldet zu bleiben, wenn du ihn zum Arbeiten benötigst. Trotzdem ist es am Besten, wenn du deine Geräte ausschaltest, sobald du diese in einer unsicheren Umgebung zurücklässt. Wenn du befürchtest, dass du Ziel eines Angriffs sein könntest, ist es die beste Praxis dein Gerät physisch dauerhaft bei dir zu behalten.

# Siehe auch

* [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
* [Security Self-defense / How to: Encrypt Your iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
