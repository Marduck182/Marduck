import requests

r = requests.get(f'https://api.deezer.com/album/{199312252}')
preview_url = ''
title = 'Str8 To North-East Lights'
data = r.json()
songs = data['tracks']['data']

for song in songs:
    if song['title_short'].lower() == title.lower():
        preview_url = song['preview']



print(preview_url)


