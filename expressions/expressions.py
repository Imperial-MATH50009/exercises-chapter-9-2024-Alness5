from functools import singledispatch
import numbers

class Expression:
    def __init__(self, operands):
        self.operands = operands
    
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            other = numbers.Number(other)
    

    
