import json
import numpy as np
import os
import requests
from collections import namedtuple
from colorama import Fore, Style
from Deezer import Album, Playlist
from interface.interface_album import Song_Album
from interface.interface_artist import Artist_Data
from interface.interface_playlist import Song_Playlist
from PIL import Image



def download_playlist(playlist: Playlist):

    create_path(playlist.path)

    for song in playlist.list_song:
        song.set_img_cover(download_cover(song.cover))
        song.set_img_artist(download_photo(song.artist_url))
        donwload_songs(song, playlist.path)


def donwload_album(album: Album):
    create_path(album.path)
    album.set_img_artist(download_cover(album.artist_url))
    album.set_img_cover(download_cover(album.cover_url))

    for song in album.songs:
        donwload_songs(song, album.path)


def create_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def donwload_songs(song: Song_Album | Song_Playlist, path: str):
    if song.preview_url == '':
        print(Fore.RED + f'[SONG]: {song.id} -{song.title}' + Style.RESET_ALL)

    else:
        r = requests.get(song.preview_url, stream=True)
        if(r.status_code):
            print(Fore.GREEN + song.title + Style.RESET_ALL)
            with open(f'{path}/{song.id}.mp3', 'wb') as f:
                f.write(r.content)
                f.close()
        else:
            print(Fore.RED + f'[SONG]: {song.title}' + Style.RESET_ALL)



def download_cover(url: str):
    img = Image.open(requests.get(url, stream=True).raw)
    return np.array(img)


def download_photo(artist_url: str):
    artist_url = artist_url.replace('www', 'api')
    r = requests.get(artist_url)
    if r.status_code == 200:
        artist_data: Artist_Data = json.loads(
            r.text, object_hook=lambda d: namedtuple('Artist_Data', d.keys())(*d.values()))
        img = Image.open(requests.get(
            artist_data.picture_medium, stream=True).raw)
        return np.array(img)
