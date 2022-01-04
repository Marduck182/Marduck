from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np
from Deezer import Album, Playlist
from interface.interface_playlist import Song_Playlist


def efect(data: Playlist | Album):
    if type(data) == Playlist:
        for song in data.list_song:
            efect_one_playlist(song)
    elif type(data) == Album:
        efecto_one_album(data)


def efecto_one_album(album: Album):
    img_cover = Image.fromarray(album.img_cover)
    img_cover_resize = img_cover.resize((660, 660))
    img_background = ReduceOpacity(img_cover, 0.3)

    img_artist = Image.fromarray(album.img_artist)
    img_artist_crop = crop_artist(img_artist)

    img_background.paste(img_cover_resize, (170, 80))
    img_background.paste(img_artist_crop, (50, 760), mask=img_artist_crop)

    font = ImageFont.truetype(
        './fonts/MarcellusSC-Regular.ttf', 33, encoding="unic")

    for song in album.songs:
        img_copy = img_background.copy()

        draw = ImageDraw.Draw(img_copy)
        draw.text((275, 780), f'{album.artist_name}', 'white', font)
        draw.text((275, 830), f'{song.index:02} - {song.title }', 'white', font)
        draw.text((275, 880), f'{album.title }', 'white', font)
        # img_final = img_copy.convert('RGB')
        # img_final.save(f'{song.id}.jpg')
        song.set_img_cover(np.array(img_copy))


def efect_one_playlist(song: Song_Playlist):
    img_cover = Image.fromarray(song.img_cover)
    img_cover_resize = img_cover.resize((660, 660))
    img_background = ReduceOpacity(img_cover, 0.3)

    img_artist = Image.fromarray(song.img_artist)
    img_artist_crop = crop_artist(img_artist)

    img_background.paste(img_cover_resize, (170, 80))
    img_background.paste(img_artist_crop, (50, 760), mask=img_artist_crop)

    font = ImageFont.truetype(
        './fonts/MarcellusSC-Regular.ttf', 33, encoding="unic")

    draw = ImageDraw.Draw(img_background)
    draw.text((275, 780), f'{song.artist}', 'white', font)
    draw.text((275, 830), f'{song.title }', 'white', font)
    draw.text((275, 880), f'{song.album }', 'white', font)
    song.set_img_cover(np.array(img_background))


def ReduceOpacity(img, opacity: float):
    new_img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 255))
    assert opacity >= 0 and opacity <= 1
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    else:
        img = img.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    img.putalpha(alpha)
    new_img.paste(img, (0, 0), mask=img)
    new_img = new_img.filter(ImageFilter.BLUR)
    return new_img


def crop_artist(img):
    npImage = np.array(img)
    h, w = img.size
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    npAlpha = np.array(alpha)
    npImage = np.dstack((npImage, npAlpha))
    art = Image.fromarray(npImage)
    art = art.resize((200, 200))
    art = art.convert('RGBA')
    return art
