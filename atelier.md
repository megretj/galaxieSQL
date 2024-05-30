---
layout: tutorial_fr
title: Exploration spatiale
dbFile: data/alien_fr.db
---

# Exploration spatiale

On a découvert la vie extraterrestre ! Le nouveau télescope SPS (space photographer system) permet d’observer la surface de planète extra-galactique.
<br>Jusqu’à maintenant, les scientifiques ont découvert trois exo-planète habitées : 
<li>Céplusplus</li>
<li>Scratchon</li>
<li>Pythos</li>
Votre tache sera de répertorier les différents types d’aliens observable. Pour cela, tous les scientifiques de la terre mettent en place une base de données qui regroupent tous les aliens observés.

<a name="base"></a>

## Une requête SQL
Pour accéder à la base de données, il faut utiliser des commandes en langage SQL. Ça ressemble à ça :
<sql-exercise
  data-question=Du code SQL"
  data-default-text="
  SELECT *
  FROM extraterrestres
  LIMITE10"
  
  </sql-exercise>





Ceci est un <span class="keyword">mot clé</span> et ça du <code class=keyword>texte formaté comme du code important</code> ou du <code>code moins important</code>.

<sql-exercise
  data-question="Titre du bloc SQL"
  data-comment="Commentaire"
  data-default-text="texte par défault dans le champs de texte à remplir"></sql-exercise>

<sql-exercise
  data-question="On peut aussi mettre une solution et afficher du texte si l'exercice est réussi"
  data-comment="Si "
  data-default-text = "/* Ceci est un commentaire. */
  Quelle est la vraie vérité?"
  data-solution="C'est la vérité vraie"
success-message="Bravo"
failure-message="Pas bravo"></sql-exercise>

<div class="warning">
Attention, ceci est un lien <a href="commandes_sql.html">vers une autre page</a> ou <a href="https://theuselessweb.com/">un site internet super</a>.
</div>

<input-feedback 
data-title="Exercice sous forme de texte"
data-solution="la solution"
success-message="Bravo"
failure-message="NUL"></input-feedback>
