""" 
Solution to mini project 1
Arnav De
4/9/2023
"""

def all_same(a_list:list)->bool:
    if not a_list: return True

    first = a_list[0]

    for item in a_list:
        if item != first:
            return False
    return True
    
def dedup(a_list:list)->list:
    if not a_list: return []

    seen = []
    deduped = []

    for item in a_list:
        if item not in seen:
            deduped.append(item)
            seen.append(item)

    return deduped



def max_run(a_list:list)->int:
    if not a_list: return 0

    max = 1
    this = 1

    for i in range(1, len(a_list)):
        if a_list[i] == a_list[i-1]:
            this += 1
        else:
            if this > max:
                max = this
            this = 1
    
    if this > max:
        max = this
    
    return max