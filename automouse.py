import pyautogui, time, sys

pyautogui.FAILSAFE = True

print("Mouse Move Start. Repeat every 10 seconds.")
try:
    while True:
        pyautogui.moveTo(100, 100, duration=1)
        pyautogui.moveTo(800, 100, duration=1)
        pyautogui.moveTo(800, 800, duration=1)
        pyautogui.moveTo(100, 800, duration=1)
        pyautogui.moveTo(100, 100, duration=1)
        time.sleep(10)
except (pyautogui.FailSafeException, KeyboardInterrupt):
    print("Mouse Move Terminate.")
    sys.exit(0)