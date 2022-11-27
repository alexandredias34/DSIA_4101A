import folium   # Importation of folium
import pandas as pd   # Importation of pandas

# Reads the data
dfloc = pd.read_csv('carte.csv')
dffiliere = dfloc['filiere'].unique()

# Adds a dot for each location on a folium map
# Changes the color of the dot based on the filiere baded on ['Solaire', 'Hydraulique', 'Eolien', 'Thermique non renouvelable', 'Stockage non hydraulique', 'Bioénergies', 'Nucléaire', 'Energies Marines','Autre']
def color_producer(filiere):
      if filiere == 'Solaire':
         return 'yellow'
      elif filiere == 'Hydraulique':
         return 'blue'
      elif filiere == 'Eolien':
         return 'green'
      elif filiere == 'Thermique non renouvelable':
         return 'orange'
      elif filiere == 'Stockage non hydraulique':
         return 'black'
      elif filiere == 'Bioénergies':
         return 'purple'
      elif filiere == 'Nucléaire':
         return 'red'
      elif filiere == 'Energies Marines':
         return 'white'
      else:
         return 'gray'
     
# Creation of the main map, featuring all energy producers. 
# puismaxinstallee can be accessed through clicking on dots. 
# Circles are colored according to color_producer.
map = folium.Map(location=[48.856614, 2.3522219], zoom_start=12)
for i in range(0,len(dfloc)):
   folium.Circle(
      location=[dfloc.iloc[i]['latitude'], dfloc.iloc[i]['longitude']],
      popup=dfloc.iloc[i]['puismaxinstallee'],
      radius=100,
      color=color_producer(dfloc.iloc[i]['filiere']),
      fill=True,
      fill_color=color_producer(dfloc.iloc[i]['filiere'])
   ).add_to(map)

map.save('map.html')

# Create a function to make a map with the different filieres
def make_map(filiere):
      map = folium.Map(location=[48.856614, 2.3522219], zoom_start=12)
      for i in range(0,len(dfloc)):
         if dfloc.iloc[i]['filiere'] == filiere:
               folium.Circle(
               location=[dfloc.iloc[i]['latitude'], dfloc.iloc[i]['longitude']],
               popup=dfloc.iloc[i]['puismaxinstallee'],
               radius=100,
               color=color_producer(dfloc.iloc[i]['filiere']),
               fill=True,
               fill_color=color_producer(dfloc.iloc[i]['filiere'])
            ).add_to(map)
      return map

# Creates a function that saves the map as different html files for each filiere

def save_map(filiere):
      map = make_map(filiere)
      map.save('map'+filiere+'.html')
      return map


for i in range(0,len(dffiliere)):
      save_map(dffiliere[i])


# Adds a legend to map with the different colors and the filieres they represent
legend_html =   '''
                  <div style="position: fixed;
                  bottom: 50px; left: 50px; width: 400px; height: 500px;
                  border:2px solid grey; z-index:9999; font-size:18px;
                  ">&nbsp; Filieres &nbsp; <br>
                     &nbsp; Solaire &nbsp; <i class="fa fa-map-marker fa-2x" style="color:yellow"></i><br>
                     &nbsp; Hydraulique &nbsp; <i class="fa fa-map-marker fa-2x" style="color:blue"></i><br>
                     &nbsp; Eolien &nbsp; <i class="fa fa-map-marker fa-2x" style="color:green"></i><br>
                     &nbsp; Thermique non renouvelable &nbsp; <i class="fa fa-map-marker fa-2x" style="color:orange"></i><br>
                     &nbsp; Stockage non hydraulique &nbsp; <i class="fa fa-map-marker fa-2x" style="color:black"></i><br>
                     &nbsp; Bioenergies &nbsp; <i class="fa fa-map-marker fa-2x" style="color:purple"></i><br>
                     &nbsp; Nucleaire &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i><br>
                     &nbsp; Energies Marines &nbsp; <i class="fa fa-map-marker fa-2x" style="color:white"></i><br>
                     &nbsp; Autre &nbsp; <i class="fa fa-map-marker fa-2x" style="color:gray"></i><br>
                  </div>
                  '''
map.get_root().html.add_child(folium.Element(legend_html))
# Save it as html
map.save('map.html')



