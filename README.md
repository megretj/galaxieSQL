# Galaxie SQL

Repo pour l'atelier du coding club des filles pour apprendre le SQL: [Accio Query](https://megretj.github.io/galaxieSQL/)

**Service de promotion des sciences de l'EPFL - 2024**

### Notes pour le développement sous windows
#### Installer Jekyll

Après avoir cloné ce repo ```git clone https://github.com/megretj/galaxieSQL.git``` on peut modifier et recompiler le projet avec Jekyll. Le plus simple est de d'abord installer [wsl](https://learn.microsoft.com/fr-fr/windows/wsl/install) (windows subsystem for linux) dans le Powershell de windows afin de pouvoir installer et utiliser [official jekyll website](https://jekyllrb.com/). Le plus important est la commande suivante qui compilera le projet et lancera un serveur de développement (par défaut à l'adresse [http://127.0.0.1:4000/](http://127.0.0.1:4000/))

```
bundle exec jekyll serve
```

Appuyer sur crtl+C pour stopper le serveur de développement.

#### Développement/déploiment

Pour le développement en local ou le déploiment, il faut changer l'url et l'url de base dans [_config.yml](/_config.yml).

-----

This work is heavily inspired by the <a href="https://selectstarsql.com">selectstarsql.com</a> website by <a href="https://kaomorphism.com/">Kao Zichong</a>.

Prose and code is licensed by <a rel="author" href="https://www.epfl.ch/education/education-and-science-outreach/fr/promotion-des-sciences/">SPS EPFL</a> under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr">CC BY-NC-ND 4.0 License</a>. Concept and code inspired by <a href="https://selectstarsql.com/">SelectStarSQL</a>. Hosted on <a href="https://github.com/megretj/galaxieSQL">Github Pages</a>.