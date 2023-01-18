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


### Déploiement
***
Introduction :

Lors de l'envoi d'un commit sur la branche "main" du projet présent sur Github, CircleCI (lui même lié au repository) va déclencher plusieurs processus automatiquement :
1. Réalisations des tests pour vérifier le fonctionnement du code.
2. Si la première étape est un succès, alors l'étape de construction de l'image de l'application démarre et sera envoyer sur DockerHub.
3. Si la première étape est un succès, l'application sera envoyée sur Heroku pour effectuer son déploiement.


Pré-requis :

- Un compte Github
- Un compte CircleCi
- Un Compte DockerHub
- Un Compte Heroku
- Un Compte Sentry


### Etape 1 Github:
***
Cloner le projet afin de pouvoir le lier à CircleCi
```bash
git clone https://github.com/Rossignol-h/P13_rossignol_hanane.git
```
***

### Etape 2 configuration de SENTRY :
***

La surveillance de l’application et le suivi des erreurs se fera via sentry.

- Connecter vous à votre compte https://sentry.io/auth/login/
- Cliquer sur "create project" en haut à droite
- Choisissez la plateforme "Django"
- Nommer le et confirmez sa création
- Dans la barre de recherche en haut à droite taper: DSN
- Choisissez votre projet
- Copier votre DSN

### Etape 3 configuration de HEROKU :
***

lien: https://dashboard.heroku.com/apps

Création d'une application dans Heroku nommée:
- oc-lettings *si non disponible ajouter un chiffre (ex: oc-lettings-1)*

Ajouter les variables d'environnement suivantes dans ( settings/conf Vars):

| Clé                   | Valeur                              |
|-----------------------|-------------------------------------|
| DEBUG                 | False                               |
| SENTRY_DSN            | DSN de votre projet Sentry          |
| SECRET_KEY            | Clé secrète de l'application Django |
| DISABLE_COLLECTSTATIC | 1                                   |
| HEROKU_APP_NAME       |  oc-lettings-2                      |

***


### Etape 4 CircleCi:
***
lien: https://circleci.com/docs/

Une fois connecté à votre compte CircleCI avec votre compte github,
dans le menu "projets" tous vos repo github seront listés
connectez vous sur le repository du projet en cliquant sur "Set Up Project".
Le projet possédant déjà un fichier de configuration dans ".circleci/config.yml" 
il vous sera alors demandé si vous souhaitez l'utiliser.<br>
Confirmez son utilisation.

Une fois sur la page de gestion de votre projet sur CircleCI,
cliquer sur :<br>
=> Organization Settings <br>
=> Contexts <br>
=> Create contexts <br>
=> nommer votre context<br> 
=> puis ajouter les variables d'environnement ci-dessous 

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

- Aller sur votre sur la pipeline de votre projet sur Circleci
- Le workflow s'activera automatiquement, en voici les étapes ci-dessous

Job 1 :<br>
==> install-and-test 
- Installe les dépendances 
- Lance le linting avec Flake8
- Lance les tests avec Pytest

Si les tests passent :

Job 2 :<br>
==> build-docker-image
- Connexion à votre compte DockerHub
- Création de l'image
- Tague de l'image avec le “hash”  de commit CircleCI ($CIRCLE_SHA1)
- Envoi (push) de l'image vers le registre des conteneurs DockerHub

Si la conteneurisation a réussi :

Job 3 :<br>
==> deploy-to-heroku
- Installation de Heroku CLI sur la machine
- Connexion à votre compte Heroku  
- Envoi de l'image
- Déploiement de la nouvelle version de l'application

#### *Note: si vous faites un push sur une autre branche que main seul le job 1 (install-and-test) sera activé dans le workflow du pipeline*

***
### Etape 6 HEROKU:
***
- Visiter le lien de déploiement de votre application
https://oc-lettings-2.herokuapp.com

- Le lien vers la page d'administration de Django
https://oc-lettings-2.herokuapp.com/admin/login/?next=/admin/
***

### Etape 7 Sentry:
***

- Générez une erreur "ZeroDivisionError" dans sentry.
en allant sur votre application déployée via ce lien:
https://oc-lettings-2.herokuapp.com/sentry-debug/

- Pour afficher et résoudre l'erreur enregistrée: 
- Connectez-vous à [sentry.io](https://sentry.io)
- Ouvrez votre projet.<br>
- Cliquer sur le titre de l'erreur
- Une page s'ouvrira, vous pourrez voir des informations détaillées et indiquer sa résolution.

## Co-Auteur

- Rossignol Hanane 
- Github Profile :octocat: [@Rossignol-h](https://github.com/Rossignol-h)
