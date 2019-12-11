@title = 'Riseup implémente un système de chiffrement de courriels en réponse à des requêtes légales.'
@nav_title = 'Déclaration de canari'
@toc = false

_16 Février, 2017_

Après avoir épuisé nos options légales, Riseup a récemment choisi de se soumettre à deux mandats juridiques secrets du FBI plutôt que de risquer un outrage au tribunal (ce qui aurait pu avoir comme résultat d'envoyer en prisons des oiseaux de Riseup et de mettre fin à notre organisation). Le premier mandat concernait l'adresse courriel publique d'une organisation internationale d'extorsion par attaque de déni de service (DDOS). Le second mandat concernait un compte utilisé par un logiciel de rançon pour extorquer de l'argent à des gens.

Les activités d'extorsion contreviennent très clairement à l'esprit et la lettre de notre contrat social \[1\]: Nous couvrons vos arrières tant et aussi longtemps que vous ne poursuivez pas des agendas misogynes, racistes, intolérants ou qui visent à exploiter les autres.

Une "obligation de silence" nous empêchait de vous faire part de l'existence même de ces mandats jusqu'à maintenant. C'est également la raison pour laquelle nous ne pouvions pas mettre à jour notre "canari" \[2\].

Nous nous sommes arrangés pour que Riseup n'ait plus jamais accès aux courriels d'une de ses utilisatrices ou d'un de ses utilisateurs en texte clair. À partir d'aujourd'hui, tous les nouveaux comptes courriel Riseup utiliserons un espace de stockage individuellement chiffré sur nos serveurs, accessible par vous seulement. Dans un futur proche, nous commencerons à migrer tous nos anciens comptes vers ce nouveau système (pour les détails techniques, veuillez lire \[3\]).

Pour que tout soit clair, ce type de chiffrement n'est pas du chiffrement bout-à-bout de vos messages. Avec le nouveau système de Riseup, vous devez encore faire confiance au serveur quand vous vous connectez. Pour un chiffrement bout-à-bout, comme auparavant, il vous faut encore utiliser un client qui supporte OpenPGP (et qui n'est pas un client web).

Nous travaillons sur un système de chiffrement bout-à-bout plus compréhensif pour l'an prochain, mais jusqu'à ce qu'il soit prêt, nous avons décidé de déployer des espaces de stockage chiffrés en attendant.

Solidarité,<br>
Les oiseaux de Riseup.

Questions

Q: Avez-vous été compromis par les agences de sécurité?

R: Non. Nous n'avons jamais permis l'installation d'aucun matériel électronique et d'aucun logiciel de surveillance sur les systèmes que nous contrôlons. Les agences de sécurité n'ont pas pris nos serveurs, n'y ont pas accès et n'y ont jamais eu accès. Nous préférerions cesser d'être Riseup bien avant de faire cela.

Q: Le gouvernement ne pourrait-il pas vous forcer à dire cela?

R: Les déclarations forcées sont en fait très rares dans le cadre légal américain. Les seules utilisations connues de cette méthode visent la protection du consommateur (par exemple sur les paquets de cigarette). Néanmoins, non, le gouvernement ne nous force pas à dire quoi que ce soit.

Q: Pourquoi n'avez-vous pas mis à jour votre canari?

R: Au cours de l'hiver 2016, notre canari n'a pas été mis à jour à temps. Le canari était tellement large que toute tentative d'en faire un nouveau aurait été en violation avec notre obligation de silence liée aux enquêtes pour extorsion par DDOS et par logiciel de rançon. Cela n'est pas souhaitable, parce que parmi une multitude de choses qui peuvent survenir, il n'en suffit que d'une pour envoyer un signal très fort aux personnes qui utilisent nos services que quelque chose est arrivé.

Q: Pourquoi le nouveau canari ne mentionne-t-il pas l'obligation de silence, le FISA (Foreign Intelligence Surveillance Act) et les lettres de sécurité nationale (National Security Letters, NSL)?

R: Notre stratégie de canari initiale ne faisait que causer du tord en donnant une tribune superflue à des événements mineurs.Un canari est supposé envoyer un signal quand de l'information importante est à risque, mais il existe également la possibilité d'envoyer le mauvais signal. Cela peut même créer une peur généralisée et de la confusion de manière injustifiée. Le nouveau canari se limite à des événements significatifs qui pourraient compromettre la sécurité des personnes qui utilisent Riseup.

* \[1\]: https://riseup.net/tos
* \[2\]: https://riseup.net/canary
* \[3\]: https://0xacab.org/riseuplabs/trees
