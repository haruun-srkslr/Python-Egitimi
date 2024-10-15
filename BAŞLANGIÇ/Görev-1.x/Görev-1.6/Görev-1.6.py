def fibonacci(n):
    fib=[1,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    return fib
def sifreleme(metin):
    try:
        n=len(metin)
        fib = fibonacci(n)
        
        sifre=""
        for i,harf in enumerate(metin):
            ascii=(ord(harf)+fib[i]) % 128
            sifre += chr(ascii)
        return sifre
    except ValueError:
        print("hatalı veri tipi girdiniz")

def cozum(metin):
    try:
        n=len(metin)
        fib = fibonacci(n)

        cozulmus=""
        for i,harf in enumerate(metin):
            ascii=(ord(harf)-fib[i]) % 128
            cozulmus += chr(ascii)
        return cozulmus
    except ValueError:
        print("hatalı veri tipi girdiniz")


def menu():
    try:
        while True:
            print("""
        1.ŞİFRELE
        2.ÇÖZÜMLE
        3.ÇIKIŞ
        """)
            secim=input("---LÜTFEN SEÇİM YAPINIZ(1-3)---")
            if secim == "1":
                metinGir=input("ŞİFRELENECEK METNİ GİRİNİZ ! ")
                sifreli=sifreleme(metinGir)
                print(sifreli)
                input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")
            elif secim == "2":
                metinGir=input("ÇÖZÜLECEK METNİ GİRİNİZ ! ")
                cozulmus=cozum(metinGir)
                print(cozulmus)
                input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")
            elif secim == "3":
                print("ÇIKIŞ YAPILIYOR...")
                break
            else:
                print("HATALI SEÇİM YAPTINIZ!")
                input("----DEVAM ETMEK İÇİN ENTER'A BASINIZ----")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")


menu()