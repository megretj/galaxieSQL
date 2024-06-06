---
layout: tutorial_de
title: Weltraumerforschung
dbFile: data/alien_de.db
---

# Weltraumerforschung

Bei den neusten Weltraumerforschungen wurden außerirdische Lebensformen entdeckt! Das neue Teleskop SPS (Space Photographer System) ermöglicht die Oberfläche von extra-galaktischen Planeten zu beobachten.
<br>Bis jetzt haben die Wissenschaftler*innen drei bewohnte Exoplaneten entdeckt:
<li>Céplusplus</li>
<li>Scratchon</li>
<li>Pythos</li>

Deine Aufgabe wird es sein, die verschiedenen beobachtbaren Alien-Typen zu katalogisieren. Zu diesem Zweck erstellen alle Wissenschaftler der Erde eine Datenbank, die die beobachteten Aliens sammelt.

<a name="base"></a>

## Eine SQL-Abfrage
Um auf die Datenbank zuzugreifen, müsst du SQL-Befehle verwenden. Das sieht so aus:
<sql-exercise
  data-question="Ein SQL-Code"
  data-comment="Klicken Sie auf Ausführen, um zu sehen, was passiert."
  data-default-text="SELECT *
  FROM Ausserirdische
  LIMIT 10">
</sql-exercise>

Das Programm zeigt die Aliens in Form einer Tabelle an. Hier sind die verschiedenen Kategorien, die die Wissenschaftler schon beobachtet haben:

<table>
 <tr>
  <td>Name</td>
  <td>Die Person, die einen neuen Alien entdeckt, kann ihm einen Namen geben</td>
 </tr>
 <tr>
  <td>Planet</td>
  <td>Der Planet, auf dem der Alien beobachtet wurde</td>
 </tr>
 <tr>
  <td>Anzahl_Koerperglieder</td>
  <td>Die Anzahl der Beine des Aliens</td>
 </tr>
 <tr>
  <td>Groesse</td>
  <td>Die Grösse des Aliens</td>
 </tr>
 <tr>
   <td>anzahl_Augen</td>
  <td>Die Anzahl der Augen des Aliens</td>
 </tr>
 <tr>
  <td>farbe_Augen</td>
  <td>Die Farbe seiner Augen</td>
 </tr>
 <tr>
  <td>Haut</td>
  <td>Wir schreiben nichts, wenn die Haut des Aliens glatt ist, sonst beschreiben wir seine Haut</td>
 </tr>
<tr>
<td>farbe_Haut</td>
  <td>Die Hauptfarbe des Aliens</td>
 </tr>
 <tr >
  <td>Antennen</td>
  <td>Achtung! Hier schreiben wir 1, wenn der Alien Antennen hat, und 0, wenn nicht. Ein Alien mit 72 Antennen wird als 1 notiert</td>
 </tr>
 <tr >
  <td >Gesicht</td>
  <td >Wir beschreiben, ob der Alien ein auffälliges Merkmal im Gesicht hat</td>
 </tr>
 <tr>
  <td >Kopf</td>
  <td >Die Form seines Kopfes</td>
 </tr>
 <tr>
  <td>Pizza</td>
  <td>Durch Beobachtung der Essgewohnheiten der Aliens können wir ihre Lieblingspizza bestimmen</td>
 </tr>
</table>

# Informationen in der Datenbank suchen:
SQL kann wie ein Satz gelesen werden (mit einigen Wörtern auf Englisch).
<sql-exercise
  data-question="Wenn wir Informationen über den Alien 'RODGERSIA_8121' haben wollen, müssen wir schreiben:"
  data-default-text="/*Wir wählen alle Variablen aus */ 
SELECT *  
/*Wir geben den Namen der Datenbank an */ 
FROM Ausserirdische
WHERE nom= 'RODGERSIA_8121'"
  data-solution="">
</sql-exercise>

<input-feedback 
data-title="Die Form des Kopfes des Aliens RODGERSIA_8121 ist"
data-solution="dreieckig"
success-message="Bravo !"
failure-message="Schau nochmal genauer hin!"></input-feedback>

Ich kann auch nach Aliens suchen, indem ich mehrere Merkmale benutze.

<sql-exercise
data-question="Aliens nach mehreren Merkmalen suchen"
data-comment="Zum Beispiel, wenn ich alle grünen Aliens mit Antennen und quadratischem Kopf suche, werde ich die folgende Suche eingeben (ergänze die '...'):"
data-default-text="SELECT *  
 FROM Ausserirdische
 WHERE farbe_Haut = '...'
 AND Kopf = '...'
 AND Antennen = 1
"></sql-exercise>
<div class="sideNote">
<p>Dir ist sicher aufgefallen, dass die Merkmale der Aliens, die Text sind, in 'einfache Anführungszeichen' geschrieben werden müssen, während die Merkmale, die Zahlen sind, keine Anführungszeichen benötigen. </p>
</div>

## Übung
Ich habe das Foto dieses schönen Aliens gefunden. Hilf mir, seinen Namen zu finden!

<img src="imgs/alien mystere.jpg" alt="drawing" width="20%"/>

<sql-exercise
data-question="Hilf mir, ihn zu finden!"
data-comment=""
data-default-text="SELECT *  
 FROM Ausserirdische
 WHERE ... "></sql-exercise>

<input-feedback 
data-title="Schreib hier seinen Namen (ohne Großbuchstaben):"
data-solution="trillium_3980"
success-message="Gute Arbeit!"
failure-message="Das ist leider nicht richtig"></input-feedback>

# Aliens zur Datenbank hinzufügen

Unglaublich, du hast einen neuen Alien auf dem Planeten Pythos entdeckt, den niemand vor dir beschrieben hat. Du hattest gerade noch Zeit, ein Foto zu machen. Als gute Wissenschaftlerin musst du ihn in die Datenbank eintragen. Da es deine Entdeckung ist, kannst du ihn nennen, wie du willst!

<img src="imgs/XXX_alien a ajouter.jpg" alt="drawing" width="30%"/>

<sql-exercise
data-question="Trage alle bekannten Merkmale des Aliens ein."
data-comment="Hier ist bereits ein Anfang. Setze ??? für die Merkmale, die du nicht kennst. Wie zum Beispiel schon getan für die Größe des Aliens, die wir nicht kennen."
data-default-text="INSERT INTO Ausserirdische
 VALUES ('der Name, den du willst',
         'pythos', 
         7, 
         '???', 
         4, 
         'grün',
         'die Textur seiner Haut',  
         'die Farbe des Aliens', 
         'die Anzahl der Antennen',
         'ein auffälliges Merkmal im Gesicht', 
         'die Form seines Kopfes', 
         'seine Lieblingspizza' );
"></sql-exercise>

<sql-exercise
data-question="Überprüfe, ob dein Alien erfolgreich in die Datenbank eingetragen wurde."
data-comment=""
data-default-text="SELECT *
 FROM Ausserirdische
 WHERE nom='...'
"></sql-exercise>

Es ist immer möglich, die Datenbank zu ändern.
<sql-exercise
data-question="Zum Beispiel kannst du die Lieblingspizza so ändern:"
data-comment=""
data-default-text="UPDATE Ausserirdische
 SET pizza= 'Pizza mit Tomatensauce'
 WHERE nom='der Name, den du willst'
"></sql-exercise>

# Eroberung des Weltraums!
Jetzt bist du an der Reihe zu erkunden!

Im Raum findest du 3 Fotos, die auf den Planeten Céplusplus, Scratchon und Pythos aufgenommen wurden. Auf diesen Fotos sehen wir viele verschiedene Aliens. Einige dieser Aliens sind bereits in unserer Datenbank erfasst. Andere sind es nicht. Deine Aufgabe und die der anderen Mädchen im Workshop wird es sein, die Namen der Aliens auf den Postern herauszufinden und diejenigen zur Datenbank hinzuzufügen, die noch nicht erfasst sind.
Wähle einen Alien von einem beliebigen Planeten. Um zu zeigen, an welchem du arbeitest, schreibe deinen Namen auf einen Post-it und klebe ihn neben den Alien.
Suche den gewählten Alien in der Datenbank. Wenn du ihn findest, schreibe seinen Namen auf den Post-it. Wenn er noch nicht erfasst ist, füge ihn mit dem Namen, den du willst, und allen beobachteten Merkmalen hinzu. Schreibe dann seinen neuen Namen auf den Post-it, um anzuzeigen, dass er jetzt Teil der Datenbank ist.

Viel Spass!

<sql-exercise
data-question="Um einen Alien zu suchen:"
data-comment=""
data-default-text="SELECT *
 FROM Ausserirdische
 WHERE nom='...'
"></sql-exercise>

<sql-exercise
data-question="Um einen Alien hinzuzufügen:"
data-comment=""
data-default-text="INSERT INTO Ausserirdische
 VALUES ('der Name, den du willst',
         'sein Planet', 
         '...', 
         '...', 
         '...', 
         '...',
         '...',  
         '...', 
         '...',
         '...', 
         '...', 
         '...' );
"></sql-exercise>

# Alien-Bilder generieren

Wir werden jetzt lernen, Alien-Zeichnungen zu generieren, indem wir bestimmte Merkmale festlegen.

## Beispiel

Du willst einen Alien nach der Beschreibung zeichnen, die du erhalten hast.
Deine Freundin Fabrizia hat heute Morgen einen Außerirdischen getroffen, leider konnte sie ihn nicht fotografieren. Sie beschreibt ihn dir:
"Er war orange und gefiedert, hatte einen Rüssel und 2 Arme sowie 7 große schwarze Augen. Leider erinnere ich mich nicht mehr an die Form seines Kopfes."
Wähle die Attribute aus, die du von deinem Alien nicht kennst.

Gehe zu deinem Computer, öffne im Ordner "cosmic data base" die Datei "Draw_alien.py" und gib die gewünschten Attribute an der richtigen Stelle im Code ein. Drücke dann auf den grünen Kreis mit einem weißen Pfeil, um das Programm auszuführen, und ein Alien sollte erscheinen.

Ein Bild deines Aliens wird im Ordner "Photo" generiert. Du kannst es Fabrizia geben, es wird ein schönes Andenken für sie sein.

## Übung

Die Forscherin Lou hat einen Alien in die Datenbank aufgenommen, er heißt "ARA LIA_8811".
Allerdings hat ihn bisher noch niemand in der Basis gesehen.
Wir werden die Aliens, die wir heute treffen, fragen, ob sie ihn schon einmal gesehen haben.
Dazu musst du ihn in der Datenbank suchen und seine Merkmale finden.
Erstelle dann ein Phantombild von ARA LIA_8811, um es den anderen Aliens zu zeigen.

<sql-exercise
data-question="Um die Merkmale des Aliens zu suchen"
data-comment=""
data-default-text="SELECT *
 FROM Ausserirdische
 WHERE nom='...'
"></sql-exercise>

# Bonus

Die Wissenschaftler haben die Außerirdischen nicht zufällig benannt. Seit Beginn hat die vierstellige Zahl im Namen jedes Aliens eine bestimmte Bedeutung.

<sql-exercise
data-question="Kannst du herausfinden, wie die Zahl im Namen jedes Aliens ausgewählt wird?"
data-comment="Schaue dir eine Liste von etwa fünfzehn Aliens an und versuche, die Logik zu verstehen."
data-default-text="SELECT *
 FROM Ausserirdische
 LIMIT 15
"></sql-exercise>
