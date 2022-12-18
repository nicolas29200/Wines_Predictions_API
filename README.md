# TP_NOTE_FastApi
ING3 ICC - Architecture microservices 

## Récupérer le repository Github

Dans un dossier vierge :

```git init```
```git remote add origin git@github.com:AkkiYacine/TP_NOTE_FastApi.git```
```git pull```

ou alors faire ```git clone git@github.com:AkkiYacine/TP_NOTE_FastApi.git```

## Installer un environnement virtuel pyhton

pour l'installer : ```python3 -m venv <environment name>```
pour l'activer : ```source <environment name>/bin/activate```

## Installation des dépendances dans l'environnement virtuel pyhton

Il faudra utiliser le fichier requirements.txt et faire :
```pip install -r requirements.txt```

## Lancement de l'application FastAPI

aller dans le dossier app : ```cd app```
lancer l'application : ```uvicorn main:app --reload```

## Lancement des tests

aller dans le dossier app : ```cd app```
lancer les tests : ```pytest test.py```





