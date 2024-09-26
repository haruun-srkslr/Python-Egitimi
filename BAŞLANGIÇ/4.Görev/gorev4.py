import random
def menu():
    print("""
        SAYI TAHMİN OYUNU
            ZORLUK SEÇİNİZ
            1.KOLAY
            2.ORTA
            3.ZOR
    """)
    secim=input("Zorluk seviyesi seçiniz")
    if secim=="1":
        kolay()
    elif secim=="2":
        orta()
    elif secim=="3":
        zor()
    else:
        print("hatalı tuşlama yaptınız")

def kolay():
    try:
        rast_sayi=random.randint(1,10)
        while True:
            s1=int(input("sayi tahmin ediniz (1-10)"))
            if s1<1 or s1>10:
                print("lütfen 1 ve 10 arasında seçim yapınız!")
            elif s1==rast_sayi:
                print("kazandınız")
                break
            elif s1>rast_sayi:
                print("daha küçük")
            elif s1<rast_sayi:
                print("daha büyük")
            else:
                print("lütfen geçerli bir sayi giriniz")
    except ValueError:
        print("hatalı veri tipi girdiniz")

def orta():
    try:
        rast_sayi=random.randint(1,100)
        while True:
            s1=int(input("sayi tahmin ediniz (1-100) "))
            if s1<1 or s1>100:
                print("lütfen 1 ve 100 arasında seçim yapınız!")
            elif s1==rast_sayi:
                print("kazandınız")
                break
            elif s1>rast_sayi:
                print("daha küçük")
            elif s1<rast_sayi:
                print("daha büyük")
            else:
                print("lütfen geçerli bir sayi giriniz")
    except ValueError:
        print("hatalı seçim yaptınız")


def zor():
    try:
        rast_sayi=random.randint(1,1000)
        while True:
            s1=int(input("sayi tahmin ediniz (1-1000) "))
            if s1<1 or s1>1000:
                print("lütfen 1 ve 1000 arasında seçim yapınız!")
            elif s1==rast_sayi:
                print("kazandınız")
                break
            elif s1>rast_sayi:
                print("daha küçük")
            elif s1<rast_sayi:
                print("daha büyük")
            else:
                print("lütfen geçerli bir sayi giriniz")
    except ValueError:
        print("hatalı veri tipi girdiniz")



menu()