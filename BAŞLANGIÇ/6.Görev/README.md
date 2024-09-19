# Fibonacci Tabanlı Şifreleme Sistemi 

## PROJE TANIMI
Bu Python tabanlı şifreleme sistemi, kullanıcıların metinlerini Fibonacci dizisi kullanarak şifrelemelerine ve şifrelerini çözmelerine olanak tanır. Kullanıcı dostu bir menü arayüzü ile basit bir deneyim sunmaktadır.

## KULLANIM
Kullanıcı, aşağıdaki seçeneklerden birini seçerek şifreleme sistemine erişebilir:

1. **Şifrele**: Kullanıcının girdiği metni Fibonacci dizisi kullanarak şifreler.
2. **Çözümle**: Şifrelenmiş metni çözer.
3. **Çıkış**: Programdan çıkış yapar.

```python
def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def sifreleme(metin):
    n = len(metin)
    fib = fibonacci(n)
    
    sifre = ""
    for i, harf in enumerate(metin):
        ascii = ord(harf) + fib[i]
        sifre += chr(ascii)
    return sifre

def cozum(metin):
    n = len(metin)
    fib = fibonacci(n)

    cozulmus = ""
    for i, harf in enumerate(metin):
        ascii = ord(harf) - fib[i]
        cozulmus += chr(ascii)
    return cozulmus

def menu():
    while True:
        print("""
    1.ŞİFRELE
    2.ÇÖZÜMLE
    3.ÇIKIŞ
        """)
        secim = input("---LÜTFEN SEÇİM YAPINIZ(1-3)---")
        if secim == "1":
            metinGir = input("ŞİFRELENECEK METNİ GİRİNİZ ! ")
            sifreli = sifreleme(metinGir)
            print(sifreli)
            input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")
        elif secim == "2":
            metinGir = input("ÇÖZÜLECEK METNİ GİRİNİZ ! ")
            cozulmus = cozum(metinGir)
            print(cozulmus)
            input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")
        elif secim == "3":
            print("ÇIKIŞ YAPILIYOR...")
            break
        else:
            print("HATALI SEÇİM YAPTINIZ!")
            input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")

menu()
