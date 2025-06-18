from pynput.keyboard import Key,Listener
def log_to_list():
    lst = []
    def press(key):
        print(f'key pressed: {key}')
        lst.append(key)

    def release(key):
        if key == Key.esc :
            return False
    with Listener(press, release) as logger:
        logger.join()
    print(lst)
log_to_list()