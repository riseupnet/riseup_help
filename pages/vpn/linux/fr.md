@title = "RiseupVPN pour Linux"

## Exigences

Pour utiliser le VPN de Riseup, il vous faut installer un programme qui s'appelle RiseupVPN.

## Snap

Malheureusement, le paquet Snap n'est actuellement plus supporté. Veuillez ne pas installer `riseup-vpn` depuis le Snap store, car il s'agit d'une version plus à jour. Nous aimerions le faire fonctionner à nouveau, [mais nous avons besoin de l'aide de la communauté](https://0xacab.org/leap/bitmask-vpn/-/issues/848#note_1205365).

## Debian

Il y a un paquet `riseup-vpn` dans les dépôts Debian officiels depuis [Debian Bookworm](https://packages.debian.org/bookworm/riseup-vpn). Pour une version plus récente, veuillez l'installer depuis `backports` ou `unstable`. Installez-le en exécutant la commande suivante dans un terminal, ou cherchez le paquet `riseup-vpn` dans votre gestionnaire de paquets préféré :

    sudo apt install riseup-vpn

## Ubuntu

Les deux dernières versions d'Ubuntu LTS sont prises en charge. Veuillez installer depuis le [ppa LEAP](https://launchpad.net/~leapcodes/+archive/ubuntu/riseup-vpn) en utilisant :

``` 
sudo add-apt-repository ppa:leapcodes/riseup-vpn
sudo apt update
sudo apt install riseup-vpn
```

## Arch Linux / Manjaro

Il y a des [paquets](https://aur.archlinux.org/packages?O=0&SeB=nd&K=riseup-vpn) AUR (Arch User Repo) pour Arch Linux et Manjaro. La version avec le suffixe `-git` contient la dernière version de développement. Pour installer, exécutez :

```
yay riseup-vpn
yay riseup-vpn-git
```

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
* Votre distribution Linux et sa version
* Le journal du programme

### Journaux de debug

Veuillez exécuter `riseup-vpn` avec une variable d'environnement `LOG_LEVEL` appropriée.

```
LOG_LEVEL=TRACE riseup-vpn
```

### Récupérer le journal

Le journal de RiseupVPN est situé dans votre répertoire personnel :

```
~/.config/leap/systray.log
```

Quand vous rapportez un bug, c'est très utile d'inclure le fichier de journal.

### Forcer la fermeture

Si quelque chose arrête de fonctionner, exécutez cette commande et essayez de nouveau :

```
sudo pkill -e -f riseup-vpn
```

### Ne démarre pas

Si l'icône dans la barre de lancement ne fonctionne pas, vous pouvez exécuter RiseupVPN à partir de la ligne de commande pour identifier le problème :

```
/snap/bin/riseup-vpn.launcher
```

Tous les problèmes de démarrage s'afficheront sur le terminal.

### Activer l'icone de RiseupVPN à côté de l'horloge

Dans les versions récentes de GNOME, les icones de la zone de notifications ne sont plus affichées par défaut, 
ou le sont parfois dans un petit menu en bas à droite de l'écran. Pour avoir l'icone de RiseupVPN visible à
côté de l'horloge, vous pouvez installer l'extension GNOME `AppIndicator` et l'activer :

Pour les distributions basées sur Debian (testé uniquement avec Debian Buster) :
* Installez le paquet `gnome-shell-extension-appindicator`, avec le gestionnaire de paquets ou avec cette ligne de commande dans un terminal : `sudo apt install gnome-shell-extension-appindicator`
* Fermez votre session et rouvrez-là, ou redémarrez votre ordinateur
* Ouvrez l'application `Ajustements`, puis dans le panneau de gauche allez dans Extensions
* Activez "Kstatusnotifieritem/appindicator support"
* Profitez :)

### Supprimer le fichier PID

Parfois, RiseupVPN ne démarre pas car le programme croit qu'il y a déjà une version en cours d'exécution.

Si vous avez cette erreur, exécutez ces commandes :

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

## Code source
Les clients RiseupVPN sont basés sur le logiciel libre Bitmask. Le code du client Linux se trouve [[ici => https://0xacab.org/leap/bitmask-vpn]].
