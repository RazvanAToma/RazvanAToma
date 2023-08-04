import os
import webbrowser
import time
import pyautogui as pyg
from mouse_control import add_song_to_list

song_name = input("What song do you want to add to your playlist?\n")

artist_name = input("\nWho is the song by?\n")

song = song_name + " " + artist_name

url = "https://music.youtube.com/search?q=" + song

def add_to_playlist():
    webbrowser.open(url)
    time.sleep(3)
    add_song_to_list()
    pyg.hotkey("ctrl", "w")

add_to_playlist()

