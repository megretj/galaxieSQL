---
title: Einführung SQL Workshop 
layout: tutorial_de
dbFile: data/alien_de.db
---
<h1>Galaxy SQL!</h1>
<div class="warning">
Dies ist eine Wiederholung der Informationen, die du bereits während der Präsentation gehört hast. Du musst also nicht alles nochmals genau lesen und kannst mit den <a href="workshop.html">Workshop</a> anfangen.
<a href="workshop.html" class="button-link center"> Workshop anfangen </a>
</div>

Heute lernen wir, Datenbanken mit einem sehr nützlichen Tool zu verwalten: SQL (Structured Query Language bedeutet auf Englisch Strukturierte Abfragesprache). Wieso braucht man Datenbanken überhaupt?

<div class="sideNote">
<p> Wenn du auf Spotify nach Musik suchst, sendet dein Telefon eine Nachricht an ein Spotify-Datenzentrum mit deiner Suche. Ein Programm im Datenzentrum wird dann ausgeführt, um die Musik zu finden, die dich interessiert, und sie dir dann zu schicken. Aber es gibt Millionen von Songs auf Spotify! Und sie haben alle einen Titel, einen Stil, eine Anzahl von Wiedergaben, einen oder mehrere Künstler... Wie findest du also schnell die Musik, die du in diesem großen Chaos suchst? Es braucht so etwas wie ein großes Archiv oder eine große digitale Bibliothek, um all das zu speichern. Diese Aufzeichnung nennt man eine <span class="keyword">Datenbank</span>. Um Daten in dieser Datenbank abzurufen oder neue Daten hinzuzufügen, müssen Befehle an den Computer gesendet werden. Spotify hat große Datenbanken, um nicht nur alle Songs der Künstler, sondern auch die Anzahl der Wiedergaben, die Playlists der Benutzer, die Wiedergabehistorie usw. zu speichern.</p>
</div>

Dank der Entwicklung der digitalen Welt ist es einfach, viele Daten zu speichern. Aber es ist manchmal nicht so einfach, sie gut zu organisieren, um sie später leicht wiederzufinden, dabei hilft uns SQL. Wie du sehen wirst, wird das Ergebnis deiner Abfragen in Form einer Tabelle angezeigt, denn schließlich sind Datenbanken nur große Tabellen! Trotzdem sind sie manchmal zu groß, um die Informationen *Zeile per Zeile* zu durchsuchen. Zum Glück sind Computer sehr gut in dieser Art von Aufgabe. Aber man muss immer noch die Sprache der Computer sprechen können, um sie höflich zu bitten, die langwierige Arbeit der Informationsrecherche zu erledigen. Für Datenbanken heisst diese sprache SQL.

Normalerweise muss man Programme installieren und ein Datenbank laden, um SQL verwenden zu können [^1], aber diese Website wurde erstellt, um SQL direkt in deinem Browser zu verwenden auf eine Datenbank über fictionale Ausserirdische. Um eine SQL-Anfrage zu stellen, musst du also deinen Befehl in einen Codeblock wie unten eingeben und auf "RUN" klicken (auf Deutsch heisst run starten oder ausführen).

[^1]: Genauer gesagt, wendet man [SQLite](https://sqlite.org/index.html), da SQL kein Programmiersprache im eigentlichen Sinne ist.

<sql-exercise
  data-question="Dies ist ein interaktiver Codeblock. Du kannst den Code unten bearbeiten."
  data-comment=""
  data-default-text="SELECT *
FROM Ausserirdische
LIMIT 3"></sql-exercise>

<div class="supplementary">
<p>Die Besonderheit von SQL ist, dass die Syntax (die Schreibregeln) ziemlich frei ist. Insbesondere neigen wir dazu, Schlüsselwörter wie <code>SELECT</code> in Großbuchstaben zu schreiben, aber SQL unterscheidet nicht zwischen Groß- und Kleinschreibung. Du kannst auch Zeilenumbrüche und Tabulatoren nach Belieben hinzufügen. Für bessere Lesbarkeit halten wir uns oft an die in diesem Workshop vorgeschlagene Syntax. Es ist jedoch wichtig, die Reihenfolge einzuhalten, in der die Befehle geschrieben werden (SELECT (MIN/MAX/COUNT/SUM) dann FROM (dann JOIN) dann WHERE/LIMIT/LIKE usw.). Es ist auch wichtig, auf die Syntax innerhalb der Datenbank zu achten.</p>
</div>


<a name="datenbankInfo"></a>

<h4>Informationen zu diese Datenbank:</h4> 

* Die Daten sind zufällig generiert.

<h4> Hilfe </h4>

Wenn du dich nicht mehr an einen Befehl erinnerst, den du verwendet hast, kannst du die <a href="sql_befehle.html">Zusammenfassung der wichtigsten SQL-Befehle</a> ansehen.

Wenn du bereit bist, kannst du mit dem Workshop beginnen, indem du auf den Link neben "Next" klickst.
