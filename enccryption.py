def char_to_binary(list_of_chars):
    encrypted_list=[]
    for char in list_of_chars:
        encrypted_char=bin(ord(char))
        encrypted_list.append(encrypted_char)
    return encrypted_list
lst=['a','v','i']
binary_lst=char_to_binary(lst)
''.join(binary_lst)
print(','.join(binary_lst))

