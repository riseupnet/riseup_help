@nav_title = "Dépannage"
@title = "VPN Riseup : Dépannage"
@summary = "Instructions de dépannage"

## Compte

Les problèmes suivants ont été remarqués pendant la période beta.

### Je ne peux pas m'inscrire avec mon nom d'utilisateur / Quelqu'un a pris mon nom d'utilisateur

Nos services de sécurité sont réalisés en utilisant la plateforme  [LEAP (qui est un projet pour l'accessibilité du chiffrement)](https://leap.se). C'est une infrastructure complètement différente et qui n'est pas directement liée avec nos services email ou pour les listes. Vous pouvez accéder à ces services par ce lien : https://black.riseup.net .

Cela veut aussi dire que vous allez avoir besoin de créer un nouveau compte pour utiliser le VPN et les autres services qui viendront. Mais pour éviter des problèmes avec les noms d'utilisateurs, nous avons mis tous les noms d'utilisateur actuellement utilisés sur riseup.net avec un statut "réservé". Mais ne vous inquiétez pas, plus tard dans l'année vous allez pouvoir transférer votre compte actuel (et notamment votre nom d'utilisateur) vers le nouveau, beaucoup plus sécurisé.


### Mon nom d'utilisateur ou mon mot de passe ne marchent pas !

Reportez vous à la question juste au-dessus !

## Bitmask

Les points suivants ont été identifiés comme problématiques dans certains environnements.

### Je n'utilise pas Debian et/ou Ubuntu. Comment puis-je installer Bitmask ?

Si vous utilisez une distribution basée sur Debian (comme CrunchBang) ou basée sur Ubuntu (comme Mint), vous devez installer [l'application autonome](#stand-alone-bundle) et nous aimerions beaucoup avoir un retour concernant l'installation de Bitmask ! Il y a énormément de distributions GNU/Linux et il n'y a aucun moyen de tester tout les environnements possibles. Si vous avez pu l'installer, faites le nous savoir... et si vous n'avez pas pu, nous attendons vraiment que vous nous le signaliez. Dans tout les cas, **Bitmask devrait marcher sur n'importe quel système moderne GNU/Linux**. 


### Je ne peux me connecter à aucun/quelques/beaucoup de sites

Exécutez les commandes suivantes et essayer les différentes solutions possibles.

#### Exécutez `sudo ip route`, cherchez la ligne commençant par 'default' et regardez si 'tun0' est la valeur après le mot 'dev'

Il y a un bug dans le gestionnaire de réseau de Debian (qui est une version test et non stable). Si vous utilisez ce gestionnaire, vous aurez probablement à faire à ce problème. Vous pouvez en lire plus concernant ça sur [Debian Bug #23755015](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23755015).

Une solution éventuelle :

    sudo ip route del default
    sudo ip route add default via 10.42.0.1 dev tun0

#### Mon problème n'apparaît pas ci-dessus... Qu'est ce que je fais maintenant ?

La première chose est de savoir ce qui cause le problème, pour obtenir cette information, ouvrez votre terminal et exécutez la commande `bitmask --debug --logfile /tmp/bitmask.log`. Cela lancera Bitmask en mode "debug" et enregistrera les résultats dans un fichier texte sur `/tmp/bitmask.log`. Si vous êtes un utilisateur expérimenté, vous pouvez peut-être avancer encore un peu dans la résolution du problème. Sinon, faites un ticket avec le contenu du fichier `/tmp/bitmask.log` et le système d'exploitation que vous utilisez (Debian Wheezy, Mint 17, Ubuntu Trusty, etc).

## Autres problèmes

### Une fenêtre "Configure Bitmask email Account" apparaît à chaque fois que je lançe Thunderbird/Icedove

Le paquet `xul-ext-bitmask` était installé. Ce n'est pas une dépendance mais un paquet suggéré qui contient une extension Thundebird/Icedove pour encourager à utiliser LEAP comme service de messagerie. Vous pouvez le supprimer si vous voulez, exécutez cette commande `sudo apt-get remove xul-ext-bitmask` et redémarrer votre client mail Thunderbird/Icedove.

....

