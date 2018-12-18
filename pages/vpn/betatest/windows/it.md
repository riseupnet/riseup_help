@title = "RiseupVPN per windows"
@toc = true
@this.alias = '/vpn/windows'

## Requirements

RiseupVPN è stato testato su windows 7 e windows 10.

## Installazione

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/windows/RiseupVPN-win-latest.exe"><i class="fa fa-download"></i> Scarica RiseupVPN per windows</a>

Per installare RiseupVPN, una volta salvato il file fai doppio click su <code>RiseupVPN-win-latest.exe</code>.

## Risoluzione dei problemi

### Segnalazione di malfunzionamenti e richieste di nuove funzionalità

RiseupVPN è totalmente basata su un software libero chiamato <b>bitmask-systray</b>.

**Passo 1:** [[Fai una ricerca per vedere => https://0xacab.org/leap/bitmask-systray/issues]] se il malfunzionamento è già stato segnalato.

**Passo 2:** [[Registra un account => https://0xacab.org/users/sign_in]] su [[0xacab.org => http://0xacab.org]] ed accedi.

**Passo 3:** Crea una [[nuova segnalazione di malfunzionamento o una richiesta di nuove funzionalità => https://0xacab.org/leap/bitmask-systray/issues/new]].

Nella tua segnalazione, per favore includi le seguenti informazioni:

* Passi per riprodurre il problema
* Qual'è il comportamento che ti saresti aspettato e cosa vedi
* Uno screenshot nel caso ci sia qualcosa di visibile
* La versione di windows
* I log del programma

### Prendere i log

Ci sono tre file di log, uno per ogni componente del client:

* Il log della barra delle applicazioni `C:\Users\<your user>\AppData\Local\leap\systray.log`
* Il log del priviledged helper: `C:\Program Files\RiseupVPN\helper.log`
* Il log del processo openvpn: `C:\Program Files\RiseupVPN\openvp.log`

Quando segnali un bug, è molto utile se includi i file di log.

### DNS leaks

Noi riteniamo che su RiseupVPN per windows non ci siano falle e perdite di informazioni né a livello di DNS che a livello IP, ma questa aspetto non è stato testato in modo intensivo. Diversamente dal Mac e da Linux, su windows non c'è un firewall di sistema.

Se dovessi trovare delle falle che causano perdite di dati, saremmo molto interessati a saperne di più.

### Testare una versione di pre-release

se vuoi aiutarci a testare una versione di sviluppo o pre-release di RiseupVPN, puoi scaricare la [[nightly builds => https://0xacab.org/leap/bitmask-systray/-/jobs/artifacts/master/download?job=win_installer]].
