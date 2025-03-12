# 🧬 Jeu de la Vie de Conway en Python

Ce projet implémente le **Jeu de la Vie** de John Conway en Python. Il s'agit d'un **automate cellulaire** où des cellules évoluent sur une grille selon des règles bien définies. Le programme génère une grille initiale aléatoire et la fait évoluer au fil des générations.

---

## 📌 Fonctionnalités

✅ Génération d'une **grille vide** ou **grille aléatoire** avec un taux de remplissage donné  
✅ Détermination des **voisins** de chaque cellule  
✅ Application des **règles du Jeu de la Vie** pour générer l'état suivant  
✅ **Affichage** de l'évolution du jeu à l'écran sur plusieurs générations  

---

## 📜 Règles du Jeu de la Vie

Le jeu suit les règles suivantes :  
1️⃣ Une cellule **vivante** avec **moins de 2 voisins vivants** meurt (sous-population).  
2️⃣ Une cellule **vivante** avec **2 ou 3 voisins vivants** survit.  
3️⃣ Une cellule **vivante** avec **plus de 3 voisins vivants** meurt (surpopulation).  
4️⃣ Une cellule **morte** avec **exactement 3 voisins vivants** devient vivante (reproduction).  

---

## 🛠️ Installation et Exécution

Aucune bibliothèque externe n'est nécessaire. Vous avez juste besoin de **Python 3**.

### 1️⃣ Installation  

Clonez ce dépôt GitHub sur votre machine :  
```sh
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
