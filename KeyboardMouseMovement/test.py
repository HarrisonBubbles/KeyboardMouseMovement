import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('alt+shift+s') and pyautogui.position()[1] < 1055:
        pyautogui.move(0, 50)
    elif keyboard.is_pressed('alt+shift+w') and pyautogui.position()[1] > 25:
        pyautogui.move(0, -50)
    elif keyboard.is_pressed('alt+shift+d') and pyautogui.position()[0] < 1895:
        pyautogui.move(50, 0)
    elif keyboard.is_pressed('alt+shift+a') and pyautogui.position()[0] > 25:
        pyautogui.move(-50, 0) 
    elif keyboard.is_pressed('alt+shift+e'):
        pyautogui.click()