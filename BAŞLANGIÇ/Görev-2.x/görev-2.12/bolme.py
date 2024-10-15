def bol(x, y):
    
    try:
        return x / y
    except ZeroDivisionError:
        return "Bölme hatası: Sıfıra bölme yapılamaz."
