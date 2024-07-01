"""
Project 8 solution
Author: Arnav De
Date: 3/2/24

• How can I state the problem in terms of the problem itself for lower-size subproblems?
• Can I restate the problem so the answer to the previous question becomes obvious?
• In the manual solution of this problem, did I recognize any patterns that lead to a
recursive solution?

"""

def count_smaller(lst: list, item: int) -> int:
    if not lst: return 0
    return(lst[0] < item) + count_smaller(lst[1:], item)

def is_palindrome(s: str) -> bool:
    if not s: return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

    
def avg_word_length(lst: list, length:int=0, count:int=0) -> float:
    if not lst: return length / count if count else 0
    length += (len(lst[0]))
    count += 1
    return avg_word_length(lst[1:], length, count)



def flatten(a_list:list) -> list:
    if not a_list: return []
    if isinstance(a_list[0], list):
        return flatten(a_list[0] + flatten(a_list[1:]))
    else:
        return a_list[0] + flatten(a_list[1:])

