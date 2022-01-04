from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
from Deezer import Album, Playlist
import os
from variables import USERPROFILE



def create_video(data: Playlist | Album):
   
    if(type(data) == Playlist):
        list_song = data.list_song
    elif(type(data) == Album):
        list_song = data.songs
    else:
        return

    list_video = []
    for song in list_song:
        audio_clip = AudioFileClip(f'{data.path}/{song.id}.mp3')
        image_clip = ImageClip(song.img_cover)
        video_clip = image_clip.set_audio(audio_clip)
        video_clip.duration = audio_clip.duration
        video_clip.fps = 1

        list_video.append(video_clip)

    final_clip = concatenate_videoclips(list_video)




    if not os.path.exists(f'{USERPROFILE}/Documents/Marduck'):
        os.mkdir(f'{USERPROFILE}/Documents/Marduck')
    final_clip.write_videofile(f'{USERPROFILE}/Documents/Marduck/{data.id}.mp4')
