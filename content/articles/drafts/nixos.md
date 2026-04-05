Title: À la découverte de NixOS une distribution Linux pas comme les autres
Category: Informatique
Tags: linux, astuce, opensource, chiffrement
Date: 2026-04-06
Status: draft

![nixos_001.png](../../assets/nixos_001.png)

Si vous êtes un Linuxien vous avez sûrement déjà testé quelques distributions dans votre vie, je vous invite à partir à l'aventure avec moi pour découvrir **tranquillement** NixOS.

"Encore une, j'ai déjà ma favorite et [NixOS stagne dans le top 20 en popularité](https://distrowatch.com)" me direz-vous. Et bien, si vous ne connaissez pas ce qui la rend spéciale, vous risquez d'être surpris.

## Pourquoi NixOS est différent ? ❄️

NixOS est une distribution qui suscite l'admiration d'un côté, mais aussi la terreur pour d'autres, ce qui explique sûrement sa popularité stagnante. À mon sens, c'est un peu comme chercher à dompter un cheval sauvage. Ça fait peur, on ne sait pas trop comment s'y prendre ... mais si l'on y parvient, c'est une satisfaction incroyable qui nous attend.

Le gros point noir de cet OS, c'est sa courbe d'apprentissage atroce. Ainsi, si vous n'êtes pas prêt à faire un gros effort, vous pouvez arrêter la lecture de cet article et retourner sur votre Ubuntu. 

![nixos_002.png](../../assets/nixos_002.png)

Toujours partant ? Alors vous allez découvrir à quel point cet OS est incroyable. Alors finalement, quel est son secret ? La réponse : **c'est un OS déclaratif**. Explications :

Sur un OS classique, vous allez vouloir, par exemple, installer un logiciel. Ainsi, vous allez le configurer pour télécharger l'outil, le déployer et le paramétrer. Sur un Ubuntu, c'est un classique `sudo apt install` dans le terminal. Et bien sur NixOS, pas du tout, car vous n'allez tout simplement **jamais le configurer**.

En effet, **NixOS ne se configure pas, il se déclare !** C'est là toute la puissance de ce système. Les adeptes de Ansible, Terraform et autres systèmes "as code" comprennent très bien l'énorme avantage du déclaratif face à l'impératif. 

Pour les autres, voici une petite analogie : vous souhaitez faire un gâteau au chocolat, pour l'amener chez vos hôtes. Dans ce cas, la logique est donc (en impératif) : avec votre recette favorite, réunissez les ingrédients, les ustensiles de cuisine, puis opérer la pâtisserie. Voilà, vous avez votre gâteau, c'est cool. Puis nous recommençons de nouveau, le mois suivant, peut-être différemment mais toujours avec cette même méthodologie.

Maintenant, la logique déclarative serait : J'écris mon livre de recettes du gâteau au chocolat, avec tous les détails de chaque étape (c'est fastidieux). Maintenant que j'ai mon livre, je le confie à un pâtissier et voilà, j'ai mon gâteau. Le mois suivant ? Pas de problème -> pâtissier -> gâteau -> 0 effort. Je veux 10 gâteaux ? Je donne ma recette à 10 pâtissiers -> 0 effort. J'ai envie de changer le dosage du sucre dans ma recette ? Et bien je mets à jour mon livre de recettes -> tous les gâteaux seront actualisés.

L'effort initial ici, qui est donc de créer le livre de recettes, c'est la phase importante (et chronophage), mais une fois fait, c'est la foire à la saucisse.

Voici un exemple simple plus concret pour bien se représenter le truc : j'ai une imprimante à la maison. Nous prenons par exemple 1h sur chaque PC, à chaque fois que nécessaire pour l'installer, mettre à jour les pilotes, logiciels, etc ... Sur NixOS, j'ai un fichier de configuration qui comprend tout ce qu'il faut pour profiter d'une imprimante opérationnelle et paramétrée aux petits oignons, ce qui m'a pris la journée entière à coder et tester. 

Et maintenant ? J'en ai oublié la notion même de devoir le faire, car cette configuration est tout simplement déployée automatiquement sur toutes mes machines en parallèle, je n'aurais plus jamais besoin de m'en soucier, tant que je ne change pas d'imprimante. L'autre avantage, c'est que revenir sur ce fichier de configuration me permet de comprendre et de maîtriser tout le processus.

Voici, par exemple, comment j'installe un logiciel. Je modifie très simplement mon fichier de configuration ainsi :

```nix hl_lines="4"
home.packages = with pkgs; [
    audacity
    gimp3
    google-chrome # Ajouter cette ligne
    firefox
    vlc
    zoom-us
  ];
```

Aussi simplement que ça, Google-Chrome sera déployé sur toutes mes machines. Avec cette logique, appliquée sur tout mon système, cela me permet de :

* Coder absolument toute ma configuration
* Prendre le temps de comprendre en profondeur ma configuration
* Versionner toute ma configuration avec GIT
* Exposer ma configuration publiquement, très pratique pour le partage (nous aborderons un peu plus loin l'aspect chiffrement des secrets)
* Ne plus jamais avoir besoin de réinstaller mon OS en Vanilla
* Me forcer à adopter un comportement rigoureux et ne plus permettre de mauvaises pratiques
* Ne plus altérer mon système à cause de manipulations regrettables
* Profiter d'environnements virtuels temporaires
* Obtenir un OS de plus en plus confortable et évolutif dans le temps
* Automatiser des déploiements
* Pré-paramétrer mon environnement utilisateur et mes outils
* ...

Ce n'est qu'un début, j'ai été témoin de sacrés trucs, pour ceux qui maîtrisent la bête, c'est fabuleux.

### Résumons

NixOS est un des OS les plus puissants et intéressants qui existent, mais il est sans pitié. 

Il force à avoir une rigueur et une logique irréprochable, chaque petite configuration de votre environnement de travail sera un challenge. Si vous vous prenez au truc, vous allez sûrement rester pendant un moment insatisfait de votre code ... puis, finalement, un beau jour, vous avez une configuration élégante que vous maîtrisez et appréciez, c'est le nirvana qui vous attend 🤩

Ma meilleure astuce, c'est finalement de configurer son système tranquillement, au plus simple, en prenant le temps de le faire pour soi-même. Vous allez ainsi progressivement basculer sur une configuration maîtrisée et très personnelle qui vous correspond.

Convaincu ? Alors je vous propose maintenant de découvrir son fonctionnement. Enfin, nous mettrons en place un versionnage de votre configuration sur GIT avec des modules expérimentaux pour en tirer le plein potentiel. Suivez le guide 👉

# Installation 📀

Bonne nouvelle, rien de nouveau ici, [vous installez NixOS exactement de la même façon que n'importe quelle autre distribution](https://nixos.org/download/#nixos-iso), aucun piège, c'est hyper simple. Choisissez votre environnement graphique favori (Gnome, KDE, ...), puis, nous démarrons sur une installation Vanilla. C'est ici que l'aventure commence : il faut se forcer à ne rien configurer, car, toute modification apportée sera perdue si vous réinstallez le système.

Je vous recommande donc de poursuivre la lecture de cet article depuis votre NixOS flambant neuf.

# Déclarer sa configuration 📋

La configuration principale s'effectue dans un fichier **configuration.nix** qui est situé dans le répertoire ``/etc/nixos/``, étudions-le :

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
  networking.wireless.enable = false;  # Le Wi-Fi
  networking.networkmanager.enable = true; # Network Manager
 
  time.timeZone = "Europe/Paris"; # Le fuseau horaire
 
  i18n.defaultLocale = "fr_FR.UTF-8"; # Le codage international

  services.xserver.enable = true; # Activer X11 si besoin
 
  # Activer GNOME Desktop Environment
  services.xserver.displayManager.gdm.enable = true;
  services.xserver.desktopManager.gnome.enable = true;
 
  # Configuration du clavier
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
  users.users.heuzef = {
    isNormalUser = true;
    description = "heuzef";
    extraGroups = [ "networkmanager" "wheel" ];
    packages = with pkgs; [
    #  ici, il est possible de définir une liste de logiciel pour cet utilisateur
    ];
  };
 
  programs.firefox.enable = true; # Activer Firefox, pour tous les utilisateurs
 
  nixpkgs.config.allowUnfree = true; # Permettre l'utilisation des logiciels non-libres
 
  # La liste des logiciels à déployer sur le system (https://search.nixos.org)
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
 
  # Configuration du Pare-feu
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  networking.firewall.enable = false;
```

Vous avez déjà envie de le bidouiller ? C'est bon signe 😜 Mais comment appliquer cette dernière ? C'est très simple, avec la commande ``sudo nixos-rebuild switch`` (l'argument **switch** permet de forcer la bascule sur votre nouvelle version, immédiatement après la re-construction).

Et si vous souhaitez effectuer la mise à jour du système : ``sudo nixos-rebuild switch --upgrade``, gérer les éventuels conflits, suivi d'un redémarrage.

Vous avez déjà les bases fondamentales de NixOS ! Continuons !

# Principes des générations 🆕

À chaque modification appliquée, une nouvelle version de l'état de votre système est créée dans un état immuable (donc non modifiable). Ainsi, si le résultat de votre rebuild ne vous convient pas, alors il vous suffit de redémarrer votre système, puis basculer sur la génération précédente depuis le menu de Grub.

![nixos_003.png](../../assets/nixos_003.png)

La commande ``nixos-rebuild list-generations`` vous permet de lister vos générations. 

Pour apprendre à manipuler, nettoyer, rollback, etc ...vos générations, [je vous renvoie vers ce très bon article dédié](https://www.linuxtricks.fr/wiki/nixos-gestion-des-generations-rollback-suppression-menage).

# Principe des environnements temporaires 🗑️

Un autre truc absolument trop cool, c'est qu'il est possible de créer des environnements éphémères pour des usages très ponctuels.

![nixos_004.png](../../assets/nixos_004.png)

Sur cette même logique, vous pouvez même créer des VM sur-mesure sur le pouce.

<video id="nixos_vm" controls preload="auto" width="900" height="500">
<source src="../../assets/nixos_vm.mp4" type='video/mp4'>
</video>

Sous condition bien sûr d'avoir activé la virtualisation sur votre système. Comment faire ? Dans le fichier de configuration évidemment :

```nix
services.qemuGuest.enable = true;
```

# Principe des modules 🧩

L'avantage de travailler avec des fichiers de configuration modulaire, c'est que cela simplifie la maintenance et la gestion du déploiement.
Par exemple, voici un fichier de configuration très basique pour Steam si vous êtes un Gamer (**steam.nix**) :

```nix
{ pkgs, ... }:

{
  programs.steam = {
    enable = true;
    remotePlay.openFirewall = true; # Open ports in the firewall for Steam Remote Play
    dedicatedServer.openFirewall = true; # Open ports in the firewall for Source Dedicated Server
    localNetworkGameTransfers.openFirewall = true; # Open ports in the firewall for Steam Local Network Game Transfers
  };

  programs.steam.gamescopeSession.enable = true;
  programs.appimage.enable = true;
  programs.appimage.binfmt = true;

  environment.systemPackages = with pkgs; [
    steam-tui
    steamcmd
  ];
}
```

Puis, sur chaque machine où vous souhaitez pouvoir jouer aux jeux-vidéo, il suffira d'ajouter :

```nix
  imports = [ ./steam.nix ];
```

Astuce, le site [mynixos.com](https://mynixos.com/nixpkgs/options/programs.steam) est très confortable pour trouver les options de configurations des programmes.

# Les AppImages

Si le programme que vous souhaitez n'existe pas dans le dépôt de NixOS, mais uniquement téléchargeable en tant que AppImage, voici une méthode très simple et efficace :

* Déclarer le package ``appimage-run``
* Télécharger votre fichier **app.AppImage** et autoriser son exécution (``sudo chmod +x -R app.AppImage``)
* Démarrer le programme : ``appimage-run app.AppImage``

# Passer au niveau supérieur ⭐

Vous êtes sûrement convaincu des possibilités, cependant, NixOS commence à prendre tout son sens lorsque nous embrassons les avantages offerts par le déclaratif. Ainsi, nous allons à présent voir comment  :

* Versionner sa configuration sur GIT
* Utiliser Home Manager avec Flake pour exploiter toutes les fonctionnalités expérimentales
* Gérer plusieurs machines

## Versionner avec Git

Pour commencer, nous allons initier un dépôt GIT (sur Github). Je considère que vous avez déjà un compte Github et que vous avez créé un dépôt. Vous pouvez le nommer **nixos-config** par exemple, c'est une sorte de convention, cela vous permet entre autres de trouver facilement [d'autres dépôts similaires pour vous inspirer de quelques pépites](https://github.com/search?q=nixos-config&type=repositories&s=stars&o=desc). 

Basculons dans le terminal, placez-vous dans le répertoire où vous souhaitez maintenir la configuration de votre système. N'ayant pas encore GIT déployé sur le système, nous utiliserons Nix-Shell pour l'instant, le temps de cloner notre dépôt.

```bash
cd ~ # Utilisation du repertoire utilisateur, ici pour notre exemple
nix-shell -p git --command "git clone git@github.com:<VOTRE-PSEUDO-GITHUB>/nixos-config.git"
```

Créons à présent un fichier de configuration contenant le minimum : ``cp -v /etc/nixos/configuration.nix ~/nixos-config/``.

En plus de la configuration minimale (vu plus tôt ci-dessus), ajoutons dedans :

```nix
  networking.hostName = "mon-pc"; # Le nom d'hôte de la machine, c'est important pour la suite
  
  # Activer et configuer GIT :
  programs.git = {
    enable = true;
    lfs.enable = true;
    settings.user.name = "<VOTRE-PSEUDO>";
    settings.user.email = "<VOTRE-EMAIL>";
  };
```

Finalement, vous pouvez déjà reconstruire votre système avec ce fichier de configuration : 

```bash
sudo nixos-rebuild switch --file ~/nixos-config/configuration.nix
git config --list # Vérifier que GIT est déployé et configuré
```

Si vous rencontrez une erreur, pas de panique, analysez-la, elles sont généralement plutôt claires et sont là pour nous aider à valider un fichier de configuration parfaitement propre.

La construction peut prendre du temps, NixOS analyse les différences trouvées entre le système et votre déclaration. Vous constaterez que le rebuild est quasiment instantané si aucun changement n'est appliqué.

Créons notre premier commit :

```bash
git add --all
git commit -m "Init my NixOS configuration"
git push
```

Et bah voilà 👌 Vous avez votre configuration versionnée sur GIT ! Vous avez compris le processus pour modifier votre configuration système :

- Éditer les fichiers de configurations
- Rebuild (en cas d'erreur, on corrige, on test, ...)
- Si l'on est satisfait, on commit et push

C'est déjà super ainsi, mais allons plus loin avec des fonctionnalités très populaires.

## Home Manager et Flakes

Si NixOS gère la structure de base, Home Manager, lui, s'occupe de personnaliser ses sessions. En effet, NixOS gère très bien la configuration du système, mais moins bien la configuration utilisateur. Home Manager s'impose alors et utilise le langage Nix pour gérer les fichiers personnels (les fameux "dotfiles" comme .bashrc, etc ...). C'est donc un complément très utile pour personnaliser son système.

Les Flakes (introduits comme une fonctionnalité expérimentale mais devenus le standard de fait) règlent un souci important : l'installation d'une configuration aujourd'hui peut varier dans le temps à cause des versions de logiciels différentes, car les "sources" de Nix ont été mises à jour entre-temps. Il s'agit donc d'un "verrou" de sécurité et de modernité.

Un Flake est donc un projet Nix qui définit explicitement ses dépendances. Un fichier **flake.lock** enregistre la version précise (le "hash" Git) de chaque source utilisée.

L'analogie de la recette de cuisine :

* Sans Flake : La recette dit "Ajouter du lait". Si le lait du supermarché change de marque, le goût du gâteau change.
* Avec Flake : La recette dit "Ajouter le lait de la marque X, lot n°1234, datant du 01/01/1970". Le gâteau sera exactement le même, à chaque fois, pour tout le monde.

C'est donc vos commits Git qui deviennent la vérité absolue. Il est donc recommandé d'effectuer un ``git add --all`` de votre dépôt, avant chaque rebuild ! (Sinon ça couine).

Voici un exemple de structure basique à avoir à ce stade, nous permettant de gérer plusieurs machines :

```bash
.
├── .git # GIT
├── configuration.nix # La configuration NixOS principale
├── flake.lock # Le verrou Flake
├── flake.nix # Configuration Flake
├── hardware # Les configurations matérielles de vos machines.
│   ├── mon-pc-01.nix
│   ├── mon-pc-02.nix
│   └── mon-pc-03.nix
├── home.nix # Configuration Home Manager
├── README.md # Vos notes perso
└── software
    └── steam.nix # Configuration du logiciel Steam pour le jeu-vidéo
```

Voyons à présent les fichiers de configuration de Home Manager et Flakes.

### Flake

Votre fichier **flake.nix** deviendra votre point d'entrée, c'est lui qui sera appelé à la reconstruction, afin de permettre une exécution avec des arguments conditionnels. Dans notre cas, cela sera pour préciser la machine en cours d'utilisation, mais après, libre à vous d'être créatif.

```nix
{
  description = "My NixOS-Config"; # Description de votre Flake

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";  # Activation de tous les paquets
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      system = "x86_64-linux";
      lib = nixpkgs.lib;
    in {
      nixosConfigurations = {

        # mon-pc-01
        mon-pc-01 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix # Nous retrouvons ici notre fichier de configuration
            ./hardware/mon-pc-01.nix # Astuce, pour afficher la configuration de votre machine : sudo nixos-generate-config --show-hardware-config
          ];
        };

        # mon-pc-02
        mon-pc-02 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
            ./software/steam.nix # Sur cette machine, je décide de déployer Steam pour jouer au jeux-vidéo
          ];
        };
        
        # mon-pc-03
        mon-pc-03 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
          ];
        };
        
      };
    };
}
```

Avec cette configuration, la commande de rebuild pour la machine **mon-pc-01** sera :

``sudo nixos-rebuild switch --flake "~/nixos-config#mon-pc-01"``

### Home Manager

Voyons à présent comment activer Home Manager, dans le fichier **flake.nix**, nous ajouterons les éléments suivants :

```nix hl_lines="6 7 8 9 25 26 27 28 29 30 31"
{
  description = "My NixOS-Config";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    home-manager = {
      url = "github:nix-community/home-manager"; # Les modules peuvent être appelées directement depuis un dépôt Github compatible, c'est beaucoup trop cool !
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      system = "x86_64-linux";
      lib = nixpkgs.lib;
    in {
      nixosConfigurations = {

        # mon-pc-01
        mon-pc-01 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-01.nix
            home-manager.nixosModules.home-manager
            {
              networking.hostName = "mon-pc-01"; # Possible de configurer votre nom d'hôte ici
              home-manager.useGlobalPkgs = true; # Activer les paquets système
              home-manager.useUserPackages = true; # Activer les paquets utilisateur
              home-manager.users.heuzef = import ./home.nix; # Nous allons importer ainsi notre configuration Home Manager
            }
          ];
        };

        # mon-pc-02
        mon-pc-02 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
            ./software/steam.nix
          ];
        };
        
        # mon-pc-03
        mon-pc-03 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
          ];
        };
        
      };
    };
}
```

Passons à présent au cœur de Home Manager, voici un exemple de fichier **home.nix** pour personnaliser votre session utilisateur :

```nix
{ config, lib, pkgs, ... }:

{
  # Activer Home-Manager
  programs.home-manager.enable = true;

  # Vos infos basiques à fournir à Home Manger
  home.username = "heuzef";
  home.homeDirectory = "/home/heuzef";
  home.stateVersion = "25.11";

  # Activer Flakes
  nix.settings.experimental-features = [ "nix-command" "flakes" ];

  # home.packages permet de déployer des logiciels dans son environment utilisateur
  home.packages = with pkgs; [
    google-chrome
    libreoffice-fresh
    librewolf
    signal-desktop
    vlc
    yt-dlp
    # etc ... => https://search.nixos.org
  ];

  # Git (à déplacer donc, depuis votre fichier configuration.nix)
  programs.git = {
    enable = true;
    lfs.enable = true;
    settings.user.name = "Heuzef";
    settings.user.email = "contact@heuzef.com";
  };

  # Editer le fichier .bashrc pour importer celui de Home Manager
  home.file.".bashrc".text = ''
    if [ -f "/etc/profiles/per-user/heuzef/etc/profile.d/hm-session-vars.sh" ]; then
      source "/etc/profiles/per-user/heuzef/etc/profile.d/hm-session-vars.sh"
    fi
  '';

    # Créer quelques Alias Bash
    shellAliases = {
      ls = "ls --color=auto";
      ll = "ls -larth";
      coin = "echo '\_ô< coin !'";
      pong = "ping -4 -c 3 1.1.1.1";
    };

  # Créer quelques variables d'environment
  home.sessionVariables = {
    EDITOR = "nano";
  };
}
```

Allons-y Alonso :

```bash
cd ~/nixos-config # On se place dans le repertoire de notre dépôt
git add --all # On versionne le tout pour permettre d'activer le verrou Flake
nix flake update # On actualise les dépôts Flake (verification des mises à jour)
nix-collect-garbage --delete-older-than 30d # Nettoyage pour supprimer les générations datant de plus de 30 jours.
sudo nixos-rebuild switch --flake "~/nixos-config#mon-pc-01" # Admirez le resultat 🤟
```

# Gérer ses secrets 🔒

Un autre avantage à publier sa configuration publiquement, en plus de pouvoir la partager facilement, c'est que cela nous oblige à être rigoureux sur la gestion de nos informations sensibles. Pour la suite, je pars du principe que vous avez des compétences en cybersécurité.

Alors comment stocker et masquer ses clés, mots de passe, certificats, etc ... dans sa configuration ? Nous allons ici voir un exemple basique, (car ajouter de la sécurité peut très vite complexifier votre configuration, c'est logique), donc assurez-vous d'être suffisamment en confort avec NixOS avant de franchir cette étape. J'ai pour ma part, laissé mon premier dépôt NixOS en privé pendant un moment, avant de tout reprendre à zéro pour ajouter une vraie gestion sécurisée des secrets.

Dans notre exemple, je vais vous expliquer comment chiffrer des fichiers de configurations et également stocker des secrets dans un document YAML chiffré pour gérer des clés. Pour cela, nous utiliserons le tout puissant **SOPS**.

## Présentation des outils de chiffrement

### AGE

[AGE](https://age-encryption.org) est un outil libre de chiffrement moderne (successeur spirituel de PGP) qui va à l'essentiel sans configuration complexe. Il utilise des paires de clés (publique/privée) ou des mots de passe. Il est facile à manipuler pour le chiffrement. Ce qui en fait bien souvent une brique de base pour des outils plus complexes tels que SOPS.

### SOPS

Développé par Mozilla, [SOPS](https://getsops.io) est un éditeur de fichiers chiffrés. Il se focalise sur la gestion des secrets dans des fichiers de configuration (YAML, JSON, ENV, ...) en s'appuyant sur des technologies de chiffrement populaires (AWS KMS, GCP KMS, Azure KV, HuaweiCloud KMS, AGE, PGP, ...)

Pour faire simple, SOPS ne chiffre que les valeurs du fichier de configuration, laissant le nom des clés en clair. Cela permet de versionner sur GIT tout en gardant une visibilité sur la structure de la configuration. Il peut également permettre un usage simultané "Multi-clés", ce qui est très confortable si vos secrets sont dispersés dans plusieurs services.

![nixos_005.gif](../../assets/nixos_005.gif)

### SOPS-NIX

Et maintenant, soyons fous, intégrons SOPS dans NixOS pour gérer et provisionner automatiquement nos secrets ! Voici [SOPS-NIX](https://github.com/Mic92/sops-nix) !

Il y a tellement de possibilités que cela devient difficile de présenter un tuto d'apprentissage. À mon sens, l'idéal est déjà de définir votre besoin clairement, puis vous y tenir, en commençant très simplement.

## Mise en pratique

Pour la prise en main de SOPS et SOPS-NIX, vous pouvez vous référer à l'exemple présenté par le mainteneur sur le dépôt Github. Mais avant, je vous recommande fortement la lecture de [l'excellent article d'Ephase à ce sujet](https://xieme-art.org/post/gerer-ses-secrets-avec-sops). C'est du pur jus de cervelle et c'est fameux.

Pour la suite de cet article, je vais continuer de présenter ma logique de gestion sur la base de la configuration que nous avons mise en place depuis le début de cet article. L'objectif est simple : centraliser les données sensibles dans un dossier "secrets", ce dernier est ensuite entièrement géré via SOPS-NIX pour y stocker des fichiers chiffrés mais également y centraliser mes clés SSH.

Pour commencer, nous éditons notre configuration pour y déclarer tous les nouveaux outils nécessaires (**configuration.nix**) :

```nix hl_lines="2 3 4"
environment.systemPackages = with pkgs; [
  age
  sops
  ssh-to-age
];
```

Ajoutons notre nouveau module Flake (**flake.nix**) :

```nix hl_lines="10 11 12 13 35"
{
  description = "My NixOS-Config";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    sops-nix = {
      url = "github:Mic92/sops-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      system = "x86_64-linux";
      lib = nixpkgs.lib;
    in {
      nixosConfigurations = {

        # mon-pc-01
        mon-pc-01 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-01.nix
            home-manager.nixosModules.home-manager
            {
              networking.hostName = "mon-pc-01";
              home-manager.useGlobalPkgs = true;
              home-manager.useUserPackages = true;
              home-manager.users.heuzef = import ./home.nix;
              home-manager.sharedModules = [ inputs.sops-nix.homeManagerModules.sops ]; # Activer SOPS-NIX sur cette machine
            }
          ];
        };

        # mon-pc-02
        mon-pc-02 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
            ./software/steam.nix
          ];
        };
        
        # mon-pc-03
        mon-pc-03 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
          ];
        };
        
      };
    };
}
```

C'est prêt, reconstruisons à ce stade pour déployer les outils, puis débutons par la génération d'une clé AGE, qui s'occupera de chiffrer tous nos secrets :

```bash
mkdir -p ~/nixos-config/secrets/ # Créer le repertoire de stockage des secrets
mkdir -p "~/.config/sops/age/" # Créer le repertoire de stockage par défaut
age-keygen -o "~/sops/age/keys.txt" # Générer la clé
cat "~/sops/age/keys.txt" # Notez votre Public Key, je la nommerais <AGE-PUBLIC-KEY> pour la suite
```

Je recommande de stocker cette dernière dans le répertoire prévu par SOPS (**~/.config/sops/age/**), en effet, changer l'emplacement par défaut prévu par SOPS est assez complexe en pratique, selon moi, l'outil n'est pas assez mature pour gérer ceci intuitivement dans la pratique (SOPS_AGE_KEY_FILE).

> Charge à vous à présent, de sauvegarder votre **keys.txt**, si vous la perdez, c'est la catastrophe.

Avant de poursuivre, jouons un peu avec le chiffrement.

```bash
echo '\_ô< coin coin !!' > secretofduck.txt # Créons un secret
sops encrypt --age <AGE-PUBLIC-KEY> secretofduck.txt > secretofduck.enc.txt # Chiffrons-le avec notre clé publique AGE.
# ASTUCE : J'ajoute un préfix .enc AVANT l'extension pour mon fichier chiffré, car, j'ai tout interet à conserver la coloration syntaxique dans mon IDE ;)
# En effet, consultez votre fichier, vous verrez que sa structure est intacte au format JSON ! Seules les valeurs des secrets sont chiffrés. SOPS POWA ! :D
sops decrypt secretofduck.enc.txt # Déchiffrons le  fichier, pas besoin de préciser la clé, il la récupère automatiquement dans ~/sops/age/keys.txt
sops edit -i secretofduck.enc.txt # Idem, l'edition direct est possible, une fois sauvegardée, le fichier sera automatiquement chiffré de nouveau (--in-place).
```

Et oui, si vous vous amusez à chiffrer des JSON, YAML, etc, leur structure sera conservée après chiffrement. SOPS permet même une gestion native des .ENV chiffrés. 
Déjà, à ce stade, c'est trop de la balle, mais allons plus loin, en créant un fichier de gestion structuré. Cela permet de définir le comportement par des règles.

Création du fichier de configuration SOPS dans ``~/nixos-config/secrets/.sops.yaml`` :

```yaml
creation_rules:
  - path_regex: .*
    age: "<AGE-PUBLIC-KEY>"
```

Ce fichier de configuration très basique, permet de préciser à SOPS la Public Key à utiliser systématiquement dans notre dossier **secrets**.
Créons un fichier YAML pour y stocker nos secrets dans ``~/nixos-config/secrets/secrets.yaml`` :

```yaml
API_KEY: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx # Une clé API, c'est un exemple de secret strocké simplement dans une chaine de caractère
id_ed25519: | # Une clé privé
    -----BEGIN OPENSSH PRIVATE KEY-----
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    -----END OPENSSH PRIVATE KEY-----
id_ed25519_pub: | # Et sa clé publique
    ssh-ed25519 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
id_rsa: | # Une clé privé
    -----BEGIN OPENSSH PRIVATE KEY-----
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    -----END OPENSSH PRIVATE KEY-----
id_rsa_pub: | # Et sa clé publique
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

```bash
# Maintenant, chiffrons-le
cd ~/nixos-config/secrets/
sops --encrypt secrets.yaml > secrets.enc.yaml
rm -v secrets.yaml
cat secrets.enc.yaml
```

Finalement, le graal, gérons les secrets avec Home Manager (**home.nix**) :

```nix hl_lines="15 16 17 18 19 20 21 22 23 24 25 26"

{ config, lib, pkgs, ... }:

{
  # Activer Home-Manager
  programs.home-manager.enable = true;

  # Vos infos basiques à fournir à Home Manger
  home.username = "heuzef";
  home.homeDirectory = "/home/heuzef";
  home.stateVersion = "25.11";

  # Activer Flakes
  nix.settings.experimental-features = [ "nix-command" "flakes" ];

  # SOPS
  sops = {
    age.keyFile = "${config.home.homeDirectory}/.config/sops/age/keys.txt"; # Charger la clé AGE
    defaultSopsFile = ./secrets/secrets.enc.yaml; # Charger le fichier de configuration SOPS (chiffré)
    secrets = { # Récupérons nos secrets pour les charger dans notre configuration NixOS
      API_KEY = {}; # Récuperation de la clé API ici
      id_ed25519 = { path = "${config.home.homeDirectory}/.ssh/id_ed25519"; };
      id_ed25519_pub = { path = "${config.home.homeDirectory}/.ssh/id_ed25519.pub"; };
      id_rsa = { path = "${config.home.homeDirectory}/.ssh/id_rsa"; };
      id_rsa_pub = { path = "${config.home.homeDirectory}/.ssh/id_rsa.pub"; };
    };
  };

  # home.packages permet de déployer des logiciels dans son environment utilisateur
  home.packages = with pkgs; [

(...)
}
```

Ainsi, je crée un lien vers des fichiers générés par NixOS dynamiquement (mes clés SSH) depuis mon **secrets.yaml**, grâce à l'argument ``path``, un pur plaisir. 

Il est possible, par exemple, d'appeler le secret **API_KEY** grâce à la variable ``${config.sops.secrets.API_KEY.path}``.

# Conclusion

Grâce à sa logique, NixOS est certainement l'un des OS Linux les plus puissants et complexes à dompter. Il sera très apprécié par ceux qui souhaitent avoir une maîtrise totale de leur machine et de son évolution dans le temps. 

Mon conseil si vous débutez : ne cherchez surtout pas à faire comme les autres, inspirez-vous, mais débutez doucement, gardez la maîtrise et la compréhension de **votre** configuration quoi qu'il arrive, puis faites-la évoluer, en évitant toute complexité inutile. Elle deviendra de plus en plus confortable à l'usage.

Avec tout ceci, vous avez de quoi faire quelques nuits blanches très satisfaisantes pour la construction de votre OS de rêve. N'hésitez pas à demander de l'aide sur le [forum de la communauté](https://discourse.nixos.org). En partageant le dépôt GIT de votre config, vous aurez un soutien très efficace.

Le mot de la fin, voici ma configuration bien sûr : [https://github.com/heuzef/nixos-config](https://github.com/heuzef/nixos-config) ❄️
