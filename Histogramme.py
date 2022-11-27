from matplotlib import pyplot as plt
import pandas as pd
import warnings

pd.options.mode.chained_assignment = None
warnings.simplefilter("ignore", category=FutureWarning)

# Reads the data
df = pd.read_csv('Data.csv', on_bad_lines='skip', dtype=object)
dfhistonucleaire = df[df['filiere'] == 'Nucléaire']
# Converts puismaxinstallee to float using .loc[row_indexer,col_indexer] = value
dfhistonucleaire.loc[:, 'puismaxinstallee'] = dfhistonucleaire.loc[:, 'puismaxinstallee'].astype(float)

# Saving the puismaxinstallee column in a csv file
ordonnee=dfhistonucleaire['puismaxinstallee']
ordonnee.to_csv('ordonnee')

# Creation of the histogram, using puismaxinstallee (from ordonnee.csv) as the x axis and the number of installations as the y axis.
plt.figure(figsize=(18,5),facecolor='gray',edgecolor='blue')
res = plt.hist(ordonnee, range = (0.8*1000000, max(ordonnee)+100000), color = "brown", bins = 'auto' ,edgecolor='black', linewidth=1.2)
plt.title("Nombre d'installations de production d'énergie nucléaire en fonction de leur puissance maximale installée")
plt.xlabel("Puissance max installée")
plt.ylabel("Nombre d'installations")


# Saves the figure
plt.savefig('Histonuc.png')
