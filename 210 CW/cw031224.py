from numpy import inf

def find_smaller_rotated(a_list: list) -> int:
    if not a_list: return None
    shortest = inf
    for item in a_list:
        if item <= shortest:
            shortest = item
    return shortest

print(find_smaller_rotated([100000, 1000, 100, 1]))

