def menu():
    while True:
        print("""
        <<<<<<<<<<<<<<<<<<<<<<<<<<<KÜTÜPHANEYE HOŞGELDİNİZ>>>>>>>>>>>>>>>>>>>>>>>>>>>
        0.KİTAPLARI GÖRÜNTÜLE
        1.KİTAP EKLE
        2.KİTAP ÇIKAR
        3.ÖDÜNÇ AL
        4.ÜYE GİRİŞİ 
        5.YENİ ÜYE KAYDI
        Q&q.ÇIKIŞ
        (LÜTFEN YAPILACAK İŞLEMİ SEÇİNİZ)
        """)

        secim =input()
        if(secim=="0"):
            kitaplar()
        elif(secim=="1"):
            ekleme()
        elif(secim=="2"):

            cikar()

        elif (secim == "3"):
            odunc()
        elif (secim == "4"):
            login()
        elif(secim == "5"):
            uyek()
        elif(secim =="Q"or"q"):
            quit()
        else:
            print("yanlış tuşa bastınız.")


def ekleme():
    try:   
        a=input("kitap adı giriniz")
        b=input("yazarını giriniz")
        with open("kitaplar.txt","a",encoding="utf-8") as file:
            file.write(f"{a} : {b} \n")
    except ValueError:
        print("hatalı veri tipi")

def kitaplar():
    with open("kitaplar.txt","r",encoding="utf-8") as file:
        for kitap in file:
            print(kitap)

def odunc():
    kitaplar =[]
    kitap_bulundu = False
    with open("kitaplar.txt","r",encoding="utf-8") as file:
        for i in file:
            liste=i.strip().split(":")
            kitaplar.append(liste)
    a=input("kiralamak istediğiniz kitabın adı ? ")
    b=input("kiralamak istediğiniz kitabın yazarı ?")
    c=int(input("günlük maliyeti 5 TL kaç gün kiralamak istersiniz ?"))
    for kitap in kitaplar:
        kitapAd = kitap[0].strip()
        yazar = kitap[1].strip()
        if kitapAd==a and yazar==b:
            z=c*5
            e=input(f"kitabın kiralanması için {z} TL alınacaktır onaylıyor musunuz ? (e/h)")
            if e=="e" or e=="E":
                kitaplar.remove(kitap)
                kitap_bulundu = True
                break
            else:
                print("işlem sonlandı")

        if not kitap_bulundu:
            print("böyle bir kitap yoktur")
        with open("kitaplar.txt","w",encoding="utf-8") as file2:
            for kitap in kitaplar:
                file2.write(f"{kitap[0]} : {kitap[1]}")





def cikar():
    kitaplar = []
    kitap_bulundu=False
    with open("kitaplar.txt", "r", encoding="utf-8") as file:
        for i in file:
            liste=i.strip().split(":")
            kitaplar.append(liste)
    a= input("kitap adı ?")
    b= input("yazar adı ?")
    for kitap in kitaplar:
        kitapAd =kitap[0].strip()
        yazarAd =kitap[1].strip()
        if kitapAd==a and yazarAd==b:
            kitaplar.remove(kitap)
            kitap_bulundu=True
            print(f"{kitap} başarıyla kaldırıldı")
            break
    if not kitap_bulundu:
        print("Böyle bir kitap yok !")

    with open("kitaplar.txt","w",encoding="utf-8") as file2:
        for kitap in kitaplar:
            file2.write(f"{kitap[0]} : {kitap[1]}\n")






# def ucret():

def uyek():
    user = input("Username seçiniz : ")
    psswd =input("Şifre seçiniz : ")
    with open("uyeler.txt","a",encoding="utf-8") as file:
        file.write(f"{user} : {psswd}\n")
    print(f"{user}  adlı üyenin kaydı başarıyla tamamlandı")

def login():
    username = input("username : ")
    password=input("password : ")
    uyeler=[]
    loggedIN=False
    with open("uyeler.txt","r",encoding="utf-8") as file:
        for i in file:
            liste =i.strip().split(":")
            uyeler.append(liste)
        for uye in uyeler:
            user=uye[0].strip()
            psswd=uye[1].strip()
            if username == user and password == psswd:
                print("giriş yapıldı")
                loggedIN=True
        if not loggedIN:
            print("parola veya k.adı yanlış")







menu()