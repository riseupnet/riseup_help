@nav_title = "Fehlersuche"
@title = "RiseupVPN: Fehlersuche"
@summary = "Problemlösungsanleitung für das LEAP-betriebene VPN"
@toc = true

## Konto

Folgende Beobachtungen für Konten wurden während der Beta-Phase gemacht.

### Ich kann meinen Namen nicht registrieren / Jemand hat meinen Namen genommen

Unsere neuen Dienste mit erhöhter Sicherheit bauen auf dem [LEAP Encryption Access Project](https://leap.se)-Plattform auf. Dieses ist eine komplett andere Infrastruktur und ist nicht direkt mit unseren bisherigen Email- oder Listen-Diensten verbunden. Du kannst diese Dienste erreichen unter der Adresse https://black.riseup.net.

Das bedeutet, dass du ein neues Konto erstellen musst, um das VPN oder andere zukünftige Dienste benutzen zu können. Um mögliche Namenskollisionen zu vermeiden, haben wir alle bisherigen riseup.net Namen in einen "reserviert" Status versetzt. Aber keine Bange, später in diesem Jahr wirst du dein altes Konto (inklusive Name) zu unseren um einiges sichereren neuen Diensten migrieren können.

### Mein Nutzername oder Passwort funktioniert nicht!

Siehe oben.

## Bitmask

Die folgenden Probleme wurden einzeln in einigen Umgebungen beobachtet.

### Ich benutze nicht Debian und/oder Ubuntu. Wie kann ich Bitmask installieren?

Bei Debian-basierten Distributionen (wie CrunchBang) oder einer Ubuntu-basierten (wie Mint) sollte das [Einzelpaket](#stand-alone-bundle) installiert werden und wir fänden es toll, Erfahrungsberichte über das Installieren von Bitmask zu bekommen! Es gibt eine große Zahl von GNU/Linux-Distributionen und es gibt keine Möglichkeit, alle möglichen Umgebungen zu testen. Wenn die Installation geklappt hat, lass es uns wissen... und wenn nicht, freuen wir uns über Rückmeldungen. Jedenfalls sollte **Bitmask auf modernen GNU/Linux Systemen funktionieren**.

### Ich kann mich nicht mit allen/einigen/verschiedenen Seiten verbinden

Führe bitte folgende Befehle aus und probiere, um es das Problem löst:

#### Führe `sudo ip route` aus und suche nach der Zeile, die mit 'default' beginnt und dass 'tun0' der Wert nach dem Wort 'dev' ist

Es gibt einen Bug in Debians Network-Manager-Paket (in testing und unstable). Wenn du dieses Paket benutzt, hast du wahrscheinlich dieses Problem. Mehr dazu findest du in [Debian Bug #23755015](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23755015).

Ein möglicher Weg das zu umgehen ist

    sudo ip route del default
    sudo ip route add default via 10.42.0.1 dev tun0

#### Mein Problem ist nicht oben aufgelistet... Was jetzt?

Zuerst geht es darum, herauszufinden, was die Ursache des Problems ist, um da ran zu kommen, öffnen dein Terminal und führe `bitmask --debug --logfile /tmp/bitmask.log` aus. Das wird Bitmask im debug-Modus starten und die Ausgabe in die Textdatei `/tmp/bitmask.log` schreiben. Wenn du erfahren bist, hilft das vielleicht, das Problem weiter zu verfolgen. Wenn nicht, [öffene ein Ticket](https://black.riseup.net/tickets/net)) mit dem Inhalt von `/tmp/bitmask.log` und deinem Betriebssystem (Debian Wheezy. Mint 17, Ubuntu Trusty, etc).

## Andere Probleme

### Ein "Configure Bitmask email Account"-Fenster öffnet sich jedes Mal, wenn ich Thunderbird/Icedove starte

Das `xul-ext-bitmask`-Paket wurde installiert. Das ist keine Abhängigkeit, aber ein empfohlenes Paket, welches die Thunderbird/Icedove-Erweiterung enthält, um LEAP als Email-Anbieter zu unterstützen. Fühl dich frei, es zu entfernen mit dem Befehl `sudo apt-get remove xul-ext-bitmask` und starte Thunderbird/Icedove neu.

....
