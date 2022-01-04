import json
import requests
import json
from interface.interface_album import Album_Data, Song_Album
from interface.interface_playlist import Playlist_Data, Song_Playlist
from collections import namedtuple
import numpy as np

from variables import TEMP


class Album:

    def __init__(self, id: str) -> None:
        self.id = id
        self.path = f'{TEMP}/{id}'
        self.get_data()

    def get_data(self) -> None:
        r = requests.get(f'https://api.deezer.com/album/{self.id}')
        album_data: Album_Data = json.loads(
            r.text, object_hook=lambda d: namedtuple('Album_Data', d.keys())(*d.values()))

        self.artist_name = album_data.artist.name
        self.artist_url  = album_data.artist.picture_medium
        self.cover_url   = album_data.cover_xl
        self.title       = album_data.title
        self.songs = [
            Song_Album(track.id, track.preview, track.title_short, index+1)
            for index, track in enumerate(album_data.tracks.data)
        ]

    def set_img_cover(self, array_numpy: np.ndarray):
        self.img_cover = array_numpy

    def set_img_artist(self, array_numpy: np.ndarray):
        self.img_artist = array_numpy


class Playlist:

    def __init__(self, id: str) -> None:
        self.id = id
        self.path = f'{TEMP}/{id}'
        self.get_data()

    def get_data(self) -> None:
        r = requests.get(f'https://api.deezer.com/playlist/{self.id}')
        playlist_data: Playlist_Data = json.loads(
            r.text, object_hook=lambda d: namedtuple('Playlist_Data', d.keys())(*d.values()))

        self.title = playlist_data.title
        self.list_song = [
            Song_Playlist(track.id, track.title_short, track.album.cover_xl,
                          track.artist.name, track.album.title, track.preview, track.artist.link, track.album.id, index+1)
            for index, track in enumerate(playlist_data.tracks.data)
        ]

    

    def __str__(self) -> str:
        return str({
            "id": self.id,
            "title": self.title,
            "list_songs": self.list_song
        })
