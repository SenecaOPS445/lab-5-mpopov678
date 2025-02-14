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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

