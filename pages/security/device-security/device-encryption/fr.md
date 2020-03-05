@title = "Chiffrement de l'appareil"
@toc = true
@summary = "Pourquoi et comment chiffrer le stockage de vos appareils"

# Pourquoi chiffrer vos appareils?

En chiffrant le contenu de vos appareils, le système d'exploitation, les logiciels que vous avez installé et vos données personnelles sont modifiés d'une telle façon qu'ils sont inaccessibles quand votre appareil est éteint ou lorsque vous êtes déconnectés.

Si votre appareil n'est pas chiffré, si une personne vole votre appareil, le trouve ou en gagne l'accès d'une autre manière elle pourrait facilement lire vos fichiers, accéder à vos comptes en ligne et faire semblant d'être vous. Pire un-e attaquant-e pourrait installer des logiciels malveillants leur permettant de surveiller à distance toute vos activités.

# Comment activer le chiffrement de vos appareils

Malgré le fait que le chiffrement complet des disques est activé par défaut sur certains appareils mobiles, il doit être configuré manuellement pour tous les ordinateurs portables et de bureau ainsi que sur de nombreux téléphones mobiles et tablettes.

Guides pour les ordinateurs portables et de bureau:

* **Windows**: [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  * IMPORTANT: Par défaut, Microsoft crée des sauvegardes de votre clef de chiffrement dans leurs serveurs distants (*cloud*). Cela veut dire que Microsoft - et tout autre gouvernement avec qui ils coopèrent - sera en mesure de facilement déchiffrer votre appareil. Si la possibilité qu'un gouvernement ait accès aux contenus de votre appareil vous inquiète, vous devriez désactiver cette "fonctionnalité" et [[générer une nouvelle clef de chiffrement => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]] dès maintenant.
* **macOS**: [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* **Linux**: Presque toutes les distributions de Linux vous permettent d'activer le chiffrement de disque lors de l'installation du système d'exploitation. Il y en a deux types différents:
  * Chiffrement complet de disque: Cette façon chiffre l'ensemble du stockage principal de l'appareil, incluant le système d'exploitation. Vous devrez entrer un mot de passe séparé lorsque l'appareil démarre.
  * Chiffrement du dossier personnel: Cette façon **ne chiffre pas** le système d'exploitation. Vos données personnelles seront protégées mais il sera plus facile pour un-e attaquant-e d'accéder à votre appareil afin d'installer des logiciels malveillants comparé au chiffrement complet de disque.

Guides pour les appareils mobiles:

* **iOS**: [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* **Android**: [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Avertissements sur le chiffrement des appareils

**Limites** Le chiffrement des appareils ne fonctionne pas toujours! Si votre [[mot de passe => passwords]] n'est pas assez fort, un ordinateur pourrait facilement le deviner et déchiffrer votre appareil. De plus le chiffrement ne protège pas contre les logiciels malveillants et les virus. Si vos données sont copiées vers un service de sauvegarde nuagique (*cloud-based*) et que ce service est compromis ou coopère avec un gouvernement, le chiffrement de l'appareil ne protégera pas vos données (à moins que vous utilisez un service qui chiffre explicitement les données du côté client).

**L'authentification doit être configurée** Le chiffrement des appareils n'est pas efficace à moins que l'appareil exige une ou plusieurs formes d'authentification. Par exemple, vous êtes obligées de vous identifier quand vous utilisez votre ordinateur portable ou de fournir un NIP quand vous utilisez votre appareil mobile.

**Cela rend la récupération d'un disque impossible** Le chiffrement complet de disque peut augmenter le risque de perdre l'accès à vos informations si des bonnes pratiques de gestion de mot de passe ou de NIP ne sont pas suivies. Un mot de passe ou NIP perdu ou un problème avec la région du disque où vos clefs de chiffrement sont stockées rendra vos données irrécupérables de manière générale. Assurez-vous d'avoir des sauvegardes périodiques de vos données afin de minimiser le risque de perte de données.

**L'appareil doit être éteint ou verrouillé** Le chiffrement d'un appareil protège seulement quand votre ordinateur ou appareil mobile est éteint ou allumé mais attendant un mot de passe pour démarrer. Une fois que vous vous êtes authentifié-e-s, l'appareil a la clef secrète nécessaire pour déchiffrer les données dans sa mémoire. Même avec un écran verrouillé il y a une risque qu'une personne puisse obtenir un accès aux contenus de votre appareil lorsque l'appareil fonctionne ou est en veille. Cependant, ce genre d'attaque est généralement hautement technique. Cela ne devrait pas vous empêcher de garder votre appareil allumé ou connecté quand vous avez besoin de travailler. Néanmoins il est mieux d'éteindre vos appareils lorsque vous vous en éloignez dans des environnements hostiles. Si vous pensez que vous êtes possiblement une cible de ce genre d'attaque, la meilleure pratique à suivre est de garder votre appareil à côté de vous tout le temps.

# Pour en savoir plus

* [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
* [Security Self-defense / Guide pratique : chiffrer votre iPhone](https://ssd.eff.org/fr/module/guide-pratique-chiffrer-votre-iphone)
