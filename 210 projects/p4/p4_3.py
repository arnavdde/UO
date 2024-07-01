'''
CS 210 Project 4
Author: Arnav De
Credits: lab
Even-odd cypher encryption
Half alphabet ascii rotation cypher

'''
msg = ''

def encrypt(msg:str) -> str:
    msg = msg.lower()
    encrypted = ''
    ascii = 0
    for ch in msg:
        ascii = ord(ch)
        if ascii >= 97 and ascii <= 109:
            new_asc = ascii + 13
            encrypted += chr(new_asc)
        elif ascii >= 110 and ascii <= 122:
            new_asc = ascii - 13
            encrypted += chr(new_asc)
        else: 
            encrypted += ch
    return encrypted

def decrypt(msg:str) -> str:
    decrypted = ''
    asc = 0
    msg = msg.lower()
    for ch in msg:
        asc = ord(ch)
        if asc >= 97 and asc <= 109:
            new_asc = asc + 13
            decrypted += chr(new_asc)
        elif asc >= 110 and asc <= 122:
            new_asc = asc - 13
            decrypted += chr(new_asc)
        else:
            decrypted += ch
    
    return decrypted

encrypt(msg)
decrypt(msg)