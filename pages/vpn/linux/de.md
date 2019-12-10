@title = "RiseupVPN für Linux"
@this.alias = '/vpn/linux'

## Voraussetzungen

Momentan ist RiseupVPN für Linux nur mit `snap` verfügbar. Wenn du Ubuntu benutzt, ist snap schon installiert. Wenn nicht, kannst du es im Terminal installieren:

```
sudo apt install snapd
```

RiseupVPN ist auf **Ubuntu LTS** und **Debian Stable** getestet. Auf anderen Versioinen funktioniert es möglicherweise nicht.

## Installation

Such einfach nach **RiseupVPN** im **Software Center** oder klick hier:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Open RiseupVPN in Software Center
</a>

Ansonsten kannst du es auch damit installieren:

```
sudo snap install --classic riseup-vpn
```

## Problemlösungen

### Bug-Meldungen und Anfragen

RiseupVPN wurde mit dem freien Programm <b>bitmask-vpn</b> gebaut.

**Schritt 1:** [[Kontrolliere => https://0xacab.org/leap/bitmask-vpn/issues]] ob dieser Bug schon gemeldet wurde.

**Schritt 2:** [[Registriere dich => https://0xacab.org/users/sign_in]] auf [[0xacab.org => https://0xacab.org]] und melde dich an.

**Schritt 3:** Erstelle eine [[neue Meldung => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Um helfen zu können brauchen mindestens diese Informationen:

* Wie können wir den Bug reproduzieren?
* Wie verhält sich der Bug und wie ist er sichtbar?
* Einen Screenshot falls es ein grafischer Bug ist
* Deine Linux-Distribution und Version
* Dein Programm-log

### Log finden

Das RiseupVPN-log befindet sich in deinem persönlichen Ordner:

```
~/.config/leap/systray.log
```

### Beenden erzwingen

Falls irgendwas nicht mehr funktioniert, führ diese Befehle aus:

```
sudo pkill -e -f riseup-vpn
```

### RiseupVPN startet nicht

Wenn es nicht über das Icon startet, kannst du es über das Terminal starten:

```
/snap/bin/riseup-vpn.launcher
```

Sollten Probleme beim Startprozess auftreten, werden diese dann angezeigt.

### Unveröffentlichte Version testen

Wenn du uns helfen willst, eine unveröffentlichte, in der Entwicklung befindliche Version von RiseupVPN zu testen, kannst du diese hiermit installieren :

```
sudo snap install --classic --beta riseup-vpn
```

### PID-Datei löschen

Manchmal startet RiseupVPN nicht, weil es denkt, dass bereits eine andere Version läuft.

Wenn du diese Fehlermeldung erhältst, führ einfach folgende Befehle aus:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```
