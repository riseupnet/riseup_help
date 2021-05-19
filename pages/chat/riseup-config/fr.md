@title = "Chat Riseup"
@nav_title = "Riseup config"

## Qu'est-ce que XMPP ?

XMPP est un protocole de messagerie instantanée ainsi que de chat audio et vidéo. XMPP permet d'envoyer et de recevoir des messages entres utilisateurs, et ce, peu importe le fournisseur parmi les milliers disponibles.

## Utiliser le service XMPP de Riseup

Votre adresse email riseup.net sert aussi d'adresse XMPP. Une personne souhaitant vous envoyez un message ou une demande d'amitié n'a qu'à l'envoyer à `utilisateur@riseup.net`.

Pour configurer votre [[client XMPP => chat/clients]], vous aurez besoin des informations suivante:

- **protocole**: "xmpp"
- **compte**: `utilisateur@riseup.net`
- **mot de passe**: votre [[mot de passe Riseup -> human-security/riseup-password]]

Il est vraiment important de toujours configurer son client à **nécessite chiffrement**. Certains clients on une option "utiliser le chiffrement si disponible", mais ce n'est pas assez. En effet, même si les serveurs de riseup.net demandent le chiffrement, si votre client est configuré à "utiliser le chiffrement si disponible", un attaquant pourra facilement récupérer votre mot de passe.

Certains clients XMPP vont demander votre nom d'utilisateur et le domaine séparément. Dans ce cas, vous devrez spécifier les informations suivante:

- **nom d'utilisateur**: `utilisateur`
- **domaine**: `riseup.net`

Pour des tutoriels spécifiques aux clients, vous pouvez regarder la page sur les [[clients XMPP => chat/clients]].

## Se connecter à des _chatrooms_ multi-utilisateurs

La syntaxe pour créer ou se connecter à un _chatroom_ sur le réseau XMPP de Riseup est la suivante:

- `votre-nom-de-chatroom@conference.riseup.net`

Si vous avez besoin de spécifiez le _chatroom_ séparément:

- **chatroom**: `votre-nom-de-chatroom`
- **domaine**: `conference.riseup.net`

Ne faites pas ça:

- `votre-nom-de-chatroom@riseup.net`

### Utiliser les _chatrooms_ avec pidgin

Pour joindre ou créer un _chatroom_ en étant connecté avec [[pidgin]], vous devez cliquer sur `Add room` dans le menu `Buddy`.

- **Room**: `votre-nom-de-room`
- **Serveur**: `conference.riseup.net`
- **Surnom**: `votre-surnom`
- **Mot de passe**: [optionnel]
- **Alias**: [optionnel]
- **Groupe**: [optionnel]

Cliquer sur `Ok` et regarder la liste de **buddy**. Vous devriez voir un groupe `Chat` avec la liste des **chatroom**.
Cliquez droit sur un **chatroom** et sélectionnez `join`.

Pour tester, vous pouvez sélectionner le **chatroom** `riseup.net` et le joindre.

## Pour plus de sécurité

Pour plus de sécurité, accédez à notre serveur XMPP en utilisant le [[VPN Riseup => vpn]] ou avec ce ["service caché"](https://www.torproject.org/docs/hidden-services.html.en): Regardez la [[page Tor => tor#riseups-tor-hidden-services]] pour une liste complètes de nos services cachés.

