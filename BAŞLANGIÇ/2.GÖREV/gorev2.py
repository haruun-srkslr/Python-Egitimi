
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
    print("""
    çevirilmesi istenen birimi giriniz:
          1.milimetre
          2.santimetre
          3.desimetre
          4.metre
          5.dekametre
          6.hektometre
          7.kilometre
""")
    b1=float(input("secim yapınız"))
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
    b2=float(input("secim yapınız"))
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
    
def sicaklik():
    print("""
    çevirilmesi istenen birimi giriniz:
          1.celsius
          2.fahrenheit
          3.kelvin
""")
    b1=input("ilk birimi giriniz")
    
    print("""
    çevrim yapmak istenen birimi giriniz:
          1.celsius
          2.fahrenheit
          3.kelvin
""")
    
    b2=(input("secim yapınız"))
    if b1=="1" and b2=="2":
        cont=True
        while cont:
            der=float(input("derece giriniz"))
            if (-273.15)<der<0:
                cont=False
            else:
                cont=True
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
def agirlik():
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





hesapMak()



