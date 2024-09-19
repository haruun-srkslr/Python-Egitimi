def menu():
    while True:
        print("""
    NOTLAR:
    1)NOTLARI GÖRÜNTÜLE
    2)NOT EKLE 
    3)NOT SİL
    Q)ÇIKIŞ 

    LÜTFEN SEÇİM YAPINIZ
    """)
        secim=input("")
        if secim=="1":
            not_oku()
            input("devam etmek için herhangi bir tuşa basınız")
        elif secim=="2":
            not_yaz()
        elif secim=="3":
            not_sil()
        elif secim=="q" or secim=="Q":
            break
        else:
            print("hatalı seçim yaptınız")

def not_oku():
    try:
        with open("notlar.txt","r",encoding="utf-8")as file:
            for yazi in file:
                print(yazi,end='')
            file.close()
    except FileNotFoundError:
        with open("notlar.txt","w",encoding="utf-8"):
            print("dosya oluşturuldu!")


def not_yaz():
    print("yazmak istediğiniz notu giriniz")
    girilen_yazi=input().strip()
    if girilen_yazi:
        with open("notlar.txt","a",encoding="utf-8")as file:
            file.write(girilen_yazi + "\n")
        print("notunuz eklendi")
    else:
        print("Boş not girilemez!")


def not_sil():
    try:
        with open("notlar.txt","r",encoding="utf-8")as file:
            satirlar=file.readlines()
        if not satirlar:
            print("silinecek satır yok!")
            return
        print("silmek istediğiniz satir numarasını giriniz")
        for i, satir in enumerate(satirlar,start=1):
            print(f"{i} : {satir.strip()}")
        try:
            satir_sayisi = int(input("Numara :"))
            if 1<=satir_sayisi<=len(satirlar):
                satirlar.pop(satir_sayisi-1)
                with open("notlar.txt","w",encoding="utf-8")as file:
                    file.writelines(satirlar)
                print("notunuz silindi")
            else:
                print("geçersiz numara!")
        except ValueError:
            print("geçersiz numara girdiniz")
    except FileNotFoundError:
        print("dosya bulunamadı")






















menu()