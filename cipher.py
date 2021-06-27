# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 21:16:51 2021

@author: Cairo
"""


def cipher(text, switch_amount, operation):
    # Text can be switched up to 94 positions, if the switch_amount is greater
    # than 94, it needs to be brought back to the start. Ex.: switch by 95 is
    # the same as switching by 1.
    if switch_amount > 94:
        switch_amount %= 94

    # If the operation is 'decode' then it should move backwards
    if operation == 'decode':
        switch_amount *= (-1)
    
    output_text = ""
    
    for char in text:
        if (ord(char) < 32) or (ord(char) > 126): # Only chars from 32 to 126 in the ASCII table are to be encrypted
            output_text += char
            continue
        
        position = ord(char) + switch_amount
        
        if position < 32: # trying to access a position lower than 32
            position += 95
        elif position > 126:
            position -= 95
            
        output_text += chr(position)
        
    print('Done!')
    print()
    return output_text

# text = input('text ')
# switch = int(input('switch '))
# operation = input('operation ').lower()

# print(cipher(text, switch, operation))