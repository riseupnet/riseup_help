@title = "Chiffrement de l'appareil"
@toc = true
@summary = "Le pourqoi et comment de chiffrer le stockage de vos appareils"

# Why Use Device Encryption?

Avec l'enchiffrement de l'appareil les contenus du stockage de votre appareil - la partie qui contient le système d'exploitation, logiciels que vous avez installé et vos données personnelles - sont modifié d'une telle façon qu'ils sont inaccessibles quand votre appareil est éteint ou lorsque vous êtes déconnectées.

Si votre appareil n'est pas chiffré, quand une personne vole votre appareil, le trouve ou l'accède autrement elle pourrait facilement lire vos fichiers, accèder à vos comptes en-ligne et faire semblant d'être vous. Pire une attaquante pourrait installer des logiciels malveillants qui leur permettera d'accèder par distance à toute vos activités.

# How To Enable Device Encryption

Malgrès le fait que le chiffrement complèt de disque est activé par défaut sur certains appareils mobiles il doit être configuré manuellement pour tout les ordinateurs portables et de bureau ainsi que sur plusieurs téléphones mobiles et tablettes.

Guides pour les ordinateurs portables et de bureau:

* **Windows**: [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  * IMPORTANT: Par défaut, Microsoft créer des sauvegardes de votre cléf de chiffrement dans la nuage. Celà veut dire que Microsoft, et tout autre gouvernement qu'il coopère avec, sera en mésure de facilement déchiffrer votre appareil. Si vous êtes inquiètées par la possibilité qu'un gouvernement ait accès aux contenus de votre appareil vous devriez désactiver cette "fonctionalité" et [[génerer un nouveau cléf de chiffrement => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]] maintenant.
* **macOS**: [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* **Linux**: Presque tout les distributions de Linux vous permettera d'activer le chiffrement de disque lors de l'installation du système d'exploitation. Il y a deux types différents:
  * Chiffrement complèt de disque: Cette façon enchiffre tout sur le stockage primaire de l'appareil, inluant le système d'exploitation. Vous devriez entrer un mot de pass différent lorsque l'appareil démarre.
  * Chiffrement du dossier personnel: Cette façon **n'enchiffre pas** le système d'explitation. Vos données personnelles seront protogées mais il sera plus facile pour une attaquante d'accèder à votre appareil afin d'installer des logiciels malveillants comparé au chiffrement complèt de disque.

Guides pour les appareils mobiles:

* **iOS**: [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* **Android**: [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Limitations du chiffrement des appareils

**Limitations** Le chiffrement des appareils ne fonctionne pas toujours! Si votre [[mot de pass => passwords]] n'est pas complèxe un ordinateur pourrait facilement le deviner et déchiffrer votre appareil. De plus le chiffrement ne protège pas contre les logiciels malveillants et viruses. Si vos données sont copiés vers un service de sauvegarde nuagique (cloud-based) et ce service est compromis ou coopère avec un gouvernement le chiffrement de l'appareil ne protègera pas vos données (à moins que vous utilisez un service qui fait l'enchiffrement explicitement du côté client).

**L'authentification doit être configuré** L'enchiffrement des appareils n'est pas utile à moins que l'appareil exige un ou plusieurs formes d'authentification. Par example, vous êtes obligées de se connecter quand vous utiliser votre ordinateur portable ou fournir un NIP quand vous utiliser votre appareil mobile.

**Rend la récuperation d'un disque impossible** Le chiffrement complèt de disque peut augmenter la risque que vous perdriez accès à vos informations si des bonnes pratiques de gestion de mot de pass ou de NIP ne sont pas suivies. Un mot de pass ou NIP perdu ou l'échec de la région du disque où vos cléfs de chiffrement sont stockés rendera vos données irrécuperables de manière générale. Assurez-vous d'avoir des sauvegardes périodique de vos données afin de minimiser la risque de perte de données.

**L'appareil doit être éteint ou barré** Le chiffrement d'un appareil protège seulement quand votre ordinateur ou appareil mobile est éteint ou allumé mais en attente d'un mot de pass pour le démarrer. Une fois que vous avez connectée, l'appareil a le cléf secrète nécessaire pour déchiffrer les données dans sa mémoire. Même avec un écran barré il y a une risque qu'une personne puisse obtenir un accès aux contenus de votre appareil lorsque l'appareil roule ou est en veille. Cependant, la dépassement de ces mésures de sécurité est généralement une attaque hautement technique et cette risque ne devrez pas vous empêcher de garder votre appareil allumé ou connecté quand vous avez besoin de travaliler. Néamoins il est mieux de fermer vos appareils lorsque vous n'êtes pas à proximité dans des environnements hostiles. Si vous penser que vous êtes possiblement un cible de ce genre d'attaque, la meilleure pratique à suivre et de garder votre appareil à côté de vous en tout temps.

# Voir aussi

* [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
* [Security Self-defense / How to: Encrypt Your iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
