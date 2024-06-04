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

# Chercher des informations dans la base de données :
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

Je peux aussi chercher des aliens en connaissant plusieurs caractéristiques.

<sql-exercise
  data-question="Rechercher des aliens selon plusieurs caractéristiques"
  data-comment="Par exemple, si je cherche tous les aliens verts avec des antennes dont la tête est carrée, je vais taper la recherche suivante (à toi de compléter les '...' ):"
  data-default-text="SELECT *  
    FROM extraterrestres
    WHERE couleur_peau = '...'
    AND tête = '...'
    AND antennes = 1
  "></sql-exercise>

<div class="sideNote">
<p>Tu remarqueras que les caractéristiques des aliens qui sont du texte doivent être écrites entre des 'simples guillemets' alors que les caractéristiques qui sont des nombres n'en ont pas besoin. </p>
</div>

## Exercice
J'ai retrouvé la photo de ce bel extraterrestre. Aide-moi à trouver son nom ! 

<img src="imgs/alien mystere.jpg" alt="drawing" width="50%">


<sql-exercise
  data-question="Aide-moi à le retrouver !"
  data-comment=""
  data-default-text="SELECT *  
    FROM extraterrestres
    WHERE ... "></sql-exercise>

<input-feedback 
data-title="Écris son nom ici:"
data-solution="TRILLIUM"
success-message="Bon travail !"
failure-message="Ce n'est malheureusement pas ça "></input-feedback>

# Ajouter des aliens à la base de donnée

Incroyable, tu as découvert un nouvel alien, sur la planète pythos, que personne n'avait vu avant toi. Tu as juste eu le temps de le prendre en photo. En tant que bonne scientifique, tu vas devoir l'ajouter à la base de données. Comme il s'agit de ta découverte, tu vas pouvoir l'appeler comme tu veux !

<img src="imgs/XXX_alien a ajouter.jpg" alt="drawing" width="50%">

<sql-exercise
  data-question="Entre toutes les caractéristiques connues de l'alien."
  data-comment="J'ai commencé à le faire pour toi. Mets des ??? pour les caractéristiques que tu ne connais pas."
  data-default-text="INSERT INTO extraterrestres
    VALUES ('le nom que tu veux',
            'pythos', 
            7, 
            '???', 
            4, 
            'vert',
            '...',  
            '...', 
            '...',
            '...', 
            '...', 
            '...' );
  "></sql-exercise>


<sql-exercise
  data-question="Vérifie que ton alien a bien été ajouté à la base de données."
  data-comment=""
  data-default-text="SELECT *
    FROM extraterrestres
    WHERE nom='...'
  "></sql-exercise>
  
Il est toujours possible de modifier la base de donnée.
<sql-exercise
  data-question="Par exemple, tu peux changer la pizza préférée ainsi:"
  data-comment=""
  data-default-text="UPDATE extraterrestres
    SET pizza= 'pizza au sugus'
    WHERE nom='le nom que tu veux'
  "></sql-exercise>
  
# À la conquête de l'espace !
C'est maintenant à toi d'explorer ! 

Dans la salle, tu trouveras 3 photos prises sur les planètes Céplusplus, Scratchon et Pythos. Sur celles-ci, nous y voyons plein d'aliens différents. Parmi ces aliens, certains sont déjà recensés dans notre base de données. D'autres ne le sont pas. Ton travail, ainsi que celui des autres filles de l'atelier, sera de trouver le nom des extraterrestres des posters et d'ajouter à la base de données ceux qui n'y sont pas encore. 
Choisis un alien, de n'importe quelle planète. Pour montrer sur lequel tu travailles, écris ton nom sur un post-it et colle-le à côté de l'alien. 
Cherche l'extraterrestre choisi dans la base de données. Si tu le trouves, écris son nom sur le post-it. Par contre, s'il n'est pas encore recensé, ajoute-le avec le nom que tu voudras et toute les caractéristiques que tu observes. Écris ensuite son nouveau nom sur le post-it pour indiquer qu'il fait maintenant parti de la base de données.

Bon travail ! 


<sql-exercise
  data-question="Pour rechercher un alien:"
  data-comment=""
  data-default-text="SELECT *
    FROM extraterrestres
    WHERE nom='...'
  "></sql-exercise>


<sql-exercise
  data-question="Pour ajouter un alien:"
  data-comment=""
  data-default-text="INSERT INTO extraterrestres
    VALUES ('le nom que tu veux',
            'sa planète', 
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

# Générer des images d'alien

Nous allons maintenant apprendre à générer des dessins d'aliens en fixant certaines caractéristiques précises. 

## Exemple
Tu veux dessiner un alien à partir de la description que tu as reçue.
Ton amie Fabrizia a croisé un extraterrestre ce matin, malheureusement, elle n'a pas réussi à le prendre en photo. Elle te le décrit: 
"Il était orange à plumes, il avait une trompe et 2 bras ainsi que 7 grands yeux noirs. Malheureusement je ne me souviens plus de la forme de sa tête."
Les attributs que tu ne connais pas de ton alien seront choisi aléatoirement.

Rends toi sur le bureau de ton ordinateur, dans le dossier "cosmic data base FR" ouvre le fichier "generation alien.py" et entre les attributs que tu souhaites au bon endroit dans le code.
Une image de ton alien sera générée dans le dossier "Photo". Tu pourras la donner à Fabrizia, ça lui fera un joli souvenir. 

## Exercice
La chercheuse Lou a ajouté un alien dans la base de données, il s'appelle "ARA LIA_8811". 
Par contre, personne n'a encore croisé cet alien à la base. 
Nous allons demander aux extraterrestres que nous croisons aujourd'hui s'ils l'ont déjà vu. 
Pour cela, il va falloir que tu le cherche dans la base de données et que tu trouves ses caractéristiques.
Génère ensuite un portrait robot de ARA LIA_8811 afin de pouvoir le montrer aux autres aliens. 

<sql-exercise
  data-question="Pour rechercher les caractéristiques de l'alien"
  data-comment=""
  data-default-text="SELECT *
    FROM extraterrestres
    WHERE nom='...'
  "></sql-exercise>

# Bonus

Les scientifiques n'ont pas nommés les extraterrestres de manière aléatoire. Depuis le début, le nombre à quatre chiffres dans le nom de chaque alien a une signification précise.  

<sql-exercise
  data-question="Arrives-tu à comprendre comment est choisi le nombre dans le nom de chaque alien"
  data-comment="Sors une liste d'une quinzaine d'aliens et essaie de comprendre la logique."
  data-default-text="SELECT *
    FROM extraterrestres
    LIMIT 15
  "></sql-exercise>

