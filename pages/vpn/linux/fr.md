@title = "RiseupVPN pour Linux"

## Exigences

Pour utiliser le VPN de Riseup, il vous faut installer un programme qui s'appelle RiseupVPN. Sous Linux, ce programme est disponible sous forme de `snap`, ou alors comme un paquet pour Debian Stable.

RiseupVPN a été testé avec **Ubuntu LTS** (18.04) et **Debian Stable**. Si vous avez une version différente, il se pourrait que le VPN ne fonctionne pas.

## Installation avec snap

Si vous utilisez Ubuntu, snap est déjà installé. Sinon, vous pouvez exécuter :

```
sudo apt install snapd gnome-software-plugin-snap
```

Puis, cherchez **RiseupVPN** dans la **Logithèque** ou cliquez sur ce lien :

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Ouvrir RiseupVPN dans la Logithèque
</a>

Si le lien ci-dessus ne fonctionne pas pour vous, il est également possible de faire l'installation en ligne de commande :

```
sudo snap install --classic riseup-vpn
```

Si jamais un message d'erreur apparaît indiquant que "python" est manquant dans /usr/bin/env, il est nécessaire d'installer python. C'est par exemple le cas dans Lubuntu depuis la version 19.04.

## Installation du paquet

Le VPN est empaqueté dans Debian bookworm et les versions suivantes, installez-le en exécutant la commande suivante dans un terminal, ou cherchez le paquet `riseup-vpn` dans votre gestionnaire de paquets préféré :

       sudo apt install riseup-vpn

Les vieilles versions ne sont actuellement pas supportées (mais vous pouvez utiliser la méthode snap au-dessus).

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

### RiseupVPN sur Linux Mint

Dans Linux Mint, Snap est parfois désactivé par défaut, il faudra alors commencer par l'activer avec la commande suivante :

```
sudo mv /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.pref.disabled
```

Puis installer Snap :

```
sudo apt install snapd
```

Installer RiseupVPN depuis Snap :

```
sudo snap install --classic riseup-vpn
```

Ajouter l'entrée RiseupVPN dans le menu de Linux Mint :

```
cp /var/lib/snapd/desktop/applications/riseup-vpn_riseup-vpn.desktop /usr/share/applications/
```


### Tester une version de développement

Si vous souhaitez nous aider à tester une version de développement de RiseupVPN, vous pouvez l'installer en exécutant cette commande :

```
sudo snap install --classic --beta riseup-vpn
```

### Supprimer le fichier PID

Parfois, RiseupVPN ne démarre pas car le programme croit qu'il y a déjà une version en cours d'exécution.

Si vous avez cette erreur, exécutez ces commandes :

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

## Code source
Les clients RiseupVPN sont basés sur le logiciel libre Bitmask. Le code du client Linux se trouve [[ici => https://0xacab.org/leap/bitmask-vpn]].
