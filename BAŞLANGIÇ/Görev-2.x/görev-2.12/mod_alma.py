import math

def mod(x, y):
    
    try:
        return math.fmod(x,y)
    except ZeroDivisionError:
        return "0'a mod alınamaz"