'''
CS 210 Project 4
Author: Arnav De
Credits: lab
Even-odd cypher encryption
msg(str) -> str

'''
msg = ''

def encrypt(msg):
    first_half = ''
    second_half = ''
    i = 0
    for ch in msg:
        i += 1
        if i % 2 == 0:
            first_half = first_half + ch
        else:
            second_half = second_half + ch
    
    encrypted = first_half + second_half

    return encrypted

def decrypt(msg):
    second_half = msg[0:(len(msg)//2)]
    first_half = msg[(len(msg)//2):]
    i = 0
    decrypted = ''
    first_half_ch = 0

    for ch in msg:
        if i % 2 == 1:
            decrypted += second_half[first_half_ch - 1]
        else:
            decrypted += first_half[first_half_ch]
            first_half_ch += 1
        i += 1

    return decrypted
        

encrypt(msg)
decrypt(msg)