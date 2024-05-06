@title = "RiseupVPN pour macOS"
@toc = true

## Exigences

RiseupVPN est testé sur High Sierra et les versions suivantes.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.dmg"><i class="fa fa-download"></i> Téléchager RiseupVPN pour macOS</a>

Une fois que vous avez sauvegardé le fichier, cliquez deux fois sur <code>RiseupVPN-OSX-latest.dmg</code> pour installer RiseupVPN.

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
* Votre version de macOS
* Les journaux du programme

### Récupérer les journaux

Il existe trois fichiers de journal pour les différentes composantes du client :

* Le journal de l'icône de démarrage : `/Users/<vous>/Library/Preferences/leap/systray.log`
* Le *priviledged helper* : `/Applications/RiseupVPN/RiseupVPN.app/Contents/helper/helper.log`
* Le processus openvpn : `/Applications/RiseupVPN/RiseupVPN.app/Contents/helper/openvpn.log`

Quand vous rapportez un bug, c'est très utile d'inclure les fichiers de journal.

## Code source
Les clients RiseupVPN sont basés sur le logiciel libre Bitmask. Le code du client macOS se trouve [[ici => https://0xacab.org/leap/bitmask-vpn]].
