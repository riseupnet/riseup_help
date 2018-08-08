@title = "Nachrichtenhygiene"
@toc = true
@summary = "Einfache Tipps für Email und sicherere Kommunikation"

# Traue keiner Quele

Der Hauptgrund, dass Emails die Hauptangriffsmöglichkeit einer Organisation sind, ist dass es keine Möglichkeit gibt, die Identität der "Von"-Adresse zu überprüfen.

Zur Wiederholung: Die "Von"-Adresse kann von allen beliebig manipuliert werden, sodass eine Email so aussieht, als käme sie von einer anderen Person.

Weil die Herkunft einer Nachricht so schwer zu verifizieren ist, ist der Posteingang eine übliche Quelle für **[Phishing-Angriffe -> phishing]** und **[Schadsoftware->malware]**.

* **Phishing** ist when someone sends an email claiming to be an entity they are not, and uses this deception to get information. They can be after social security numbers, bank information, passwords, or other sensitive information.
* **Schadsoftware** ist solche, die einen Trick nutzt, um einen zum Ausführen / Installieren von schädlicher Software verleitet, z.B. durch einen Anhang oder Link.

Im Allgemeinen sollte alles Unerwarte in Emails Misstrauen erregen. Sei gewarnt vor allen Nachrichten, die auffordern, etwas zu tun, wie einen Link zu klicken, einen Anhang zu öffnen oder Informationen zurück zu senden.

Wenn in Dein Konto eingebrochen wurde, siehst Du eventuell unverständliche Antworten, zusätzliche gesendete Nachrichten, neue Ordner oder Filter, oder Änderungen der Einstellung. Seltsame Nachrichten oder Kontoverhalten sollten einer Person vom technischen Support gemeldet werden und vorsichtshalber solltest Du Dein Passwort ändern.

# Klicke keine Links in Emails

Verweise in Emails, oft harmlos wirkend oder sogar versteckt, sind die weitverbreitetste Angriffsmethode, um Deine Daten oder Geräte zu gelangen.

Am besten ist es, niemals Links in Emails anzuklicken. Wenn doch, befolge diese Checkliste:

(1) Hast Du die Email erwartet? Selbst wenn die "Von"-Adresse von einer Person, die Du kennst, zu sein scheint, solltest Du vorsichtig sein.

(2) Kannst Du den Verweis abtippen, anstatt ihn zu kopieren? Was angezeigt wird, ist nicht immer der tatsächliche Link. Ein Verweis auf <https://riseup.net> könnte tatsächlich auf die Seite eines Angreifers wie z.B. <%= '<a href="https://riseuρ.net">https://riseuρ.net</a>' %> führen (der zweite verwendet einen griechischen Buchstaben anstatt des “p”). Die sicherste Methode ist es, Links niemals von einer unsicheren Quelle zu kopieren und immer URLs direkt in die Adresszeile einzutippen.

(3) Kennst Du die Adresse? Die meisten Emailprogramme als auch Webbrowser zeigen die Adresse eines Verweises beim Herüberfahren mit der Maus an. Wenn die angezeigte URL unbekannt ist, frage nach, ob die Email wirklich von der angezeigten Adresse verschickt wurde. Links sollten immer mit "https://" beginnen. Wenn stattdessen eine Adresse mit "data://" anfängt, ist es sehr wahrscheinlich ein versuchter Angriff.

Also, klicke nicht einfach auf Links und öffne keine Dateien von irgendwoher. Eine fremde Person wird dir sicher keine Datei schicken, die Du unbedingt brauchst; wenn ein Link von unbekannter Quelle tatsächlich nützliche Information enthält, kannst Du sie auch auf einem sichereren Weg finden (z.B. im Netz suchen).

# Niemals nach dem Klicken eines Links anmelden

If you do click a link in your email, it is very important to not log in to the website that is opened. If the website prompts you to log in, you should instead follow these steps:

1. Open a new tab in the browser, and type the domain of the website manually.
2. Using this new tab, log in to the website.
3. Go back to your email and click on the link again.
4. When this link opens, it should not require you to log in. If it does require that you log in, then the email is probably a phishing attack.

Auf diese Weise bist Du vor den meisten Phishing-Angriffen geschützt.

# Vermeide Anhänge

Email-Anhänge stellen verschiedene Risiken dar, inklusive ihrer Verwendung für Phishing. Sie sind nicht davor geschützt, angesehen oder verändert zu werden. Du kannst also nicht feststellen, dass das empfangene Dokument dasselbe ist, das auch abgeschicht wurde. Ein bösartiger Server zwischen Dir und der Quelle könnte es ersetzen mit einem Programm oder einer anderen Datei, z.B. ein bösartiges Skript. Zusätzlich neigen Anhänge dazu, länger in Postfächern herum zu liegen. Das füllt diese nicht nur unnötig, sondern ist auch gefährlich, wenn in das Emailkonto Deiner Freunde oder einer Firma, mit der Du Kontakt hattest, eingebrochen wird und alle unverschlüsselten Dokumente mit Deinen Daten so in die Hände Dritter gelangen.

Eine better Methode als Emailanhänge ist es, die Dateien auf einem Server abzulegen und den Link an Stelle des Dokuments selbst zu verschicken. Idealerweise führt solch ein Link an einen Ort, der selbst auch durch ein Passwort geschützt ist oder eine andere Authentifizierung verlangt. Oder der Link ist nur eine begrenzte Zeit gültig und wird bald nach der Benutzung unbrauchbar. Diese Verweise können einfach generiert werden mit fast allen Dateispeicher-System, entweder auf Büro-Servern (wie ein Windows-Dateiserver), oder im Internet (wie Google Drive, Box, oder Dropbox).

Für zusätzliche Sicherheit kannst Du verschlüsselte Datei mit temporären Links erzeugen, indem Du Dateien zu <https://share.riseup.net> hoch lädst.

# Siehe auch

* [Security Self-defense / How to Avoid Phishing Attacks](https://ssd.eff.org/en/module/how-avoid-phishing-attacks)
* [Security Education Companion / Phishing and Malware](https://sec.eff.org/topics/phishing-and-malware)
* [Security In-a-box / Protect Your Device From Malware and Hackers](https://securityinabox.org/en/guide/malware/)
* [Security In-a-box / Keep Your Online Communications Private](https://securityinabox.org/en/guide/secure-communication/)
* [Security Planner / Spot Suspicious Emails](https://securityplanner.org/#/tool/spot-suspicious-emails)
