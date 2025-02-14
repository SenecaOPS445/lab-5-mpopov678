#!/usr/bin/env python3
# Author ID: mpopov

def read_file_string(file_name):
    f = open('/home/mpopov/ops445/lab5/'+file_name, 'r')
    r = f.read()
    f.close()
    return(r)
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open('/home/mpopov/ops445/lab5/'+file_name, 'r')
    r = f.readlines()
    f.close()
    r = [line.strip() for line in r]
    return(r)
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

def append_file_string(file_name, string_of_lines):
    f = open('/home/mpopov/ops445/lab5/'+file_name, 'a')
    f.write(string_of_lines)
    f.close
    return()
    # Takes two strings, appends the string to the end of the file

def write_file_list(file_name, list_of_lines):
    f = open('/home/mpopov/ops445/lab5/'+file_name, 'w')
    for item in list_of_lines:
        f.write(item + '\n')
    f.close
    return()
    # Takes a string and list, writes all items from list to file where each item is one line

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f = open('/home/mpopov/ops445/lab5/'+file_name_read, 'r')
    f1 = f.readlines()
    f2 = open('/home/mpopov/ops445/lab5/'+file_name_write, 'w')
    x = 0
    for line in f1:
        x = x + 1
        f2.write(str(x) +":"+line)
    f.close()
    f2.close
    return()
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

