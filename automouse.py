import pyautogui, time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print(pyautogui.size())

while True:
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.moveTo(800, 100, duration=1)
    pyautogui.moveTo(800, 800, duration=1)
    pyautogui.moveTo(100, 800, duration=1)
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.click()
    time.sleep(3)