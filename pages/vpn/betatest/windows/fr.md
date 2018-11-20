@title = "RiseupVPN pour windows"
@toc = true
@this.alias = '/vpn/windows'

## Exigences

RiseupVPN est testé pour windows 7 et windows 10.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/windows/RiseupVPN-win-latest.exe"><i class="fa fa-download"></i> Télécharger RiseupVPN pour windows</a>

Une fois que vous avez sauvegardé le fichier, cliquez deux fois sur <code>RiseupVPN-win-latest.exe</code> pour installer RiseupVPN.

## Problèmes

### Rapport de bug et demandes de fonctionnalités 

RiseupVPN utilise un programme libre nommé <b>bitmask-systray</b>.

**Étape 1:** [[Parcourez => https://0xacab.org/leap/bitmask-systray/issues]] pour voir si le bug a déjà été identifié.

**Étape 2:** [[Créez un compte => https://0xacab.org/users/sign_in]] sur [[0xacab.org => http://0xacab.org]] et connectez-vous.

**Étape 3:** Créez un nouveau [[rapport de bug ou une nouvelle demande de fonctionnalité => https://0xacab.org/leap/bitmask-systray/issues/new]].

Veuillez inclure les détails suivants dans votre rapport de bug:

* Les étapes pour reproduire le bug
* Ce que que le programme était supposé faire et ce qui est réellement arrivé
* Une capture d'écran si c'est pertinent
* Votre version de windows
* Les journaux du programme

### Récupérez les journaux

Il existe trois fichiers de journal pour les différentes composantes du client:

* Le journal de l'icône de démarrage: `C:\Users\<your user>\AppData\Local\leap\systray.log`
* Le *priviledged helper*: `C:\Program Files\RiseupVPN\helper.log`
* Le processus openvpn: `C:\Program Files\RiseupVPN\openvp.log`

Quand vous rapportez un bug, c'est très utile d'inclure le fichier de journal.

### Fuites DNS

Nous croyons qu'il n'y a pas de fuites de DNS ou d'adresse IP sur RiseupVPN pour windows, mais nous n'avons pas effectués de tests très poussés. Contrairement à Mac ou Linux, il n'y a pas de pare-feu sur windows.

Si vous trouvez des fuites, faites-nous signe!

### Tester une version de développement

Si vous souhaitez nous aider à tester une version de développement de RiseupVPN, vous pouvez télécharger [[les versions quotidiennes => https://0xacab.org/leap/bitmask-systray/-/jobs/artifacts/master/download?job=win_installer]].
