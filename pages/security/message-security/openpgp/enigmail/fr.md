@title = 'Encrypter des courriels avec Thunderbird'

Vous souhaitez améliorer la sécurité de vos courriels en apprenant comment utiliser OpenPGP avec Thunderbird? Ce court tutoriel vous aidera à encrypter et à décrypter vos courriels et à vérifier que les courriels que vous recevez ont bien été envoyés par les personnes qui prétendent l'avoir fait.

h2. Avant de commencer

Nous vous recommandons de commencer par lire notre guide [[gpg-best-practices]]. Il est particulièrement important de vous assurer que vous avez configuré votre client gpg manière à avoir une clef robuste *avant de la générer*, car les paramètres par défaut ne sont pas optimaux.

Si vous avez déjà une clef, vous devriez [[vérifier qu'elle est bien robuste -> /gpg-best-practices#openpgp-key-checks]] avant de continuer.

h2. Installer Enigmail et configurer OpenPGP avec l'assistant d'installation

Enigmail est une extension de Thunderbird qui permet d'utiliser l'encryption OpenPGP avec vos courriels.

# (optionnel) Vous pouvez laisser Enigmail générer une paire de clefs pour vous ou vous pouvez [[générer une paire de clefs OpenPGP manuellement =>  /security/gpg-keys]]
# Téléchargez "Enigmail":https://www.enigmail.net **Sur Linux** - Il est préférable d'installer l'extension plutôt que d'utiliser le paquet fournir par votre gestionnaire de programmes, qui risque de ne pas être à jour. Thunderbird met à jour Enigmail automatiquement.
# Naviguez vers **Outils** -> **Modules complémentaires**
# Cliquez sur **Installer un module depuis un fichier**
# Naviguez vers le fichier .xpi d'Enigmail et sélectionnez **Ouvrir**. Enigmail s'installera.
# Redémarrez Thunderbird si nécessaire
# Naviguez vers le nouveau menu intitulé **Enigmail** -> **Assistant de configuration**
# Sélectionnez **Oui** et cliquez sur **Suivant**
# Si vous avez plusieurs identités Thunderbird, décidez si vous souhaitez configurer OpenPGP pour toutes vos identités ou seulement pour certaines d'entre elles. Si vous avez plusieurs identités, choisir de configurer OpenPGP pour l'ensemble d'entre elles n'utilisera qu'une seule clef.
# Choisissez si vous souhaitez signer l'ensemble de vos messages sortants. **Signer un message ne l'encrypte pas** -- cela ne fait que placer votre signature électronique pour permettre aux autres de vérifier que c'est bien vous qui avez envoyé le message. Il est recommandé **de ne pas signer vos messages sortant** non encryptés car cela permet de vous lier directement à votre courriel.
# Décidez si vous voulez encrypter vos messages sortants par défaut. **Ceci n'est pas recommandé** car il se peut que vos destinataires ne supportent pas les courriels chiffrés. Vous pouvez configurer des règles d'encryption plus tard, ce qui vous permettra d'encrypter vos courriels dans les conditions voulues.
# Choisissez d'effectuer les changements recommandés par OpenPGP. Ce sont tous des changements techniques qui augmentent la compatibilité de Thunderbird et OpenPGP. Tous ces changements sont sécuritaires, même si parfois ils changent certaines fonctionnalités comme la composition des messages en HTML.
# Créez une clef si vous ne l'avez pas déjà fait ou alors sélectionnez votre clef déjà existante. Si vous avez plusieurs clefs ou plusieurs identités, vous devrez faire des changements manuellement pour associer la bonne clef à la bonne identité.
# Vérifier les changements et cliquez sur **Suivant**.
# S'il n'y a pas d'erreurs, OpenPGP est prêt à être utilisé. Cliquez sur **Terminer**

h2. Mettre en place des règles OpenPGP

Dans Thunderbird, le module complémentaire Enigmail permet d'écrire des règles qui expliquent à Thunderbird qui doit recevoir des courriels encryptés et qui doit recevoir des courriels en clair.

Le système de règles est relativement puissant et permet de créer une vaste éventail de possibilités. Ce guide va vous guider pour créer des règles qui envoient toujours des messages encryptés pour une adresse courriel spécifique (ou pour plusieurs adresses) et qui prennent pour acquis que vos messages ne sont pas encryptés par défaut. Cependant, le système de règles est assez puissant pour que si jamais la grande majorité de vos contacts utilisent des courriels encryptés, vous pouvez encrypter l'ensemble de vos courriels par défaut et écrire une règle pour envoyer des courriels en clair aux quelques autres contacts .

# Naviguez vers **OpenPGP** -> **Modifier les règles par destinataires**
# Cliquez sur le bouton **Ajouter** dans le coin droit, en haut.
# Entrez les adresses courriels dans le haut de la page, séparées par des espaces si vous rentrez plusieurs adresses et cliquez sur **Est exactement**.
# Choisissez **l'Action** à appliquer pour la règle. Pour cet exemple, choisissez **Utilisez les clefs OpenPGP suivantes:** et cliquez sur le bouton **Sélectionner les clefs...**. Dans la fenêtre qui s'ouvre, sélectionnez la clef OpenPGP de la personne à qui vous souhaitez envoyer le courriel. Si vous n'avez pas sa clef publique, cliquez sur le bouton **Télécharger les clefs manquantes**, ce qui lancera une recherche sur un serveur de clefs pour les courriels entrés plus tôt.
# Changez **Chiffrement** dans la section **Par défaut pour...** à **Toujours** et laissez la signature et le PGP/MIME à **Oui, si sélectionné lors de la composition du message**
# Appuyez sur le bouton **OK** quand vous avez complété la configuration de la règle. !enigmail-create-rule.gif!

Vous êtes maintenant prêt-e à envoyer des courriels OpenPGP (GPG) à n'importe quel destinataire et à laisser Thunderbird activer l'encryption automatiquement pour les destinataires choisis dans les règles que vous venez de créer.
