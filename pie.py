import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV en spécifiant le séparateur et le traitement des milliers
df = pd.read_csv("data/2023-12-depenses-décembre.csv", sep=",", thousands=",")

# Grouper les données par catégorie et calculer la somme des montants
data_grouped = df.groupby("catégorie")["montant"].sum()

# Créer le diagramme circulaire
plt.pie(data_grouped, labels=data_grouped.index, autopct="%1.1f%%", startangle=140)
plt.title("Répartition des montants par catégorie")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Afficher le diagramme
plt.show()
