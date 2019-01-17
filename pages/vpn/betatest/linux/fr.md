@title = "RiseupVPN pour Linux"
@this.alias = '/vpn/linux'

## Exigences

En ce moment, RiseupVPN n'est disponible sous Linux qu'en utilisant `snap`. Si vous utilisez Ubuntu, snap est déjà installé. Sinon, vous pouvez exécuter:

```
sudo apt install snapd
```

RiseupVPN est actuellement à l'essai sur **Ubuntu LTS** et **Debian Stable**. Si vous avez une version différente, il se pourrait que le VPN ne fonctionne pas.

## Installation

Cherchez **RiseupVPN** dans la **Logithèque** ou cliquez sur ce lien:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Ouvrir RiseupVPN dans la Logithèque
</a>

Si le lien ci-dessus ne fonctionne pas pour vous, il est également possible de faire l'installation en ligne de commande:

```
sudo snap install --classic riseup-vpn
```

## Problèmes

### Rapport de bug et demandes de fonctionnalités 

RiseupVPN utilise un programme libre nommé <b>bitmask-vpn</b>.

**Étape 1:** [[Parcourez => https://0xacab.org/leap/bitmask-vpn/issues]] pour voir si le bug a déjà été identifié.

**Étape 2:** [[Créez un compte => https://0xacab.org/users/sign_in]] sur [[0xacab.org => http://0xacab.org]] et connectez-vous.

**Étape 3:** Créez un nouveau [[rapport de bug ou une nouvelle demande de fonctionnalité => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Veuillez inclure les détails suivants dans votre rapport de bug:

* Les étapes pour reproduire le bug
* Ce que que le programme était supposé faire et ce qui est réellement arrivé
* Une capture d'écran si c'est pertinent
* Votre distribution Linux et sa version
* Le journal du programme

### Récupérez le journal

Le journal de RiseupVPN est situé dans votre répertoire personnel:

```
~/.config/leap/systray.log
```

Quand vous rapportez un bug, c'est très utile d'inclure le fichier de journal.

### Forcer la fermeture

Si quelque chose arrête de fonctionner, exécutez ces commandes et essayez de nouveau:

```
sudo pkill -e -f riseup-vpn
sudo /snap/bin/riseup-vpn.bitmask-root firewall stop
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

Ces commandes s'assurent que tous les processus RiseupVPN sont fermés, que les sorties de pare-feu sont supprimées et le que fichier PID est nettoyé.

### Le VPN ne démarre pas

Si l'icône dans la barre de lancement ne fonctionne pas, vous pouvez exécuter RiseupVPN à partir de la ligne de commande pour identifier le problème:

```
/snap/bin/riseup-vpn.launcher
```

Tous les problèmes de démarrage s'afficheront sur le terminal.

### Tester une version de développement

Si vous souhaitez nous aider à tester une version de développement de RiseupVPN, vous pouvez en installer une en exécutant cette commande:

```
sudo snap install --classic --beta riseup-vpn
```

### Supprimer le fichier PID

Parfois, RiseupVPN ne démarre pas car le programme croît qu'il y a déjà une version en cours d'exécution.

Si vous avez cette erreurs, exécutez cette commande:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```
