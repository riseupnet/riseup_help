@nav_title = "GNU/Linux"
@title = "Comment faire: GNU/Linux"
@summary = "Bitmask sur Linux : Obtenir, installer et configurer"

Pour utiliser le service VPN de Riseup vous allez avoir besoin d'un compte LEAP (propulsé par Riseup). Vous pouvez en créer un depuis Bitmask (le client LEAP) ou depuis [https://black.riseup.net/signup](https://black.riseup.net/signup). **Il est recommandé de vous inscrire depuis l'application Bitmask sauf si vous pensez utilisez le VPN seulement depuis Android.**

## Obtenir et installer Bitmask

L'application Bitmask pour GNU/Linux peut être obtenue de deux manières. Si vous utilisez [Ubuntu](#ubuntu) ou [Debian](#debian) vous pouvez ajouter le dépôt logiciel Bitmask pour garder votre version à jour. Autrement vous pouvez télécharger [l'application autonome](#stand-alone-bundle), que vous pouvez exécuter depuis un média externe comme une clé USB. Soyez conscient que l'application autonome sera plus lente, prendra plus de place et sera moins intégrée au bureau qu'avec le paquet Ubuntu/Debian et vous devrez la mettre à jour manuellement.

**Nous recommandons d'utiliser le paquet Ubuntu/Debian.** Cependant, si le paquet ne marche pas pour votre distribution, vous devez utilisez l'application autonome.

### Ubuntu

Les étapes décrites ci-dessous ajouteront le dépôt Bitmask sur votre système. Ces commandes doivent être exécutées sur un terminal, une par une après avoir entré votre mot de passe sudo. Les informations concernant le dépôt seront stockées dans `/etc/apt/sources.list.d/bitmask.list`.

#### Installer sur Trusty Thar (14.04)

	echo "deb http://deb.bitmask.net/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Désinstaller

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### Debian

Les étapes décrites ci-dessous ajouteront le dépôt Bitmask sur votre système. Ces commandes doivent être exécutées sur un terminal, une par une après avoir entré votre mot de passe sudo. Les informations concernant le dépôt seront stockées dans `/etc/apt/sources.list.d/bitmask.list`.

#### Installer sur Wheezy (Debian 7)

Vous avez besoin d'ajouter `wheezy-backports` comme étant une source logicielle.

	echo "deb http://deb.bitmask.net/debian wheezy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Installer sur Jessie (Debian 8)

	echo "deb http://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Installer sur Jessie en utilisant le réseau anonymisé Tor :

	sudo apt-get install apt-transport-tor
	echo "deb tor://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Désinstaller

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### L'application autonome

L'application autonome Bitmask devrait fonctionner pour les versions récentes des distributions GNU/Linux dérivées de Debian (Mint, Ubuntu, Elementary, etc). Souvenez-vous que c'est vous la personne chargée de garder ce logiciel à jour.

Pour avoir l'application, il faut déjà que vous déterminiez le type de noyau que vous avez. Cela peut être fait avec cette commande : `uname -m`.

#### 64bits

Si le résultat de cette commande est 'x86_64' ou 'amd64' alors téléchargez la dernière version disponible sur [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2) et sa signature OpenPGP sur [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc). 

Les commandes suivantes téléchargeront et vérifieront l'authenticité de l'application.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc
	gpg --verify Bitmask-GNU/Linux64-latest.tar.bz2.asc Bitmask-GNU/Linux64-latest.tar.bz2

Si vous obtenez 'Correct signature' ou 'Good signature' en résultat, décompresser avec cette commande :

	tar xfj https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2

#### 32bits

Si le résultat de cette commande est 'i686' ou 'i386' alors téléchargez la dernière version disponible sur [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2) et sa signature OpenPGP sur [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc).

Les commandes suivantes téléchargeront et vérifieront l'authenticité de l'application.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc
	gpg --verify Bitmask-GNU/Linux32-latest.tar.bz2.asc Bitmask-GNU/Linux32-latest.tar.bz2


Si vous obtenez 'Correct signature' ou 'Good signature' en résultat, décompresser avec cette commande :

	tar xfj Bitmask-GNU/Linux32-latest.tar.bz2

## Utiliser Bitmask pour la première fois

Quand vous lancez Bitmask pour la première fois, nous aurons besoin de configurer Riseup comme le fournisseur LEAP. Ces étapes vous guideront dans cet objectif.

h3. Créer un compte LEAP propulsé par Riseup

![Etape 1](Bitmask-1.png)

Sélectionner sign up for a new account et cliquer sur le bouton *next*.

![Etape 1](Bitmask-2.png)

Sélectionner Configure a new provider et remplissez le champ demandé avec 'riseup.net'. Après ça, cliquer sur le bouton *check*.

![Etape 3](Bitmask-3.png)

Bitmask doit être sûr que riseup.net est un fournisseur valide. Après cette vérification, cliquer sur *next* pour continuer. S'il y a un problème à cette étape, allez dans la section Dépannages sur cette page

![Etape 4](Bitmask-4.png)

Si tout est bien allé, vous devrez voir ça sur l'écran. Cliquer sur *next* après ça.

![Etape 5](Bitmask-5.png)

Bitmask doit vérifier qu'il peut se connecter de manière sécurisé à riseup.net. Après ça, cliquer sur *next* pour continuer. S'il y a un problème à cette étape, allez dans la section Dépannages sur cette page.

![Etape 6](GNU/Linux/Bitmask-6.png)

La prochaine étape permet de définir un nom d'utilisateur et un mot de passe pour votre compte. Prenez soin de bien vous souvenir de ces informations.

Il faut savoir qu'à cette étape de la version beta, les noms d'utilisateurs actuels sont réservés et ne peuvent pas être utilisés. Vous devez donc en créer un nouveau. Pas d'inquiétude : il sera utile seulement pour ce service et pendant la beta.

![Step 6](Bitmask-7.png)

Message de confirmation. Vous pouvez laissez Bitmask se souvenir de votre nom d'utilisateur et de votre mot de passe. Si vous faites ce choix, notez quand même ces informations quelque part ! Cliquez sur *next* pour continuer.

![Etape 7](Bitmask-8.png)

Sélectionnez Encrypted Internet et Connect. Bienvenue dans le service VPN de Riseup. Yeah !

## Dépannages

Allez dans la [[section Dépannages -> troubleshooting]].

