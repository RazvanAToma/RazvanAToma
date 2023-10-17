import pyautogui as pyg
import webbrowser
import time
import os
from PIL import Image
import pytesseract

# Open URL
webbrowser.open('http://monkeytype.com')

# Get screenwidth and center 
screenWidth, screenHeight = pyg.size()
print(screenWidth, screenHeight)


# Move mouse to center of screen and click
pyg.moveTo(screenWidth/2, screenHeight/2)
time.sleep(3.5)
pyg.click()

def take_screenshot():
    screenshot_path = "C:/Users/razva/OneDrive - Viken fylkeskommune/Backup/Dokumenter/GitHub/RazvanAToma/python/textscreenshot.png"

    # Check if image already exists, if so delete it and take new
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
        textimage = pyg.screenshot(region=(200,450, 1490, 175))
        textimage.save(screenshot_path)

    # If no image, take screenshot
    else:
        textimage = pyg.screenshot()
        textimage.save(screenshot_path)

take_screenshot()

# Simple image to string
print(pytesseract.image_to_string('textscreenshot.png'))