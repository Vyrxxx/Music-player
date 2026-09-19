# libraries
import easygui
import os
import random
from pytubefix import YouTube
import pygame
from pydub import AudioSegment
import customtkinter as ctk
pygame.mixer.init()



current_playlist = None
playlist = []


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# functions
def add_to_playlist():
    global playlist
    file_path = easygui.fileopenbox("Select a song to add to the playlist")
    playlist.append(file_path)
    with open(f"{current_playlist}", "w") as file:
           for song in playlist:
             file.write(song + "\n")
             
def download_youtube_audio():
        url = url_entry.get()
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()

        base, ext = os.path.splitext(out_file)
        new_file = base + ".ogg"

        sound = AudioSegment.from_file(out_file)
        sound.export(new_file, format="ogg")
        os.remove(out_file)

def play_playlist():
            random.shuffle(playlist)
            for song in playlist:
               pygame.mixer.music.load(song)
               pygame.mixer.music.play()
               pygame.window.after(500, check_song_progress)

def select_playlist():
    global current_playlist
    global playlist
    current_playlist = easygui.fileopenbox(title="Select playlist to load", multiple=False)
    playlist = []
    if os.path.exists(current_playlist):
        with open(current_playlist, "r") as file:
            for line in file:
                playlist.append(line.strip())

def select_song():
    file_paths = easygui.fileopenbox()
    global file_path
    file_path = f"{file_paths}"

def play_action():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
def pause_action():
    pygame.mixer.music.pause()
    
def resume_action():
    pygame.mixer.music.unpause()
    
def skip_song():
    pygame.mixer.music.stop()
    play_playlist()


window = ctk.CTk()
window.geometry("400x300")
# buttons
select_btn = ctk.CTkButton(window, text="Select Song", command=select_song, width=60, height=60, corner_radius=30)
select_btn.grid(row=0, column=0, padx=10, pady=10)

play_btn = ctk.CTkButton(window, text="▶", command=play_action, width=60, height=60, corner_radius=30)
play_btn.grid(row=0, column=1, padx=10, pady=10)

pause_btn = ctk.CTkButton(window, text="⏸", command=pause_action, width=60, height=60, corner_radius=30)
pause_btn.grid(row=0, column=2, padx=10, pady=10)

resume_btn = ctk.CTkButton(window, text="↻", command=resume_action, width=60, height=60, corner_radius=30)
resume_btn.grid(row=0, column=3, padx=10, pady=10)

select_playlist_btn = ctk.CTkButton(window, text="Select Playlist", command=select_playlist, width=60, height=60, corner_radius=30)
select_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

play_playlist_btn = ctk.CTkButton(window, text="Play Playlist", command=play_playlist, width=60, height=60, corner_radius=30)
play_playlist_btn.grid(row=0, column=5, padx=10, pady=10)

skip_song_btn = ctk.CTkButton(window, text="Skip Song", command=skip_song, width=60, height=60, corner_radius=30)
skip_song_btn.grid(row=0, column=6, padx=10, pady=10)

download_btn = ctk.CTkButton(window, text="Download YouTube Audio", command=download_youtube_audio, width=60, height=60, corner_radius=30)
download_btn.grid(row=0, column=7, padx=10, pady=10)

url_entry = ctk.CTkEntry(window, placeholder_text="Paste YouTube URL")
url_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

playlistadd_btn = ctk.CTkButton(window, text="Add to Playlist", command =add_to_playlist, width=60, height=60, corner_radius=30)
playlistadd_btn.grid(row=1, column=3, padx=10, pady=10)

window.mainloop()
