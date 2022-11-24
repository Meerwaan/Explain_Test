# Consultation des elus 

## Brainstorming

Disclaimer:  J'ai choisi Django comme Framework web basé sur Pyhton car il est du type Model Template Views pour pouvoir me concentrer sur la base de donnée et non sur le UI comme mentionné dans l'enoncer

## Etapes a suivre pour le projet 

### Architecture du projet

- TestExplain/
- display_electors/
- Création de la base de donnée 
- display.html

### Installation 

- Installation de pipenv
- Installation de Django
- Création du projet : TestExplain
- Création de l'application :display_electors 

### Créations des models

- Création des classes dans le fichier models.py
    - Territories
    - TerritoriesParents
- Ajout des models dans settings.py

### Transfert de la base de donnée .csv à SQLITE3 

- Verifier la BDD 
- Sqlite shell 
    - .mode csv
    - .import <file.csv> <django_db_file>


### Création du compte Admin

- Le compte Admin pourra gerer les données (supprimer, ajout ...)
 

### Création d'une page qui affiche les données 

- Mise en place du template 
- afficher les données de la class Territories sur le template

