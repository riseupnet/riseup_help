@title = "Zertifikate"

h1.  Was sind Zertifikate? 

Im Internet ist ein [[Public-Key-Zertifikat ->https://de.wikipedia.org/wiki/Public-Key-Zertifikat]] notwendig, um die Identität von Personen oder Computern zu überprüfen. Diese Zertifikate werden auch "SSL-Zertifikate" oder "Identitäts-Zertifikate" genannt. Wir werden sie hier einfach "Zertifikate" nennen.

Konkret werden Zertifikate benötigt, um [[sichere Verbindungen->https://help.riseup.net/de/sichere_verbindungen]] herzustellen. Ohne Zertifikate könntest Du zwar ausschließen, dass niemand mitliest - aber Du könntest mit einem völlig falschen Computer kommunizieren! Alle Riseup-Server und -Dienste ermöglichen oder benötigen sichere Verbindungen. 

Um sicherzustellen, daß Du die sichere Verbindung auch wirklich mit Riseup herstellst, kannst Du die folgenden Schritte unternehmen, um unsere Zertifikate zu überprüfen. Dies ist zwar nicht notwendig, um Riseups Dienste zu nutzen, aber ohne diese Verifizierung hast Du keine Garantie, daß Du wirklich mit unseren Servern verbunden bist, bzw. daß die Verbindung sicher ist.

h1. Verifizierung der Gültigkeit von Riseups Zertifikaten

Um diese Prüfsummen ("Fingerprints") zu verifizieren, musst Du schauen, welche Prüfsummen Dein Browser für die Zertifikate angibt und diese dann mit den unten gelisteten vergleichen. Wenn sie sich unterscheiden, besteht ein Problem. Sei gewarnt: die vollständige Verifizierung ist schwierig und erfordert Verständnis von [[OpenPGP]].

Die Prüfsummen von Riseups Zertifikaten sind:

<pre>
<%= render :file => 'riseup-signed-certificate-fingerprints.txt', :type => :raw %>
</pre>

h2. Wann sollte ich diese Prüfsummen verifizieren?

Du solltest diese Prüfsummen immer dann verifizieren, wenn sie sich ändern - oder wenn Du einen Computer nutzt, der nicht unter Deiner Kontrolle steht, wie z.B. im Internetcafe oder in der Bücherei.

h2. Einfache Verifizierung

Zuerst finde die Prüfsumme von Riseups Zertifikat in Deinem Browser. Dafür musst Du in den meisten Browsern entweder das kleine Vorhängeschloss-Symbol, das Du am unteren Fensterrand oder in der Adresszeile findest, oder unseren schwarz-roten Stern in der Adresszeile anklicken. Dies sollte ein Fenster mit detaillierten Informationen zum genutzten Zertifikat öffnen, das auch die Prüfsumme beinhaltet. 

Wenn Du nun diese Prüfsumme mit den unten Stehenden vergleichst, hast Du schon mal eine einfache Verifizierung durchgeführt.

Falls Du an einer vollständigen Verifizierung interessiert bist, musst Du einen etwas komplizierteren technischen Vorgang durchführen, der Verständnis von OpenPGP erfordert.

h2. Vollständige Verifizierung

Warnung: Dieser Vorgang ist ziemlich technisch. Er erfordert Kenntnis von OpenPGP und der Befehlszeile. Es geht davon aus, dass das Programm @gpg@ installiert ist.

Die folgende Anleitung zeigt die Befehle, die Du im Terminal eingeben musst. Den Befehlen ist ein '$'-Zeichen vorangestellt, das für die Eingabeaufforderung steht. Diese Eingabeaufforderung zeigt an, dass das System auf einzutippende Befehle wartet. In deiner Kommandozeile kann das anders aussehen, falls es also kein '$' ist, macht das nichts! Gib einfach den Befehl in Deiner Kommandozeile ein, der diesem Zeichen folgt.

h3. Importieren von Riseups öffentlichem Schlüssel

Bevor du weiter machst, [[wähle einen sicheren Schlüsselserver -> /gpg-best-practices#selecting-a-keyserver-and-configuring-your-machine-to-refresh-your-keyring]].

Öffne ein Terminal (drücke *Alt+F2* und gib @gnome-terminal@ ein) und importiere Riseups öffentlichen OpenPGP-Schlüssel von einem Schlüsselserver:

@$ gpg --keyserver keys.riseup.net --recv-key 0x4E0791268F7C67EABE88F1B03043E2B7139A768E@
@$ gpg --fingerprint 0x4E0791268F7C67EABE88F1B03043E2B7139A768E@

Die erste Zeile importiert den Schlüssel in deinen Schlüsselbund, aber es gibt keine Garantie, dass das der richtige ist. Daher zeigt dir der zweite Befehl die Prüfsumme des importierten Schlüssel an. Stelle sicher, dass sie mit dieser übereinstimmt:

bq. Key fingerprint = 4E07 9126 8F7C 67EA BE88  F1B0 3043 E2B7 139A 768E

Es gibt keinen guten Grund, diesem Schlüssel zu vertrauen. Du kannst aber sehen, wer dem Schlüssel das Vertrauen ausgesprochen hat: 

@$ gpg --list-sigs 0x4E0791268F7C67EABE88F1B03043E2B7139A768E@

h3. Verifiziere Riseups Zertifikat

Mit folgendem Befehl können die Fingerabdrücke auf dieser Seite verifiziert werden:

bc. wget -qO - https://riseup.net/certificates/riseup-signed-certificate-fingerprints.txt | gpg --auto-key-retrieve --verify --output -

Du solltest obige signierte Nachricht sehen, gefolgt von:

bq. gpg: Signatur vom Mi 11 Okt 2017 21:13:32 CEST
gpg:                mittels RSA-Schlüssel 4E0791268F7C67EABE88F1B03043E2B7139A768E                              
gpg: Korrekte Signatur von "Riseup Treasurer <treasurer@riseup.net>" [unbekannt]                                
gpg:                     alias "Riseup Networks <collective@riseup.net>" [unbekannt]                            
gpg: WARNUNG: Dieser Schlüssel trägt keine vertrauenswürdige Signatur!                                          
gpg:          Es gibt keinen Hinweis, daß die Signatur wirklich dem vorgeblichen Besitzer gehört.               
Haupt-Fingerabdruck  = 4E07 9126 8F7C 67EA BE88  F1B0 3043 E2B7 139A 768E                                       

Stelle sicher, dass dort wirklich "Korrekte Unterschrift" (oder "Good signature") steht! Falls der Text abweicht, ist der Information nicht zu trauen.

Falls Du keine konkreten Schritte unternommen hast, einen Vertrauenspfad zum Schlüssel des Riseup-Kollektivs aufzubauen, wirst Du eine Warnung erhalten, die dieser ähnelt:

bq. gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.

Trotzdem solltest Du "Korrekte Unterschrift" sehen.

h3. Vergleichen der Prüfsummen

Jetzt, da Du sichergestellt hast, daß die obige Nachricht wirklich die Prüfsummen unserer Zertifikate enthält, kannst Du sie mit den Werten, die Dein Browser angibt, vergleichen. Dafür musst Du in den meisten Browsern entweder das kleine Vorhängeschloss-Symbol, das Du am unteren Fensterrand oder in der Adresszeile findest, oder unseren schwarz-roten Stern in der Adresszeile anklicken. Dies sollte ein Fenster mit detaillierten Informationen zum genutzten Zertifikat öffnen, das auch die Prüfsumme beinhaltet. 

Falls sie übereinstimmen und Du Riseups öffentlichem PGP-Schlüssel traust, kannst Du davon ausgehen, daß Du wirklich mit Riseups Servern kommunizierst.

h1. Ich will mehr wissen!

Super, dies ist auch ein wichtiges Thema und wir wollen Dir nahelegen, [[diesen (englischen) Text -> http://lair.fifthhorseman.net/~dkg/tls-centralization/]] zu lesen, der auf nicht-technische Weise sehr gut die Probleme mit zentralen Zertifizierungsstellen darstellt und gleichzeitig einige interessante Vorschläge macht, wie die Situation mit kleinen Veränderungen der existierenden Infrastruktur und Protokolle verbessert werden könnte.
