stack []


operations list []

loop: iterate through input, adding item within to stack

    if item in input in operations list:
        dont add it to stack, pop prev 2 in stack, operate on them, replace in stack
        keep track of operation, add to print message

    return when len(stack[]) == 1

