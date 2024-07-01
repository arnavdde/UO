"""This function has two bugs.
Your mission is to dubug it, i.e., analyze it,
write scaffolding code, whatever it takes to uncover both.
Then fix it and reupload the solution here.
"""

def max_run(l: list) -> list:
    """Returns the longest 'run' in the list.
    Example:  max_run([ 1, 1, 2, 2, 2, 3, 3 ]
    returns [2, 2, 2]
    """
    if not l: return []
    cur_item = l[0]
    longest = []
    cur_run = []
    for item in l:
        if item == cur_item:
            cur_run.append(item)
        else:
            if len(cur_run) > len(longest):
                longest = cur_run
            cur_run = [ item ]
            cur_item = item
        if len(cur_run) > len(longest):
            longest = cur_run
    return longest
