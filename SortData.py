import pandas as pd
import numpy as np
import csv

# Reads the data
DataFrameMain = pd.read_csv('Data.csv', on_bad_lines='skip', dtype=object)

# Selects the interesting columns to reduce the data mass.
dfl = DataFrameMain[['codeeicresourceobject','codeinseecommune','commune','codedepartement','departement','coderegion','region','filiere','technologie','puismaxinstallee']]
dfNucleaire = DataFrameMain[DataFrameMain['filiere'] == 'Nucléaire'] # Creates a specific dataframe for the nuclear plants.

# Gets the quantiles of the column "puismaxinstallee" of the dataframe dataframemMain and retrun them in a list.
def getQuantiles(dataframe):
    return dataframe['puismaxinstallee'].quantile([0.25,0.5,0.75]).tolist()

dfgeo = pd.read_csv('geo.csv', on_bad_lines='skip', dtype=object) # Reads the geo csv file, cleaning it. 

# Modifies geo.csv code_commune_INSEE to add a 0 at the beginning of the code if it is a 4 digit number
dfgeo['code_commune_INSEE'] = dfgeo['code_commune_INSEE'].apply(lambda x: '0'+x if len(x) == 4 else x)

# Creates a function to get the latitude and longitude and the codeinseecommune of the city from the geo.csv file
def getLatLong(city):
    df = dfgeo[dfgeo['code_commune_INSEE'] == city]
    if df.empty:
        return np.nan
    else:
        return df.iloc[0]['latitude'],df.iloc[0]['longitude'],df.iloc[0]['code_commune_INSEE'] 

# Creates a dataframe named dfdatageo that combines the longitude and latitude from dfgeo and the codeinseecommune from the Dfl by matching the codeinseecommune from the dfgeo with the code_commune_INSEE from the dfl and keeping only the rows that have a match
dfdatageo = pd.merge(dfl, dfgeo, left_on='codeinseecommune', right_on='code_commune_INSEE', how='inner')

dfdatageo['count'] = dfdatageo.groupby('codeinseecommune')['codeinseecommune'].transform('count') # Gets the number of time each codeinseecommune appears in the dataframe

dfdatageo = dfdatageo.drop_duplicates(subset=['codeinseecommune'], keep='first') # Drops duplicates from dfdatageo

dfcarte = dfdatageo[['codeinseecommune','latitude','longitude','count', 'filiere','puismaxinstallee']] # Selecting the pertinent data for dfcarte

dfcarte = dfcarte.dropna() # Deletes the rows that have a NaN value
dfcarte.to_csv('carte.csv', index=False)  # Saves the dataframe to a csv file

dffiliere = dfcarte['filiere'].unique() # Gets the different filieres

dfHistogramme = DataFrameMain[['filiere','puismaxinstallee']] # Selecting the columns to be used for the histogram
dfHistogramme.to_csv('histogramme.csv', index=False) # Save the dataframe to a csv file


