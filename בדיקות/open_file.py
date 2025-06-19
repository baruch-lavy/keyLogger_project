def mkdir(name_of_file):
    File=open(name_of_file, 'w')
    return File
file=mkdir('test.txt')

def write_to_file(file_name,insert):
    file_name.write(insert)
write_to_file('test.txt','this is a test run \n hope it works')
