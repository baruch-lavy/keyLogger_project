from pynput.keyboard import Listener, Key
from datetime import datetime
filename = f"keyboard_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
def on_press(key):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(key.char)
    except AttributeError:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"[{key}]")
def on_release(key):
    if key == Key.esc:
        print("יציאה מהתוכנה")
        return False  # עוצר את ההאזנה
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()