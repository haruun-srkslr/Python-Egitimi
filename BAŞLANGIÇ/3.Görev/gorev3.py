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
    if n < 0:
        return "Negatif sayıların faktöriyeli hesaplanamaz."
    return math.factorial(n)

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
    cont=True
    
    while cont:
        a = float(input("a değerini girin: "))
        if a==0:
            cont=True
            print("a sıfır olamaz")
        else:
            cont=False
    b = float(input("b değerini girin: "))
    c = float(input("c değerini girin: "))
    diskriminant = b**2 - 4*a*c
    if diskriminant > 0:
        kok1 = (-b + math.sqrt(diskriminant)) / (2*a)
        kok2 = (-b - math.sqrt(diskriminant)) / (2*a)
        return kok1, kok2
    elif diskriminant == 0:
        kok = -b / (2*a)
        return kok,
    else:
        return "Karmaşık kökler var."

def menü():
    while True:
        print_menu()
        secim = input("Bir seçenek girin (1-9): ")

        if secim == "9":
            print("Çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4', '7']:
            s1 = float(input("Birinci sayıyı girin: "))
            s2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print("Sonuç:", top(s1, s2))
        elif secim == '2':
            print("Sonuç:", cikarma(s1, s2))
        elif secim == '3':
            print("Sonuç:", carp(s1, s2))
        elif secim == '4':
            print("Sonuç:", bol(s1, s2))
        elif secim == '5':
            sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
            print("Sonuç:", fakt(sayi))
        elif secim == '6':
            taban = float(input("Tabanı girin: "))
            ust = float(input("Üssü girin: "))
            print("Sonuç:", ustalma(taban, ust))
        elif secim == '7':
            print("Sonuç:", mod(s1, s2))
        elif secim == '8':
            print(kokbulma())
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

menü()
