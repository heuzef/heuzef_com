Title: Mettre en service sa propre instance de Matrix avec Bridges
Category: Informatique
Tags: autohébergement, web, social, docker, tchat, communication
Date: 2024-03-01
Status: draft

Pour ceux qui ne connaisse pas encore Matrix, je le présente succinctement ainsi : c'est un outil messagerie moderne, qui est supérieur technologiquement à toutes les autres solution équivalente (Instagram, WhatsApp, Messenger, Signal, WeChat, Telegram, Discord, etc ...). 

Mais ce n'est pas tout, en plus d'être très sécurisé, c'est aussi une solution libre, éthique et décentralisée et en constante évolution grâce à une large communautée très impliquée dans cette solution de messagerie utlime que n'importe qui peux utiliser ou auto-héberger.

Il n'y a donc absolument aucun argument en faveur des autres platformes (même pour Signal oui oui) et dans un monde idéal l'humanitée entière utiliserais Matrix comme solution unique de communiquation.

J'ajoute que tout bon dirigeant d'entreprise qui utilise une solution de tchat en interne doit forcément déployer Matrix pour sa société, tout autre choix sera fondalement moins pertinant, voir dangereux. Le monopôle de Microsoft avec Teams n'est d'ailleur pas un freins, car il est tous à fait possible d'integrer des solutions de Visio comme [Jitsi](https://meet.jit.si) dans l'instance Matrix. Et une fois que nous avons goûté à l'outil, nous sommes rapidement convaincu.

![Messenger FR](../../assets/messenger_fr.png)

Maintenant que les présentations sont faite, je vais expliquer dans cette note comment déployer simplement une instance avec Docker et surtout avec des Bridges. Je précise que cette note est co-rédigéré avec [Lucas Assier](https://www.linkedin.com/in/lucasassier), qui à également une expérience fraîche avec Matrix de son côté !

Avant de débuter l'aventure, [commencez par créer un compte Matrix](https://app.element.io/#/register). Réserver votre identifiant et profitez-en pour tester Matrix sur les serveurs d'Element.

# Qui utilise Matrix en 2024 ? 🗣

Je dirais, quasiment personne, comme beaucoup d'outil libre, pas de gros marketing derrière. Même [Signal](https://www.signal.org), qui met pourtant les moyens, peine à concurencer ses concurents qui sont pourtant naze au possible, alors autant dire que Matrix n'est pas prêt de percer, mais patience cela arrivera car contrairement au autre, Matrix est pereine dans le temps et sera là encore bien après eux (l'e-mail, xmpp et irc en témoignent). Finalement, les seuls qui ont, en 2024, un interêt à déployer du Matrix, sont les entreprises, associations et organisations qui souhaitent disposer d'un outil de communication en interne. Pour les autres, on y retrouvera majoritairement des Geek élitiste qui ont la chance d'avoir les connaissances et le temps pour maintenir cet outil.

# Les Bridges ! 🏗

En plus de pouvoir choisir n'importe quel interface de tchat pour votre Matrix (ce qui est déjà génial), Matrix à donc lancé une idée révolutionaire : **Les bridges** !

L'idée est extaorinaire car elle promet récupérer le trafic (donnés et messages) des autres plateformes dans votre instance Matrix, carément !

[<i class="fa fa-link"></i> matrix.org/ecosystem/bridges](https://matrix.org/ecosystem/bridges)

Il faut comprendre que les Bridges sont additionnels et heuresement, car il y à baleine sous gravillon, explication dans le chapitre suivant.

# Le piège des Bridges 🚧

Après plusieurs mois d'utilisation des Bridges, je vais être honnête, c'est un calvaire et la maintenance est chronophage au possible. Les Bridges sont essentiellement des prototypes en Alpha et plus nous en ajoutons plus c'est instable, la maintenance n'en devient que plus lourde.

Chaque Bridge à son lot de galère c'est sans fin, **il faut donc être determiné à y consacrer beaucoup de temps !**

Autrement, la meilleur alternative que je connaisse est [Element-ONE](https://ems.element.io/element-one), payant et avec seulement trois Bridges, mais c'est un début 😉

# Déploiement basique avec Docker 🐳

Si vous êtes à l'aise avec Docker, alors la configuration suivante vous permettra de mettre en place votre instance Martrix. Pour les plus barbus, vous pouvez aussi [jouer avec Ansible](https://github.com/spantaleev/matrix-docker-ansible-deploy) 🤓

La configuration générale ici est donc d'installer le moteur Synapse avec sa DB Postgres. Avec seulement ceci, vous pourrez bénéficier d'une instance Matrix qui tourne super bien.

Pour tout le reste, ce sont les Bridges, que vous pouvez simplement commenter pour ne pas les déployer dans un premier temps, voir jamais, vu l'enfer que s'est à gérer.

## Docker compose file

```yaml
version: '3'

services:

  # Synapse
  synapse:
    image: matrixdotorg/synapse:latest
    container_name: matrix-synapse
    hostname: matrix-synapse
    restart: unless-stopped
    environment:
      - SYNAPSE_CONFIG_PATH=/data/homeserver.yaml
    volumes:
      - /home/matrix/Synapse:/data
      - /home/matrix/bridges:/bridges
      - /tmp/test:/var/log
    depends_on:
      - matrix-db
    ports:
      - 8448:8448/tcp
      - 8008:8008/tcp

  matrix-db:
    image: postgres
    container_name: matrix-db
    hostname: matrix-db
    restart: unless-stopped
    environment:
      - POSTGRES_USER=synapse
      - POSTGRES_PASSWORD=**********
      - POSTGRESQL_PASSWORD=**********
      - POSTGRES_DB=matrix
      - POSTGRES_INITDB_ARGS=--encoding=UTF-8 --lc-collate=C --lc-ctype=C
    volumes:
      - /home/matrix/Postgres:/var/lib/postgresql/data

# BRIDGES CONTAINERS ##########

  # Signal bridge
  mautrix-signal:
    image: dock.mau.dev/mautrix/signal
    container_name: mautrix-signal
    hostname: mautrix-signal
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/signal/signald:/signald
      - /home/matrix/bridges/signal/data:/data
    ports:
      - 29328:29328/tcp
    depends_on:
      - synapse
      - signald
      - signal-db

  signald:
    image: docker.io/signald/signald
    container_name: signald
    hostname: signald
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/signal/signald:/signald

  signal-db:
    image: postgres
    container_name: signal-db
    hostname: signal-db
    restart: unless-stopped
    environment:
      - POSTGRES_USER=mautrixsignal
      - POSTGRES_DATABASE=mautrixsignal
      - POSTGRES_PASSWORD=**********
    volumes:
      - /home/matrix/bridges/signal/Postgres:/var/lib/postgresql/data

  # Discord bridge
  mautrix-discord:
    image: dock.mau.dev/mautrix/discord
    container_name: mautrix-discord
    hostname: mautrix-discord
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/discord/data:/data
    ports:
      - 29334:29334/tcp
    depends_on:
      - synapse

  # Whatsapp bridge
  mautrix-whatsapp:
    image: dock.mau.dev/mautrix/whatsapp
    container_name: mautrix-whatsapp
    hostname: mautrix-whatsapp
    restart: unless-stopped
    volumes:
      - /home/bridges/whatsapp/data:/data
    ports:
      - 29318:29318/tcp
    depends_on:
      - synapse

  # Facebook bridge
  mautrix-facebook:
    image: dock.mau.dev/mautrix/facebook
    container_name: mautrix-facebook
    hostname: mautrix-facebook
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/facebook/data:/data
    ports:
      - 29319:29319/tcp
    depends_on:
      - synapse

  # Instagram bridge
  mautrix-instagram:
    image: dock.mau.dev/mautrix/instagram
    container_name: mautrix-instragram
    hostname: mautrix-instagram
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/instagram/data:/data
    ports:
      - 29330:29330/tcp
    depends_on:
      - synapse

  # Telegram bridge
  mautrix-telegram:
    image: dock.mau.dev/mautrix/telegram
    container_name: mautrix-telegram
    hostname: mautrix-telegram
    restart: unless-stopped
    volumes:
      - /home/matrix/bridges/telegram/data:/data
    ports:
      - 29317:29317/tcp
    depends_on:
       - synapse

# Slack bridge
mautrix-slack:
  image: dock.mau.dev/mautrix/slack
  container_name: mautrix-slack
  hostname: mautrix-slack
  restart: unless-stopped
  volumes:
    - /home/matrix/bridges/slack/data:/data
  ports:
    - 29335:29335/tcp
 depends_on:
    - synapse

# Wechat bridge 
matrix-wechat:
  image: lxduo/matrix-wechat
  container_name: matrix-wechat
  hostname: matrix-wechat
  restart: unless-stopped
  volumes:
    - /home/heuzef/matrix/bridges/wechat/data:/data
  ports:
    - 17778:17778/tcp
  depends_on:
    - synapse

# Wechat agent
agent-wechat:
  image: lxduo/matrix-wechat-docker
  container_name: agent-wechat
  hostname: agent-wechat
  restart: unless-stopped
  environment:
    - WECHAT_HOST=wss://matrix-wechat/_wechat/
    - WECHAT_SECRET=00000000000
  volumes:
    - /home/heuzef/matrix/bridges/wechat/hongli/:/home/user/matrix-wechat-agent
  depends_on:
    - matrix-wechat
```

## Configuration de Synapse

Générer le fichier de config Synapse : 

```
docker run -it --rm -v /home/matrix/Synapse/:/data -e SYNAPSE_SERVER_NAME=matrix.domain.tld -e SYNAPSE_REPORT_STATS=no matrixdotorg/synapse:latest generate
```

Ce fichier de configuration sera généré dans  **/home/matrix/Synapse/homeserver.yaml**, plutôt simple à comprendre, voici quelques paramètres à modifier celon vos besoins :



```yaml
max_upload_size: 100M
enable_registration: true
enable_registration_without_verification: true
app_service_config_files:
    - /bridges/discord/data/registration.yaml
    - /bridges/facebook/data/registration.yaml
    - /bridges/instagram/data/registration.yaml
    - /bridges/signal/data/registration.yaml
    - /bridges/slack/data/registration.yaml
    - /bridges/telegram/data/registration.yaml
    - /bridges/wechat/data/registration.yaml
    - /bridges/whatsapp/data/registration.yaml
```

Chaque fichier de configuration des bridges est similaire, les paramètres récurents à modifier sont les suivants :

```yaml
homeserver:
    address: https://matrix.domain.tld
    domain: matrix.domain.tld
    address: http://<hostname>:<port>
    hostname: 0.0.0.0
    port: <port>
    database:
        type: sqlite3
        uri: <bridge>-db.sqlite
    permissions:
        "*": relay
        "matrix.domain.tld": user
        "@votre-pseudo:matrix.domain.tld": admin
```

Maintenant, vous pouvez démarrer toute la tambouille : ``docker compose -f /home/matrix/docker-compose.yml up``

Le premier lancement peu prendre du temps, le temps que les fichiers de configuration et de **registration.yaml** soit générés.

N'anticiper pas leur création, ces derniers doivent être générés par synapse, confirmant que tout fonctionne correctement, enssuite vous pouvez éditer les paramètres, puis finalement relancer les services.

Vous aurrez probablement une erreur de permission sur ces fichiers d'ailleur, corrigez simplement cela :

```bash
sudo chmod 644 /home/matrix/bridges/*/data/registration.yaml
```

## Visio-conférence

Si vous souhaitez utiliser la visio-conférence, notez bien que cette dernière ne fonctionnera que en local sur votre réseau interne. Pour aller plus loin et profiter pleinement des fonctionnalités de la visio-conférence, il vous faudra mettre en service un serveur TURN : [Configuring a Turn Server - Synapse](https://matrix-org.github.io/synapse/latest/turn-howto.html)

# Mon retour d'expérience sur les différents Bridges

Vous remarquerez que la plupart des Bridges sont déployé via [MAUTRIX](https://docs.mau.fi/bridges/general/docker-setup.html?bridge=telegram&ref=infos.zogg.fr). Ce n'est pas pour rien car la plus grande panoplie est édité par eux et c'est aussi bien souvent les bridges les plus stable.

Pour rappel, [la liste des Bridges est diffusée sur le site officiel de Matrix](https://matrix.org/ecosystem/bridges/).

De façon général, la logique d'ajout d'un bridge est toujours la même :

1. Execution du bridge.

2. Depuis votre client Matrix préféré, rechercher le bot du bridge pour commencer une discution avec lui.

3. Dans le canal de discution avec le bot taper ``help`` pour afficher les actions possibles.

## Signal

Le Bridge de Signal est un peu lourd à mettre en place car il réclame une DB à part (ce que je vous conseil vivement de faire pour les performances). Après cela, il tourne plutôt bien !

1. Inviter @signalbot
2. Enregistrez votre téléphone ``register +33000000000``
3. Récupérer un jeton captcha sur le site dédié de signal
   - https://signalcaptchas.org/registration/generate.html
   - Récupérer le token situé après le **signalcaptcha://signal-recaptcha-v2.**
4. Valider le code SMS
5. Définir son nom : ``set-profile-name USER``

## Discord

Pour Discord, la première initialisation ne permet que de jongler avec les messagerie privée, vous aurez ensuite besoin de jouer avec les commandes du bridges pour rejoindre les différentes guildes (plus communément appelés "Serveurs Discord" par les moldus) via leur identifiants uniques.

Ensuite, c'est le gros dawa, si vous invitez une guilde assez grose, vous allez vous retrouver avec autant de notification d'invitation à accépter que de catégories ! Bon une fois que c'est validés, vous êtes tranquille, mais faite très attention aux journaux qui vont être générés sur votre serveur, ça va très rapidement remplir l'espace disque s'il y a de l'activité sur vos salons discord !



1. Inviter @discordbot

2. Sur l'app mobile : *paramètres de l'app > "Scanner le QR code"*

3. Envoyer la commande au bot : ``login-qr``

4. La commande ``guilds status`` permet d'afficher les différents "Serveurs Discord"



## WhatsApp

Alors WhatsApp, pour faire simple, dispose d'une sécuritée très agréable qui consite à déconnecter tous vos périphériques tiers après une semaine, super ...

Cela concerne donc également votre Bridge qu'il vous faudra reconnecter avec un QRCode toute les semaines. Voila voila ... 👌

1. Inviter @whatsappbot
2. Sur l'app mobile : *paramètres de l'app > "Scanner le QR QR"*
3. Envoyer la commande au bot : ``login``

## Facebook et Instagram

Dans le même type de flood absurde que discord, vous aller recevoir une notif d'invite à accépter pour chaque personne ... J'espère pour vous que vous êtes un associal avec peu d'amis sur ces plateformes, sinon vous aller user votre souris à accépter des centaines d'invitations.
A et un conseil, tester bien vos volumes docker, le redémarrage du bridge à tendance à tout remettre à zéro, histoire de vous pousser au sucide une bonne fois pour toute 😖

## Telegram

Un peu plus de difficulté à mettre en place le bridge Télégram, le bot étant encore en Alpha protoype au moment de mon test, mais enssuite, fonctionne correctement.

Sur la configuration, il est nécessaire d'ajouter une clef d'API récupérable sur : https://my.telegram.org/apps

```yalm
App api_id: 00000000
App api_hash: 00000000000000000000000000000000 
```

1. Inviter @telegrambot
2. Sur l'app mobile : *paramètres de l'app > "Scanner le code QR"*
3. Envoyer la commande au bot : ``login-qr``

## WeChat

La palme d'or de la torture reviens à nos amis Chinois avec leur messagerie abominable.

Créé par un nerd Chinois répondant au doux nom de [lxduo](https://github.com/duo/matrix-wechat-docker), ce dernier probablement considéré par un teroriste par le gouvernement chinois, à eu la patience de mettre au monde un Brige capable de s'accoupler avec cette horreur de WeChat. 

Ce qui donne naissance à une terrible usine à Gaz qui vous servira d'hote, qui vous faudra accompagner d'autant usine à gaz supplémentaire que vous souhaitez ajouter de compte WeChat ... Le gros délire en terme de consomation de ressource 😭.

Bon dans mon cas, [je n'ai même pas réussis à le faire tomber en marche](https://github.com/duo/matrix-wechat-docker/issues/2) et à vrais dire, j'ai surement été banni par le gouvernement Chinois de leur app car impossible de me créer un compte, j'ai donc rennoncé.
Bon je prévois un voyage en Chine en 2024, je vais en profiter pour me créer un compte en lousdé sur place, je ferais peut-être un article à ce sujet un jour si c'est croustillant.



1. Inviter @wechatbot
2. Sur l'app mobile : *paramètres de l'app > "Scanner le code QR"*
3. Envoyer la commande au bot : ``login`` pour tenter de détecter l'agent WeChat



## SMS

En bonus, j'ai tenté l'utilisation de [SmsMatrix](https://f-droid.org/en/packages/eu.droogers.smsmatrix/), une app tiers qui peux tourner avec un bridg, j'ai fait tomber en marche le machin ainsi :

S'authentifier sur le compte **@smsbot:matrix.domain.tld** et inviter son compte utilisateur pour créer un canal de discution.
Après autorisation, installer SmsMatrix sur votre téléphone :

```
Bot Username : smsbot
Bot Password : **********
Homeserver url : https://matrix.domain.tld
Your username @<USER>:matrix.com
Devicename : <NOM-DU-TEL>
```

Il suffit ensuite de recevoir un SMS pour initialiser une conversation.



Attention, cette solution est crade car si vous commencez à vouloir partager ce bridge avec d'autre utilisateur, en plus de devoir vous partager le mot de passe du compte @smsbot, cela va mettre un sacré merdier dans qui envoi/reçoi les sms ...

Préférez plutôt une solution plus complexe comme [mautrix-gmessages](https://github.com/mautrix/gmessages) qui fonctionnera avec le client SMS natif d'Android.



# Conclusion

* Matrix c'est le top du top. Les autres alternatives font pâles figure. Tant sur l'aspect technique que éthique.

* Quasiment personne ne connais et n'utilise ça dans le monde pro et encore moins ailleur.

* La configuration d'un serveur TURN supplémentaire est nécessaire si vous souhaiter profiter de la Visio-conférence.

* La configuration des Bridges est très chonophage et instable.



C'est tout pour moi 😉 je vous relais maintenant les notes de mon amis [Lucas Assier](https://www.linkedin.com/in/lucasassier), qui souhaite également partager son expérience avec Matrix.
Sans aller aussi loin que moi sur la quantité de Bridge testés, il a cependant abordé le Double Puppetting, très interessant pour profiter pleinement des Bridges.



---
