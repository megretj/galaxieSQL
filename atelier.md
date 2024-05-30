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
  data-question="Du code SQL"
  data-comment="Appuie sur Run pour voir ce qui se passe."
  data-default-text="SELECT *
  FROM extraterrestres
  LIMITE 10">
  </sql-exercise>
  
Le programme affiche un tableau. Voici les différentes catégories que les scientifiques observent :

<table>
 <tr>
  <td>nom</td>
  <td>La personne qui
  découvre un nouvel alien peut lui donner un nom</td>
 </tr>
 <tr>
  <td >planète</td>
  <td>La planète sur lequel a été observé l’alien</td>
 </tr>
 <tr>
  <td>nombre_membres</td>
  <td>Le nombre de pattes d’un alien</td>
 </tr>
 <tr>
  <td>taille</td>
  <td>La taille d’un  alien</td>
 </tr>
 <tr>
   <td>nombre_yeux</td>
  <td>Le nombre d’yeux de l’alien</td>
 </tr>
 <tr>
  <td>couleur_yeux</td>
  <td>La couleur de leur yeux</td>
 </tr>
 <tr>
  <td>peau</td>
  <td>On n’écrit rien si la peau d’un alien est lisse et sinon on décrit sa peau</td>
 </tr>
<tr>
<td>couleur_peau</td>
  <td>La couleur globalede l’alien </td>
 </tr>
 <tr >
  <td>antennes</td>
  <td>Attention! ici on écrit 1 si l’alien a des antennes et 0 sinon. Un alien avec 72 antennes sera noté !</td>
 </tr>
 <tr >
  <td >visage</td>
  <td >On décrit sil’alien à un signe distinctif sur son visage </td>
 </tr>
 <tr>
  <td > tête</td>
  <td >La forme de sa tête</td>
 </tr>
 <tr>
  <td> pizza </td>
  <td> En observant les habitudes alimentaires des aliens, on peut déterminer sa pizza préférée.</td>
 </tr>
</table>

## Chercher des infos dans la base de données :
Le SQL peut se lire comme une phrase. (Avec quelques mots en anglais). 
<sql-exercise
  data-question="Si on veut chercher l'alien " RODGERSIA_8121", il faut écrire:"
  data-comment=""
  data-default-text="/*On sélectionne toute les variables */ 
SELECT *  
/*On indique quelle base de données */ 
FROM extraterrestres
WHERE nom= "RODGERSIA_8121"
"
 data-solution=""
></sql-exercise>



# Save au cas OU

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
