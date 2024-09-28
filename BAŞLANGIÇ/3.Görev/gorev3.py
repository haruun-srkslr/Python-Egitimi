import math

def print_menu():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Faktöriyel")
    print("6. Üs Alma")
    print("7. Mod Alma")
    print("8. İkinci Dereceden Denklem Çözme")
    print("9. Çıkış")

def top(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Bölme hatası: Sıfıra bölme yapılamaz."

def fakt(n):
    try:
        if n < 0:
            return "Negatif sayıların faktöriyeli hesaplanamaz."
        return math.factorial(n)
    except OverflowError:
        print("çok büyük sayı girdin ")
def ustalma(x, y):
    try:
        return pow(x,y)
    except ValueError:
        print("tam sayı giriniz")
def mod(x, y):
    
    try:
        return x % y
    except ZeroDivisionError:
        return "0'a mod alınamaz"


def kokbulma():
    print("denklem ax^2+bx+c olmak üzere ;")   
    while True:
        try:
            a=float(input("a katsayısını giriniz "))
            if a==0:
                print("a katsayısı 0'a eşit olamaz!")
            else:
                break
        except ValueError:
            print("hatalı giriş yaptınız")
    while True:
        try:
            b=float(input("b katsayısını giriniz "))
            break
        except ValueError:
            print("hatalı giriş yaptınız")
    while True:
        try:
            c =float(input("c katsayısını giriniz "))
            break
        except ValueError:
            print("hatalı giriş yaptınız")
    diskriminant=math.pow(b,2)-4*a*c
    print(f"diskriminant = {diskriminant}")
    if diskriminant<0:
        print("reel kök yok")
    elif diskriminant > 0:
        
        kok1=(-b+math.sqrt(diskriminant))/(2*a)
        kok2=(-b-math.sqrt(diskriminant))/(2*a) 
        print(kok1)
        print(kok2)
    elif diskriminant == 0:
        kok = -b / (2*a)
        print(kok)

def menü():
    while True:
        print_menu()
        secim = input("Bir seçenek girin (1-9): ")

        if secim == "9":
            print("Çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4', '7']:
            try:
                s1 = float(input("Birinci sayıyı girin: "))
                s2 = float(input("İkinci sayıyı girin: "))
            
            except ValueError:
                print("hatalı veri tipi girdiniz")
                break
            except UnboundLocalError:
                print("hatalı veri tipi girdiniz")
                break

        if secim == '1':
            print("Sonuç:", top(s1, s2))
        elif secim == '2':
            print("Sonuç:", cikarma(s1, s2))
        elif secim == '3':
            print("Sonuç:", carp(s1, s2))
        elif secim == '4':
            print("Sonuç:", bol(s1, s2))
        elif secim == '5':
            try:
                sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
                print("Sonuç:", fakt(sayi))
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif secim == '6':
            try:
                taban = float(input("Tabanı girin: "))
                ust = float(input("Üssü girin: "))
                print("Sonuç:", ustalma(taban, ust))
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif secim == '7':
            print("Sonuç:", mod(s1, s2))
        elif secim == '8':
            print(kokbulma())
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

menü()
