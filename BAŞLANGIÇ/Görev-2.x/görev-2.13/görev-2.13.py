import time

def kelime_bulma(filename,kelime):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            icerik=file.read().lower()
            print(icerik)
        sayi=icerik.count(kelime)

        print(f"{filename} adlı dosyada {kelime} den {sayi} adet sayıldı")
        if sayi==0:
            print("böyle bir kelime yok ")
            return 0,0,0
        
        
        choice=input("değiştirmek ister misiniz ? (E/H)").lower()
        if choice=="e":
            değişen=input(f"{kelime} kelimesini hangi kelime ile değiştirmek istersiniz ? ")
            
            start_time=time.time()
            yeni_icerik=icerik.replace(kelime, değişen)
            end_time=time.time()
            total_time=end_time - start_time

            
            return yeni_icerik,total_time,sayi
        elif choice=="h":
            quit()
            return icerik 
        else:
            print("hatalı tuşlama yaptınız ! ")
    except Exception as e:
        print(f"hata oluştu : {e}")
        
def dosya_kayıt(filename,icerik):
    try:
        with open(filename,"a",encoding="utf-8") as file:
            file.write(icerik+"\n")
            file.write("---------------------------------------------------\n")
    except Exception as e :
        print(f"hata oluştu : {e}")
def rapor(filename,kelime_sayisi,time):
    try:
        with open("rapor.txt","a",encoding="utf-8") as file:
            file.write(f"Dosya Adı : {filename}\n")
            file.write(f"değiştirilen kelime sayısı : {kelime_sayisi} \n ")
            file.write(f"Toplam geçen süre : {time:.6f}\n")
            file.write("------------------------------------------\n")
    except Exception as e: 
        print(f"hata oluştu : {e}")

def main():
    try:
        filename=input("yazının olduğu dosya adını giriniz !")
        kelime=input("değiştirmek istediğiniz kelimeyi giriniz").strip().lower()
        icerik,totaltime,sayi=kelime_bulma(filename,kelime)
        wfilename=input("yeni metinin kaydedilmesini istediğiniz dosyanın adını yazınız ! ")
        dosya_kayıt(wfilename,icerik)
        rapor(wfilename,sayi,totaltime)
    except Exception as e :
        print(f"hata oluştu  : {e}")
main()
 