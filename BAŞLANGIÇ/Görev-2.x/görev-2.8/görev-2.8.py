import random
def cevaplar():
    try:
        dosya_adi = "yanitlar.txt"
        with open(dosya_adi, "r", encoding="utf-8") as file:
            satirlar = file.readlines()
            # Rastgele bir yanıt seç
            return random.choice(satirlar).strip()
    except Exception as e:
        print(f"hata oluştu : {e}")

   
    

def dosyaya_yazmak(filename,soru,cevap):
    try:
        with open(filename,"a",encoding="utf-8") as file:
            file.write(f"{soru} -->  {cevap} \n")
    except FileNotFoundError:
        print("dosya bulunamadı")
    except Exception as e:
        print(f"beklenmedik hata : {e}")



def yanit_ekle():
    yeni_yanit = input("Eklemek istediğiniz yanıtı giriniz: ")
    try:
        dosya_adi = "yanitlar.txt"
        # Yanıtı dosyaya ekle
        with open(dosya_adi, "a", encoding="utf-8") as file:
            file.write(f"{yeni_yanit}\n")  # Yeni yanıtı dosyaya ekle

        print(f"{yeni_yanit} başarıyla {dosya_adi}'na eklendi!")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
            

        print(cevaplar)
            
                
        print(f"{yeni_yanit} başarıyla {dosya_adi}'na eklendi !")
    except Exception as e :
        print(f"beklenmedik bir hata oluştu : {e}")







def main():
    try:
        filename=input("yanıtları ve soruları kaydedeceğiniz dosyanın adını giriniz ! ")
        
        print("""
        <<<<<<<<<<<<<<<<<<<<<<--------- MAGİC 8 BALL ------>>>>>>>>>>>>>>>>>>>>>>>>>>>
        <<<<<<<<<<<<<<<<<<<<<<--------- HOŞGELDİNİZ  ------>>>>>>>>>>>>>>>>>>>>>>>>>>>
                            !!ÇIKIŞ YAPMAK İÇİN Q&q YAZINIZ!!
                    !!YENİ YANITLAR EKLEMEK İÇİN "I" TUŞUNA BASINIZ!!

        """)    

        while True:       
            soru = input("soru sorunuz : ")
            if soru=="q" or soru=="Q":
                print("ÇIKIŞ YAPILIYOR......")
                break
            if soru=="I" or soru=="ı":
                yanit_ekle()
            
            cevap=cevaplar()
            print(cevap)
            print("-----------------------------------------------------------------")
            dosyaya_yazmak(filename,soru,cevap)
    except Exception as e:
        print(f"hata oluştu : {e}")


main()