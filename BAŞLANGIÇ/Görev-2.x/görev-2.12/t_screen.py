import toplama
import bolme
import carp
import cikarma
import faktorial
import kokbulma
import us_alma
import mod_alma

def screen():
    while True:
            
        print("""
        <<<<<<<<<<<<<<<<<<<-------HESAP MAKİNESİ------->>>>>>>>>>>>>>>>>>>
            1)TOPLAMA
            2)ÇIKARMA
            3)ÇARPMA 
            4)BÖLME
            5)FAKTÖRİYEL
            6)ÜS ALMA 
            7)2. DERECEDEN DENKLEMLERİN KÖKLERİNİ BULMAK
            Q)MENÜYE DÖN
            
            """)
        choice=input("lütfen seçim yapınız : ").lower().strip()
        if choice == '1':
            sonuc=toplama.toplama()
            print("Sonuç:",sonuc)
        elif choice == '2':
            sonuc=cikarma.cikarma()
            print("Sonuç:",sonuc)
        elif choice == '3':
            print("Sonuç:", carp.carpma())
        elif choice == '4':
            x=int(input("bölünecek sayiyi giriniz : "))
            y=int(input("bölecek sayiyi giriniz : "))
            print("Sonuç:",bolme.bol(x,y))
        elif choice == '5':
            try:
                sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
                print("Sonuç:", faktorial.fakt(sayi))
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif choice == '6':
            try:
                taban = float(input("Tabanı girin: "))
                ust = float(input("Üssü girin: "))
                print("Sonuç:", us_alma.ustalma(taban, ust))
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif choice == '7':
            s1 = float(input("Birinci sayıyı girin: "))
            s2 = float(input("İkinci sayıyı girin: "))
            print("Sonuç:", mod_alma.mod(s1,s2))
        elif choice == '8':
            kokbulma.kokbulma()
        elif choice=="q":
            print("MENÜYE DÖNÜLÜYOR...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


