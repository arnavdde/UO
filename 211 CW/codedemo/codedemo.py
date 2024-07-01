# -- A Fibonacci sequence is the integer sequence of
# -- 0, 1, 1, 2, 3, 5, 8, ...

# -- The first two terms are 0 and 1. All the other terms are obtained by adding the preceding two
# -- terms. For example, the 3rd term is 1 because 0+1=1, the 4th term is 2 because 1+1=2, etc.
# -- Therefore, the n
# -- th
# -- term is the sum of the (n − 2)
# -- th
# -- term and the (n − 1)
# -- th
# -- term.
# -- To do:
# -- Please create a python class named Fibonacci and add the following functions:
# -- 1. Constructor: this class has only one attribute called nterms, it represents the number of
# -- terms we want to display. For example, if we assign nterms to be 3, that means the first 3
# -- of the Fibonacci sequence (0, 1, 1)
# -- Hint: the base case for recursion is to return n when n ≤ 1,
# -- 2. A recursive function that calculates the n
# -- th
# -- term of the sequence called recur_fib(n). For
# -- example, if we call recur_fib(3), it will return 2 because it is the 3rd term of the sequence.
# -- The term starts from 0. (0th, 1st, 2nd, ...)
# -- 3. An output function that prints out all terms in the sequence.
# -- Test:
# -- Create an object called myFib to print out the first 10 terms of the Fibonacci Sequence.
# -- The correct output is
# -- ≫ 0
# -- ≫ 1
# -- ≫ 1
# -- ≫ 2
# -- ≫ 3
# -- ≫ 5
# -- ≫ 8
# -- ≫ 13
# -- ≫ 21
# -- ≫ 34

class Fibonacci:
    def __init__(self, nterms) -> None:
        self.nterms = nterms

    def recur_fib(self, nterms):
        if nterms <= 1:
            return nterms
        else:
            return self.recur_fib((nterms-1)) + self.recur_fib((nterms-2))
        
    def output(self):
        for term in range(0, self.nterms):
            print(self.recur_fib(term))
        

if __name__ == "__main__":
    myFib = Fibonacci(10)
    myFib.output()