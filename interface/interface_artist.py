class Artist_Data:
    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    nb_album: int
    nb_fan: int
    radio: bool
    tracklist: str
    type: str

    def __init__(self, id: int, name: str, link: str, share: str, picture: str, picture_small: str, picture_medium: str, picture_big: str, picture_xl: str, nb_album: int, nb_fan: int, radio: bool, tracklist: str, type: str) -> None:
        self.id = id
        self.name = name
        self.link = link
        self.share = share
        self.picture = picture
        self.picture_small = picture_small
        self.picture_medium = picture_medium
        self.picture_big = picture_big
        self.picture_xl = picture_xl
        self.nb_album = nb_album
        self.nb_fan = nb_fan
        self.radio = radio
        self.tracklist = tracklist
        self.type = type
