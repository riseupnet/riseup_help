@title = "Mobilgeräte-Sicherheit"
@nav_title = "Mobile Geräte"
@toc = true

# Welche mobilen Geräte sind am besten für mich?

Welches das ideale Mobilgerät ist, hängt von Deiner Situation ab:

- **Hohes Risiko**: Du vermutest, Ziel einer professionellen Überwachungsfirma zu sein.
- **Gemäßigtes Risiko**: Du wirst nicht aktiv beobachtet aber bevorzugst ein Gerät, das mit physischem Zugang nicht einfach zu kompromittieren ist.
- **Geringes Risiko**: Du benutzt Mobilgeräte nicht für sensitive Informationen.

## Hohes Risiko

Wenn Du gefährdet bist, **vermeide die Nutzung von Telefonen für sensitive Kommunikation**. Der Grund ist, dass alle Telefone ein Baseband-Modem für Mobilfunk-Kommunikation verwenden. Diese Modems sind proprietär und voller Sicherheitslöcher, die von Ferne ausgenutzt werden können. In diesem Fall kann das Modem zum Überwachen Deiner Kommunikation und Auslesen von Daten genutzt werden.

Als Alternative zu Smartphones kannst Du ein Tablet verwenden, welches nur WiFi unterstützt und damit nicht über Mobilfunk fernsteuerbar ist. Mit einem externen mobilen Hotspot ist es zudem möglich, nur dann Mobilfunk einzuschalten, wenn Du es möchtest.

Beachte, dass Flugzeugmodus nicht ausreicht. Je nach Gerät hat das Baseband-Modem auch im "airplane mode" Strom.

Empfohlene Nur-WiFi-Geräte:

- [[Pixel C => https://en.wikipedia.org/wiki/Pixel_C]] oder [[Pixelbook => https://en.wikipedia.org/wiki/Google_Pixelbook]] by Google.
- [[iPad => https://en.wikipedia.org/wiki/IPad]] von Apple, aber nur Modelle **ohne Unterstützung für Mobilfunk**.

## Gemäßigtes Risiko

Hast Du sensible Daten auf deinem Mobilgerät, die besser nicht von Kriminellen, Regierungen oder nervigen Nachbarn gesehen werden sollen? Selbstverständlich, so wie wir alle.

In diesem Fall wirst Du versuchen, es anderen schwer zu machen in Dein Gerät einzubrechen, wenn es gefunden oder gestohlen wird.

Unglücklicherweise ist die beste Möglichkeit, ein Gerät von Google oder Apple zu kaufen. Diese Geräte zeichnen sich durch höhere Hardware-Sicherheit als andere Hersteller aus und veröffentlich regelmäßig Sicherheits-Aktualisierungen. Allerdings kann auch in diese Geräte eingebrochen werden, wenn ein Angreifer mächtig genug ist, oder das Gerät entsperrt ist.

Empfohlene Geräte:

- [[Pixel => https://en.wikipedia.org/wiki/Google_Pixel]] von Google
- [[iPhone or iPad => https://en.wikipedia.org/wiki/IPhone]] von Apple (iPhone 4S oder neuer ist nötig für Geräteverschlüsselung)

## Geringes Risiko

Lässt Du Geräte entsperrt herumliegen? Glückwunsch, du umarmst die Realität, dass mobile Hardware nicht sehr sicher ist.

Dennoch warten auf dieser Seite einige nützliche Tipps für Dich und Menschen mit denen du kommunizierst.

# Behalte Geräte bei dir

Es ist eine gute Idee, Mobilgeräte immer in physischer Reichweite zu behalten. Ansonsten haben Angreifer viele Möglichkeiten, sich Zugang zu verschaffen, Daten zu kopieren, oder Software zu installieren, die zukünftige Aktivitäten überwacht.

Die Angreifbarkeit Deines Gerätes hängt davon ab, ob Du "empfohlene Hardware" verwendest, ob [[device-encryption]] aktiviert ist und ob das Gerät mit einer PIN geschützt ist.

**Die Wahrscheinlichkeit, dass ein Angreifer in ein Gerät einbrechen kann:**

<table class="table">
<tr>
  <th>Dein Gerät</th>
  <th>komplexe Angriffe</th>
  <th>gehobene Angriffe</th>
  <th>gewöhnliche Angriffe</th>
</tr>
<tr>
  <td>Empfohlene Hardware + verschlüsselt + gesperrt</td>
  <td>NIEDRIG</td>
  <td>SEHR NIEDRIG</td>
  <td>KEINE</td>
</tr>
<tr>
  <td>Empfohlene Hardware + gesperrt</td>
  <td>MITTEL</td>
  <td>NIEDRIG</td>
  <td>SEHR NIEDRIG</td>
</tr>
<tr>
  <td>Normale Hardware + verschlüsselt + gesperrt</td>
  <td>HOCH</td>
  <td>MITTEL</td>
  <td>NIEDRIG</td>
</tr>
<tr>
  <td>Normale Hardware + gesperrt</td>
  <td>SEHR HOCH</td>
  <td>HOCH</td>
  <td>MITTEL</td>
</tr>
<tr>
  <td>Entsperrt</td>
  <td>GEWISS</td>
  <td>GEWISS</td>
  <td>GEWISS</td>
</tr>
</table>

Arten von Angreifern:

- **komplexe Angriffe** durch große Regierungen und internationale Firmen, die auf das Überwachen von Mobilgeräten spezialisiert sind
- **gehobene Angriffe** von Polizei und Geräte-Entsperr-Firmen
- **gewöhnliche Angriffe** von erfahrenen Technologen ohne besondere Ausrüstung

Wenn Dein Gerät Deine Anwesenheit verlässt und Du vermutest, es wurde eingebrochen, solltest Du Deine Daten sichern und ein **factory reset** vornehmen (oder erwägen, ein neues Gerät zu verwenden).

# Benutze Signal

Lade Signal für:

<%= render partial: 'signal_android' %> <%= render partial: 'signal_ios' %>

**Signal** ist eine freie Chat-Software, die als sichere Alternative für normale Textnachrichten (SMS) gilt. Es funktioniert ähnlich wie WhatsApp und Telegram, bietet jedoch wesentlich höhere Sicherheit.

Warum sollte ich Signal benutzen?

- Dein Mobilfunkprovider speichert alle gesendeten Textnachrichten. Mit Signal hat dieser keinen Zugang zu Deinen Nachrichten und Kommunikationsmustern.
- Es ist relativ einfach für einen Angreifer, Deine Telefonnummmer zu übernehmen. Mit Signal wirst Du in diesem Fall darüber informiert, dass die "Sicherheitsnummer" eines Gegenüber geändert wurde. Dies geschieht auch, wenn ein neues Gerät verwendet wird.
- Signal kann auch für hochsichere Audiokommunikation verwendet werden. Dein Mobilfunkprovider speichert, wen Du anrufst, von wem Du angerufen wirst und die Dauer all Deiner Anrufe. Mit Signal hat Dein Provider keine dieser Information. Daher ist der Inhalt Deiner Kommunikation vertraulich, so lange Dein Gerät nicht kompromittiert wurde.
- Andere "sichere" Chatanwendungen wie WhatsApp, Telegram oder Wire haben einige Probleme im Vergleich zu Signal.

Für weitere Informationen siehe [[Security Planner / Signal => https://securityplanner.org/#/tool/signal]].

# Aktiviere Geräteortung ("Find My Device")

Erwäge, "Find My Device" zu aktivieren. Das erlaubt es Dir, das Gerät von Ferne zu finden, sperren und persönliche Informationen zu löschen, falls es gestohlen wird.

Für weitere Informationen siehe:

- [[Security Planner / Find My Device (Android) => https://securityplanner.org/#/tool/find-my-device]].
  - Beachte: Diese Funktion erfordert, das Gerät mit einem Google-Konto zu verknüpfen. Außerdem wird Google in diesem Fall mehr Informationen speichern, wie z.B. Bewegungsmuster.
- [[Security Planner / Find My iPhone (iOS) => https://securityplanner.org/#/tool/find-my-iphone]]

# Mache Photos sicher

Deine Telefon-Kamera fügt jedem Photo sensitive Information hinzu. Es ist daher eine gute Idee, diese Metadaten vor dem Veröffentlichen zu entfernen.

Um **Geotagging** zu verhindern, öffne die Kamera-Einstellungen und suche nach Lokalisierungsdaten.

Selbst ohne Geotagging werden das Model und andere möglicherweise sensible Information gespeichert. Um diese zu entfernen, brauchst Du ein Programm, um **EXIF**-Daten von den Bilddateien zu entfernen. Diese Anwendungen können auch Lokalisierungsinformationen von älteren Bildern entfernen.

Für weitere Information siehe: [[3 ways to remove EXIF metadata from photos => https://www.makeuseof.com/tag/3-ways-to-remove-exif-metadata-from-photos-and-why-you-might-want-to/]].

# Weitere Hinweise

- Erfodere ein Passwort, oder zumindest eine PIN, um Dein Gerät zu entsperren. Benutze nicht Fingerabdruck- oder Gesichtserkennung, da diese nicht sicher sind.
- Konfigurieren Dein Gerät, keine detaillierten Benachrichtigungen auf dem Sperr-Bildschirm anzuzeigen
- Sei gewahr, dass sich Dein Telefon mit der Cloud synchronisiert. Zum Beispiel wenn Du Photos löschst, sind diese möglicherweise bereits in iCloud oder Dropbox.
