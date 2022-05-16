music_list = [
        {
        "artist": "The Dandy Warhols",
        "song_name":  "Bohemian Like You",
        "genre": "Pop/Rock",
        "release_year": 2000
    },
    {
        "artist": "Rag n Bone Man",
        "song_name": "Arrrow",
        "genre": "Blues",
        "release_year": 2017
    },
    {
    "artist": "Rag n Bone Man",
    "song_name": "Human",
    "genre": "Blues",
    "release_year": 2017
    },
    {
    "artist": "Stereophonics",
    "song_name": "Indian Summer" ,
    "genre": "Pop/Rock",
    "release_year": 2013
    }
]

fave_bands = []

for dict_i in music_list:
    fave_bands.append(list(dict_i.values())[0])

def add_to_list(band):
    fave_bands.append(band)