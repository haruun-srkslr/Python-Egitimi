import random
import time
def islem_belirleme():
    try:
        operatorler=["artı","eksi","çarpma","bölme"]
        secili=random.choice(operatorler)
        return secili
    except Exception as e:
        print(f"hata oluştu : {e}") 
def islem_yazma_kontrol(islem):
    try:
        if islem=="artı":
            start_time=time.time()
            s1=random.randrange(1,100)
            s2=random.randrange(1,100)
            sonuc = s1+s2
            totaltime=time.time()-start_time
            print(f"{s1} + {s2} = ?")
            return sonuc,totaltime
        elif islem=="eksi":
            start_time=time.time()        
            s1=random.randrange(1,100)
            s2=random.randrange(1,100)
            sonuc = s1-s2
            totaltime=time.time()-start_time
            print(f"{s1} - {s2} = ?")
            return sonuc,totaltime
        elif islem=="çarpma":
            start_time=time.time()
            s1=random.randrange(1,100)
            s2=random.randrange(1,100)
            sonuc=s1*s2
            totaltime=time.time()-start_time
            print(f"{s1} * {s2} = ?")
            return sonuc,totaltime
        else:
            start_time=time.time()
            while True:
                s1=random.randrange(1,100)
                s2=random.randrange(1,100)
                sonuc=s1/s2
                if sonuc.is_integer():
                    totaltime=time.time()-start_time
                    print(f"{s1} / {s2} = ?")
                    return sonuc,totaltime
                    
                else:
                    print("bekleyiniz yeni sayı seçiliyor")
    except ValueError:
        print("hatalı veri girişi !")
    except Exception as e:
        print(f"hata oluştu : {e}")                 
def dosya_kayit(dogru,yanlis,ttime):
    try:

        with open("sonuc_raporlari.txt","a",encoding="utf-8") as file:
            file.write(f"Doğru sayısı = {dogru}\n Yanlış sayısı = {yanlis}\n")
            file.write(f"{ttime}\n")
            file.write("--------------------------------------------------\n")
    except Exception as e:
        print(f"hata oluştu : {e}")         

def oyun():
    try:
        dogru_sayisi=0
        yanlis_sayisi=0
        while True:
            islem=islem_belirleme()
            cevap,ttime=islem_yazma_kontrol(islem)
            kullanici_cevap=input("").strip().upper()
            if kullanici_cevap.isdigit():
                if int(kullanici_cevap)==cevap:
                    dogru_sayisi+=1
                    dosya_kayit(dogru_sayisi,yanlis_sayisi,ttime)
                elif int(kullanici_cevap) != cevap :
                    yanlis_sayisi+=1
                    dosya_kayit(dogru_sayisi,yanlis_sayisi,ttime)
            if kullanici_cevap== "Q" :
                break
            else:
                print("hatalı seçim")
    except Exception as e:
        print(f"hata oluştu : {e}")     
def main():
    try:
        while True:
            print("<<<<<<<<<<<HESAP MAKİNESİ OYUNU>>>>>>>>>>>>>>>")
            print("oynamak için 1'e basınız")
            print("çıkış yapmak için 'Q' ya basınız ! ")
            print("cevap vermek yerine çıkış yapmak istiyorsanız 'Q' tuşuna basmanız yeterli ! ")
            choice=input("seçim yapınız : ").upper()
            if choice=="1":
                oyun()    
            elif choice=="Q":
                print("Çıkış Yapılıyor...")
                break
    except Exception as e:
        print(f"hata oluştu : {e}") 
main()   
