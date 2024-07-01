import sys
sys.getrecursionlimit()
sys.setrecursionlimit(10^6)

def fact(n):
    if n == 0: return 1
    return n * fact(n-1)

def facto(n):
    if n == 0:
        return 1
    res = n * fact(n - 1)
    print(f"fact({n}) = {res}")
    # print("-" * 30)
    return res

def hanoi(n):
    print("----- hanoi("+str(n)+")")
    #han('A', 'B', 'C', n)

def fib(n):
    if n == 1: return 1
    if n == 2: return 1
    return fib(n-2) + fib(n-1)




if __name__ == '__main__':
    # print(fact(3))
    # print(facto(3))
    print(fib(10))