## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

***
## Déploiement

Le déploiement de cette application utilise la méthodologie CI/CD avec CircleCI


***
### Pré-requis :
***

- Un compte Github
- Un compte CircleCi
- Un Compte DockerHub
- Un Compte Heroku
- Un Compte Sentry

***
### Etape 1 GITHUB :
***
Cloner le projet afin de pouvoir le lier à CircleCi
```bash
git clone https://github.com/Rossignol-h/p13_OCL_Rossignol_Hanane.git
```


***
### Etape 2 configuration de SENTRY :
***

La surveillance de l’application et le suivi des erreurs se fera via sentry.

- Connecter vous à votre compte https://sentry.io/auth/login/
- Cliquer sur "create project" en haut à droite
- Choisissez la plateforme "Django"
- Nommer le et confirmez sa création
- Dans la barre de recherche en haut à droite taper : "DSN"
- Choisissez votre projet
- Copier votre DSN et réservé le pour la suite.


***
### Etape 3 configuration de HEROKU :
***

lien: https://dashboard.heroku.com/apps

Création d'une application dans Heroku nommée:
- oc-lettings [ *si non disponible ajouter un chiffre (ex: oc-lettings-1)* ]

Ajouter les variables d'environnement suivantes dans ( settings/conf Vars):

| Clé                   | Valeur                              |
|-----------------------|-------------------------------------|
| DEBUG                 | False                               |
| SENTRY_DSN            | DSN de votre projet Sentry          |
| SECRET_KEY            | Clé secrète de l'application Django |

- Dans les settings de votre compte, 
- Copier votre API KEY et réservé la pour la suite.
  lien: https://dashboard.heroku.com/account


***
### Etape 4 configuration de CircleCi :
***

lien de connexion : https://circleci.com/vcs-authorize/

Une fois connecté à votre compte CircleCI __avec votre compte github__ :

- Dans le menu "projets" tous vos repo github seront listés.
- Connectez vous sur le repo du projet en cliquant sur "Set Up Project".
- Le projet possédant déjà un fichier de configuration dans ".circleci/config.yml". 
- il vous sera alors demandé si vous souhaitez l'utiliser.<br>
Confirmez son utilisation.
- Ajouter "main" dans la branche demandée.

Une fois sur la page de gestion de votre projet cliquer sur :<br>
- Organization Settings <br>
- Contexts <br>
- Create contexts <br>
- nommer votre context : oc-lettings<br> 
- puis ajouter les variables d'environnement ci-dessous 

Variables du context CircleCi :

| Clé               | Valeur                                     |
|-------------------|--------------------------------------------|
| DOCKERHUB_USER    | Username de votre DockerHub                |
| DOCKERHUB_TOKEN   | Token d'acces de votre DockerHub           |
| IMAGE_NAME        | Nom de l'image de votre projet             |
| HEROKU_APP_NAME   | Nom de l'app sur Heroku                    |
| HEROKU_API_KEY    | API Key récupérée sur votre compte Heroku  |
| SENTRY_DSN        | DSN de votre projet Sentry                 |
| SECRET_KEY        | Clé secrète de l'application Django        |

***
### Etape 5 activation du Pipeline:
***

Une fois les différents comptes crées et paramétrés:
- Sur votre IDE 
- réalisez une modification sur un fichier de l'application de la branche main et poussez cette modification sur le repo Github.<br>
```
git add .
git commit -m "<commentaire>"
git push -u origin main
``` 
<br>

- Aller sur votre sur le pipeline de votre projet sur Circleci
- lien : https://app.circleci.com/pipelines/github/[my-github-username]
- Le workflow s'activera automatiquement, en voici les étapes ci-dessous

__Job 1__ :<br>
==> install-and-test 
- Installe les dépendances 
- Lance le linting avec Flake8
- Lance les tests avec Pytest

Si les tests passent :

__Job 2__ :<br>
==> build-docker-image
- Connexion à votre compte DockerHub
- Création de l'image
- Tague de l'image avec le “hash”  de commit CircleCI ($CIRCLE_SHA1)
- Envoi (push) de l'image vers le registre des conteneurs DockerHub

Si la conteneurisation a réussi :

__Job 3__ :<br>
==> deploy-to-heroku
- Installation de Heroku CLI sur la machine
- Connexion à votre compte Heroku  
- Envoi de l'image
- Déploiement de la nouvelle version de l'application

#### *Note:*<br>
#### *Si vous faites un push sur une autre branche que "main"*
#### *seul le job 1 (install-and-test) sera activé dans le workflow du pipeline*

***
### Etape 6 HEROKU:
***
- Visiter le lien de déploiement de votre application
https://[nom-de-votre-app].herokuapp.com

- Le lien vers la page d'administration de Django
https://[nom-de-votre-app].herokuapp.com/admin


***
### Etape 7 Sentry:
***

- Générez une erreur "ZeroDivisionError" dans sentry.
en allant sur votre application déployée via ce lien:
https://[nom-de-votre-app].herokuapp.com/sentry-debug/

- Pour afficher et résoudre l'erreur enregistrée: 
- Connectez-vous à [sentry.io](https://sentry.io)
- Ouvrez votre projet.<br>
- Cliquer sur le titre de l'erreur : ZeroDivisionError
- Une page s'ouvrira, vous pourrez voir des informations détaillées et indiquer sa résolution.

***
## Co-Auteur

- Rossignol Hanane 
- Github Profile :octocat: [@Rossignol-h](https://github.com/Rossignol-h)
