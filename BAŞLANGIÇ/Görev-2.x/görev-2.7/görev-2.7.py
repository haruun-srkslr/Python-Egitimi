def ISBN13(kod):
    try:
        a=0
        toplam=0
        for i in range(len(kod)):
            if a % 2 ==1:
                toplam += (int(kod[i])*3)
                a +=1
            else:
                toplam +=int(kod[i])
                a+=1
        if toplam%10 == 0 :
            print("geçerli ISBN kodu !")
            return "geçerli kod!!"
        else:
            print("geçersiz ISBN kodu !!")
            return "geçersiz kod !!"  
    except Exception as e :
        print(f"hata oluştu : {e}")    

def ISBN10(kod):
    try:
        a=0
        toplam=0
        for i in range(len(kod)-1):
            sonuc=0
            sonuc=(i+1)*int(kod[i])
            toplam+=sonuc
        digit_kont=kod[9]
        if digit_kont=="X":
            toplam+=10
        else:
            toplam+=int(digit_kont)
        if toplam % 11 == 0:
            print("geçerli ISBN kodu")
            return "geçerli kod !"
        else:
            print("geçersiz ISBN kodu")
            sonuc=toplam%11
            return "geçersiz kod !"
    except Exception as e :
        print(f"hata oluştu : {e}")    


def ISBN_düzenleme(kod):
    try:
        kod=kod.replace("-","").upper()
        if len(kod) == 10:
            return ISBN10(kod)
        elif len(kod) == 13:
            return ISBN13(kod)
        else:
            print("hatalı giriş var kontrol ediniz !")
            return "hatalı giriş var kontrol ediniz !"
    except ValueError:
        print("hatalı veri girişi ")
    except Exception as e :
        print(f"hata oluştu : {e}")

def dosya_okuma(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            satirlar = file.readlines()
            if not satirlar:
                print("henüz not yok ! ")
                return
            else:
                kodlar=[]
                for i in range(len(satirlar)):
                    print(len(satirlar))
                    kodlar.append(satirlar[i].strip())
                return kodlar
    except FileNotFoundError:
        print("böyle bir dosya yoktur ! ")
    except Exception as e :
        print(f"bilinmeyen bir hata oluştu : {e}")

def dosya_yazma(filename,sonuclar):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            for isbn,sonuc in sonuclar:
                file.write(f"{isbn} -> {sonuc} \n")
            
            
    except FileNotFoundError:
        print("böyle bir dosya yoktur ! ")
    except Exception as e :
        print(f"bilinmeyen bir hata oluştu : {e}")




def main():
    try:
        filename = input("dosya adı giriniz : ")
        kodlar=dosya_okuma(filename)
        cikti_dosyasi = input("Sonuçların kaydedileceği dosyanın adını giriniz: ")

        sonuclar= []
        for kod in kodlar:
            sonuc=ISBN_düzenleme(kod)
            sonuclar.append((kod,sonuc))
        dosya_yazma(cikti_dosyasi,sonuclar)
    except Exception as e:
        print(f"hata oluştu : {e}")    

main()