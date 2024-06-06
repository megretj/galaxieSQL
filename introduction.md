---
title: Introduction atelier SQL
layout: tutorial_fr
dbFile: data/alien_fr.db
---
<h1>Cosmic Data Base!</h1>

<div class="warning">
Les informations présentes dans l'introduction seront données lors de la présentation. Si tu as écouté la présentation, tu n'as pas besoin de tout lire et tu peux directement commencer avec <a href="atelier.html">l'atelier</a>.<a href="atelier.html" class="button-link center"> Commencer l'atelier</a></div>

Aujourd'hui nous allons apprendre à gérer des bases de données grace à un outil bien pratique: SQL (Structured Query Language en anglais veut dire Langage de Requête Structurée). Mais à quoi servent les bases de données?

<div class="sideNote">
<p>Quand tu cherches une musique sur Spotify, ton téléphone envoie un message à un centre de données de Spotify (un datacenter) avec ta recherche. Un programme dans le datacenter s'exécutera alors pour chercher les musiques qui t'intéressent et ensuite te les proposer. Mais il y a des millions de musiques sur Spotify ! Et elles ont chacune un titre, un style, un nombre d'écoutes, un ou plusieurs artistes ... Comment rapidement trouver la musique que tu cherches dans ce grand bazar ? Il faut une sorte de grosse archive ou grande bibliothèque digitale pour enregistrer tout ça. On appelle cette archive une <span class="keyword">base de données</span>. Pour aller chercher des données sur cette base, ou y déposer de nouvelles données, il faut envoyer des commandes à l'ordinateur. Spotify a de grandes bases de données pour enregistrer non seulement toutes les musiques des artistes mais aussi le nombre d'écoutes, les playlists des utilisatrices, l'historique des écoutes, etc...</p>
</div>

Grâce au développement du monde numérique il est facile d'enregistrer beaucoup de données. Mais c'est parfois pas si facile de bien les ranger pour facilement les retrouver plus tard. Comme tu pourras le voir, le résultat de tes requêtes est donné sous forme de tableau, car après tout, les bases de données ne sont que de grands tableaux ! Néanmoins, ces derniers sont un peu trop grands pour pouvoir chercher les informations à la main. Mais heuresement, les ordinateurs sont très bons pour ce genre de tâche. Encore faut-il savoir parler leur langue pour leur demander poliment de faire le long et fastudieux travail de recherche d'informations. 

Comme pour tous les langages de programmation, il faut normalement installer des programmes pour pouvoir utiliser SQL mais ce site internet à été créé pour utiliser le SQL directement depuis ton navigateur. Pour faire une requête SQL [^1] il te suffit donc d'écrire ta commande dans un bloc de code comme celui ci et de cliquer sur "RUN" (lancer ou exécuter en anglais). 

[^1]: Plus précisément, on utilise [SQLite](https://sqlite.org/index.html), car SQL est un concept de programmation plus qu'un vrai langage.

<sql-exercise
  data-question="Ceci est un bloc de code interactif, tu peux éditer le code ci-dessous."
  data-comment="(Pour les pros: Shift+Enter est un raccourci clavier pour exécuter la commande au lieu de cliquer sur RUN)"
  data-default-text="SELECT *
FROM extraterrestres
LIMIT 5"></sql-exercise>

<div class="supplementary">
La particularité de SQL est que la syntaxe (les règles d'écriture) est assez libre. En particulier, on prend l'habitude d'écrire des mots clés comme <code>SELECT</code> en majuscule mais SQLite ne fait pas la différence entre majuscules et minuscule. On peut aussi ajouter des retours à la ligne et des tabulations à souhait. Pour une meilleure lisibilité, on garde souvent la syntaxe proposée dans cet atelier. Il est par contre important de suivre l'ordre dans laquelle on écrit les commandes (SELECT (MIN/MAX/COUNT/SUM) puis FROM (puis JOIN) puis WHERE/LIMIT/LIKE etc...). Il faut aussi faire attention à l'orthographe des éléments de la base de données.
</div>

<h4> Informations sur la base de données</h4>

Les données sont toutes générées aléatoirement.

Si tu ne te souviens plus d'une commande que tu as utilisée, tu peux te référer au <a href="commandes_sql.html">résumé des principales commandes sql</a>.

Dès que tu es prête, tu peux commencer l'atelier en cliquant sur le lien à coté de Next ci-dessous.
