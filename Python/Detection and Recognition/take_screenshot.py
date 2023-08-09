import pyautogui as pyg


asmd = pyg.locateOnScreen("C:/Users/razva/Documents/GitHub/RazvanAToma/python/Detection and Recognition/Screenshot 2023-08-08 212127.png")
print(asmd)

screenshot = pyg.screenshot(region=(1634, 0, 285, 72))
screenshot.show()
