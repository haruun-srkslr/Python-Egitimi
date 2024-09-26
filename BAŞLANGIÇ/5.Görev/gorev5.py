stok={}
def menü():
    while True:
        print("""
    1.ÜRÜN EKLE
    2.ÜRÜNLERİ LİSTELE
    3.ÜRÜNLERİ ÇIKAR
    4.AZ OLAN ÜRÜNLERİ LİSTELE
    Q.ÇIKIŞ

    """)
        secim=input("---SEÇİM YAPINIZ(1-4/Q)---")
        if secim=="1":
            urunEkle()
        elif secim =="2":
            urunListele()
        elif secim =="3":
            urunCıkar()
        elif secim=="4" :
            AzOlan()
        elif secim.lower()=="q":
            print("ÇIKIŞ YAPILIYOR...")
            break
        else:
            print("Hatalı seçim yaptınız !")
    
def urunEkle():
    ad=input("Eklenecek ürünü giriniz : ").strip()
    if ad in stok:
        print("bu ürün zaten mevcut")
        input("devam etmek için ENTER'a basınız")
    else:
        try:
            adet=int(input("kaç adet ürün eklenecek ? "))
            if adet<=0:
                print("Ürün sayısı negatif veya sıfır olamaz!")
                input("devam etmek için ENTER'a basınız")
            else:
                stok[ad]=adet
                print("ürün başarıyla eklendi")
                input("devam etmek için ENTER'a basınız")
        except ValueError:
            print("geçersiz ürün adedi")
            input("devam etmek için ENTER'a basınız")
def urunListele():
    if not stok:
        print("Ürün bulunamadı")
        input("devam etmek için ENTER'a basınız")
    else:
        print("\n---ÜRÜNLER---\n")
        for urun,adet in stok.items():
            print(f"{urun} : {adet}")
            input("devam etmek için ENTER'a basınız")
def urunCıkar():
    urunListele()
    ad=input("stoktan çıkarılacak ürünün adını yazınız : ").strip()
    if ad in stok:
        try:
            
            adet=int(input(f"Bu üründen {stok[ad]} tane vardır. Kaç tane çıkarılsın ? "))

            if adet<=0:
                print("üründen negatif sayıda veya sıfır adet çıkarılamaz!")
                input("devam etmek için ENTER'a basınız")
            elif adet>stok[ad]:
                print("Ürünün mevcut sayısından daha fazla ürün çıkaramazsınız! ")
                input("devam etmek için ENTER'a basınız")
            else:
                stok[ad]-=adet
                if stok[ad]==0:
                    del stok[ad]
                print(f"{ad} ürününden {adet} kadar listeden çıkartıldı")
                input("devam etmek için ENTER'a basınız")
        except ValueError:
            print("geçersiz ürün sayısı ? ")
            input("devam etmek için ENTER'a basınız")
    else:
        print("böyle bir ürün bulunamadı !")
        input("devam etmek için ENTER'a basınız")
def AzOlan():
    if not stok:
        print("listede ürün yok")
        input("devam etmek için ENTER'a basınız")
    else:  
        cont=True    
        for urun,adet in stok.items():
            if adet<=5:
                print(f"{urun} : {adet}")
                input("devam etmek için ENTER'a basınız")
                cont=False
        if cont:
            print("listede az olan ürün yok!")
            input("devam etmek için ENTER'a basınız")
        












menü()       