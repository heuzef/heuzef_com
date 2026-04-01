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

La meilleur astuce, c'est finalement de configurer votre système tranquillement, au minimum de ce que vous avez vraiment besoin, en prenant le temps de le faire vous même, tester et bien maitriser votre code. Vous aller ainsi progressivement basculer sur une configuration maîtrisé et très personnel qui vous correspond.

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
  users.users.heuzef = {
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

Et si vous souhaitez effectuer la mise à jour du système : ``sudo nixos-rebuild switch --upgrade``, gérer les éventuels conflits, suivi d'un redémarrage.

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

Sous condition bien sûr d'avoir activé la virtualisation sur votre système. Comment faire ? Dans le fichier de configuration évidement :

```nix
services.qemuGuest.enable = true;
```

# Principe des modules 🧩

L'avantage de travailler avec des fichiers de configuration modulaire, c'est que cela simplifie la maintenance et la gestion du déploiement.
Par exemple, voici un fichier de configuration très basique pour Steam :

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
* Télécharger votre fichier .AppImage et autoriser son execution (``sudo chmod +x -R *.AppImage``)
* Démarrer le programme : ``appimage-run *.AppImage``

# Passer au niveau supérieur ⭐

Vous êtes surement convaincu des possibilités, cependant, NixOS commence à prendre tout son sens lorsque nous embrassons tout les avantages offert par le déclaratif. Ainsi, nous allons à présent voir comment  :

* Versionner sa configuration sur GIT
* Utiliser Home-Manager avec Flake pour exploiter toutes les fonctionnalités expérimentales
* Gérer plusieurs machines

## Versionning Git

Pour commencer, nous allons initier un dépôt GIT sur Github. Je considère que vous avez déjà un compte Github et créé un dépôt. Vous pouvez le nommer **nixos-config** par exemple, c'est une sorte de convention, cela vous permet entre autre de trouver facilement [d'autre dépôt similaire pour vous inspirer de quelques pépites](https://github.com/search?q=nixos-config&type=repositories&s=stars&o=desc). Par exemple, voici le miens : [https://github.com/heuzef/nixos-config](https://github.com/heuzef/nixos-config)

Basculons dans le terminal, placez-vous dans le repertoire où vous souhaitez maintenir la configuration de votre système. N'ayant pas encore GIT déployé sur le système, nous utiliserons Nix-Shell pour l'instant, le temps de cloner notre dépôt.

```bash
cd ~ # Utilisation du repertoire utilisateur, ici pour notre exemple
nix-shell -p git --command "git clone git@github.com:<VOTRE-PSEUDO-GITHUB>/nixos-config.git"
exit
cd nixos-config
```
Créons à présent dedans un fichier de configuration contenant le minimum : ``cp -v /etc/nixos/configuration.nix ~/nixos-config/``.

En plus de la configuration minimal (vu plus tôt ci-dessus), déclarer également :

```nix
  networking.hostName = "mon-pc"; # Le nom d'hôte de votre machine, c'est important
  
  programs.firefox.enable = true; # Activer Firefox

  # Activer et configuer Git :
  programs.git = {
    enable = true;
    lfs.enable = true;
    settings.user.name = "<VOTRE-PSEUDO-GITHUB>";
    settings.user.email = "<VOTRE-EMAIL>";
  };
```

Finalement, vous pouvez déjà reconstruire votre système avec ce fichier de configuration : ``sudo nixos-rebuild switch --file ~/nixos-config/configuration.nix``

Si vous rencontrez une erreur, pas de panique, analyser-la, elle sont généralement plutôt claire et sont là pour vous aider à valider un fichier de configuration parfaitement propre.
Si cela prend du temps aussi c'est normal, NixOS analyse les différences trouvés entre le système et votre déclaration. Si vous re-construiser à nouveau sans rien modifier dans la configuration, vous constaterez que le rebuild est quasiment instantané, car aucun changement n'est appliqué.

Git est maintenant installé et configuré, créons notre premier commit :

```bash
git add --all
git commit -m "Init my NixOS configuration"
git push
```

Et ba voilà 👌 Vous avez votre configuration verssionné sur GIT ! Vous avez compris le processus pour modifier votre configuration système :
- Éditer les fichiers de configurations
- Rebuild (en cas d'erreur, on corrige, on test, ...)
- Si l'on est satisfait, on commit et push

C'est déjà super ainsi, mais allons plus loins avec des fonctionnalités très populaires.

## Home-Manager et Flakes

Si NixOS gère la structure de base, Home-Manager, lui, s'occupe de personnaliser ses sessions. En effet, NixOS gère très bien la configuration du système, mais moins bien la configuration utilisateur. Home-Manager s'impose alors et utilise le langage Nix pour gérer les fichiers personnels (les fameux "dotfiles" comme .bashrc, etc ...). C'est donc un complément très utile pour personnaliser son système.

Les Flakes (introduits comme une fonctionnalité expérimentale mais devenue le standard de fait) règlent un souci important : l'installation d'une configuration aujourd'hui peut varier dans le temps à cause des versions de logiciels différentes, car les "sources" de Nix ont été mises à jour entre-temps. Il s'agit donc d'un "verrou" de sécurité et de modernité.

Un Flake est donc un projet, Nix qui définit explicitement ses dépendances. Un fichier __flake.lock__ enregistre la version précise (le "hash" Git) de chaque source utilisés.

L'analogie de la recette de cuisine :

* Sans Flake : La recette dit "Prenez du lait". Si le lait du supermarché change de marque, le goût du gâteau change.
* Avec Flake : La recette dit "Prenez le lait de la marque X, lot n°1234, datant du 01/01/1970". Le gâteau sera exactement le même, à chaque fois, pour tout le monde.

C'est donc vos commits Git qui deviennent la véritée absolue. Il donc recommandé d'effectuer un ``git add --all`` de votre dépôt, avant chaque rebuild ! (Sinon ça couine).

Voici un exemple de structure basique à avoir à ce stade, nous permettant de gérer plusieurs machine :

```bash
 .
├──  .git # GIT
├──  configuration.nix # La configuration NixOS principale
├──  flake.lock # Le verrou Flake
├──  flake.nix # Configuration Flake
├──  hardware # Les configurations matérielles de vos machines. Astuce, pour afficher la configuration de votre machine : sudo nixos-generate-config --show-hardware-config
│   ├──  mon-pc-01.nix
│   ├──  mon-pc-02.nix
│   └──  mon-pc-03.nix
├──  home.nix # Configuration Home-Manager
├── 󰂺 README.md # Vos notes perso pour le dépôt
└──  software
    └──  steam # Configuration du logiciel Steam pour le jeu-vidéo
```

Voyons à présent les fichiers de configuration de Home-Manager et Flakes

### flake.nix

Votre fichier **flake.nix** deviendra votre point d'entrée, c'est lui qui sera appelé pour le rebuild, afin de vous permettre d'executer avec des arguments conditionnels. Dans notre cas, cela sera pour préciser la machine, mais après, libre à vous d'être créatif.

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
            ./hardware/mon-pc-01.nix # sudo nixos-generate-config --show-hardware-config
          ];
        };

        # mon-pc-02
        mon-pc-02 = lib.nixosSystem {
          inherit system;
          modules = [
            ./configuration.nix
            ./hardware/mon-pc-02.nix
            ./software/steam.nix # sur cette machine, je décide de déployer Steam pour jouer au jeux-vidéo
          ];
        };
        
        # mon-pc-03
        mon-pc-03 = lib.nixosSystem {
          inherit system;
          modules = [
            ./config-light.nix # cette machine est peu puissante, j'utilise une configuration plus économe en ressource.
            ./hardware/mon-pc-02.nix
          ];
        };
        
      };
    };
}
```

Avec cette configuration, la commande de rebuild pour la machine __mon-pc-01__ sera :

``sudo nixos-rebuild switch --flake "~/nixos-config#mon-pc-01"``

### home.nix

Voyons à présent comment activer Home-Manger, dans le fichier **flake.nix**, nous ajouterons les éléments suivants :

Dans la partie __inputs__ :
```nix
    home-manager = {
      url = "github:nix-community/home-manager"; # Les modules peuvent être appelées directement depuis un dépôt Github compatible, c'est beaucoup trop cool !
      inputs.nixpkgs.follows = "nixpkgs";
    };
```

Puis, dans la section __modules__ d'une machine :

```nix
home-manager.nixosModules.home-manager
{
  networking.hostName = "mon-pc-01"; # Possible de configurer votre nom d'hôte ici, à supprimer, bien sûr, de configuration.nix qui est communs à toutes les machines
  home-manager.useGlobalPkgs = true; # Activer les paquets système
  home-manager.useUserPackages = true; # Activer les paquets utilisateur
  home-manager.users.heuzef = import ./home.nix; # Nous allons importer ainsi notre configuration Home-Manager
}
```

Passons à présent au coeur de Home-Manager, voici un exemple de fichier **home.nix**  :

```nix
...
```
