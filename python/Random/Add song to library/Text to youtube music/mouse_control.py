import pyautogui as pyg
import time


def press_songs_button():
    songs_button_location = pyg.locateCenterOnScreen("C:/Users/razva/Documents/GitHub/RazvanAToma/python/Add song to library/images/songs.png", grayscale=True)

    pyg.moveTo(songs_button_location)

    pyg.click()

    pyg.move(0, 125)


def press_three_dots():
    time.sleep(1)
    three_dots_location = pyg.locateCenterOnScreen("C:/Users/razva/Documents/GitHub/RazvanAToma/python/Add song to library/images/three_dots.png")

    pyg.moveTo(three_dots_location)

    pyg.click()


def press_save_to_playlist():
    time.sleep(0.2)
    save_to_playlist_location = pyg.locateCenterOnScreen("C:/Users/razva/Documents/GitHub/RazvanAToma/python/Add song to library/images/save_to_playlist.png")

    pyg.moveTo(save_to_playlist_location)

    pyg.click()


def press_playlist():
    time.sleep(0.2)
    playlist_location = pyg.locateCenterOnScreen("C:/Users/razva/Documents/GitHub/RazvanAToma/python/Add song to library/images/playlist.png")

    pyg.moveTo(playlist_location)

    pyg.click()


def add_song_to_playlist():
    press_songs_button()
    press_three_dots()
    press_save_to_playlist()
    press_playlist()