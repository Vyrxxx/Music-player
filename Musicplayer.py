from playsound3 import playsound
import easygui
import os
import random
from pytubefix import YouTube
import pygame
from pydub import AudioSegment
pygame.mixer.init()


current_playlist = None
playlist = []

while True:
    
    

    os.path.exists(f"{current_playlist}")
    playlist = [] 
    if os.path.exists(f"{current_playlist}"):
      with open(f"{current_playlist}", "r") as file:
        for line in file:
            playlist.append(line.strip())
    else:
     ignore = True
    os.system("pause")
    os.system("cls")
    option = input("""
========================
       MUSIC PLAYER
========================
0. Import playlist
1. Play local song
2. Download from YouTube
3. Add song to playlist
4. Play playlist
5. View playlist
6. Exit

Choose an option:
""")

    if option == "0":
        playlists = []
        current_playlist = easygui.fileopenbox(title="Select playlist to load", multiple=False)
        for song in playlists:
            print(song)

    if option == "1":
        file_path = easygui.fileopenbox()
        loop = input("Enter the number of times to loop the song (-1 for infinite): ")
        print(f"Playing {file_path}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops=int(loop))

    if option == "2":
        url = input("Enter the url: ")
        yt = YouTube(url)
        print(f"Downloading + {url}")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()

        base, ext = os.path.splitext(out_file)
        new_file = base + ".ogg"

        sound = AudioSegment.from_file(out_file)
        sound.export(new_file, format="ogg")
        os.remove(out_file)
        print(f"Saved as {new_file}")

    if option == "3":
        file_path = easygui.fileopenbox()
        playlist.append(file_path)
        with open(f"{current_playlist}", "w") as file:
           for song in playlist:
             file.write(song + "\n")

    if option == "4":
        random.shuffle(playlist)
        for song in playlist:
            print(f"Playing {song}")
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            pygame.time.wait(int(pygame.mixer.Sound(song).get_length() * 1000))
            
            
            

    if option == "5":
        for song in playlist:
            print(song)

    if option == "6":
        print("Closing...")
        break
