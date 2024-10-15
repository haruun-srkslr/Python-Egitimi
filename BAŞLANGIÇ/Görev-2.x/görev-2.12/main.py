import c_screen
import t_screen





def main():
    try:
        while True:
            print("""

            <<<<<<<<<<<<<<<<<<<-------HESAP MAKİNESİ------->>>>>>>>>>>>>>>>>>>
                    1)ARİTMETİK İŞLEMLER
                    2)LOGARİTMİK VE TRİGONOMETRİK İŞLEMLER
                    Q)ÇIKIŞ
                    

                    
            """)
            choice=input("SEÇİM YAPINIZ : ").lower().strip()
            if choice =="1":
                t_screen.screen()
            elif choice=="2":
                c_screen.c_screen()
            elif choice=="q":
                print("ÇIKIŞ YAPILIYOR ! ")
                break
            else:
                print("HATALI TUŞLAMA YAPTINIZ ! ")   
    except Exception as e :
        print(f"hata oluştu : {e}")

main()  
    