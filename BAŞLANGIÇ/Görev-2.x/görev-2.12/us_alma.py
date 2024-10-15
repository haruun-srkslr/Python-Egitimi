def ustalma(x, y):
    try:
        return pow(x,y)
    except ValueError:
        print("tam sayı giriniz")
    except OverflowError:
        print("çok büyük sayı girdiniz")