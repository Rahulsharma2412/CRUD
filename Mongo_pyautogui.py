
import pyautogui

while True:
    a = input('>>>')
    pyautogui.press('win')
    pyautogui.typewrite(a)
    pyautogui.press('enter')
