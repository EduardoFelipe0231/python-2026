import pyautogui

sites = ['youtube.com', 'facebook.com', 'superlive.com', 'hbomax.com', 'cursoemvideo.com']

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

for site in sites:
    pyautogui.write(site)
    pyautogui.press("enter")
