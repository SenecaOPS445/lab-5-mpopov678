#!/usr/bin/env python3
# Author ID: mpopov

def add(number1, number2):
    try:
        return(int(number1) + int(number2))
    except (ValueError):
        return("error: could not add numbers")
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'

def read_file(filename):
    try:
        f = open('/home/mpopov/ops445/lab5/'+filename, 'r')
        return(f.readlines())
    except (FileNotFoundError):
        return("error: could not read file")
    # Read a file, return a list of all lines, if error return string 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception