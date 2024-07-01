from math import *

class Fraction:
    
    def __init__(self, num, den):

        assert num >= 0 and den >= 0, f"invalid case, negative num or den"
        assert den != 0, f"invalid case, division by 0"
        # could be done as one statement, num >= 0 and den > 0 but there there wouldnt be a specific message for division by 0"
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.den})"

    def __add__(self, other:"Fraction") -> "Fraction":
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den).simplify()
    
    def __mul__(self, other:"Fraction") -> "Fraction":
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den).simplify()
    
    def simplify(self) -> "Fraction":
        div = gcd(self.num, self.den)
        self.num //= div
        self.den //= div
        return self
    




