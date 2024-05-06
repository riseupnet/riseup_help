@title = "RiseupVPN pour windows"
@toc = true

## Exigences

RiseupVPN est testé sur Windows 10.

Si vous avez une précédente version installée, veuillez d'abord essayer de la désinstaller : cliquez
sur <code>uninstall.exe</code> dans le dossier où l'app est installée
(<code>c:\Program Files (x86)\RiseupVPN\uninstall.exe</code>). Seules les versions
récentes incluent le désinstallateur.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/windows/RiseupVPN-win-latest.exe"><i class="fa fa-download"></i> Télécharger RiseupVPN pour windows</a>

Une fois que vous avez sauvegardé le fichier, cliquez deux fois sur <code>RiseupVPN-win-latest.exe</code> pour installer RiseupVPN.

## Résolution des problèmes

### Rapport de bug et demandes de fonctionnalités

RiseupVPN est basé sur un logiciel libre nommé <b>bitmask-vpn</b>.

**Étape 1 :** [[Parcourez => https://0xacab.org/leap/bitmask-vpn/issues]] pour voir si le bug a déjà été identifié.

**Étape 2 :** [[Créez un compte => https://0xacab.org/users/sign_in]] sur [[0xacab.org => https://0xacab.org]] et connectez-vous.

**Étape 3 :** Créez un nouveau [[rapport de bug ou une nouvelle demande de fonctionnalité => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Veuillez inclure les détails suivants dans votre rapport de bug :

* Les étapes pour reproduire le bug
* Ce que que le programme était supposé faire et ce qui est réellement arrivé
* Une capture d'écran si c'est pertinent
* Votre version de windows
* Les journaux du programme

### Récupérer les journaux

Il existe deux fichiers de journal pour les différentes composantes du client :

* Le journal de l'icône de démarrage : `C:\Users\<vous>\AppData\Local\leap\systray.log`
* Le processus openvpn : `C:\Program Files (x86)\RiseupVPN\openvp.log`

Quand vous rapportez un bug, c'est très utile d'inclure les fichiers de journal.

### Fuites DNS

Nous croyons qu'il n'y a pas de fuites de DNS ou d'adresse IP dans RiseupVPN pour windows, mais nous n'avons pas effectué de tests très poussés. Contrairement à Mac ou Linux, il n'y a pas de killswitch sur windows.

Si vous trouvez des fuites, faites-nous signe !

## Code source
Les clients RiseupVPN sont basés sur le logiciel libre Bitmask. Le code du client Windows se trouve [[ici => https://0xacab.org/leap/bitmask-vpn]].
