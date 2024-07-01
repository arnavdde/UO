'''closed intervals of integers 
Arnav De, 4/2/24, cs 211'''

import re


class Interval:
    '''and interval [m..n] represents the set of integers from m to n'''

    def __init__(self, low:int, high: int):
        '''interval(low, high) represents the interval [low..high]'''
        self.low = low
        self.high = high

        if low > high:
            raise ValueError("the low value of the interval cannot be higher than the high value")
        
    def contains(self, i:int) -> bool:
        '''integer i is within the clsoed interval'''
        if i <= self.high and i >= self.low:
            return True
        else:
            return False

    def overlaps(self, other: "Interval") -> bool:
        '''i.overlaps(j) iff i and j have some elements in common'''
        # x = self.low - 1     #edge case - what if it shouldnt work because of the first intervals lower bound not working, but this solution misses that because x+1 is automatically done at the beginning of the loop?
        # while x < self.high:
        #     x += 1
        #     if x <= other.high and x >= other.low:
        #         return True
        #     else:
        #         return False
        
        if self.low < other.low and (self.high - self.low) > (other.high - other.low):
            return True
        elif self.low > other.low and (self.high - self.low) < (other.high - other.low):
            return True
        else:
            return False


        
    def __eq__(self, other: "Interval") -> bool:
        '''intervals are equal if they have the same low and high bounds'''
        min1 = self.low
        max1 = self.high
        min2 = other.low
        max2 = other.high
        if min1 == min2 and max1 == max2:
            return True
        else:
            return False


    def join(self, other:"Interval") -> "Interval":
        '''create a new interval that contains the union of elements in self and other'''
        new_low = min(self.low, other.low)
        new_high = max(self.high, other.high)
        return(Interval(new_low, new_high))

    def __str__(self) -> str:
        '''changes the string returned when the print fucntion is called so it returns the low and high 
        values of the interval in the invterval class object'''
        print(f"{self.low}")

    def __repr__(self) -> str:
        '''provide the string we sould see when evaluating the interval class object in the python console'''