def mkdir(name_of_file):
    File=open(name_of_file, 'w')
    return File

file=mkdir('test.txt')
#it can both write to an existing file or make a knew one
def write_in_file(file_name,insert):
    with open(file_name,'a') as f:
        f.write(insert)

write_in_file('test.txt','this is a test run \nhope it works\n')
write_in_file('test2.txt','it dose work!!')