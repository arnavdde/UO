import math

def prime(n):
# n is the number we want to check for primality

# n is divisible by k?

# if n%k is 0 not prime 

# loop from 2 to n-1
    k = 1
    for k in range (1, n-1):
        k += 1
        if n%k == 0:
            return False
    return True

def prime_optimized(n):
    if n<2:
        return False
    for x in range(2, int(math.sqrt(n))):
        if n % x == 0:
            return False
    return True

def dr_fib(n):
    f_dict = {1:1, 2:1}

    def d_fib_r(n):
        print(f"d_fib_r({n})")
        if n in f_dict.keys():
            print(f"stop rec -> f_dict[{n}] = {f_dict[n]}")
            return f_dict[n]
        f_dict[n] = d_fib_r(n-2) + d_fib_r(n-1)
        print(f"->f_dict[{n}] = {f_dict[n]}")
        return f_dict[n]
    
    return d_fib_r(n)

def remove_outliers(a_list, n):
    # remove first and last n elements from a list
    # take list, sort it in numerical order, remove outliers
    a_list.sort()
    if len(a_list) <= 2 * n or n == 0:
        return a_list
    print(remove_outliers(a_list[n:-n], n))
    return remove_outliers(a_list[n:-n], n)


if __name__ == '__main__':
    # for i in range(15):
    #     print(f"{i} is prime: ", end='')
    #     if prime(i):
    #         print('true')
    #     else:
    #         print('false')

    # for i in range(20, 100):
    #     print(f"{i} is prime? :", end='')
    #     if prime_optimized(i):
    #         print("True")
    #     else:
    #         print("False")
            
    kist = [1, 3, 5, 6, 7, 4, 2, 3, 5, 6, 6, 3, 23, 5, 3, 4, 5, 6, 9, 9, 9, 9, 9, 9, 9, 9]
    remove_outliers(kist, 3)