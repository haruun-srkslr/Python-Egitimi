def toplama():
    sonuc=0
    while True:
        try:
            x=int(input("toplama işlemi için bir sayi giriniz : "))
            sonuc+=x
        except ValueError:
            print("hatalı veri tipi girildi ! ")
        except Exception as e :
            print(f"beklenmedik bir hata oluştu : {e} ")
        try:
            choice=input("devam etmek ister misiniz ? (E/H)").lower()
            
            if choice=="e":
                continue
            elif choice=="h":
                print("işlem sonlandırılıyor ! ")
                return sonuc
            else:
                print("hatalı seçim yaptınız ! ")
        except Exception as e :
            print(f"beklenmedik bir hata oluştu : {e}")


