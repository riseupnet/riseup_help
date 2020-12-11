@title = 'Pidgin'

## À propos de Pidgin

![logopidgin](logo.pidgin.png)

Pidgin est le client de messagerie instantanée le plus populaire sous GNU/Linux, Windows, et macOS. Vous pouvez le télécharger sur https://pidgin.im/download. Pour OSX, jetez un coup d'oeil à [[Adium]], il s'agit d'une version native de pidgin pour OSX.

## Configurer un compte

Quand vous lancez pidgin pour la première fois, cliquez sur le boutton `Ajouter...` pour ajouter un nouveau compte.

(1) Sous l'onglet `Essentiel`, mettez les valeurs suivantes:

![newaccountbasictab](new-account-basic-tab.png)

- `Protocole`: XMPP
- `Utilisateur`: votre nom d'utilisateur Riseup
- `Domaine`: riseup.net
- `Mot de passe`: votre [[mot de passe Riseup => riseup-password]]

Accessoirement, vous pouvez mettre un alias local qui sera votre nom et une icône que les autres utilisateurs verront dans leur client XMPP.

## Pour utiliser OTR

Voir le tutoriel [[otr]] pour plus de détails sur l'utilisation de l'encryption bout-à-bout avec Pidgin.

## Sécuriser Pidgin sous GNU/Linux avec ["AppArmor"](https://gitlab.com/apparmor/apparmor/wikis/home/)

Nous vous recommandons de suivre les étapes suivantes pour sécuriser Pidgin sous GNU/Linux

- copiez usr.bin.pidgin vers `/etc/apparmor.d/usr.bin.pidgin`
  * [usr.bin.pidgin sous Ubuntu 14.04](https://bazaar.launchpad.net/~apparmor-dev/apparmor-profiles/master/view/head:/ubuntu/14.04/usr.bin.pidgin)
- redémarrez apparmor
`sudo /etc/init.d/apparmor restart`
- redémarrez pidgin

## Configuration de Tor avec Pidgin

Pour configurer Pidgin pour utiliser Tor, vous devez modifier la configuration de votre compte de la façon suivante:

Premièrement choisissez `Modifier le compte`...

![pidginmodifyaccount](pidgin-modify-account.png)

Ensuite, allez sous l'onglet `Avancé` et mettez les valeurs suivantes:

- `Sécurité de la connexion`: Nécessite chiffrement
- `Port de connexion`: 5222
- `Serveur de connexion`: [[page Tor => tor#riseups-tor-hidden-services]]
- `Proxy pour le transfert de fichiers`: proxy.riseup.net

Finalement, allez sur l'onglet `Proxy`...

![pidginmodifyaccountproxy](pidgin-modify-account-proxy.png)

Mettez le type de proxy à `Socks5` et mettez les valeurs suivantes:

- `Hôte`: 127.0.0.1
- `Port`: 9050
- `Utilisateur`: votre nom d'utilisateur
- `Mot de passe`: votre mot de passe
