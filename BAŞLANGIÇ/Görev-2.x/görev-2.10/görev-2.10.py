import random
import string
import time 

def kullanıcı_girdisi():
    while True:
        try:
            uz=input("oluşturulacak şifrenin uzunluğunu giriniz ! ")
            if 0>=int(uz):
                print("lütfen pozitif bir tam sayı giriniz ! ")
                
            break
        except ValueError:
            print("hatalı veri girişi")
        except Exception as e:
            print(f"beklenmedik hata : {e}")
    seti={
    "büyük harf" : False,
    "küçük harf" : False,
    "rakam" : False,
    "özel karakter" : False
    }
    buyuk_harf=input("Büyük harfler (A-Z) kullanmak istiyor musunuz? (E/H): ").strip().lower()
    if buyuk_harf == "e":
        seti["büyük harf"] = True
    elif buyuk_harf=="h":
        seti["büyük harf"]=False
    else:
        print("hatalı veri girişi program sonlandırılıyor !")
        quit()
    kucuk_harf_secimi = input("Küçük harf kullanmak ister misiniz? (E/H): ").strip().lower()
    if kucuk_harf_secimi == 'e':
        seti["küçük harf"] = True
    elif kucuk_harf_secimi=="h":
        seti["küçük harf"]=False
    else:
        print("hatalı veri girişi program sonlandırılıyor !")
        quit()
    rakam_secimi = input("Rakam kullanmak ister misiniz? (E/H): ").strip().lower()
    if rakam_secimi == 'e':
        seti["rakam"] = True
    elif rakam_secimi=="h":
        seti["rakam"]=False
    else:
        print("hatalı veri girişi program sonlandırılıyor !")
        quit()
    ozel_karakter_secimi = input("Özel karakter kullanmak ister misiniz? (E/H): ").strip().lower()
    if ozel_karakter_secimi == 'e':
        seti["özel karakter"] = True
    elif ozel_karakter_secimi=="h":
        seti["özel karakter"]=False
    else:
        print("hatalı veri girişi program sonlandırılıyor !")
        quit()
    if not any(seti.values()):
        print("en az bir seçenek seçmek zorundasınız ! ")
        
    return uz,seti





def karakter_seti_olustur(seti):
    try:
        karakter_seti=""
        if seti["büyük harf"]:
            karakter_seti+=string.ascii_uppercase
        if seti["küçük harf"]:
            karakter_seti+=string.ascii_lowercase
        if seti["rakam"]:
            karakter_seti+=string.digits
        if seti["özel karakter"]:
            karakter_seti+=string.punctuation
        return karakter_seti
    except Exception as e :
        print(f"hata oluştu : {e}")


def sifre_olustur(uz,kset):
    try:
        start_time=time.time()
        sifre=""
        for i in range(uz):
            harf=''.join(random.choice(kset))
            sifre+=harf
        sonuc = time.time() - start_time
        return sifre, sonuc
    except Exception as e:
        print(f"hata oluştu : {e}")

def dosya_islemleri(sifre,time):
    try:
        with open("sifre.txt","a",encoding="utf-8") as file:
            file.write(f"{sifre} -> süre : {time:.12f} \n ")
    except Exception as e:
        print(f"beklenmedik bir hata oluştu : {e}")





def main():
    try:
            
        uz,kayarlari=kullanıcı_girdisi()
        kset=karakter_seti_olustur(kayarlari)
        sonuc, süre=sifre_olustur(int(uz),kset)
        dosya_islemleri(sonuc, süre)
        print(f"{sonuc} -> {süre:.6f}")

    except Exception as e:
        print(f"hata oluştu : {e}")

main()
