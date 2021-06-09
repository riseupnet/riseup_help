@title = "RiseupVPN per macOS"
@toc = true
@this.alias = '/vpn/macos'

## Requirements

RiseupVPN è stato testato su Sierra e High Sierra.

## Installazione

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.dmg"><i class="fa fa-download"></i> Scarica RiseupVPN per macOS</a>

Per installare RiseupVPN, una volta che ha salvato il file, fai doppio click sul file <code>RiseupVPN-OSX-latest.dmg</code>.

## Risoluzione dei problemi

### Segnalazione di malfunzionamenti e richieste di nuove funzionalità

RiseupVPN è totalmente basata su un software libero chiamato <b>bitmask-vpn</b>.

**Passo 1:** [[Fai una ricerca per vedere => https://0xacab.org/leap/bitmask-vpn/issues]] se il malfunzionamento è già stato segnalato.

**Passo 2:** [[Registra un account => https://0xacab.org/users/sign_in]] su [[0xacab.org => https://0xacab.org]] ed accedi.

**Passo 3:** Crea una [[nuova segnalazione di malfunzionamento o una richiesta di nuove funzionalità => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Nella tua segnalazione, per favore includi le seguenti informazioni:

* Passi per riprodurre il problema
* Qual'è il comportamento che ti saresti aspettato e cosa vedi
* Uno screenshot nel caso ci sia qualcosa di visibile
* La versione di macOS
* I log del programma


### Per prendere i log

Ci sono tre file di log diversi, uno per ogni componente del client:

* Il log della barra dei menu: `/Users/<your user>/Library/Preferences/leap/systray.log`
* Il log del priviledged helper: `/Applications/RiseupVPN.app/Contents/helper/helper.log`
* Il log del processo openvpn: `/Applications/RiseupVPN.app/Contents/helper/openvpn.log`

Quando segnali un malfunzionamento, è molto utile che tu includa i file di log.
