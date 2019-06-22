# documentation-ultime
http://codex.alwaysdata.net/

Site contenant des liens, ressources, explication de concepts, faq des erreurs courantes etc... Pour les domaine du Machine Learning, Deep Learning, Python, base de donnees, web

# Installation
## 1. Téléchargement
```
git clone https://github.com/June-So/documentation-ultime.git
cd documentation-ultime
```
## 2.a Environnement virtuel: Window
```
python -m venv venv
venv\Scripts\activate
```

## 2.b Environnement virtuel: Linux
```
python -m venv venv
source venv/Scripts/activate
```

## 3. Installation dépendances
```
pip install requirements.txt
```
## 4. Configuration de la base de données
[ Vous devez créer au préalable une base de données locale postgres ]

Modifier le fichier SECRET.py avec vos identifiants permettant la connexion à la base de données.

### a. Importer la base de données
````
psql -U username dbname < codex.dump
````
### b. Créer une base de donnée vierge
``` 
flask db init
flask db migrate
flask db upgrade
```


# Lancer l'application
```
python run.py
```
