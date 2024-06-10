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
- **Mettre en place authetification et des rôles utilisateur** : Permet de se connecter avec différents niveaux d'accès et de permissions.

    Il y a deux type d'utilisateur : user et admin. 
    ### Endpoints et Permissions

| Méthode | Endpoint           | Description                                    | Accès                   |
|---------|--------------------|------------------------------------------------|-------------------------|
| GET     | /firewall          | Obtenir tous les firewalls                     | Ouvert à tous           |
| POST    | /firewall          | Créer un nouveau firewall                      | Admin uniquement        |
| DELETE  | /firewall/{id}     | Supprimer un firewall                          | Admin uniquement        |
| GET     | /firewall/search   | Rechercher des firewalls par adresse IP        | Utilisateurs et Admin   |
| POST    | /policy            | Créer une nouvelle politique                   | Admin uniquement        |
| GET     | /policy/{id}       | Obtenir les politiques pour un firewall        | Utilisateurs et Admin   |
| DELETE  | /policy/{id}       | Supprimer une politique                        | Admin uniquement        |
| GET     | /rules             | Obtenir toutes les règles pour un firewall (avec pagination) | Utilisateurs et Admin |
| GET     | /rule/{id}         | Obtenir toutes les règles par ID de politique  | Utilisateurs et Admin   |
| PUT     | /rule/{id}         | Mettre à jour une règle existante              | Admin uniquement        |
| DELETE  | /rule/{id}         | Supprimer une règle                            | Admin uniquement        |

#### Gestion des Rôles et Permissions

Pour garantir que seules les actions appropriées soient effectuées par les utilisateurs autorisés, j'ai utilisé les fonctions dans `werkzeug` et `flask_jwt_extended`:

- Utiliser JWT pour la gestion des sessions permet une intégration simple avec Swagger, où les tokens Bearer peuvent être facilement utilisés pour authentifier les requêtes. C'est la méthode plus simple et directe.

#### Décorateurs Personnalisés pour l'Admin

J'ai défini un décorateur personnalisé pour vérifier le rôle de l'utilisateur avant d'autoriser l'accès à certaines routes. Ce décorateur garantit que seules les personnes ayant le rôle d'admin peuvent ajouter, supprimer ou modifier des entrées.

### Utilisation de Templates pour les Politiques de Filtrage
- **Création de politiques avec templates** : Permet de créer des politiques de filtrage avec des règles prédéfinies en utilisant des templates. 

- Deux templates ont été définis : `basic` et `strict`. Cette fonctionnalité facilite la configuration rapide des politiques de filtrage et des règles.

### Mise à jour des Règles
- **Mettre à jour une règle** : Permet de mettre à jour les détails d'une règle existante. Cette fonctionnalité a été ajoutée pour permettre une gestion plus flexible des règles.
- Bien que la mise à jour soit possible pour les firewalls et les politiques, j'ai particulièrement mis l'accent sur la personnalisation des règles. Cela s'explique par le fait que utilisateurs ont la possibilité de créer des règles à partir de templates. Ainsi, pour une compatibilité et une flexibilité maximales, les utilisateurs peuvent également personnaliser ces règles selon leurs besoins spécifiques.



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

2. Journalisation et Suivi des Activités
Mettre en place un système de journalisation(logging) pour surveiller et enregistrer les activités des utilisateurs, ce qui peut aider à :
    - Détecter et prévenir les comportements malveillants.
    - Analyser les actions pour améliorer l'application.

3. Gestion des sessions : 
    Implémenter un système de rafraîchissement des tokens, Ajouter des délais d'expiration plus fins pour les tokens d'accès et de rafraîchissement

4. Dans l'environnement de production, on utilise normalement un serveur WGSI comme Guinicorn, mais c'est un application légere donc je n'ai pas mettre en place cela.

5. Gestion d'utilisateur : Mettre en place des fonctionnalités comme réinitialiser leur mot de passe en cas d'oubli, ajouter des rôles supplémentaires, implémenter l'authentification à deux facteurs pour la sécurité




### Tester API
Accédez à la documentation Swagger de l'API via : `/swagger`

si vous souhaitez tester avec une BDD vide, supprimez jouerflux.db dans instance et accedez à `/`, il réinitialiser la BDD et ajouter un example de firewall.

Comment connecter 
`Bearer <copy_your_token>`


