@title = "Hygiène des messages"
@toc = true
@summary = "Des trucs simples pour utiliser vos courriels de manière plus sécuritaire"

# Ne faites jamais confiance à l'expéditrice ou à l'expéditeur

Les courriels sont la principale source d'attaques informatiques. C'est le cas car il n'y a pas de moyens de vérifier l'identité du champ "De:" dans un courriel.

Nous le répétons: n'importe qui peut falsifier le champ "De:" dans un courriel et peut se faire passer pour une autre personne.

Parce ce qu'il est difficile de vérifier l'identité de l'expéditrice ou de l'expéditeur, votre boîte de réception est une source commune **d'attaques par hammeçonnage** (*phising*) et **d'attaques par logiciels malveillants**.

* **L'hammeçonnage** est quand une personne vous envoie un courriel en se faisant passer pour une autre personne et utilise cette supercherie pour soutirer de l'information. Ces personnes peuvent chercher à subtiliser vos numéros d'assurance sociale, vos informations bancaires, vos mots de passes ou d'autres informations sensibles.
* **Une attaques par logiciels malveillants** survient quand une personne tente de vous piéger et de vous faire installer un logiciel malveillant sur votre ordinateur. Ces attaques sont couramment effectuées quand vous cliquez sur un lien ou que vous ouvrez une pièce-jointe.

En général, tout message suspect dans vos courriels devrait être inspectée avec attention. Méfiez-vous des messages qui vous demandent de faire quelque chose - cliquer sur un lien, ouvrir une pièce-jointe ou encore envoyer de l'information - même si le message provient d'une personne que vous connaissez!

Si quelqu'un a pris le contrôle de votre compte, il se pourrait que vous voyiez des messages envoyés que vous ne comprenez pas, de nouveaux dossiers ou des filtres additionnels. Tout changement dans vos paramètres ou dans votre compte que vous n'avez pas effectués devraient être mentionnés au support technique et vous devriez immédiatement changer votre mots de passe.

# Évitez les liens dans les courriels

Les liens, malgré le fait qu'ils ont parfois l'air inoffensifs, sont la manière la plus utilisée pour voler vos données et prendre le contrôle de vos appareils.

La meilleure chose à faire est de ne jamais cliquer sur un lien dans un courriel. Si vous devez absolument le faire, voici une liste de choses à vérifier:

* Vous attendiez-vous à avoir ce courriel? Même si le champ "De:" dans le courriel appartient à une personne que vous connaissez, vous devriez toujours faire attention quand vous recevez un courriel que vous n'attendiez pas.
* Pouvez-vous taper manuellement le lien plutôt que cliquer dessus? Il y a des chances que le lien que vous voyez est frauduleux. Les noms de domaines contiennent des homographes ou différents caractères qui se ressemblent (par exemple, le chiffre "0" et la lettre majuscule "O", ou encore des caractères cyrilliques plutôt que des caractères latins). Un lien qui ressemble à <https://riseup.net> pourrait en fait pointer vers le site d'un-e attaquant-e au <%= '<a href="https://riseuρ.net">https://riseuρ.net</a>' %> (le second lien utilise une lettre grecque pour le "p"). La manière la plus sécuritaire pour éviter ce type d'attaque est de ne jamais copier un URL et de toujours taper les liens dans votre navigateur web directement.
* Reconnaissez-vous le nom de domaine? Dans la plupart des clients de messagerie, comme sur le web, survoler un lien affiche l'URL vers lequel il pointe. Si la destination du lien ne vous est pas familière, vérifiez avec la personne qui vous l'a envoyé pour vous assurer que c'est bien un courriel légitime. Le lien devrait toujours commencer par "https://". Si jamais il commence par "data://", c'est que vous être victime d'une attaque par hammeçonnage.

Ne cliquez jamais sur des liens et n'ouvrez jamais de pièce-jointes envoyées par une personne que vous ne connaissez pas. De même pour les courriels qui vous semblent suspicieux. Contrairement aux personnes que vous connaissez et avec qui vous travaillez, les personnes que vous ne connaissez pas ne vous enverront jamais un fichier dont vous avez besoin; si le lien qu'une telle personne vous envoie est réellement pertinent, vous serez en mesure d'accéder à cette information d'une autre manière (comme en faisant une recherche sur le web par exemple).

# Ne vous connectez jamais après avoir cliqué sur un lien

Si vous cliquez sur un lien dans votre courriel malgré ces recommandations, il est particulièrement important de ne pas se connecter au site web qui vient de s'ouvrir. Si le site web vous demande de vous connecter, suivez ces étapes:

1. Ouvrez un nouvel onglet dans votre navigateur web et tapez le nom de domaine manuellement.
2. En utilisant cet onglet, connectez-vous au site web.
3. Retournez dans vos courriels et cliquez de nouveaux sur le lien.
4. Quand ce lien s'ouvre, vous ne devriez plus avoir besoin de vous connecter. Si le site web vous demande encore de vous connecter, c'est que vous êtes victime d'une attaque par hammeçonnage.

Ces quelques trucs vous aideront à vous protéger de la plupart des attaques par hammeçonnage.

# Évitez les pièce-jointes

Les pièce-jointes dans les courriels présentent de nombreux risques, dont leur utilisation pour de l'hammeçonnage. Les pièce-jointes peuvent être altérées ou encore consultées durant leur transit: vous ne pouvez donc pas être certain-e que le fichier que vous avez envoyé est le même que celui qui est reçu. Un serveur malveillant situé entre vous et votre récipiendaire pourrait altérer le fichier et y ajouter un virus ou un programme malicieux. De plus, les pièce-jointes ont tendance à rester dans la boîte de réception de la personne à qui vous l'avez envoyée pendant très longtemps, là où vous n'en avez plus le contrôle. Par exemple, si vous avez remplit un formulaire en utilisant la carte de crédit de votre organisation et que vous l'avez envoyée à une compagnie par courriel, cette compagnie aura accès à vos informations de carte de crédit jusqu'à temps qu'elle supprime le courriel.

Une pratique alternative aux pièce-jointes est l'ajout d'un lien vers un fichier stocké sur un serveur. Idéalement, ces liens pointent vers une page protégée par un mot de passe où il est possible de récupérer le fichier. Ces liens devraient également être temporaires et expirer peu après leur utilisation. Ce genre de liens peuvent facilement être générés par la plupart des systèmes de stockages, que ce soit dans à votre bureau (un serveur de fichiers Windows) ou encore sur le web (par Google Drive, Box ou encore Dropbox).

Pour plus de sécurité, vous pouvez chiffrez vos fichiers grâce à des liens temporaires en les téléversants au <https://share.riseup.net>.

# Pour aller plus loin

* [Security Self-defense / How to Avoid Phishing Attacks](https://ssd.eff.org/en/module/how-avoid-phishing-attacks)
* [Security Education Companion / Phishing and Malware](https://sec.eff.org/topics/phishing-and-malware)
* [Security In-a-box / Protect Your Device From Malware and Hackers](https://securityinabox.org/en/guide/malware/)
* [Security In-a-box / Keep Your Online Communications Private](https://securityinabox.org/en/guide/secure-communication/)
* [Security Planner / Spot Suspicious Emails](https://securityplanner.org/#/tool/spot-suspicious-emails)
