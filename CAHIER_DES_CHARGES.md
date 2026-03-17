---
title: "Cahier des Charges — Remake Piment"
subtitle: "Application de gestion de casernes de pompiers"
author: "Projet personnel — École d'ingénieur"
date: "Mars 2026"
---

# Cahier des Charges — Remake Piment

**Application de gestion de casernes de pompiers**  
Version 1.0 — Mars 2026

---

## 1. Présentation du projet

### 1.1 Contexte

*Piment* est un projet de développement d'application web initialement réalisé par les étudiants de BTS SIO filière SLAM à l'Institution des Chartreux. En filière SISR à l'époque, ce projet ne faisait pas partie du programme. Ce document décrit la réalisation personnelle de ce projet, sur temps libre, en suivant le cahier des charges d'origine, sans contrainte de délai imposée.

### 1.2 Objectif général

Développer une application web complète permettant de **gérer de A à Z une ou plusieurs casernes de pompiers** : structure organisationnelle, ressources humaines, parc de véhicules, équipements, interventions, plannings et formations.

### 1.3 Périmètre

Le projet couvre :

- La gestion des entités métier (casernes, pompiers, véhicules, interventions, plannings, formations, équipements)
- Un système d'authentification et de contrôle d'accès basé sur les rôles (RBAC)
- Une API REST en PHP natif
- Une interface utilisateur en React
- Des tests unitaires et une documentation technique complète

---

## 2. Spécifications fonctionnelles

### 2.1 Entités métier

#### Caserne
- Identifiant unique
- Nom, adresse, numéro de département
- Peut contenir plusieurs pompiers et plusieurs véhicules
- Un pompier et un véhicule ne peuvent appartenir qu'à une seule caserne

#### Pompier
- Identifiant unique
- Nom, prénom, date de naissance, numéro de matricule
- Affecté à **une seule caserne**
- Possède **un seul grade** à la fois (modifiable par l'Assistance ou l'Admin)
- Peut participer à des interventions, formations et être planifié sur des gardes
- Dispose d'un compte utilisateur avec un rôle

#### Grade
- Identifiant unique
- Libellé (ex : Sapeur, Caporal, Sergent, Lieutenant, Capitaine…)
- Associé à un ou plusieurs pompiers

#### Véhicule
- Identifiant unique
- Immatriculation, modèle, type (voiture légère, camion citerne, ambulance légère, VSAV…)
- Affecté à **une seule caserne**
- Peut être affecté à des interventions
- Peut porter des équipements

#### Équipement
- Identifiant unique
- Désignation, quantité, état
- Peut être associé à un véhicule et/ou à un pompier

#### Intervention / Mission
- Identifiant unique
- Libellé, type d'intervention, date et heure, adresse
- Statut (planifiée, en cours, terminée)
- Liste de pompiers affectés
- Liste de véhicules affectés

#### Planning / Garde
- Identifiant unique
- Pompier concerné, date, heure de début, heure de fin
- Type (garde de jour, garde de nuit, astreinte)
- Créé et modifié par l'Assistance ou l'Admin

#### Formation / Certification
- Identifiant unique
- Intitulé, organisme, date, durée
- Pompiers inscrits avec statut de participation (inscrit, validé, échoué)

---

### 2.2 Gestion des rôles (RBAC)

L'application distingue trois rôles utilisateur.

#### ROLE_USER (Pompier)

Accès en **lecture seule** sur ses propres données :

- Consultation de son profil (nom, grade, caserne)
- Consultation de son planning personnel
- Consultation de ses interventions passées et à venir
- Consultation de ses formations

#### ROLE_ASSISTANCE

Accès étendu en **lecture/écriture** sur les données opérationnelles :

- Tout ce que ROLE_USER peut faire
- Création et modification des plannings de tous les pompiers
- Affectation des pompiers aux formations (inscription, mise à jour du statut)
- Création et modification des interventions
- Affectation des pompiers et véhicules aux interventions
- Modification du grade d'un pompier
- Consultation de toutes les fiches pompiers et véhicules

#### ROLE_ADMIN

**Accès total** à l'ensemble de l'application :

- Tout ce que ROLE_ASSISTANCE peut faire
- Création, modification, suppression des casernes
- Création, modification, suppression des pompiers
- Création, modification, suppression des véhicules
- Gestion des équipements
- Création et modification des grades
- Gestion des comptes utilisateurs (création, attribution de rôle, désactivation)
- Consultation des logs et statistiques globales

---

### 2.3 Fonctionnalités par module

#### Module Authentification
- Inscription (par un Admin uniquement)
- Connexion avec email + mot de passe
- Déconnexion
- Gestion de session par JWT
- Rafraîchissement du token

#### Module Casernes
- Lister toutes les casernes (Admin)
- Créer / modifier / supprimer une caserne (Admin)
- Consulter le détail d'une caserne avec ses pompiers et véhicules

#### Module Pompiers
- Lister les pompiers d'une caserne
- Créer / modifier / supprimer un pompier (Admin)
- Affecter un pompier à une caserne (Admin)
- Modifier le grade d'un pompier (Admin, Assistance)
- Consulter la fiche d'un pompier

#### Module Véhicules
- Lister les véhicules d'une caserne
- Créer / modifier / supprimer un véhicule (Admin)
- Affecter un véhicule à une caserne (Admin)
- Consulter la fiche d'un véhicule

#### Module Interventions
- Lister les interventions (toutes ou filtrées par caserne/date/statut)
- Créer / modifier / supprimer une intervention (Admin, Assistance)
- Affecter des pompiers et véhicules à une intervention (Admin, Assistance)
- Changer le statut d'une intervention (Admin, Assistance)

#### Module Planning
- Afficher le planning d'un pompier (semaine/mois)
- Créer / modifier / supprimer un créneau de garde (Admin, Assistance)
- Vue globale du planning d'une caserne (Admin, Assistance)
- Lecture seule du planning personnel (User)

#### Module Formations
- Lister les formations disponibles
- Créer / modifier / supprimer une formation (Admin)
- Inscrire un pompier à une formation (Admin, Assistance)
- Mettre à jour le statut de participation (Admin, Assistance)
- Consulter le parcours de formation d'un pompier

#### Module Équipements
- Lister les équipements
- Créer / modifier / supprimer un équipement (Admin)
- Associer un équipement à un véhicule ou un pompier (Admin)

---

## 3. Spécifications techniques

### 3.1 Architecture générale

L'application suit une architecture **client-serveur** :

- **Backend** : API REST en PHP natif, exposant des endpoints JSON
- **Frontend** : Single Page Application (SPA) React, consommant l'API
- **Base de données** : MariaDB

### 3.2 Architecture backend — MVC + DAO

```
backend/
├── public/
│   └── index.php          ← Point d'entrée unique (Front Controller)
├── src/
│   ├── Core/
│   │   ├── Database.php   ← Singleton de connexion PDO
│   │   ├── Router.php     ← Routeur HTTP
│   │   └── App.php        ← Bootstrap de l'application
│   ├── Controllers/       ← Contrôleurs MVC (un par module)
│   ├── Models/            ← Entités PHP (mapping objet)
│   ├── DAO/               ← Accès aux données (requêtes SQL PDO)
│   ├── Middleware/
│   │   ├── AuthMiddleware.php   ← Vérification JWT
│   │   ├── RbacMiddleware.php   ← Contrôle des rôles
│   │   └── FilterMiddleware.php ← Validation et filtrage des inputs
│   └── Security/
│       ├── JwtManager.php
│       └── PasswordManager.php
├── tests/                 ← Tests PHPUnit
├── docs/                  ← Documentation Doxygen
├── composer.json
└── .env
```

#### Pattern MVC
- **Modèle** : classe PHP représentant une entité (propriétés + getters/setters)
- **DAO** : classe dédiée aux requêtes SQL via PDO (séparation totale de la logique métier)
- **Controller** : reçoit la requête HTTP, appelle le DAO, retourne une réponse JSON

#### Singleton
- La connexion à la base de données est gérée par un Singleton `Database::getInstance()` pour garantir une instance unique de PDO

#### Routeur
- Routes déclarées explicitement (méthode HTTP + URI)
- Support des paramètres dynamiques dans les URI (ex : `/api/pompiers/{id}`)
- Dispatch vers le controller et la méthode appropriés

#### Filtrage
- Validation de chaque paramètre entrant (type, longueur, format)
- Assainissement avant toute utilisation en base de données
- Retour d'erreurs HTTP 422 avec détail des champs invalides

### 3.3 Sécurité

| Menace | Contre-mesure |
|---|---|
| Injection SQL | Requêtes préparées PDO exclusivement |
| XSS | Échappement de toutes les sorties (htmlspecialchars) |
| CSRF | Token CSRF sur toutes les mutations d'état |
| Vol de mot de passe | `password_hash()` / `password_verify()` (bcrypt) |
| Accès non autorisé | JWT + RBAC vérifié côté serveur sur chaque route |
| Exposition de données | Réponses filtrées selon le rôle de l'appelant |
| Headers HTTP | CSP, X-Frame-Options, X-Content-Type-Options |

### 3.4 Authentification — JWT

- Génération d'un token JWT signé à la connexion (payload : id utilisateur, rôle, expiration)
- Transmis dans le header `Authorization: Bearer <token>`
- Vérifié par le middleware auth sur chaque route protégée
- Expiration configurée (ex : 1h), avec mécanisme de refresh token

### 3.5 Architecture frontend — React

```
frontend/
├── src/
│   ├── components/        ← Composants réutilisables (boutons, formulaires, tableaux…)
│   ├── pages/             ← Une page par module
│   ├── services/          ← Appels API Axios (un service par module)
│   ├── context/
│   │   └── AuthContext.jsx ← Contexte global d'authentification
│   ├── hooks/             ← Hooks personnalisés
│   └── router/            ← Routes React Router avec protection par rôle
└── package.json
```

- **Routing** : React Router v6 avec routes protégées (PrivateRoute selon le rôle)
- **Requêtes API** : Axios avec intercepteurs (ajout du JWT, gestion des erreurs 401/403)
- **État global** : Context API (authentification + rôle)
- **UI** : composants maison ou bibliothèque légère (TailwindCSS recommandé)

### 3.6 Base de données — MariaDB

Principales tables prévues :

| Table | Description |
|---|---|
| `casernes` | Casernes de pompiers |
| `grades` | Grades disponibles |
| `pompiers` | Pompiers (FK caserne, FK grade) |
| `utilisateurs` | Comptes utilisateurs (FK pompier, rôle) |
| `vehicules` | Véhicules (FK caserne, type) |
| `equipements` | Équipements |
| `equipement_pompier` | Association équipement ↔ pompier |
| `equipement_vehicule` | Association équipement ↔ véhicule |
| `interventions` | Interventions / missions |
| `intervention_pompier` | Affectation pompier ↔ intervention |
| `intervention_vehicule` | Affectation véhicule ↔ intervention |
| `plannings` | Créneaux de garde |
| `formations` | Formations disponibles |
| `formation_pompier` | Inscription pompier ↔ formation + statut |

### 3.7 Tests — PHPUnit

- **Tests unitaires** sur chaque classe DAO (mocking de PDO)
- **Tests unitaires** sur les modèles et la logique de validation
- **Tests d'intégration** sur les routes API (avec base de données de test dédiée)
- Objectif de couverture : > 70 % du backend
- Exécution automatique dans le pipeline CI

### 3.8 Documentation — Doxygen

- Toutes les classes et méthodes PHP documentées avec :
  - `@brief` description courte
  - `@param` pour chaque paramètre
  - `@return` pour la valeur de retour
  - `@throws` pour les exceptions possibles
- Génération automatique de la documentation HTML via `doxygen Doxyfile`
- Documentation des routes API dans des fichiers Markdown dédiés

### 3.9 CI/CD

Pipeline GitHub Actions (ou GitLab CI) déclenché à chaque push/PR :

1. **Lint** : vérification du style PHP (phpcs / PSR-12)
2. **Tests** : exécution de la suite PHPUnit
3. **Build frontend** : `npm run build`
4. **Déploiement** (branche main uniquement) : push sur le serveur cible via SSH

---

## 4. Contraintes et non-objectifs

### 4.1 Contraintes techniques obligatoires
- PHP natif (aucun framework PHP type Laravel/Symfony)
- MariaDB comme seul SGBD
- Architecture MVC + DAO strictement respectée
- Pattern Singleton pour la connexion BDD
- RBAC implémenté et vérifié côté serveur
- Diagrammes UML produits avant le développement
- Documentation Doxygen complète
- Tests PHPUnit présents

### 4.2 Non-objectifs (hors périmètre)
- Application mobile native
- Notifications push en temps réel (WebSockets)
- Module de comptabilité / budget
- Intégration avec des systèmes d'alarme réels
- Multilingue

---

## 5. Livrables attendus

| Livrable | Format |
|---|---|
| Code source backend | PHP (dépôt Git) |
| Code source frontend | React / JavaScript (dépôt Git) |
| Scripts de migration BDD | SQL |
| Diagramme de classes UML | PlantUML ou draw.io |
| Diagramme entité-relation | PlantUML ou draw.io |
| Documentation Doxygen | HTML généré |
| Documentation API | Markdown |
| Suite de tests PHPUnit | PHP |
| Pipeline CI/CD | YAML (GitHub Actions) |
| README complet | Markdown |
| Cahier des charges | Ce document |

---

## 6. Glossaire

| Terme | Définition |
|---|---|
| MVC | Model-View-Controller — patron d'architecture séparant données, logique et présentation |
| DAO | Data Access Object — couche d'abstraction des accès à la base de données |
| RBAC | Role-Based Access Control — contrôle d'accès basé sur les rôles |
| JWT | JSON Web Token — mécanisme d'authentification sans état par token signé |
| SPA | Single Page Application — application web à page unique |
| PDO | PHP Data Objects — couche d'abstraction d'accès aux bases de données en PHP |
| CI/CD | Continuous Integration / Continuous Deployment — automatisation des tests et du déploiement |
| PSR | PHP Standards Recommendation — standards de codage PHP interopérables |
