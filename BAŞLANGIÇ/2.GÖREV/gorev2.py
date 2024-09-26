
def hesapMak():
    print("""
    BİRİM DÖNÜŞTÜRÜCÜYE HOŞGELDİNİZ
        1. UZUNLUK
        2. SICAKLIK
        3. AĞIRLIK
    """)
    secim=input("bir seçim yapınız")
    if (secim =="1"):
        print(uzunluk())
    elif(secim =="2"):
        print(sicaklik())

    elif(secim=="3"):
        print(agirlik())
    else:
        print("hatalı seçim yaptınız")
       

def uzunluk():
    try:
        print("""
        çevirilmesi istenen birimi giriniz(lütfen sırasıyla seçimi yapınız!):
            1.milimetre
            2.santimetre
            3.desimetre
            4.metre
            5.dekametre
            6.hektometre
            7.kilometre
    """)
        b1=int(input("lütfen sırayla seçim yapınız ! "))
        if 1>b1 or b1>7:
            return print("geçersiz seçenek girdiniz!")


        print("""
        çevirim yapmak istenen birimi giriniz:
            1.milimetre
            2.santimetre
            3.desimetre
            4.metre
            5.dekametre
            6.hektometre
            7.kilometre
    """)
        b2=int(input("lütfen sırayla seçim yapınız ! "))
        if 1>b2 or b2>7:
            return print("geçersiz seçenek giriniz!")
            

        cont=True
        while cont:
            olcu=float(input("ölcüyü giriniz"))
            if olcu>0:
                cont=False
            else:
                print("ölcü negatif olamaz")
                cont=True
  
        if b2>b1:
            
            ust=abs(b2-b1)      
            sonuc=olcu/pow(10,ust)
            return sonuc
        elif b1>b2:
            ust=abs(b2-b1)
        
            sonuc=olcu*pow(10,ust)
            return sonuc
        else:
            return print("aynı birim")
    except ValueError:
        print("geçersiz veri tipi")
    except UnboundLocalError:
        print("geçersiz veri tipi")
    
def sicaklik():
    try:
        print("""
        çevirilmesi istenen birimi giriniz:
            1.celsius
            2.fahrenheit
            3.kelvin
    """)
        b1=int(input("ilk birimi giriniz"))
        if b1<1 or b1>3:
            print("hatalı seçim yaptınız ! ")
            return
        
        print("""
        çevrim yapmak istenen birimi giriniz:
            1.celsius
            2.fahrenheit
            3.kelvin
    """)
        
        b2=int(input("secim yapınız"))
        if b2<1 or b2>3:
            print("hatalı seçim yaptınız ! ")
            return
        
        der=float(input("derece giriniz"))
        
        if b1=="1" and b2=="2":
            sonuc=der*1.8+32
            return sonuc
        elif b1=="2" and b2=="1":
            sonuc=(der-32)/1.8
            return sonuc
        elif b1=="1" and b2=="3":
            sonuc=der+273.15
            return sonuc
        elif b1=="3" and b2=="1":
            sonuc=der-273.15
            return sonuc
        elif b1=="2" and b2=="3":
            sonuc=der+457.87
            return sonuc
        elif b1=="3" and b2=="2":
            sonuc=der-457.87
            return sonuc        
    except ValueError:
        print("hatalı veri tipi ! ")
def agirlik():
    try:
        print("""
        çevirilecek birimi seçiniz:
            1.Ton
            2.kental
            3.Kilogram
            4.Hektogram
            5.Dekagram
            6.Gram

    """)
        b1=int(input("birim seçiniz"))
        if b1<1 or b1>6:
            print("geçersiz seçenek girdiniz ! ")
            return
        print("""
        çevrilmesi istenen birimi seçiniz:
            1.Ton
            2.kental
            3.Kilogram
            4.Hektogram
            5.Dekagram
            6.Gram

    """)
        b2=int(input("birim seçiniz"))
        if b2<1 or b2>6:
            print("geçersiz seçenek girdiniz ! ")
            return
        cont=True
        while cont:
            olcu=float(input("ağırlık giriniz"))
            if olcu<0:
                cont=True
                print("ağırlık negatif olamaz")
            else:
                cont=False
        if b1>b2:
            ust=abs(b1-b2+1)
            sonuc=olcu/pow(10,ust)
            return sonuc
        elif b1<b2:
            ust=abs(b2-b1+1)
            sonuc=olcu*pow(10,ust) 
            return sonuc
    except ValueError:
        print("geçersiz veri tipi girdiniz ! ")




hesapMak()



