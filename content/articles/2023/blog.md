Title: Lancement de mon blog
Category: Informatique
Tags: pelican, python, autohébergement, web, blog
Date: 2023-07-27
Status: published

Suite à une bouillante réflexion, j'ai finalement pris la décision brillante d'exploiter mon site pour y partager toutes mes expériences excentriques.
J'ai bon espoir que les plus audacieux d'entre vous seront ravis de découvrir toutes les informations et astuces que je partage ici à la sueur de mon front 😁

## Pourquoi et pour quoi ?

Transformer mon site, qui, jusqu'à présent, assurait la simple fonction de "point d'accueil de mon nom de domaine parce qu'il en faut bien un" en quelque chose de plus pertinent.

Écrire mes expériences de vie, apportera, je l'espère, plusieurs avantages. Les passionnés comme moi ont tous secrètement cette envie de partage, mais c'est autre chose de se lancer.

Sur ce blog, pas de thème précis, j'aborderais tout sujet et thématique selon mon humeur délirante du moment, sous la seule condition que le contenu sera en mesure de créer une frénésie de passion sans précédent auprès d'une foule en délire qui ne manquera pas de s'abonner au [Flux RSS <i class="fa fa-rss"></i>](https://heuzef.com/feeds/all.atom.xml).

## Salut Pelican

C'est donc naturellement que je vais commencer à vous parler du choix de l'outil que j'utilise pour me lancer dans cette aventure : [Pelican](https://getpelican.com)

![Pelican](../../assets/pelican.png)

Cet outil est absolument parfait pour les dingos exigeants comme moi, ce moteur Python ultra léger permet de générer un site statique à partir de vos fichiers Markdown ou reStructuredText.

Aucune base de données ni moteur web requis, il suffit de lancer la moulinette et Pelican va vous recracher fissa un site web statique complet (HTML, CSS, JS).

Cette note est la première que je fais suite à une installation et configuration de mon instance Pelican et c'est clairement très efficace, car l'outil n'en reste pas moins puissant et offre un large choix de fonction (Gestion de thème, extenssion, Flux RSS, publications multi-langue, etc ... ), et surtout tout est à plât et versionné sur mon [git](https://git.heuzef.com/heuzef/heuzef_com), et la personnalisation est possible sans contrainte.

C'est auto-hébergeable, libre et documenté, bref rien à redire, c'est le pied, fait tourner c'est de la bonne.

Merci à mon tout-puissant Sensei [Ephase](https://xieme-art.org) pour m'avoir inspiré et aidé à découvrir cet outil 😎

## Faire connaissance avec le piaf

Une fois votre serveur web prêt, il vous faudra installer quelques nécessités : Python avec virtualenv, pip et make.

Pour les modules pip, voici une liste de quelques dépendances que j'utilise : [<i class="fa fa-file"></i> requirements.txt](https://git.heuzef.com/heuzef/heuzef_com/src/branch/master/requirements.txt)

### Installation et configuration

Allons-y Alonso ! ✊

```bash
# Activation du virtualenv Python
virtualenv ~/virtualenvs/pelican
cd ~/virtualenvs/pelican
source bin/activate

# Installation de Pelican dans votre dossier d'hébergement web
cd /var/www/html/
pip3 install -r requirements.txt
```

Puis il suffit de se laisser guider pour la configuration :

```bash
pelican-quickstart
```

Vient alors le choix du thème (j'ai personnellement opté pour [Pelican-Alchemy ✨](https://github.com/nairobilug/pelican-alchemy) pour le moment) et des extenssions.
Puis finalement, il faut passer du temps à personnaliser les fichiers de configuration **.py**, ajouter votre contenu dans le dossier **content** et faire pointer votre serveur web sur le dossier **output** qui contient votre site statique généré.

```bash
/
├── content
│   └── (pages)
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

### Exemple d'utilisation

Pour exemple, voici à quoi ressemble le fichier Markdown de cet article :

```Makefile
Title: Lancement de mon blog
Cover: assets/bg_pelican.jpg
Category: Informatique
Tags: pelican, python, autohébergement, web, blog
Date: 2023-08-01 0:00
Status: published

Blah blah ... et ils trépignèrent à la lecture de cette note ... blah blah !
```
Un pti coup de moulinette :

```bash
make publish
```

Et vouualaaa ! 👌

Vous avez les bases, la [documentation](https://docs.getpelican.com) de Pelican vous permettra d'aller plus loin ensuite.

À bientôt pour de nouvelles aventures !
