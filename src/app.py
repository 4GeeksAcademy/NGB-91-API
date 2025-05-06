import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ID ARTISTA:

amadeus = '67gijcaeSFEAdDBqytOqTX'
artist_info = spotify.artist(amadeus)
print(artist_info)

artist_id = amadeus
top_tracks = spotify.artist_top_tracks(artist_id, country='ES')

# TOP 10 CANCIONES MÁS POPULARES:

for i, track in enumerate(top_tracks['tracks'][:10], start=1):
    name = track['name']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    duration_min = round(duration_ms/60000, 2)
    print(f"{i}. {name}(Popularidad: {popularity}) - Duración: {duration_min} min")

songs_info = []

for track in top_tracks['tracks'][:10]:
    songs_dictionary = {
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': round(track['duration_ms'] / 60000, 2)
    }
    
    songs_info.append(songs_dictionary)

df = pd.DataFrame(songs_info)

# TOP 3 CANCIONES:

df_sorted = df.sort_values(by='popularity', ascending=True)

print("Top 3 Canciones más populares de Amadeüs")
print(df_sorted.head(3))

# ANALISIS DE POPULARIDAD EN RELACIÓN A LA DURACIÓN:

df['top'] = range(1, len(df) + 1)

plt.figure(figsize=(8, 5))
plt.scatter(df['duration_min'], df['popularity'], color='indigo', edgecolors='black')

# AÑADIR EL TITULO DE LA CANCIÓN AL GRÁFICO:

for i, row in df.iterrows():
    plt.text(row['duration_min'] + 0.02, row['popularity'], row['name'], fontsize=8)

plt.xlabel('Duración de la canción (minutos)')
plt.ylabel('Popularidad')
plt.title("Relación de la duración de la canción con la popularidad de la misma")
plt.grid(True)
plt.tight_layout()
plt.show()

Este grupo se caracteríza por sus canciones de más de 4 minutos, por lo que en su caso la popularidad de sus canciones no viene dada por la duración de las mismas; aunque si hay que añadir, que su canción más escuchada actualmente es de más 8 minutos de duración. 

Este grupo llevaba más de diez años inactivo, por lo que las tres canciones que superan los 8 minutos de duración, pertenecen a su último álbum; por lo que su ranking en el TOP 10 se debe en gran parte, no sólo a que son obras maestras que muestran la madurez del compositor, sino también a la novedad y el fin de la espera por las nuevas obras. 
