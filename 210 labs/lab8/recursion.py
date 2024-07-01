import sys
sys.getrecursionlimit()
from copy import deepcopy as dc

def get_vowel_count(s:str) -> int:
    if not s: return 0
    return ((s[0] in 'aeiou') + get_vowel_count(s[1:]))
      

def multiply(a:float, b:int) -> float:
    if b == 0: return 0
    elif b < 0:
        return -a - multiply(a, 1+b)
    else:
        return a + multiply(a, 1-b)

def deep_reverse(a_list: list) -> list:
    if not a_list: return []
    r_list = []
    
    for item in a_list:
        if isinstance(item, list):
            deep_reverse(item)
        
        r_list.append(dc(item))
    
    return r_list



