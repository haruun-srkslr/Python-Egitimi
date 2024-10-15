import math
def fakt(n):
    try:
        if n < 0:
            return "Negatif sayıların faktöriyeli hesaplanamaz."
        return math.factorial(n)
    except OverflowError:
        print("çok büyük sayı girdin ")