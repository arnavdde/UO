"""Sample solution for calculator project, expr.py"""

# One global environment (scope) for
# the calculator


# One global environment variable
from typing import Dict

ENV: Dict[str, "IntConst"] = {}

class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that
    is not in ENV
    """
    pass

class Expr():
    """Abstract base class of all expressions."""

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        pass

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        pass

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        pass

class IntConst(Expr):
    """Integer constant"""
    def __init__(self, value: int):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __eq__(self, other: Expr) -> bool:
        pass`

    def eval(self) -> "IntConst":
        pass


class BinOp(Expr):
    """Abstract base class for binary operations"""
    def __init__(self, left: Expr, right: Expr, symbol: str="?Operation symbol undefined"):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def _apply(self, left_val: int, right_val: int) -> int:
        """Each concrete BinOp subclass provides the appropriate method"""
        pass

    def eval(self) -> "IntConst":
        """Evaluate using the concrete _apply method"""
        pass


class Plus(BinOp):
    """Represents left + right"""
    def __init__(self, left: Expr, right: Expr):
        pass

    def _apply(self, left: int, right: int) -> int:
        pass

class Times(BinOp):
    """left * right"""
    def __init__(self, left: Expr, right: Expr):
        pass

    def _apply(self, left: int, right: int) -> int:
        pass

class Div(BinOp):
    """left / right"""
    def __init__(self, left: Expr, right: Expr):
        pass

    def _apply(self, left: int, right: int) -> int:
        pass

class Minus(BinOp):
    """left - right"""
    def __init__(self, left: Expr, right: Expr):
        pass

    def _apply(self, left: int, right: int) -> int:
        pass


class UnOp(Expr):
    """Abstract base class for binary operations"""
    def __init__(self, left: Expr, symbol: str="?Operation symbol undefined"):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def _apply(self, left_val: int) -> int:
        """Each concrete UnOp subclass provides the appropriate method"""
        pass

    def eval(self) -> "IntConst":
        """Evaluate using the concrete _apply method"""
        pass

class Neg(UnOp):
    """- left, written as ~ left"""
    def __init__(self, left: Expr):
        pass

    def _apply(self, left: int) -> int:
        pass

class Abs(UnOp):
    """|left|, written as @left"""
    def __init__(self, left: Expr):
        pass

    def _apply(self, left: int) -> int:
        pass


class Var(Expr):
    """A variable that can be assigned or changed."""

    def __init__(self, name: str):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def eval(self):
        pass

    def assign(self, value: IntConst):
        pass


class Assign(Expr):
    """Assignment:  x = E represented as Assign(x, E)"""

    def __init__(self, left: Var, right: Expr):
        pass

    def eval(self) -> IntConst:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


if __name__ == "__main__":
    a = IntConst(7)
    b = IntConst(5)
    res = Plus(a, b)
    print("a = ", a)
    print("b = ", b)
    print("res = ", res)
    print([res])