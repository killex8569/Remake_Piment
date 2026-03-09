# Remake_Piment

## Contexte
Piment est un projet de développement d'application initialement réalisé par les étudiants BTS SIO filière SLAM à l'Institution des Chartreux. 
En filière SISR à l'époque, je n'ai pas eu à le développer. 
Je réalise donc ce projet __**en autonomie et sur mon temps libre**__, en suivant le même cahier des charges d'origine, sans contrainte de délai imposée

## Contraintes d'architecture & bonnes pratiques

- Architecture MVC
- DAO
- Controllers
- Filtrage
- Routeurs
- Render
- Sécurité
- CI/CD
- RBAC
- Singloton
- Réaliser un diagramme UML
- Ajout de Doxgyène
- PHPUnit
- Contruit en PHP Natif sur une base de donnée mariaDB et pour le frontend en React


## En plus dans le projet 

Ma valeur ajouter : 
- Chaque pompier aura un équipement / matériel
- Chaque pompier pourras partir pour une ou plusieurs interventions (genre 1 à la fois mais il peut en faire plusieurs dans la journée)
- Chaque pompier à un planning et un grade (8h 17h et grade : chef, sous chef, pompier, colonnel, assistance téléphonique, spécialiste incendie etc...)
- Chaque pompier peut participer à une ou plusieurs formations dans l'année
- Pour le RBAC: Il y aura trois niveau de privilège : Utilisateur (les pompier), assistance/direction (c'est eux qui définisse les grade, les emplois du temps et les formations sur l'application ou encore si ils sont en missions aujourd'hui ou pas) et enfin l'admin (qui à les droits suprême)
