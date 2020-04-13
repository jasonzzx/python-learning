import pyautogui, time

time.sleep(3)
pyautogui.hotkey('ctrl', 'esc')
pyautogui.typewrite('notepad', 0.5)
time.sleep(2)
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.moveTo(300, 300, duration=0.5)
pyautogui.click()
pyautogui.typewrite("Hello World Jason!!", 0.5)

