# Creation of the dashboard, also used as the main program
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
from PIL import Image # Imports png from the folder
import SortData     #
import Carte        # Importing the other programs, necessary for the dashboard to work.
import Histogramme  #

dfdatageo = pd.read_csv('carte.csv') # Dataframe using the carte.csv data
pil_image = Image.open('Histonuc.png') # Imports Histonuc.png using the PIL library

app = dash.Dash()
server = app.server

# Creates a layout for the dashboard that will display the different maps depending on the label selected. 
# The user can choose the desired map. The map selected in the iframe will be the one selected in the dropdown menu.
# For instance, selecting the label 'Solaire' the Iframe will use mapSolaire.html, selecting the label 'Toutes' will result in the Iframe using  map.html
# The histogram is also displayed.
app.layout = html.Div([
    html.H1("Carte de la répartition des sites de production d'électricité en fonction de leur filière"),
    html.Iframe(id='map', srcDoc=open('map.html', 'r').read(), width='100%', height='750'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Solaire', 'value': 'Solaire'},
            {'label': 'Hydraulique', 'value': 'Hydraulique'},
            {'label': 'Eolien', 'value': 'Eolien'},
            {'label': 'Thermique non renouvelable', 'value': 'Thermique non renouvelable'},
            {'label': 'Stockage non hydraulique', 'value': 'Stockage non hydraulique'},
            {'label': 'Bioénergies', 'value': 'Bioénergies'},
            {'label': 'Nucléaire', 'value': 'Nucléaire'},
            {'label': 'Energies Marines', 'value': 'Energies Marines'},
            {'label': 'Autre', 'value': 'Autre'},
            {'label': 'Toutes', 'value': 'Toutes'}
        ],
        value='Toutes'
    ),

    html.H1('Histogramme du nombre de centrales nucléaires en fonction de leur puissance max installée'),
    html.Img(src=pil_image, style={'width': '100%', 'height': '30%'})
    
    ])

# Creation of a callback for the dropdown menu
@app.callback(
    Output(component_id='map', component_property='srcDoc'),
    [Input(component_id='dropdown', component_property='value')]
)

# Returns the chosen map to be displayed
def update_output_div(input_value):
    if input_value == 'Solaire':
        return open('mapSolaire.html', 'r').read()
    elif input_value == 'Hydraulique':
        return open('mapHydraulique.html', 'r').read()
    elif input_value == 'Eolien':
        return open('mapEolien.html', 'r').read()
    elif input_value == 'Thermique non renouvelable':
        return open('mapThermique non renouvelable.html', 'r').read()
    elif input_value == 'Stockage non hydraulique':
        return open('mapStockage non hydraulique.html', 'r').read()
    elif input_value == 'Bioénergies':
        return open('mapBioénergies.html', 'r').read()
    elif input_value == 'Nucléaire':
        return open('mapNucléaire.html', 'r').read()
    elif input_value == 'Energies Marines':
        return open('mapEnergies Marines.html', 'r').read()
    elif input_value == 'Autre':
        return open('mapAutre.html', 'r').read()
    elif input_value == 'Toutes':
        return open('map.html', 'r').read()

# Putting the dashboard online
if __name__ == '__main__':
    app.run_server(debug=True)
    
