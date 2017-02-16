@title = 'Connexions sécurisées'

h2. Qu'est-ce qu'une connexion sécurisée?

Vous devriez utiliser une forme de chiffrement quand vous utilisez les services de Riseup. Si vous n'utilisez pas des connexions sécurisées, votre trafic internet n'est pas chiffré. Cela veut dire qu'une personne qui le souhaite peut espionner vos courriels ou pire encore obtenir votre mot de passe et votre nom d'utilisateur. Avec des connexions non sécurisées, il est également possible de se faire passer pour nos serveurs à votre insu. Mettre en place une connexion sécurisée avec Riseup permet une protection raisonnable contre l'espionnage et les imposteurs.

h2. Comment utiliser une connexion sécurisée?

Pour faire en sorte que votre client de messagerie utilise une connexion sécurisée, vous allez devoir modifier certains paramètres. Ne vous en faîtes pas! Nous vous aiderons pas à pas.

Si vous savez que vous utilisez Thunderbird, vous pouvez passer directement à la [[section sur Thunderbird => /secure-connections#thunderbird]] pour voir quels paramètres changer. Si vous utilisez un client de messagerie différent, il vous faut lire la section sur les [[paramètres généraux =>/secure-connections#general-settings]]. Si vous n'avez aucune idée du client de messagerie que vous utilisez, lisez la section ci-dessous et nous vous apprendrons à le reconnaître.

h2. Qu'est-ce qu'un client de messagerie?

Qu'est-ce qu'un client de messagerie? Un client de messagerie est un programme spécifique qui permet de lire et de composer des courriels. Il peut être Thunderbird, Apple Mail, Outlook, Eudora, etc. Peu importe son nom, le logiciel que vous utilisez pour lire et écrire des courriels est votre client de messagerie.

h2. Paramètres généraux

Peu importe le client de messagerie, vous devez être en mesure de modifier votre configuration pour vous assurer que votre client est paramétré pour utiliser les standards SSL ou TLS sur toutes vos connexions (que ce soit pour les connexions POP, IMAP ou SMTP). Il faut également que vous vous assuriez que vous utilisez les bons ports de connexion. Si vous ne savez pas ce que tout ceci veut dire, ne vous en faites pas: nous allons vous montrer comment faire.

La marche à suivre pour les différents programmes est très différente. C'est parfois également le cas entre diverses versions d'un même programme.

En général, nous n'offrons pas de support pour les clients de messagerie. Cependant, nous avons [[de l'information générale sur la configuration à suivre pour les divers clients de messagerie => email/clients]]. Si votre client de messagerie est dans cette liste, ces informations vous aiderons à faire les modifications nécessaires.

Si vous n'utilisez pas Mozilla Thunderbird, nous aimerions prendre un instant pour vous convaincre d'y migrer. C'est un programme relativement sécuritaire, facile à utiliser et qui est un logiciel libre. Il n'y a pas de mal à l'essayer! [[Le mieux, c'est que nos instructions pour paramétrer Thunderbird => thunderbird]] sont réellement excellentes. De plus, comme nous connaissons mieux ce programme que les autres, il nous est plus facile de vous aider en cas de problème.

Si vous ne souhaitez pas utiliser Thunderbird, que vous n'êtes pas familières ou familiers avec la manière de faire ces changements et que nos pages d'aides ne vous aident pas, vous devrez aller demander de l'aide aux personnes proches de vous qui s'y connaissent en informatique. La compagnie ou la communauté qui développe votre logiciel peut aussi peut-être vous aider.

h2. Thunderbird

Pour faire les modifications requises dans Thunderbird, suivez ces étapes:

Premièrement, il vous faut trouver la version de Thunderbird que vous utilisez en cliquant sur le menu "Aide" --> "À propos de Thunderbird"

Une fois que vous avez déterminé la version du logiciel, suivez le guide ci-dessous. Si vous utilisez Thunderbird 2.x ou une version encore plus ancienne, vous devez vraiment la mettre à jour! Malheureusement nous ne pouvons pas vous expliquer comment faire ici, mais vous pouvez trouver un grande quantité d'information en ligne si vous faites une recherche pour « mises à jour Thunderbird ».

h3. Thunderbird 3.x ou plus récent

Pour paramétrer Thunderbird 3.x ou une version plus récente de manière sécuritaire, veuillez suivre ces étapes:

* Choisissez l'option "Paramètres des comptes" dans le menu "Édition"
* Sélectionnez "Paramètres serveur" sous votre nom de compte Riseup dans la fenêtre qui viens de s'ouvrir
* Au milieu de la fenêtre, vous verrez alors un entête intitulé "Paramètres de sécurité"
* Sous cet entête se trouve un menu déroulant nommé "Sécurité de la connexion"
* Ce menu déroulant doit être mis à l'option "SSL/TLS"
* Dans le coin supérieur droit de la fenêtre se trouve un paramètre nommé "Port"
* Ce paramètre devrait être paramétré automatiquement, mais c'est une bonne idée de le vérifier tout de même
** Le numéro de port devrait être 993 si vous utilisez IMAP
** Le numéro de port devrait être 995 si vous utilisez POP
* Une ligne nommée "Type de serveur" en haut de la fenêtre vous indique si vous utilisez IMAP ou POP
* Ensuite, cliquez sur l'option "Serveur sortant (SMTP)" dans le menu de gauche
* Cliquez une fois sur le serveur SMTP Riseup dans la liste à droite
* Cliquez sur le bouton "Modifier" complètement à droite de la fenêtre
* Assurez-vous que le paramètre "Sécurité des connexions" est à "SSL/TLS"
* Assurez-vous que le paramètre "Port" est à 465
* Cliquez sur "OK"
* Cliquez sur "OK" une seconde fois
* En aucun cas vous ne devriez modifier le paramètre "Méthode d'authentification". Il devrait être laissé à "Mot de passe normal"
* Et voilà, vous avez fini! Bravo!!

h2. iOS

Si vous avez un appareil Apple, vous pouvez lire nos [[instructions->https://help.riseup.net/fr/iphone-mail]] pour savoir quels paramètres il est nécessaire de modifier pour sécuriser vos connexions.

h2. FAQ

Q: Et si j'utilise la messagerie web, est-ce sécuritaire?

R: Quand vous utilisez le web, vous faites des connexions depuis votre ordinateur, à travers divers serveurs sur l'internet, vers le serveur que vous tentez de visiter. Vous faites de connexions en utilisant quelque chose nommée "HTTP. Cette connexion est faite en clair et n'est pas sécuritaire. Des attaquant-e-s peuvent avoir accès à vos comptes en ligne ainsi qu'à toute l'information que vous envoyez ou que vous recevez en ligne. Il y a cependant de l'espoir! Il y a une version sécurisée de "HTTP" nomée "HTTPS" (remarquez ici le petit 's' pour sécurisé). HTTPS est construite pour fournir des connexions sécurisés qui résistent aux attaques.

Pour plus de sécurité, vous devriez considérer la vérifier si les sites webs que vous visitez sont biens ceux qu'ils prétendent être. Quand vous utilisez HTTPS, vous recevez un certificat du serveur qui est supposé prouver qu'il est authentique. Pour vérifier que le site est bien celui que vous tentez de visiter, vous [[devriez vérifier que le certificat qui vous est présenté est le bon => /certificates]].

Il existe cependant des problèmes avec les certificats et vous devriez en être conscient-e-s (voir plus bas les limites des connexions sécurisées).

Regardez dans la barre d'URL, où l'adresse d'un site se trouve. Si elle commence par <code>https://</code> (NOTEZ le 's'), alors vous avez une connexion sécurisé. Si vous ne voyez que <code>http://</code> (SANS 's'), alors votre connexion n'est pas sécurisée. Vous pouvez changer le "http" pour "https" en cliquant dans la barre d'URL, en y ajoutant le 's' et en pesant sur la touche "Entrée" pour charger la page de manière sécurisée.

Une troisième manière de faire (elle est très peu fiable) est de chercher la petite image de cadenas. Elle apparaît soit dans la basse d'URL, soit en bas de la fenêtre de navigation (sa place diffère d'un navigateur à l'autre). Ce petit cadenas devrait être fermé. Si le cadenas n'existe pas ou qu'il semble être ouvert, votre connexion n'est pas sécurisée. Vous pouvez toujours déplacer votre souris sur cette image pour avoir plus d'informations. Souvent vous pouvez obtenir plus d'informations sur le certificat SSL utilisé en cliquant (clic gauche ou droit) sur ce cadenas.

Q: Qu'est-ce que POP/IMAP & SMTP?

R: POP et IMAP sont deux protocoles communs qui sont utilisés par des programmes pour récupérer des courriels sur un serveur distant. La plupart du temps vous utiliserez l'un ou l'autre, mais jamais les deux en même temps. SMTP est un autre protocole courant, mais qui sert à envoyer des courriels de votre ordinateur au serveur de courriels.

Q: Si je configure mon client de messagerie, quels ports devrais-je utiliser?

R: Pour les connexions POP utilisez TLS, avec le port numéro 995.
   Pour les connexions IMAP utilisez TLS, avec le port numéro 993.
   Pour les connexions SMTP utilisez TLS, avec le port numéro 465.

Q: Que faire si j'ai plus de questions sur l'utilisation sécuritaire des courriels?

R: Si, après avoir lu avec attention [[les pages d'aide de Riseup => https://help.riseup.net/fr]] et que vous avez toujours des questions, nous vous encourageons à ouvrir [[un billet d'aide Riseup => https://support.riseup.net/fr/topics/new]]. Nous sommes enjoués d'aider les personnes qui utilisent nos services à comprendre comment sécuriser leurs communications et à améliorer la défense de la vie privée de toutes les personnes en ligne.

h2. Les limites des connexions sécurisées

Maintenant que vos connexions sont sécurisées, tout est parfaitement sécurisé, n'est-ce pas? Malheureusement, ce n'est pas le cas! Les connexions sécurisées ne sécurisent que le transport des données elles-mêmes: elles ne garantissent pas la confidentialité des données. Par exemple, quand vous envoyez des courriels en utilisant une connexion sécurisée, ces derniers sont chiffrés par nos serveurs. Avant d'être livrés aux récipiendaires finaux, vos messages font cependant de nombreux "sauts" d'un serveur à l'autre. Ces "sauts" sont rarement chiffrés, ce qui crée de nombreuses opportunités d'avoir accès à vos courriels, tant pendant le "transit" sur internet que quand ils sont "au repos" sur les serveurs courriels ou sur la machine des récipiendaires. Passer à une connexion sécurisée est la seule manière de vous assurer que votre nom d'utilisateur et votre mot de passe sont en sécurité quand vous vous connectez sur nos serveurs.

Que pouvez-vous donc faire pour améliorer la sécurité de vos communications par courriel? Si vous voulez une sécurité bout-à-bout pour vos courriels vous devez [[utiliser un chiffrement fort comme OpenPGP => openpgp]] et convaincre les personnes avec qui vous communiquez de faire de même. Il existe un [[plugin Thunderbird nommé Enigmail => enigmail]] qui vous permet d'intégrer facilement un chiffrement fort dans Thunderbird.

La sécurité sur le web tourne autour d'HTTPS. Cela implique de déterminer si un certificat particulier pour un serveur devrait être considéré comme "valide" par un navigateur web. La manière dont cela fonctionne en ce moment est qu'une liste d'autorités de certification à qui l'on fait "confiance" est distribuée par votre navigateur. C'est nul, parce que cela vous force à faire confiance à une autorité centrale pour valider si vos connexions sont sécurisées. Pourquoi devriez-vous faire confiance à une autorité auto-proclamée pour utiliser des connexions sécurisées? Pour plus d'informations sur pourquoi cela est une mauvaise idée, vous pouvez lire cette article qui explique [[comment l'architecture technique forme nos structures sociales => http://lair.fifthhorseman.net/~dkg/tls-centralization/]] et comment cette hiérarchie centralisée du contrôle est extrêmement problématique.
