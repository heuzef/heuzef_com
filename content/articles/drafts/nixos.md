Title: À la découverte de NixOS une distribution Linux pas comme les autres
Category: Parentalité
Tags: linux, astuce, opensource, chiffrement
Date: 2026-04-01
Status: draft

Si vous êtes un Linuxien et avez déjà testé quelques distributions dans votre vie, je vous invite à partir à l'aventure avec moi pour découvrir **tranquillement** NixOS.

"Encore une, j'ai déjà ma favortie et [NixOS stagne dans le top 20 en popularité](https://distrowatch.com) ..." me direz-vous. Et bien, si vous ne connaissez pas encore ce qui la rend spéciale, vous risquez d'être surpris.

## Pourquoi NixOS est différent ? ❄️

NixOS est une distribution qui suscite l'admiration d'un côté, mais aussi la terreur pour d'autre, ce qui explique surement sa popularitée stagnante. À mon sens, c'est un peu comme chercher à dompter un cheval sauvage. Ça fait peur, on ne sait pas trop commment s'y prendre ... mais si l'on y parvient, c'est une satisfaction incroyable qui nous attend.

Le gros point noir de cet OS, c'est sa courbe d'apprentissage attroce. Ainsi, si vous n'êtes pas prêt à faire un gros effort pour sortir de votre zone de confort, vous pouvez arrêter la lecture de cet article et retourner sur votre Ubuntu, autrement, vous aller découvrir à quel point cet OS est incroyable.

![nixos_001.png](../../assets/nixos_001.png)

Alors finalement, quel est sont secret ? La réponse : c'est un OS déclaratif. 

Explications :

Sur un OS classique, vous aller vouloir, par exemple, installer un logiciel. Ainsi, vous aller le configurer pour télécharger l'outil, le déployer et le paramétrer. Sur un Ubuntu, c'est un classique `sudo apt install` dans le terminal. Et bien sur NixOS, pas du tout, car vous n'allez tous simplement **jamais le configurer**.

En effet, **NixOS ne se configure pas, il se déclare !** C'est là toute la puissance de ce système. Les adèptes de Ansible, Terraform et autre système "as code" comprennent très bien l'énorme avantage du déclaratif face à l'impératif. 

Pour les autres, voici une petite analogie : vous souhaitez faire un gâteau aux chocolat, pour l'ammener chez vos hôtes. Dans ce cas, la logique voudrais donc (en imperatif donc) que vous preniez votre recette favorite, réunissez les ingrédients, les ustenssils de cuisines, puis vous opérer la patisserie. Bam, vous avez votre gâteau, c'est cool. Puis nous recommençons de nouveau, le mois suivants, probablement différement mais toujours avec cette même méthodologie.

Maintenant, la logique déclarative, ça serait plutôt : J'écris mon livre de recette du gâteau au chocolat, avec tous les détails de chaque étape (c'est fastidieux). Maintenant que j'ai mon livre, je le confie à un patissier et Bam, j'ai mon gâteau direct. Le mois suivant ? Pas de problème -> patissier -> bam gâteau -> 0 effort. Je veux 10 gâteaux ? Je donne ma recettes à 10 patissiers -> 0 effort. J'ai envie de changer le dossage du sucre dans ma rectte ? Et bien je met à jour mon livre de recette -> tous les gâteaux seront actualisés.

L'effort initiale ici qui est donc de créer le livre de recette et donc la phase importante et chronophage, mais une fois fait, c'est la foire à la saucisse.

Voici un exemple simple plus concret pour bien se représenter le truc : j'ai une imprimante à la maison. Auparravant, je prenais 1h sur chaque PC à chaque fois que nécessaire de pour l'installer, mettre à jour les pilotes, logiciels, etc ... Sur NixOS, j'ai un fichier de configuration qui comprend tous ce qu'il faut pour profiter d'une imprimante opérationnelle et paramétré aux oinions, ce qui m'a pris 1 journée entière à coder et tester. Et maintenant ? J'en ai oublié la notion même de devoir ce farcir ça, car cette configuration est tous simplement déployé automatiquement sur toutes mes machines en parrallèles, je n'aurais plus jamais besoin de m'en soucier, tant que je ne change pas d'imprimante. L'autre avantage, c'est que revenir sur ce fichier de configuration me permet de comprendre et de maîtriser tous le processus.

Voici par exemple comment je gère ma liste de logiciels depuis mon fichier de configuration :

```nix
home.packages = with pkgs; [
    audacity
    gimp3
    libreoffice-fresh
    vlc
    zoom-us
  ];
```

Et maintenant, si je souhaite par exemple installer Google-Chrome, je modifie très simplement mon fichier de configuration ainsi :

```nix
home.packages = with pkgs; [
    audacity
    gimp3
    google-chrome # <---- Ajouter simplement cette ligne
    libreoffice-fresh
    vlc
    zoom-us
  ];
```

Aussi simplement que ça, j'ai Google-Chrome qui sera déployé sur toutes mes machines.

Avec cette logique, appliqué sur tous mon système, cela me permet de :

* Coder absolument toute ma configuration
* Prendre le temps de comprendre en profondeur la configuration que j'applique
* Versionner toute ma configuration sur GIT
* Exposer ma configuration publiquement, très pratique pour le partage (nous abordement un peu plus loin l'aspect chiffrement des secrets)
* Ne plus jamais avoir besoin de réinstaller mon OS en Vanilla
* Me forcer à adopoter un comportement rigoureux et ne plus permettre de mauvaises pratique (sécurité, organisation, etc ...)
* Ne plus altérer mon système à cause de manipulations regretables
* Profiter d'environnement virtuelle temporaires pour des besoins ponctuelle
* Obtenir un OS de plus en plus confortable et évolutif dans le temps
* Automatiser des déploiements
* Pré-paramétrer tous mes outils
* ...

Je ne peux faire seulement que ça pour l'instant, car je suis encore qu'un débutant sur cet OS. Mais j'ai été témoins de sacrés trucs, pour ceux qui matrîse la bête, c'est fabuleux.
