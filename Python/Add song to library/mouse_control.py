import pyautogui as pyg
import time


sleeptime = 0.3

def add_song_to_list():
    pyg.moveTo(-1559, 127)
    pyg.click()
    time.sleep(0.7)
    pyg.moveTo(-555, 260)
    pyg.click()
    time.sleep(sleeptime)
    pyg.moveTo(-555, 630)
    pyg.click()
    time.sleep(sleeptime)
    pyg.moveTo(-1387, 650)
    pyg.click()

