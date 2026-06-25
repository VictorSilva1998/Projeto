import pyautogui
import time

pyautogui.press('win')

pyautogui.write('mspaint')
pyautogui.press('enter')

time.sleep(2)

pyautogui.moveTo(600, 300)
pyautogui.dragTo(700, 300)
pyautogui.dragTo(700, 400)
pyautogui.dragTo(600, 400)
pyautogui.dragTo(600, 300)