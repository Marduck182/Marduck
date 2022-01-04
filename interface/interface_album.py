from dataclasses import dataclass, field
import numpy as np
from enum import Enum
from typing import Optional, List
from datetime import datetime
from dataclasses import dataclass


class ArtistType(Enum):
    ARTIST = "artist"
    GENRE = "genre"


class Artist:
    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    tracklist: str
    type: ArtistType

    def __init__(self, id: int, name: str, picture: str, picture_small: str, picture_medium: str, picture_big: str, picture_xl: str, tracklist: str, type: ArtistType) -> None:
        self.id = id
        self.name = name
        self.picture = picture
        self.picture_small = picture_small
        self.picture_medium = picture_medium
        self.picture_big = picture_big
        self.picture_xl = picture_xl
        self.tracklist = tracklist
        self.type = type


class Contributor:
    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    radio: bool
    tracklist: str
    type: ArtistType
    role: str

    def __init__(self, id: int, name: str, link: str, share: str, picture: str, picture_small: str, picture_medium: str, picture_big: str, picture_xl: str, radio: bool, tracklist: str, type: ArtistType, role: str) -> None:
        self.id = id
        self.name = name
        self.link = link
        self.share = share
        self.picture = picture
        self.picture_small = picture_small
        self.picture_medium = picture_medium
        self.picture_big = picture_big
        self.picture_xl = picture_xl
        self.radio = radio
        self.tracklist = tracklist
        self.type = type
        self.role = role


class ArtistElement:
    id: int
    name: str
    picture: Optional[str]
    type: ArtistType
    tracklist: Optional[str]

    def __init__(self, id: int, name: str, picture: Optional[str], type: ArtistType, tracklist: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.picture = picture
        self.type = type
        self.tracklist = tracklist


class Genres:
    data: List[ArtistElement]

    def __init__(self, data: List[ArtistElement]) -> None:
        self.data = data


class Md5Image(Enum):
    D8_C270_FBA04_EA091_A66_F6_D406_E5344_FC = "d8c270fba04ea091a66f6d406e5344fc"


class PurpleType(Enum):
    TRACK = "track"


class TracksDatum:
    id: int
    readable: bool
    title: str
    title_version: str
    link: str
    duration: int
    rank: int
    explicit_lyrics: bool
    explicit_content_lyrics: int
    explicit_content_cover: int
    preview: str
    md5_image: Md5Image
    artist: ArtistElement
    type: PurpleType
    title_short: Optional[str]

    def __init__(self, id: int, readable: bool, title: str, title_version: str, link: str, duration: int, rank: int, explicit_lyrics: bool, explicit_content_lyrics: int, explicit_content_cover: int, preview: str, md5_image: Md5Image, artist: ArtistElement, type: PurpleType, title_short: Optional[str]) -> None:
        self.id = id
        self.readable = readable
        self.title = title
        self.title_version = title_version
        self.link = link
        self.duration = duration
        self.rank = rank
        self.explicit_lyrics = explicit_lyrics
        self.explicit_content_lyrics = explicit_content_lyrics
        self.explicit_content_cover = explicit_content_cover
        self.preview = preview
        self.md5_image = md5_image
        self.artist = artist
        self.type = type
        self.title_short = title_short


class Tracks:
    data: List[TracksDatum]

    def __init__(self, data: List[TracksDatum]) -> None:
        self.data = data


class Album_Data:
    id: int
    title: str
    upc: str
    link: str
    share: str
    cover: str
    cover_small: str
    cover_medium: str
    cover_big: str
    cover_xl: str
    md5_image: Md5Image
    genre_id: int
    genres: Genres
    label: str
    nb_tracks: int
    duration: int
    fans: int
    release_date: datetime
    record_type: str
    available: bool
    tracklist: str
    explicit_lyrics: bool
    explicit_content_lyrics: int
    explicit_content_cover: int
    contributors: List[Contributor]
    artist: Artist
    type: str
    tracks: Tracks

    def __init__(self, id: int, title: str, upc: str, link: str, share: str, cover: str, cover_small: str, cover_medium: str, cover_big: str, cover_xl: str, md5_image: Md5Image, genre_id: int, genres: Genres, label: str, nb_tracks: int, duration: int, fans: int, release_date: datetime, record_type: str, available: bool, tracklist: str, explicit_lyrics: bool, explicit_content_lyrics: int, explicit_content_cover: int, contributors: List[Contributor], artist: Artist, type: str, tracks: Tracks) -> None:
        self.id = id
        self.title = title
        self.upc = upc
        self.link = link
        self.share = share
        self.cover = cover
        self.cover_small = cover_small
        self.cover_medium = cover_medium
        self.cover_big = cover_big
        self.cover_xl = cover_xl
        self.md5_image = md5_image
        self.genre_id = genre_id
        self.genres = genres
        self.label = label
        self.nb_tracks = nb_tracks
        self.duration = duration
        self.fans = fans
        self.release_date = release_date
        self.record_type = record_type
        self.available = available
        self.tracklist = tracklist
        self.explicit_lyrics = explicit_lyrics
        self.explicit_content_lyrics = explicit_content_lyrics
        self.explicit_content_cover = explicit_content_cover
        self.contributors = contributors
        self.artist = artist
        self.type = type
        self.tracks = tracks


@dataclass
class Song_Album:
    id: int
    preview_url: str
    title: str
    index: int
    img_cover: np.ndarray = field(init=False)


    def set_img_cover(self, array_numpy: np.ndarray):
        self.img_cover = array_numpy
