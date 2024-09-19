# BİRİM DÖNÜŞTÜRÜCÜ 

## PROJE TANIMI
Bu Python projesi, farklı birimler arasında dönüşüm yapabilen bir birim dönüştürücü uygulamasıdır. Uygulama, uzunluk, sıcaklık ve ağırlık birimleri arasında dönüşüm işlemleri gerçekleştirebilir.

## KULLANIM
Kullanıcı, ana menüden dönüşüm yapmak istediği birimi seçer ve ardından gerekli bilgileri girerek dönüşüm işlemini gerçekleştirir. Uygulama, geçerli olmayan birim veya değer girişi yapıldığında kullanıcıyı bilgilendirir.

### ADIMLAR

1. **Ana Menü**:
   - `hesapMak()` fonksiyonu ile kullanıcıya birim seçenekleri sunulur: Uzunluk, Sıcaklık ve Ağırlık.
   - Kullanıcı, dönüşüm yapmak istediği birimi seçer.

2. **Uzunluk Dönüşümü**:
   - `uzunluk()` fonksiyonu ile farklı uzunluk birimleri arasında dönüşüm yapılır. Kullanıcıdan çevrilecek ve hedef birimleri girmesi istenir.

3. **Sıcaklık Dönüşümü**:
   - `sicaklik()` fonksiyonu ile Celsius, Fahrenheit ve Kelvin arasında dönüşüm yapılır. Kullanıcıdan sıcaklık birimlerini seçmesi istenir.

4. **Ağırlık Dönüşümü**:
   - `agirlik()` fonksiyonu ile Ton, Kental, Kilogram, Hektogram, Dekagram ve Gram arasında dönüşüm yapılır. Kullanıcıdan ağırlık birimlerini seçmesi istenir.

### KOD ÖRNEKLERİ

```python
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
