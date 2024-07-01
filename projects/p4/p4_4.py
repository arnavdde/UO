'''
CS 210 Project 4
Author: Arnav De
Credits: lab
cipher chooser function
msg(str) -> str

'''
import p4_1, p4_2, p4_3
from p4_1 import encrypt as encrypt1, decrypt as decrypt1
from p4_2 import encrypt as encrypt2, decrypt as decrypt2
from p4_3 import encrypt as encrypt3, decrypt as decrypt3

msg = ''
func = p4_1.encrypt

def crypt(msg, func):
    if func == p4_1.encrypt:
        print(encrypt1(msg))
    if func == p4_2.encrypt:
        print(encrypt2(msg))
    if func == p4_3.encrypt:
        print(encrypt3(msg))
    if func == p4_1.decrypt:
        print(decrypt1(msg))
    if func == p4_2.decrypt:
        print(decrypt2(msg))
    if func == p4_3.decrypt:
        print(decrypt3(msg))

crypt("Ahoy, there", p4_3.encrypt)
    