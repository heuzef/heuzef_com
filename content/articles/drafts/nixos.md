Title: À la découverte de NixOS une distribution Linux pas comme les autres
Category: Parentalité
Tags: linux, astuce, opensource, chiffrement
Date: 2026-04-01
Status: draft

![nixos_001.png](../../assets/nixos_001.png)

Si vous êtes un Linuxien vous avez surement déjà testé quelques distributions dans votre vie, je vous invite à partir à l'aventure avec moi pour découvrir **tranquillement** NixOS.

"Encore une, j'ai déjà ma favortie et [NixOS stagne dans le top 20 en popularité](https://distrowatch.com) ..." me direz-vous. Et bien, si vous ne connaissez pas ce qui la rend spéciale, vous risquez d'être surpris.

## Pourquoi NixOS est différent ? ❄️

NixOS est une distribution qui suscite l'admiration d'un côté, mais aussi la terreur pour d'autre, ce qui explique surement sa popularitée stagnante. À mon sens, c'est un peu comme chercher à dompter un cheval sauvage. Ça fait peur, on ne sait pas trop commment s'y prendre ... mais si l'on y parvient, c'est une satisfaction incroyable qui nous attend.

Le gros point noir de cet OS, c'est sa courbe d'apprentissage attroce. Ainsi, si vous n'êtes pas prêt à faire un gros effort, vous pouvez arrêter la lecture de cet article et retourner sur votre Ubuntu. 

![nixos_002.png](../../assets/nixos_002.png)

Toujours partant ? Alors vous aller découvrir à quel point cet OS est incroyable. Alors finalement, quel est son secret ? La réponse : **c'est un OS déclaratif**. Explications :

Sur un OS classique, vous aller vouloir, par exemple, installer un logiciel. Ainsi, vous aller le configurer pour télécharger l'outil, le déployer et le paramétrer. Sur un Ubuntu, c'est un classique `sudo apt install` dans le terminal. Et bien sur NixOS, pas du tout, car vous n'allez tous simplement **jamais le configurer**.

En effet, **NixOS ne se configure pas, il se déclare !** C'est là toute la puissance de ce système. Les adèptes de Ansible, Terraform et autre système "as code" comprennent très bien l'énorme avantage du déclaratif face à l'impératif. 

Pour les autres, voici une petite analogie : vous souhaitez faire un gâteau aux chocolat, pour l'ammener chez vos hôtes. Dans ce cas, la logique est donc (en imperatif) : avec votre recette favorite, réunissez les ingrédients, les ustenssils de cuisines, puis opérer la patisserie. Voila, vous avez votre gâteau, c'est cool. Puis nous recommençons de nouveau, le mois suivants, peut-être différement mais toujours avec cette même méthodologie.

Maintenant, la logique déclarative serait : J'écris mon livre de recette du gâteau au chocolat, avec tous les détails de chaque étape (c'est fastidieux). Maintenant que j'ai mon livre, je le confie à un patissier et voila, j'ai mon gâteau. Le mois suivant ? Pas de problème -> patissier -> gâteau -> 0 effort. Je veux 10 gâteaux ? Je donne ma recettes à 10 patissiers -> 0 effort. J'ai envie de changer le dossage du sucre dans ma rectte ? Et bien je met à jour mon livre de recette -> tous les gâteaux seront actualisés.

L'effort initiale ici qui est donc de créer le livre de recette, c'est la phase importante (et chronophage), mais une fois fait, c'est la foire à la saucisse.

Voici un exemple simple plus concret pour bien se représenter le truc : j'ai une imprimante à la maison. Nous prenons par exemple 1h sur chaque PC, à chaque fois que nécessaire de pour l'installer, mettre à jour les pilotes, logiciels, etc ... Sur NixOS, j'ai un fichier de configuration qui comprend tous ce qu'il faut pour profiter d'une imprimante opérationnelle et paramétré aux oinions, ce qui m'a pris 1 journée entière à coder et tester. 

Et maintenant ? J'en ai oublié la notion même de devoir le faire, car cette configuration est tous simplement déployé automatiquement sur toutes mes machines en parallèles, je n'aurais plus jamais besoin de m'en soucier, tant que je ne change pas d'imprimante. L'autre avantage, c'est que revenir sur ce fichier de configuration me permet de comprendre et de maîtriser tous le processus.

Voici par exemple comment j'installe un logiciel. Si je souhaite, par exemple, installer Google-Chrome, je modifie très simplement mon fichier de configuration ainsi :

```nix
home.packages = with pkgs; [
    audacity
    gimp3
    google-chrome # <---- Ajouter cette ligne
    firefox
    vlc
    zoom-us
  ];
```

Aussi simplement que ça, Google-Chrome sera déployé sur toutes mes machines.

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

Ce n'est qu'un début, j'ai été témoins de sacrés trucs, pour ceux qui matrîse la bête, c'est fabuleux.

### Résumons

NixOS est un des OS les plus puissants et interessant qui existe, mais il est sans pitié. 

Il force à avoir une rigueur et une logique irréprochable, chaque petite configuration de votre environnement de travail sera un challenge. Si vous vous prenez au truc, vous aller surement rester pendant un moment insatisfait de votre code ... puis, finalement, un beau jour, vous avez une configuration élégante qui vous maitrisez et appréciez, c'est le nirvana qui vous attend 🤩 

Convaincu ? Alors je vous propose maintenant de découvrir son fonctionnement. Enfin, nous metterons en place un versionnage de votre configuration sur GIT avec des modules expérimentaux pour en tirer le plein potentiel. Suivez le guide 👉

# Installation 📀

Bonne nouvelle, rien de nouveau ici, [vous installez NixOS exactement de la même façon que n'importe quel autre distribution](https://nixos.org/download/#nixos-iso), aucun piège, c'est hyper simple. Choisiez votre environnement graphique favoris (Gnome, KDE, ...), puis, vous démarrez sur votre installation toute fraîche. 

C'est ici que l'aventure commence : forcez-vous a ne rien configurer, car, toute modification apportée sera perdue, par exemple, si vous réinstallez le système.

Je vous recommande donc de poursuivre la lecture de cet article depuis votre NixOS flambant neuf.

# Déclarer sa configuration 📋

La configuration principale s'effectue dans un fichier **configuration.nix** qui est situé dans le repertoire ``/etc/nixos/``, étudions-le :

```nix
{ config, pkgs, ... }:
 
{
  imports = # NixOS permet d'importer d'autre fichier de configuration au format .nix
    [ 
      ./hardware-configuration.nix # Contient la configuration physique de votre machine actuelle (partitionnement, pilotes matériels, ...)
    ];
 
  # Activer le Bootloader
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
 
  networking.hostName = "nixos"; # Le nom d'hôte de votre machine
  networking.wireless.enable = false;  # Activer le Wi-Fi
 
  networking.networkmanager.enable = true; # Activer Network Manager
 
  time.timeZone = "Europe/Paris"; # Le fuseau horaire
 
  i18n.defaultLocale = "fr_FR.UTF-8"; # Le codage international

  services.xserver.enable = true; # Activer X11
 
  # Activer GNOME Desktop Environment
  services.xserver.displayManager.gdm.enable = true;
  services.xserver.desktopManager.gnome.enable = true;
 
  # Configurer votre clavier
  services.xserver.xkb = {
    layout = "fr";
    variant = "azerty";
  };
 
  console.keyMap = "fr";
 
  services.printing.enable = true; # Activer CUPS, si vous avez une imprimante
 
  # Activer l'audio (avec pipewire)
  hardware.pulseaudio.enable = false;
  security.rtkit.enable = true;
  services.pipewire = {
    enable = true;
    alsa.enable = true;
    alsa.support32Bit = true;
    pulse.enable = true;
  };
 
  # Votre compte utilisateur
  users.users.adrien = {
    isNormalUser = true;
    description = "heuzef";
    extraGroups = [ "networkmanager" "wheel" ];
    packages = with pkgs; [
    #  ici, vous pouvez définir une liste de logiciel pour cet utilisateur
    ];
  };
 
  programs.firefox.enable = true; # Activer Firefox, pour tous les utilisateurs
 
  nixpkgs.config.allowUnfree = true; # Permettre l'utilisation des logiciels non-libres
 
  # La liste des logiciels à déployer sur votre system (https://search.nixos.org)
  environment.systemPackages = with pkgs; [
   vim
   wget
   git
   gparted
   ntfs3g
   sshfs
   usbutils
  ];
 
  # Activation de service
  services.openssh.enable = true;
 
  # Configurer votre Pare-feu
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  networking.firewall.enable = false;
```

Vous avez déjà envie de le bidouiller ? C'est bon signe 😜 Mais comment appliquer cette dernière ? C'est très simple, avec la commande ``sudo nixos-rebuild switch`` (l'argument __switch__ permet de forcer la bascule sur votre nouvelle version, immédiatement après la re-construction).

Et si vous souhaitez effectuer la mise à jour du système : ``sudo nixos-rebuild switch --upgrade``, suivi d'un redémarrage.

Vous avez déjà les bases fondamentales de NixOS ! Continuons !

# Principes des générations 🆕

A chaque modification appliqués, une nouvelle version de l'état de votre système est créée dans un état immuable (donc non modifiable). Ainsi, si le resultat de votre rebuild ne vous convient pas, alors il vous suffit de redémarrer votre système, puis basculer sur la génération précédente depuis le menu de Grub.

![nixos_003.png](../../assets/nixos_003.png)

La commande ``nixos-rebuild list-generations`` vous permet de lister vos generations. 

Pour apprendre à manipuler, nettoyer, rollback, etc ...vos générations, [je vous renvoi vers ce très bon article dédié](https://www.linuxtricks.fr/wiki/nixos-gestion-des-generations-rollback-suppression-menage).

# Principe des environnements temporaires 🗑️

Un autre truc absolument trop cool, c'est qu'il est possible de créer des environnements éphémères pour des usages très ponctuelle.

![nixos_004.png](../../assets/nixos_004.png)

Sur cette même logique, vous pouvez même créer des VM sur-mesure sur le pouce.

<video id="nixos_vm" controls preload="auto" width="900" height="500">
<source src="../../assets/nixos_vm.mp4" type='video/mp4'>
</video>
