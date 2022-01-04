from Deezer import Album, Playlist
from efects import efect
from resources import donwload_album, download_playlist
from video import create_video
from args import args
from colorama import Fore, Style


if __name__ == '__main__':

    if args.test:
        playlist = Playlist(args.playlist)
        for song in playlist.list_song:
            if song.preview_url == '':
                print(Fore.RED + f'[SONG]: {song.id} -{song.title} - {song.artist}' + Style.RESET_ALL)
            
    else:
        if not args.playlist == None: 
            playlist = Playlist(args.playlist)
            download_playlist(playlist)
            efect(playlist)
            create_video(playlist)

        elif not args.album == None:
            album = Album(args.album)
            donwload_album(album)
            efect(album)
            create_video(album)
            

