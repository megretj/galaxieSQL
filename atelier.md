---
layout: tutorial_fr
title: Exploration spatiale
dbFile: data/alien_fr.db
---

# Exploration spatiale

On a découvert une forme de vie extraterrestre ! Le nouveau télescope SPS (space photographer system) permet d’observer la surface de planètes extra-galactiques.
<br>Jusqu’à maintenant, les scientifiques ont découvert trois exo-planètes habitées : 
<li>Céplusplus</li>
<li>Scratchon</li>
<li>Pythos</li>
Votre tâche sera de répertorier les différents types d’aliens observables. Pour cela, toutes les scientifiques de la terre mettent en place une base de données qui regroupe les aliens observés.

<a name="base"></a>

## Une requête SQL
Pour accéder à la base de données, il faut utiliser des commandes en langage SQL. Ça ressemble à ça :
<sql-exercise
  data-question="Du code SQL"
  data-comment="Appuie sur Run pour voir ce qui se passe."
  data-default-text="SELECT *
  FROM extraterrestres
  LIMIT 10">
  </sql-exercise>
  
Le programme affiche les extraterrestres sous la forme d'un tableau. Voici les différentes catégories que les scientifiques observent :

<table>
 <tr>
  <td>nom</td>
  <td>La personne qui
  découvre un nouvel alien peut lui donner un nom</td>
 </tr>
 <tr>
  <td >planète</td>
  <td>La planète sur laquelle a été observé l’alien</td>
 </tr>
 <tr>
  <td>nombre_membres</td>
  <td>Le nombre de pattes de l'alien</td>
 </tr>
 <tr>
  <td>taille</td>
  <td>La taille de l'alien</td>
 </tr>
 <tr>
   <td>nombre_yeux</td>
  <td>Le nombre d’yeux de l’alien</td>
 </tr>
 <tr>
  <td>couleur_yeux</td>
  <td>La couleur de ses yeux</td>
 </tr>
 <tr>
  <td>peau</td>
  <td>On n’écrit rien si la peau de l'alien est lisse, sinon on décrit sa peau</td>
 </tr>
<tr>
<td>couleur_peau</td>
  <td>La couleur globale de l’alien </td>
 </tr>
 <tr >
  <td>antennes</td>
  <td>Attention! ici on écrit 1 si l’alien a des antennes et 0 sinon. Un alien avec 72 antennes sera noté 1 </td>
 </tr>
 <tr >
  <td >visage</td>
  <td >On décrit si l’alien a un signe distinctif sur son visage </td>
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

# Chercher des infos dans la base de données :
Le SQL peut se lire comme une phrase. (Avec quelques mots en anglais). 
<sql-exercise
  data-question="Si on veut avoir des informations sur l'alien ' RODGERSIA_8121', il faut écrire:"
  data-default-text="/*On sélectionne toutes les variables */ 
SELECT *  
/*On indique le nom de la base de données */ 
FROM extraterrestres
WHERE nom= 'RODGERSIA_8121'"
  data-solution="">
  </sql-exercise>

<input-feedback 
data-title="La forme de la tête de l'alien RODGERSIA_8121 est"
data-solution="triangulaire"
success-message="Bravo !"
failure-message="Regarde mieux !"></input-feedback>

Je peux aussi chercher un alien en connaissant plusieurs de ses caractéristiques même si j'ai oublié son nom.


<sql-exercise
  data-question="Rechercher un alien selon des caractéristiques"
  data-comment="Par exemple, si je cherche un alien vert avec des antennes dont la tête est carrée, je vais taper la recherche suivante (à toi de compléter):"
  data-default-text="
  SELECT *  
    FROM extraterrestres
    WHERE couleur_peau = '...'
    AND tête = '...'
    AND antennes = 1
  "></sql-exercise>

<div class="sideNote">
<p>Tu remarqueras que les caractéristiques des aliens qui sont du texte doivent être écrites entre des 'simples guillemets' alors que les caractéristiques qui sont des nombres n'en ont pas besoin. </p>
</div>

## Exercice
J'ai retrouvé la photo de ce bel extraterrestre. Aide-moi à retrouver son nom ! 

<img src="imgs/luna_lovegood_portrait.jpg">

<sql-exercise
  data-question="Aide-moi à le retrouver !"
  data-comment=""
  data-default-text="SELECT *  
    FROM extraterrestres
    WHERE ... "></sql-exercise>

<input-feedback 
data-title="Écris son nom ici:"
data-solution="TRILLIUM_3980"
success-message="Bon travail !"
failure-message="Ce n'est malheureusement pas ça..."></input-feedback>

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
