# TAL
# Projet TAL : Analyse de relations sémantiques avec JeuxDeMots

## Description
Ce projet vise à analyser des phrases en français pour construire un graphe sémantique représentant des relations linguistiques telles que `r_agent`, `r_patient`, et autres. Le projet utilise l'API JeuxDeMots pour enrichir les données linguistiques et applique des règles définies pour générer des relations sémantiques entre les nœuds du graphe.

---

## Statut actuel
- **Fonctionnalités implémentées :**
  - Tokenisation basique de phrases.
  - Création d'un graphe initial avec des relations `r_succ` pour relier les tokens.
  - Ajout de relations morphosyntaxiques (`r_pos`) à partir de JeuxDeMots.
  - Application de règles pour enrichir le graphe avec des relations comme `r_agent` et `r_patient`.
  - Exportation du graphe en format BRAT pour visualisation.

- **Problèmes connus :**
  - Les relations `r_agent`, `r_patient`, etc., ne sont pas systématiquement générées pour toutes les phrases.
  - Difficulté à généraliser les règles pour des phrases complexes sans une analyse grammaticale avancée.
  - Les types morphosyntaxiques (`GN`, `GV`, etc.) doivent être définis manuellement pour chaque mot.

---

## Étapes suivantes
### 1. Améliorer la détection des relations sémantiques
- **Objectif :** Générer automatiquement des relations `r_agent` et `r_patient` de manière cohérente.
- **Actions :**
  - Implémenter une logique pour détecter les groupes nominaux (`GN`) et les groupes verbaux (`GV`) sans intervention manuelle.
  - Intégrer un système de règles plus robuste pour capturer des relations complexes :
    - Exemple : Ajouter `r_lieu` pour des phrases avec des compléments circonstanciels de lieu.
    - Exemple : Ajouter `r_cible` pour des phrases avec des objectifs explicites.
  - Automatiser la validation des types morphosyntaxiques via une liste ou une bibliothèque linguistique.

### 2. Étendre la couverture linguistique
- **Objectif :** Manipuler des phrases plus variées.
- **Actions :**
  - Traiter des phrases avec des anaphores (e.g., "il", "elle") pour ajouter des relations `r_reference`.
  - Ajouter des règles pour les phrases passives, e.g., "Le fromage est mangé par la souris."

### 3. Optimiser l'interaction avec l'API JeuxDeMots
- **Objectif :** Réduire le temps de traitement et améliorer la qualité des données récupérées.
- **Actions :**
  - Mettre en place un cache robuste pour éviter des appels répétitifs à l'API pour les mêmes mots.
  - Ajouter des vérifications pour gérer les erreurs de l'API, comme les codes d'état 500.

### 4. Tester et valider les résultats
- **Objectif :** S'assurer que les relations ajoutées sont pertinentes.
- **Actions :**
  - Tester le système sur un corpus varié (par exemple, des extraits de textes classiques comme *Vingt mille lieues sous les mers*).
  - Comparer les résultats obtenus avec les relations réelles prévues pour ces textes.
  - Générer des rapports d'évaluation (précision, rappel, F1-score).

---
