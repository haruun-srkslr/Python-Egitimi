def sayi_yaziyla(sayilar):
    kelimeler=[]
    try:
        for sayi in sayilar:
            birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
            onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"] 
            if sayi==0:
                kelimeler.append("sıfır") 
                continue
            if sayi<0:
                kelimeler.append("eksi" + sayi_yaziyla(abs(sayi))) 
                continue
            kelime = ""

            # milyon
            milyon = sayi//1000000
            sayi = sayi % 1000000
            if milyon>0:
                if milyon == 1:
                    kelime += "bir milyon" 
                else:
                    kelime += sayi_yaziyla([milyon])[0] + " milyon "


            #binler
            binn = sayi // 1000
            sayi = sayi % 1000 
            if binn>0:
                if binn == 1:
                    kelime += "bin"
                else:
                    kelime += sayi_yaziyla([binn])[0] + " bin  "
            
            
            # yüzler
            yüz = sayi // 100
            sayi = sayi % 100
            if yüz>0:
                if yüz==1:
                    kelime += "yüz"
                else:
                    kelime += sayi_yaziyla([yüz])[0] + " yüz "
            # onlar
            on = sayi//10
            bir = sayi % 10
            if on>0:
                kelime += onlar[on] + " "
            if bir>0:
                kelime += birler[bir] + " "


            kelimeler.append(kelime.strip())
        return kelimeler
    except Exception as e:
        print(f"hata oluştu : {e}") 
    

def dosya_yazma(inputlar,kelime):
    try:
        with open("kelime.txt","a",encoding="utf-8") as file:
            for i,j in zip(kelime,inputlar):
                file.write(f"{i} --> {j}\n")
                file.write("-------------\n")
    except Exception as e :
        print(f"hata oluştu : {e}")



def dosya_okuma(filename):
    sayilar=[]
    try:
        with open(filename,"r",encoding="utf-8") as file:
            satirlar=file.readlines()
            for sayi in satirlar:
                sayilar.append(int(sayi.strip()))
        return sayilar
    except FileNotFoundError:
        print("dosya adını veya yolunu yanlış girdiniz !")
    except ValueError:
        print("hatalı girdi")
    except Exception as e:
        print(f"hata oluştu : {e}")



def main():
    try:
        dosya_adi=input("Dosya adını giriniz :  ")
        sayilar=dosya_okuma(dosya_adi)
        kelimeler = sayi_yaziyla(sayilar)
        dosya_yazma(sayilar,kelimeler)
    except ValueError:
        print("hatalı girdi")
    except Exception as e: 
        print(f"hata oluştu {e}")


main()
