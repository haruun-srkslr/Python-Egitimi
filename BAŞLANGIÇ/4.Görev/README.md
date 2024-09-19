# SAYI TAHMİN OYUNU 

## PROJE TANIMI
Bu Python projesi, kullanıcıların belirli bir aralıkta rastgele bir sayıyı tahmin etmeye çalıştığı bir sayı tahmin oyunudur. Oyun, kolay, orta ve zor olmak üzere üç farklı zorluk seviyesine sahiptir.

## KULLANIM
Kullanıcı, zorluk seviyesini seçerek oyuna başlayabilir. Seçilen zorluk seviyesine göre, bilgisayar rastgele bir sayı oluşturur ve kullanıcı bu sayıyı tahmin etmeye çalışır.

### OYUNUN AŞAMALARI

1. **Zorluk Seçimi**:
   - Kullanıcı, 1 (Kolay), 2 (Orta) veya 3 (Zor) seçeneklerinden birini girerek zorluk seviyesini seçer.

2. **Tahmin Süreci**:
   - Kullanıcı, belirtilen aralıkta bir sayı tahmin eder.
   - Bilgisayar, kullanıcının tahminine göre "daha küçük" veya "daha büyük" ipuçları verir.
   - Kullanıcı doğru tahmin ettiğinde oyunun sonlandığını belirtir.

### KOD ÖRNEKLERİ

```python
import random

def menu():
    print("""
        SAYI TAHMİN OYUNU
            ZORLUK SEÇİNİZ
            1.KOLAY
            2.ORTA
            3.ZOR
    """)
    secim = input("Zorluk seviyesi seçiniz: ")
    if secim == "1":
        kolay()
    elif secim == "2":
        orta()
    elif secim == "3":
        zor()
    else:
        print("Hatalı tuşlama yaptınız.")

def kolay():
    rast_sayi = random.randint(1, 10)
    while True:
        s1 = int(input("Sayı tahmin ediniz (1-10): "))
        if s1 == rast_sayi:
            print("Kazandınız!")
            break
        elif s1 > rast_sayi:
            print("Daha küçük.")
        elif s1 < rast_sayi:
            print("Daha büyük.")
        else:
            print("Lütfen geçerli bir sayı giriniz.")

def orta():
    rast_sayi = random.randint(1, 100)
    while True:
        s1 = int(input("Sayı tahmin ediniz (1-100): "))
        if s1 == rast_sayi:
            print("Kazandınız!")
            break
        elif s1 > rast_sayi:
            print("Daha küçük.")
        elif s1 < rast_sayi:
            print("Daha büyük.")
        else:
            print("Lütfen geçerli bir sayı giriniz.")

def zor():
    rast_sayi = random.randint(1, 1000)
    while True:
        s1 = int(input("Sayı tahmin ediniz (1-1000): "))
        if s1 == rast_sayi:
            print("Kazandınız!")
            break
        elif s1 > rast_sayi:
            print("Daha küçük.")
        elif s1 < rast_sayi:
            print("Daha büyük.")
        else:
            print("Lütfen geçerli bir sayı giriniz.")

menu()
