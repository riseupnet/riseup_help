@title = 'Cryptage des courriels avec OpenPGP'
@nav_title = 'Courriels cryptés'

h2. Qu'est-ce qu'un courriel crypté?

Crypter un courriel permet d'éviter que son contenu ne soit intercepté pendant qu'il circule sur internet. Le type le plus commun de cryptage est l'OpenPGP (OpenPGP est un standard, PGP vient de l'anglais «Pretty Good Privacy» et est propriétaire et GNU Private Guards, ou GPG, est un logiciel libre). Plusieurs ressources sur internet offrent une explication détaillée du fonctionnement du cryptage. Pour nos besoins, il est utile d'en comprendre trois composantes: la *clé publique*, la *clé privée* et la *phrase secrète*.

Votre *clé publique* doit être, comme vous l'avez deviné, rendu public. On utilise parfois des serveurs pour partager les clés publiques, ce qui rend l'envoi de courriels cryptés plus facile. Pour envoyer un courriel crypté, il faut disposer de la clé publique du destinataire. De manière similaire, une personne qui souhaite vous envoyer un message crypté doit disposer de votre clé publique.

À chaque clé publique correspond une *clé privée*. Sans la clé privée, le contenu d'un message crypté est extrêmement difficile à déchiffrer. À l'ère des superordinateurs, rien n'est impossible, mais décrypter un message sans la clé privée est extraordinairement difficile. Votre clé privée est extrêmement importante et devrait être conservée dans un endroit sécuritaire en tout temps.

Votre *phrase secrète* devrait être composée d'au moins 21 caractères et contenir des caractères en MAJUSCULE et en minuscule, ainsi que des symboles (&$"{@). Votre phrase secrète permet d'accéder à votre clé privée et de l'utiliser, avec votre clé publique, pour envoyer et recevoir des messages.

h2. Comment utiliser le cryptage pour mes courriels?

Il y a trois fonctions de base dans PGP: *signer*, *crypter* et *vérifier*.

*Signer*: lorsque vous signez un message, vous utilisez votre clé privée et votre phrase secrète pour générer un *bloc de signature* qui est ajouté à la fin du message. Le bloc de signature dépend de deux choses: (1) une valeur numérique calculée à partir du contenu du message et (2) votre clé privée. 

*Vérifier*: quand quelqu'un reçoit un message signé, il peut le vérifier en utilisant la clé publique avec lequel il a été crypté. Cette clé publique est parfois téléchargée à partir d'un serveur de clés ou envoyée avec le message. La vérification permet d'établir deux choses --> (1) le message a été signée par une personne ayant accès à la clé privée correspondante et (2) le contenu du message n'a pas été modifié pendant sa transmission.

*Crypter*: Pour crypter un message, vous avez besoin de la clé publique du destinataire. Il n'est pas nécessaire d'avoir une phrase secrète ni votre propre clé gpg pour crypter quelque chose. Néanmoins, la plupart des programmes vont aussi crypter le message en utilisant votre propre clé privée. Autrement, il vous serait impossible de relire votre message après l'avoir crypté. Une fois crypté, le contenu du courriel n'est plus visible pour la durée de la transmission. *Néanmoins, le sujet, le destinataire et le destinateur sont encore visibles.*

h2. Est-il possible d'envoyer et de recevoir des courriels cryptés en utilisant la messagerie riseup?

Ce n'est pas possible à l'heure actuelle. Pour les utilisateurs et utilisatrices de riseup qui veulent crypter leurs courriels, il est préférable d'utiliser un client de messagerie (comme thunderbird) pour envoyer et recevoir des courriels et de conserver votre clé privée de manière sécuritaire sur votre ordinateur.

h2. Quelles sont les limites des communications cryptées?

La communication cryptée ne vous protège pas de la *surveillance relationnelle*, c'est-à-dire la surveillance des associations entre les personnes. Par exemple, si jedetestebush@riseup.net envoie régulièrement des messages cryptés à joehill@riseup.net, une personne qui intercepte les communications ne peut peut-être pas lire le *contenu* des messages, mais le fait que ces adresses communiquent régulièrement est une information intéressante en elle-même. De plus, l'objet du message n'est *pas crypté*.

La signature et la vérification ne garantissent pas que le courriel a vraiment été envoyé par l'adresse associée à la clé. Il est très facile d'usurper une adresse de retour. Par exemple, quelqu'un avec l'adresse agentfederal@yahoo.com pourrait (1) créer une clé pour joehill@riseup.net, (2) téléverser la clé dans un serveur de clés publiques et (3) envoyer un courriel à partir de l'adresse federalagent@yahoo.com qui apparaît comme étant un message signé de joehill@riseup.net. Si vous n'avez fait que télécharger la clé publique et que vous vérifiez le message, il indiquera une «signature valide de joehill@riseup.net», même si le message n'a pas été envoyé par joehill! C'est pourquoi la *toile de confiance* est si importante (voir plus bas).

h2. Comment vérifier l'identité de l'utilisateur ou utilisatrice d'une clé?

Félicitations! Vous utilisez maintenant des courriels cryptés et vous envoyez et recevez allègrement des messages. Mais comment faire pour vous assurer que vous communiquez vraiment avec la bonne personne? C'est ici que les *empreintes numériques* (key fingerprints) entrent en jeu.

Chaque clé publique possède une unique *empreinte numérique*. Cette empreinte est générée à partir d'une fonction de hachage, qui est comme un portail à sens unique. Pour une entrée donnée, il existe *une et une seule* sortie correspondante. Tout comme vos empreintes digitales sont uniques, il existe seulement une empreinte pour chaque clé publique. Pourquoi c'est utile? Parce que pour s'assurer de l'intégrité du processus, il faut s'assurer qu'un message signé reçu de l'adresse joehill@riseup.net a effectivement été envoyé par votre ami Joe Hill. Il existe deux (possiblement trois) façons d'y arriver:
    
    1. Vous rencontrez Joe en personne et il vous donne une copie électronique de sa clé publique.
    2. Vous rencontrez Joe en personne et il vous donne une copie de l'empreinte numérique de sa clé. Vous vérifiez ensuite que l'empreinte correspond à sa clé publique.
    3. (moins sécuritaire) Si vous connaissez Joe très bien et que vous pouvez reconnaître sa voix, Joe peut vous dicter son empreinte par téléphone.

L'empreinte n'est pas une information secrète --- n'importe qui peut générer une empreinte à partir d'une clé publique.

h2. Comment et pourquoi signer une clé?

Passons à la vitesse supérieure et supposons que vous et Joe ayez échangés vos clés de manière sécuritaire. Vous pouvez maintenant envoyer des messages à Joe en ayant la certitude que vous communiquez véritablement avec lui (parce qu'il signe ses courriels), et que vos messages ne seront pas lus par un tiers (car vous utilisez la clé publique de Joe pour crypter vos courriels). Mais supposons que Joe rencontre Rita pendant une action et que Joe et Rita échangent leurs clés d'une manière sécuritaire. Vous connaissez Joe et lui faites confiance, mais n'avez jamais rencontré Rita. Comment établir que la clé de Rita est authentique sans la rencontrer en personne?

Entre en jeu la *toile de confiance* et la signature de clés. 

Une fois que Joe a vérifié la clé de Rita de manière sécuritaire, Joe peut *signer la clé publique de Rita*. Il y a deux écoles de pensées concernant la signature de clés - certaines personnes pensent que vous devriez signer la clé d'une personne (même d'une personne que vous connaissez depuis longtemps) seulement après avoir validé que le nom réel associé avec l'adresse courriel correspond à celui sur une pièce d'identité *émise par un gouvernement* (comme un passeport). D'autres vont signer des clés sans vérifier le vrai nom de l'utilisateur ou de l'utilisatrice, ce qui permet d'établir que la clé appartient bien au propriétaire de l'adresse. Néanmoins, cela ne permet pas de valider l'identité réelle de l'utilisateur ou utilisatrice de la clé.

Si vous faîtes confiance à Joe pour vérifier les clés des individus, vous pouvez ajoutez à votre trousseau de clés un niveau de confiance pour la clé de Joe. Dans ce cas, si Joe a déjà vérifié la clé d'une personne que vous n'avez jamais rencontré, vous pouvez établir un niveau de confiance pour la clé en vous basant sur le fait que Joe l'a déjà signé.

Vous pouvez organiser une *soirée d'échange de clés* pour encourager vos ami-e-s et collègues à échanger leurs clés et à les signer. C'est une bonne manière de vérifier l'identité des gens que vous n'avez jamais rencontré mais que des personnes de confiance ont déjà rencontrés.

h2. Avez-vous d'autres conseils à propos du cryptage de courriels?

Bonne question!

* *UTILISEZ UNE PARTITION CRYPTÉE* pour sauvegarder votre phrase secrète sur votre disque dur: c'est ce qui protège l'intégrité de votre clé privée si votre ordinateur est perdu, volé ou saisi.
* *NE PARTAGEZ PAS VOTRE CLÉ PRIVÉE* et ne l'enregistrez pas sur un ordinateur public.
* *UTILISER UNE PHRASE SECRÈTE ROBUSTE*: votre phrase secrète est votre dernière ligne de défense contre l'usurpation de votre clé privée. Ne ruinez pas toute l'affaire en utilisant une phrase secrète trop chétive. Les phrases secrètes devraient comporter plus de 21 caractères et ne devraient contenir aucun mot du dictionnaire ou d'autres combinaisons faciles à deviner. Préférez une phrase secrète aléatoire conservée dans un endroit sécuritaire à une longue phrase secrète composée de mots du dictionnaire.
* *UTILISEZ DES OBJETS GÉNÉRIQUES POUR VOS MESSAGES*. Les objets des messages ne sont pas cryptés. Par conséquent, vous devriez toujours utiliser des objets génériques pour vos communications cryptées.
* *ORGANISEZ UNE SOIRÉE D'ÉCHANGE DE CLÉS* pour encourager vos ami-e-s à échanger leurs clés et à les signer.
* *ENVOYEZ DES MESSAGES CRYPTÉS MÊME QUAND LE CONTENU N'EST PAS IMPORTANT*, c'est vital!! Si tous les messages cryptés concernent des communications secrètes, la quantité de messages à analyser est faible. Si tout le monde utilise le cryptage pour toutes leurs communications, même pour décider s'il faut mettre des anchois sur la pizza, la quantité de messages cryptés en circulation augmente.

h2. Comment configurer OpenPGP sur mon ordinateur?

Plus d'informations ici:

* [[LISEZ CECI D'ABORD -> gpg-best-practices]]
* [[gpg-keys]]
* [[enigmail]]
