@title = "RiseupVPN für Windows"
@toc = true
@this.alias = '/vpn/windows'

## Voraussetzungen

RiseupVPN wurde für Windows 10 getestet.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/windows/RiseupVPN-win-latest.exe"><i class="fa fa-download"></i> RiseupVPN für Windows downloaden</a>

Wenn du die Datei gespeichert hast kannst du RiseupVPN einfach per Doppelklick auf <code>RiseupVPN-win-latest.exe</code> installieren.

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
* Deine Windows-Version
* Deine Programm-logs

### Logs finden

Es gibt 3 Logs für verschiedene Komponenten des Clients:

* Das systray log: `C:\Users\<your user>\AppData\Local\leap\systray.log`
* Der priviledged helper: `C:\Program Files\RiseupVPN\helper.log`
* Der openvpn Prozess: `C:\Program Files\RiseupVPN\openvp.log`

Wenn du einen Bug meldest, schicke diese bitte mit.

### DNS leaks

Es sollte keine DNS- oder IP-Leaks geben, aber RiseupVPN für Windows ist noch nicht kampferprobt. Im Gegensatz zu Mac oder Linux gibt es auf Windows keine Firewall.

Falls du doch irgendwelche Leaks finden solltest, gib uns bitte Bescheid.

### Unveröffentlichte Version testen

Wenn du uns beim Testen einer in der Entwicklung befindlichen Version helfen willst, kannst du die [[nightly builds => https://0xacab.org/leap/bitmask-vpn/-/jobs/artifacts/master/download?job=vendorize]] herunterladen.

## Source Code
Die Clients von RiseupVPN basieren auf der Open-Source-Software Bitmask. Den Code des Windows-Clients könnt ihr [[hier => https://0xacab.org/leap/bitmask-vpn]] finden.
