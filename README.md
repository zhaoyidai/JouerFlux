# JouerFlux Application

## Description du projet

Le but de ce test est de vérifier les compétences en développement Python, la qualité et la robustesse du code. Il faudra concevoir une application en Python (version 3.X) Flask permettant de modéliser le modèle d'une application « JouerFlux » gérant des firewalls, des politiques de filtrages et des règles firewalls.

Vous êtes libre de mettre en place les fonctionnalités et règles de gestion que vous le souhaitez. Amusez-vous et impressionnez-nous !

Néanmoins, l'application devra comporter au moins les éléments suivants :
- Une base de données SQLite
- Des APIs permettant d'ajouter, afficher et supprimer des firewalls
- Des APIs permettant d'ajouter, afficher et supprimer des politiques de filtrages à un firewall
- Des APIs permettant d'ajouter, afficher et supprimer des règles firewalls à une politique de filtrage
- Le Swagger pour qu'on puisse tester les APIs
- Un README
- BONUS : un Dockerfile permettant de tester facilement l'application

## Fonctionnalités de base

### Gestion des Firewalls
- **Ajouter un firewall** : Permet d'ajouter un nouveau firewall.
- **Afficher les firewalls** : Permet d'afficher la liste des firewalls existants.
- **Supprimer un firewall** : Permet de supprimer un firewall existant.

### Gestion des Politiques de Filtrage
- **Ajouter une politique de filtrage** : Permet d'ajouter une nouvelle politique de filtrage à un firewall.
- **Afficher les politiques de filtrage** : Permet d'afficher les politiques de filtrage associées à un firewall spécifique.
- **Supprimer une politique de filtrage** : Permet de supprimer une politique de filtrage existante.

### Gestion des Règles Firewalls
- **Ajouter une règle** : Permet d'ajouter une nouvelle règle à une politique de filtrage.
- **Afficher les règles** : Permet d'afficher les règles associées à une politique de filtrage spécifique.
- **Supprimer une règle** : Permet de supprimer une règle existante.

## Fonctionnalités ajoutées

### Authentification et Autorisation Avancées
- **Mettre en place authetification et des rôles utilisateur** Permet de se connecter avec différents niveaux d'accès et de permissions.

### Mise à jour des Règles
- **Mettre à jour une règle** : Permet de mettre à jour les détails d'une règle existante. Cette fonctionnalité a été ajoutée pour permettre une gestion plus flexible des règles de filtrage.

### Utilisation de Templates pour les Politiques de Filtrage
- **Création de politiques avec templates** : Permet de créer des politiques de filtrage avec des règles prédéfinies en utilisant des templates. Deux templates ont été définis : `basic` et `strict`. Cette fonctionnalité facilite la configuration rapide des politiques de filtrage.

### Recherche de Firewalls par Adresse IP
- **Rechercher un firewall par adresse IP** : Permet de rechercher des firewalls en fonction de leur adresse IP. Cette fonctionnalité est utile pour retrouver rapidement un firewall spécifique.

### Pagination des Règles pour un Firewall
- **Afficher et paginer les règles d'un firewall** : Permet d'afficher les règles associées à un firewall avec la possibilité de paginer les résultats. Cette fonctionnalité améliore la convivialité en permettant de naviguer facilement parmi un grand nombre de règles.


**PEP 8** : J'ai essayé de respecter maximum

## Instructions pour tester l'application

### Prérequis
- Python 3.X
- Docker (optionnel pour tester via Docker)

### Installation
1. Clonez le dépôt :

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Lancez l'application :
    ```bash
    flask run
    ```

### Utilisation de Docker
1. Construisez l'image Docker :
    ```bash
    docker build -t jouerflux .
    ```

2. Exécutez le conteneur Docker :
    ```bash
    docker run -p 5000:5000 jouerflux
    ```

## Améliorations futures

Si j'avais plus de temps, voici quelques améliorations que j'envisagerais d'apporter :

1. **Tests Unitaires et d'Intégration**
    - Écrire des tests unitaires et d'intégration pour garantir la robustesse et la qualité du code.

2. **Interface Utilisateur**
    - Développer une interface utilisateur front-end pour rendre l'application plus conviviale.

3. **Optimisation des Performances**
    - Optimiser les requêtes à la base de données et améliorer les performances globales de l'application.





### Documentation API
Accédez à la documentation Swagger de l'API via : /swagger
