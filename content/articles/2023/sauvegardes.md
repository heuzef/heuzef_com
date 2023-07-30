Title: Externalisations de sauvegardes sécurisé et économique
Category: Informatique
Tags: auto-hébergement, sauvegardes, chiffrement, astuce, open-source
Date: 2023-07-31
Status: draft

Un point crucial en Informatique, c'est l'externalisation des sauvegardes. En effet, si vous ne comptez que sur vos sauvegardes locales (stockés chez vous, sur votre PC ou autre), vous aller forcément être punis un de ces jours via une panne de matériel, cambriolage ou autre et votre vie numérique sera réduite à néant.

L'externalisation des sauvegardes règle donc ce problème, mais dans mon cas, je suis habitué à des solutions vraiment pro, avec des outils et des moyens important car les enjeux sont de taille pour la clientelle. Mais comment faire lorsque l'on veux cela à l'echelle d'une TPE ou dans le cadre d'un Auto-Hérbergement sans ce ruiner ? J'ai longtemps peiné pour trouver une solution à la hauteur de ma radinerie.

![Sauvegardes](../../assets/backup.png)

## L'outil utilisé : Borg

Pour ceux qui ne connaisse pas encore, [Borg](https://borgbackup.org) coche pour moi toutes les cases pour remplir ce rôle, c'est un outil de sauvegarde sérieux, qui répondra parfaitement à des besoins quotidiens de sauvegardes automatique et sécurisés. Il est open-source et pour l'utiliser depuis un moment, je ne peux que le recommander.

[![asciicast](https://asciinema.org/a/133292.svg)](https://www.borgbackup.org/demo.html)

Il n'est pas encore aussi évolué qu'un [Bacula](https://bacula.org) par son manque de GUI et d'outils à usage pro, mais il l'un des meilleurs outils de sauvegarde du moment et plusieurs projets peuvent ce completer à Borg si besoin de combler des manques (ex : [Borgmatic](https://torsion.org/borgmatic)).

Je considère bien évidement que les outils non open-source tel que Acronis sont à bannir, il ne faut pas avoir froid au yeux de confirer aveuglément ses données à un tiers.

Bien que très fiable, bye-bye également le contre-intuitif BackupPC avec son interface à vomir, il est de toute façon déjà mort, comme en témoigne mon [Pull Request](https://github.com/backuppc/backuppc/pull/419) resté sans réponse depuis la nuit des temps.

## Externaliser où ?

Entrons donc dans le coeur du problème : [la thune](https://youtu.be/Eo9JmYYbACA?t=161) 💸

Pour avoir une externalisation digne de ce nom sans ce ruiner il faut bien s'embêter ou trouver des bons plans.

J'ai déjà tenté de le faire à l'ancienne en déplaçant régulièrement des HDD, mais perdre l'automatisation nocturne est vraiment trop pénible et difficile à assurer dans le temps. J'ai également tenté de passer par les amis, ça fonctionne, mais n'éspérez pas avoir une solution pérenne, je me suis retrouvé à déménager ma solution chez un autre chaque année, pour X ou Y raisons ! 😫

Finalement, je me suis décidé à y mettre des sous, mais chercher une solution pour stocker (5To de sauvegarde dans mon cas) compatible avec Borg tout en étant radin est vraiment difficile.

C'est du côté des casques à pointe que j'ai trouvé bonheur ! **[<i class="fa fa-link"></i> Hetzner](https://www.hetzner.com)** propose un service appelé **[<i class="fa fa-link"></i> Storage Box](https://www.hetzner.com/storage/storage-box)** compatible avec Borg et à bas prix (12,97€ les 5 To en 2023 dans mon cas !).

J'exporte depuis quelques mois mes sauvegardes chiffrés chez eux et ça tourne super. Leur documentation technique est disponible **[<i class="fa fa-link"></i> ICI](https://community.hetzner.com/tutorials/install-and-configure-borgbackup)** pour relier leur stockage à votre serveur Borg.

Je n'ai pas mesuré les débits, mais pour ce prix là, je peux vous assurer que c'est vraiment top, dans mon cas, je remplis sans problème les 5 To dans la nuit ✌️
