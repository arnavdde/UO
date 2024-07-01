def proper_divisors(n):
    print('n mut be > 1')

    divisors = []
    for i in range(1, n):
        if not (n % i):
            divisors.append(i)
    
    return divisors


def perfect_numbers(n):
    prop_div = proper_divisors(n)
    if sum(prop_div) == n:
        return True
    return False

def all_perfect_numbers(n):
    a_p_n = []
    for i in range(1, n + 1):
        if perfect_numbers(i)
