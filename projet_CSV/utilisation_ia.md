# Rapport sur l’utilisation des outils d’IA

## 1. **Outils utilisés**
### **ChatGPT**
J'ai utilisé **ChatGPT** pour différentes étapes du projet :
- **Génération d’idées pour la base de données** : ChatGPT m’a aidé à définir les colonnes à inclure dans les tables de la base de données. Par exemple, des suggestions pour les champs comme `nom_produit`, `description`, `quantité`, et `prix_unitaire` ont été utiles pour organiser les tables *produits*, *départements*, et *fournisseurs*.
- **Création de fichiers CSV** : L'IA a été utilisée pour générer rapidement des jeux de données réalistes pour remplir les fichiers CSV nécessaires à l'application.
- **Mise en forme et refactorisation du code** : ChatGPT a permis de réorganiser mon code pour le rendre plus propre et lisible, tout en respectant les bonnes pratiques de développement.

### **PyCharm** (Auto-complétion)
L’auto-complétion et les outils intégrés de **PyCharm** ont grandement facilité le développement :
- **Suggestions intelligentes** : L’auto-complétion m’a permis d'écrire plus rapidement du code en proposant des noms de variables, méthodes, et classes.
- **Réduction des erreurs** : PyCharm a minimisé les fautes de syntaxe et les oublis grâce à ses alertes en temps réel.
- **Navigation fluide** : PyCharm a facilité la gestion et l’accès aux différents fichiers du projet comme `Menu.py`, `CrudManager.py`, et `Database.py`.

## 2. **Création et tests unitaires**
ChatGPT a joué un rôle clé dans la rédaction des tests unitaires :
- **Méthodes principales** : Les tests pour `_verifier_produit_vendu` et `_calculer_total_quantite` ont été générés avec des outils comme `unittest` et `mock`. Cela a permis de couvrir les cas normaux, limites et d’erreurs.
- **Rechargement de la base de données** : J'ai également obtenu des exemples pour tester la fonctionnalité `--reload` qui permet de réinitialiser la base de données.

### **Exemple de test**  
Un exemple simple généré pour tester le menu interactif :
```python
@patch('builtins.input', side_effect=["1"])
def test_afficher_menu_option_1(self, mock_input):
    self.menu.afficher_menu()
    self.mock_crud_manager.afficher_toutes_entites.assert_called_once_with('departments')
