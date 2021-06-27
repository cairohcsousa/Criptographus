# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:53:20 2021

@author: Cairo
"""
from logo import logo
from cipher import cipher
import os
import sys

print(logo)


def error_message():
    print('An error has occurred.')
    sys.exit('Exiting now.')


# In this program we will use the ASCII table. More specifically, the values
# from 32 ' ' to 126 '~'.

# Opening the file
got_file = False  # Boolean to exit the while loop when file is opened
try:
    while not got_file:
        filepath = input('Enter the file path or directory: ')
        if os.path.exists(filepath):
            if os.path.isfile(filepath):
                start_file = open(filepath, 'r')
                start_file_content = start_file.read()
                print('File opened!')
                print()
                got_file = True
            elif os.path.isdir(filepath):
                os.chdir(filepath)
        else:
            print('File or directory could not be found.')
            print('Please try again.')
            print()
except:
    error_message()

operation = input('Type anything, or skip, to "encode" the file. '
                  'Type "decode" to decode it.\n')
switch_factor = int(input('Enter the switch factor\n'))

end_text = cipher(start_file_content, switch_factor, operation)
start_file.close()

output_path = input('Enter the desired name of the output file to save it: ')
try:
    end_file = open(output_path, 'w')
    end_file.write(end_text)
    end_file.close()
except:
    error_message()
