@title = "RiseupVPN per Linux"
@this.alias = '/vpn/linux'

## Requisiti

Al momento RiseupVPN è disponibile per Linux come pacchetto solo usando `snap`. Se usi Ubuntu snap è già installato, altrimenti lancia il seguente comando:

```
sudo apt install snapd
```

RiseupVPN per ora è stato testato su **Ubuntu LTS** e **Debian Stable**. Se hai una release differente, non è detto che funzioni.

## Installazione

E' sufficiente cercare **RiseupVPN** nel **Software Center** o cliccare questo link:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Apri RiseupVPN nel Software Center
</a>

se il link qui sopra non dovesse funzionare, può effettuare l'installazione da riga di comando:

```
sudo snap install --classic riseup-vpn
```

## Risoluzione dei problemi

### Segnalazione dei malfunzionamenti e richiesta di nuove funzionalità

RiseupVPN è totalmente basata su un software libero chiamato <b>bitmask-systray</b>.

**Passo 1:** [[Fai una ricerca per vedere => https://0xacab.org/leap/bitmask-systray/issues]] se il malfunzionamento è già stato segnalato.

**Passo 2:** [[Registra un account => https://0xacab.org/users/sign_in]] su [[0xacab.org => http://0xacab.org]] ed accedi.

**Passo 3:** Crea una [[nuova segnalazione di malfunzionamento o una richiesta di nuove funzionalità => https://0xacab.org/leap/bitmask-systray/issues/new]].

Per favore, includi le seguenti informazioni nella tua segnalazione di malfunzionamento:

* Passi per riprodurre il problema
* Qual'è il comportamento che ti saresti aspettato e cosa vedi
* Uno screenshot nel caso ci sia qualcosa di visibile
* La tua distribuzione linux e la relativa versione
* Il log del programma

### Per prendere i log

Il log di RiseupVPN si trova nella tua cartella home:

```
~/.config/leap/systray.log
```

Quando segnali un malfunzionamento, è molto utile includere il file di log.

### Forzare l'uscita

Se qualcosa smette di funzionare, lancia questo comando e prova di nuovo:

```
sudo pkill -e -f riseup-vpn
sudo /snap/bin/riseup-vpn.bitmask-root firewall stop
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

Questi comandi assicurano che tutti i processi di RiseupVPN vengano killati, le regole di uscita del firewall vengano rimosse e che il PID file venga ripulito.

### Problemi all'avvio

Se l'icona non dovesse funzionare, puoi lanciare RiseupVPN dalla linea di comando per identificare il problema:

```
/snap/bin/riseup-vpn.launcher
```

Qualsiasi problema di avvio verrà mostrato nel terminale.

### Testare una versione di pre-release

se vuoi aiutarci a testare una versione di sviluppo o pre-release di RiseupVPN, la puoi installare usando il seguente comando:

```
sudo snap install --classic --beta riseup-vpn
```

### Rimuovere il PID file

A volte RiseupVPN non parte perché pensa che ci sia un'altra versione attiva sul sistema.

Nel caso ti capitasse questo errore, lancia i seguenti comandi:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```
