'''
CS 210 Project 4
Author: Arnav De
Credits: lab
3 rail cypher encryption
msg(str) -> str

'''
msg=''

def encrypt(msg:str) -> str:
    i = 0
    string1 = ''
    string2 = ''
    string3 = ''
    for ch in msg:
        if i % 3 == 0 or i == 0:
            string1 += msg[i]
        elif i % 3 == 1 or i == 1:
            string2 += msg[i]
        else:
            string3 += msg[i]
        i += 1
    
    encrypted = string1 + string2 + string3
    print(encrypted)

def decrypt(msg:str) -> str:
    i = 0
    j = 0
    string1 = ''
    string2 = ''
    string3 = ''
    decrypted = ''
    for ch in msg:
        if i <= len(msg) / 3 -1:
            string1 += msg[i]
        elif len(msg) / 3 <= i and i <= 2 * len(msg) / 3 -1:
            string2 += msg[i]
        else:
            string3 += msg[i]
        i += 1

    for j in range(0, len(msg) // 3):
        decrypted += string1[j]
        decrypted += string2[j]
        decrypted += string3[j]
    
    return decrypted



encrypt("The true sign of intelligence is not knowledge but imagination.")
decrypt(msg)