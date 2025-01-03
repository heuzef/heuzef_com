Title: Fabriquez son clavier machanique sur mesure
Category: Informatique
Tags: clavier, mécanique, diy
Date: 2023-08-01
Status: draft

# Pourquoi fabriquer son propre clavier sur mesure ? 🧰

Si vous passer une grande partie de votre vie derière un écran, vous avez probablement déjà investi dans un clavier haut de gamme et vous ne regrettez certainement pas l'achat de ce périphértique très important.

Je vous proprose d'aller encore plus loin dans cette logique en fabriquant votre propre clavier sur-mesure, le temps et l'argent que cela demande est largement compensée par le gain en confort et productivité que cela vous apportera. De plus, le petit bijoux que vous aller fabriquer sera unique pour vous, vraiment durable, évolutif et facile d'entretient.

![keyboard_001](../../assets/keyboard_001.webp)

Pensez-y sérieusement, la prochaine fois que vous reflechissez à acheter un nouveau clavier : **fabriquez-le !** Je vous rassure, c'est simple et agréable, un peu comme fabriquer son propre PC finalement.

Nous allons donc passer en revue toutes les étapes à suivre dans l'ordre pour obtenir le clavier ultime de vos rêves et pour la vie.

# Mais combien ça va me coûter !? 🧐

Bonne nouvelle, ça dépend de vous, même si le but du projet c'est d'y mettre plus cher qu'un clavier de luxe, il faut savoir que certaines marque, comme par exemple Razer, vendent des claviers à 350€, ils ont en moyenne une durée de vie de 1 an, c'est donc clairement un mauvais investissement.
Pour ce projet, je vous recommande d'envisager une enveloppe de 300€ à 500€, vous aviserez ensuite selon vos ambitions, car il  est facile de se laisser  tenter pour se faire plaisir 🤗

# Deux types de clavier ⌨️
Il est important de bien comprendre que les vrais clavier historique, sont mécaniques. Car il existe également des clavier plus récent, de bien moindre qualitée et donc moins cher, que nous retrouvons assez fréquement : les claviers à membrane.

![keyboard_002](../../assets/keyboard_002.webp)

## Clavier à membrane
Comme le nom l'indique, ces claviers disposent d'une membrane en silicone pour la pression des touches ce qui en fais clavier :

* Pas chère (prix moyen 20€)
* Capable d'encaisser des accidents de café (le silicone est étanche et "protegera" des liquides)
* Silencieux

C'est simple et efficace, adapté pour de la bureautique occasionnelle, ce type de clavier jetable est particulièrement médiocre et dispose d'une durée de vie de quelques année tout au  plus.
Certaines marque peux scrupuleuses ne vont pas hésiter à vendre ce type de clavier plusieurs centaines d'euro, ne vous faites plus avoir.

## Clavier mécanique
Bénéficie d'une vitesse de frappe rapide, fluide, précise et peuvent bénéficier de toutes les qualités imaginable et s'absoudre de tout les défauts. Sont prix est assez élevé.

![keyboard_003](../../assets/keyboard_003.webp)

## Le choix est  donc simple
Donc pour résumer, si vous n'êtes pas prêt à mettre la main au portefeuille, procurez-vous un clavier à membrane en grande surface, sinon, nous allons pouvoir commencer à jouer dans la cours des grands 🤓

# Composant d'un clavier

Un clavier, c'est plutôt simple, nous avons  :

* Une carte PCB, le coeur du clavier, dans un chassis.
* Le chassis lui même est en deux parties inférieur et supérieur dans laquel nous retrouverons une plaque qui accueillera les touches.
* Les touches se décomposent en deux parties :
	* les switchs (commutateurs)
	* les keycaps (capuchons)

Voila, il vous suffira donc de concentrer vos choix sur ces composants. Mais vous allez voir, que nous avons l'embarra du choix justement !

# La mise en page et le format

Commençons par le plus important : décider du layout que vous souhaitez, il s'agit de la taille et forme de votre clavier. Puis enfin le format, qui est définie par une norme.

## Mise en page

Concernant le layout, le standard est le 100%, soit la taille offrant un pavé numérique complet, une rangée de fonctions et un cluster de navigation. C'est le format le plus grand et le plus proche d'un clavier d'ordinateur historique.

Si votre but est d'avoir le clavier le plus complet, alors le 100% est fait pour vous.

Plus grand que 100%, signifirais un ajout de module externe au clavier.

Enssuite, il est possible de rendre le clavier plus compact en supprimant des touches :

80% ou TKL (Tenkeyless) est en faite un clavier 100% mais sans le pavé numérique.

40%, c'est le plus petit, si vous cherchez du ultra-compact.

Et bien entendu, il existe toutes une multitude de layout entre 100% et 40%, pour répondre à votre besoin.

## Format

La norme ISO est la plus répendue car international, c'est surement ce type de clavier que vous avez l'habitude d'utiliser. Mais il existe également une norme américaine ANSI.
La différence n’est pas évidente de prime abord. Mais il existe des nuances bien réelles qui les distinguent :

* Le nombre de touches peut varier, jusqu'à quatre.
* Sur un clavier ISO, la touche ENTER est large, alors que sur un modèle ANSI, il n’apparaît que sur une seule.
* La touche Shift gauche est plus large sur les clavier ANSI. Supprimant donc une touche.

Voici une image pour visualiser les différences :

IMAGE

Les nuances entre ces 2 normes est importante et je vous recommande de tester les deux claviers pendant un temps pour conforter dans votre choix.

Pour ma part, j'ai banni le ANSI, car j'avais tendance à appuyer sur ``* + ENTER`` pour simplement appuyer sur ``ENTER``. Ce qui à été fatal le jour où j'ai saisi une commande de suppression dans un terminal linux, (les adeptes du ``rm /*`` comprendrons ma douleur).

# L'agencement

Pour terminer, afin d'aider nos décisons future, il est important de choisir un agencement pour notre clavier.

Gardez à l'ésprit, que cette étape pourra être très facilement modifiée grâce au principe des Keycaps des claviers mécanique, il est en effet très facile de changer l'emplacement des touches. Mais bon, il faut bien commencer par un agencement.

Si vous êtes Français, vous aller très surement opter pour du classique **AZERTY** ou éventuellement du **QWERTY** si vous êtes habitué au clavier anglophone.

Sachez juste pour votre culture, que ces deux agencements sont très médiocres et non optimal pour la vitesse et le confort de frappe. Ils se sont juste trop imposés pour être remplacés :(

Si cela vous interesse, l'équivalent le plus optimal de l'**AZERTY** s'appel le **BÉPO**. Et l'équivalent du **QWERTY** est le **DVORAK**.

Si vous êtes prêt à vous réadapter et réapprendre à tapper au clavier, vous pouvez envisager ces agencements : **gain monumental de confort et vitesse de frappe assuré !**

## Où en somme-nous ?

Nous avons donc décidé le Layout, le format et l'agencement de notre bébé. Nous allons donc pouvoir commencer à regarder autour des constructeurs ce qu'ils nous propose. Pour ma part, je vous recommande Keychron car j'ai une expérience parfaite avec eux.

> Découvrir la marque **KEYCHRON** sur [https://keychron.fr](https://keychron.fr)

Libre à vous de fouiller chez la concurence pour comparer.
Le plus important et de garder à l'esprit que vous chercher un fabricant sérieux, capable de vous fournir :

* Un clavier mechanique entièrement démontable.
* Le PCB et le chassis peuvent être achetée séparéments.
* Possible d'acheter les pièces en kit pour monter le clavier soit même.
* Offre de nombreux accessoires et pièces dans sa boutique.

> Découvrir d'autres marques sur [https://mechanicalkeyboards.com/pages/brands](https://mechanicalkeyboards.com/pages/brands)

L'objectif est de gagner en résilience pour être autonome sur l'évolution et l'entretient de la bête.
 Pour cela, le clavier devra **obligatoirement** disposer d'une carte PCB **HOT-SWAPPABLE** pour vous permettre de disposer les switchs comme bon vous semble. Si le clavier ne permet pas ça, c'est éliminatoire.

Vous pouvez également envisager que le clavier soit compatible **QMK et VIA**, si vous souhaitez aller très loins dans la personalisation des touches de votre clavier, c'est pertinent. Ce firmware Open-Source s'impose comme un standard des claviers mécanique de plus en plus.

C'est bon, vous avez trouvez le model de vos rêves, nous allons maintenons commencer à le pimper !

# Personalisation

A vous de décidez de la couleur du chassis, des matériaux et si vous souhaitez du sans-fils.
Gardez à l'esprit que ces choix sont généralement définitif car couteux à changer, ainsi, je vous recommande de partir sur quelques chose de durable et intemporelle. Un chassis en métal (exit le plastique) noir, en filaire (pas de problème de piles ou batterie). Mais c'est strictement personnel comme décision.

Il est temps de concevoir vos touches maintenant ! :)

# Les Switchs (Commutateurs)

Si vous avez bien pris soin de vous assurer que votre clavier est compatible **Hot-Swap**, cela signifie que chaque touches de votre clavier peut être changés à chaud.
Plus précisément, il vous est possible de changer le switch, qui correspond a la méchanique du bouton avec un simple extracteur.

Il existe ainsi de nombreux type de switch ayant des effets et senssation bien différentes ainsi que plusieurs fabricants, le plus connus et servant de standard sont **Cherry MX** car ce sont les pionniers, cependant il existe aussi des alternatives populaires comme **Gateron**, leur gammes et tarrifs sont plus abordable. **Kailh**, qui eux vont plutôt chercher à vendre de la haute qualité innovante. **Outemu**, fabricant chinois avec des prix agressifs et d'autres marques plus spécialisée (TTC, Tealios, Holy Panda, ...).

Ces fabriquants peuvent proposer des centaines de type de Switch diversifiant alors la sensation de frappe, la durabilité, les matériaux, les tendances et innovation, ...

Ce qui est interessant ici, c'est qu'un Switch équivaudra de façon universel à une touche de votre clavier, peut importe la marque ou la touche, c'est pour cela que l'on à tendance à acheter des boites de switch pour avoir un petit stock et de la variété, surtout si vous souhaitez utilisez plusieurs type de switch pour votre clavier (ce que je vous recommande ! Faites vous plaisir !).

Voici les 4 catégories communes à tous les switchs :

**Tactile, (classique et infaillible)** : désigne un interrupteur doté d'une bosse physique et sensorielle pendant la frappe, ce qui vous donne la tranquillité d'esprit subconsciente pendant que vous tapez, sachant que vos frappes sont enregistrées.

**Linéaire, (vite vite !)** : désigne un interrupteur sans bosse tactile. Un interrupteur linéaire est souvent privilégié par les joueurs, en particulier pour les jeux nécessitant une saisie rapide.

**Cliquable (CLIC CLIC !)** : signifie exactement ce que cela signifie. Ce type d'interrupteur est connu pour son "CLICKY !" fort et audible pendant que vous tapez. Similaire aux interrupteurs que l'on trouve sur un clavier d'ordinateur vintage ou une machine à écrire. Adoré par les dactylos et destesté par les personnes dans le même bureau que vous.

**Silencieux (chuuut ...)** : sont conçus pour minimiser le bruit produit pendant la frappe. Ils sont généralement dotés d'un matériau souple qui atténue le bruit de l'actionnement de l'interrupteur et de son appui, ce qui les rend idéaux pour les environnements de bureau ou les espaces partagés.

Mais comment savoir quel type de Switch choisir dans ce cas ! Facile de s'y perdre en effet. Et bien la réponse est simple : il vous faut vous procurer des testeurs de Switch.

En général les testeurs de switch comprennent une dizaine de switch d'une marque et il est possible d'en avoir qui offrent une centaine de touches. Les prix varient en moyenne entre 10€ et 50€ pour des versions sans Keycaps.

Le problème ici, c'est qu'il est assez important de prendre son temps pour tester un maximum de switch possible et de plusieurs marque. Je me suis surpris à tapoter des testeurs pendant 1h et aller jusqu'à prendre des notes pour chaque touche tant l'expérience est interessante pour trouver la senssation idéal pour nous. Ainsi, dans le meilleur des mondes, nous avons tout un tas de grands testeurs pour chacune des marques, ce qui revient à plusieurs centaines d'euro pour juste choisir et enfin les mettres aux placards ... Ou alors vous êtes copains avec un geek qui dispose déjà d'un stock de testeurs chez lui.

Pas simple, mais je vais être honnête, je vous conseil d'éviter de limiter votre expérience de choix à un petit testeur de 9 touches.
Certaines personnes propose des vidéos pendant les tests, mais cela donne une idée de la senssation, bien éloignée de votre réalitée propre.

Je vous laisse avec votre conscience et votre portefeuille à ce stade ;)

# Les Keycaps (Capuchons)

Dernière étape, les Keycaps, la c'est juste l'éclate sur la personalisation !

Quelques infos technique :

* Le matériaux le plus commun et adaptée, c'est le **PBT**, mais tous est possible (ABS, résine, bois, marbre, céramique, laiton, titane, or massif, ...)
* La plupart des Switch utilise une potence compatible "Cherry MX", mais vérifier toujours vos switchs avant d'acheter vos Keycaps pour ne pas vous faire avoir.
* Les keycaps sont divisées 4 profils (R1, R2, R3 et R4).
* Il existe plusieurs familles de profils.

Un ensemble complet de touche personalisée de qualitée coûte dans les 50€ en moyenne. Il est possible surement de trouver des clavier mecanique d'occasion ou en vide grenier pour récupérer les keycaps (voir avec les switchs si vous êtes chanceux) pour vraiment pas chère.

Il est possible de trouver des artistes très talenteux qui fabriquent de véritables oeuvres d'art qui viderons votre compte en banque : [https://www.etsy.com/fr/search?q=capuchons%20de%20clavier](https://www.etsy.com/fr/search?q=capuchons%20de%20clavier)

# Bonus : Créez vos propres Keycaps

Si vous êtes motivés, voici comment procéder. 

Vous aurez besoin dêtre à l'aise avec Inkscape pour concevoir vos motifs au format SVG. Pour cela, l'entreprise WASD à mis à disposition des templates prêt à l'emplois. Je partage les fichiers directement ici, car leur site ne semblent pas très pérenne.

keyboard_templates.zip

Si vous n'êtes pas inspiré, [SVG Repo](https://www.svgrepo.com) vous dépannera.

Imprimez vos motifs sur du papier de sublimation. Si vous ne souhaitez pas investir dans ce type d'imprimante spéciale, [certaines personnes vous ferons payer dans les 10€ la page A4 sur ce papier spécial](https://www.etsy.com/fr/search?q=Impression%20sublimation%20A4).

**Attention, vos motifs doivent être imprimés en mirroir sur le papier !**

Procurez-vous des Keycaps vierges, il en existe pas mal sur [Aliexpress](https://fr.aliexpress.com/w/wholesale-blank-keycaps-PBT.html). Faites attention à choisir du PBT dans notre cas.

Finalement, pour le transfert, vous devez presser à chaud le papier de sublimation sur une touche vierge pendant quelques secondes.

Pour cela, une machine à bronzer ou une presse à chaud est idéal.
De mon côté, j'ai fabriqué un petit socle pour y stabiliser un petit fer à lisser, ça fonctionne, prévoyer 230°C minimum (40W).

IMAGE SOCLE FER

Voici les sources du socle pour fer à lisser si vous avez accès à une imprimante 3D cela peut vous servir :

 keyboard_keycaps_machine.zip

Il existe aussi une methode à la graveuse laser, personnellement le rendu était très moche de mon côté, je vous recommande de tenter l'aventure avec des graveuses de haute précision.

N'hésitez pas à chercher [des vidéos sur ce sujet](https://www.youtube.com/watch?v=8NTH36BTq4Y&list=PLDAnRch_iwbGM9jQVQaib-y4iswCPqIIr), c'est très instructif.

Prévoyez bien sur quelques echecs, le temps de maîtriser les gestes.

# Conclusion

Vous avez toutes les armes en main pour vous équiper du meilleur clavier possible pour vous. Ce petit bijou vous accompagnera probablement quotidiennement et pour toute la vie, prenez en soin, huiler les switch et faite lui un nettoyage à l'alcool IPA de temps en temps.

Et pour ceux qui en veulent toujours plus, les [Macropad](https://xieme-art.org/post/jouer-avec-le-macropad-adafruit-mais-en-serie) devrait vous instéresser.