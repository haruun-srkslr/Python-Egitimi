import time

def atbash_sifreleme(metin):
    try:
        alfabe ="ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
        ters_alfabe=alfabe[::-1]
        start_time=time.time()
        metin=metin.upper()
        sifrelenmis=""
        for harf in metin:
            if harf in alfabe:
                indexNum=alfabe.index(harf)
                sifrelenmis+=ters_alfabe[indexNum]
            else:
                sifrelenmis+=harf
        total_time=time.time()-start_time
        return sifrelenmis, total_time
    except Exception as e:
        print(f"hata oluştu : {e}")
def dosya_kayit(sifreleme,inputs,ttime):
    try:
        with open("Atbash_sifreleme.txt","a",encoding="utf-8") as file:
            file.write(f"{inputs} ---> {sifreleme}\n")
            file.write(f"{ttime:.12f}\n")
            file.write("|----------------------------------------------------------|\n")
    except Exception as e :
        print(f"hata oluştu : {e}")

def cozumleme(metin):
    try:
        ters_alfabe ="ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
        alfabe=ters_alfabe[::-1]
        start_time=time.time()
        metin.upper()
        cozulmus=""
        for harf in metin:
            if harf in alfabe:
                index_num=alfabe.index(harf)
                cozulmus+=ters_alfabe[index_num]
            else:
                cozulmus+=harf
        total_time=time.time()-start_time
        
        return cozulmus,total_time
    except Exception as e :
        print(f"hata oluştu : {e}")

def main():
    try:
        while True:
            print("<<<<<<<<<<<< ATBASH ŞİFRELEME >>>>>>>>>>>>>>>>>>>>")
            print("1)ŞİFRELEME")
            print("2)ÇÖZME")
            print("Q)Çıkış")
            choice=input("Seçim yapınız : ")
            if choice=="1":
                metin=input("Şifrelenecek metini giriniz : ").upper()
                sifreleme,ttime=atbash_sifreleme(metin)
                print(sifreleme)
                dosya_kayit(sifreleme,metin,ttime)
            elif choice=="2":
                metin=input("Şifrelenecek metini giriniz : ").upper()
                cozulmus,time2=cozumleme(metin)
                print(cozulmus)
                dosya_kayit(cozulmus,metin,time2)
                
            elif choice.upper()=="Q":
                print("Çıkış yapılıyor... ")
                break
            else:
                print("hatalı seçim yaptınız !")
    except Exception as e :
        print(f"hata oluştu : {e}")



main()