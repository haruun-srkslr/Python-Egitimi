import time

def üçgen_çiz(satir):
    try:
        with open("shapes.txt","a")as file:
            start_time=time.time()
            for i in range(1,satir+1):
                print(" " + (i) * "* ")
                file.write((" " + (i) * "* "+"\n"))
            total_time=time.time()-start_time
            file.write(str(total_time)+"\n")
            file.write("-----------------------------------------------\n")
            print(total_time)
            print("----------------------------------------------------")
    except ValueError:
        print("hatalı veri tipi !")
    except Exception as e:
        print(f"hata oluştu : {e}")            
def dikdortgen_ciz(satir,sutun):
    try:
        with open("shapes.txt","a") as file:    
            start_time=time.time()
            for i in range(1,satir+1):
                print(" "+ sutun*" * ")
                file.write(" "+ sutun*" * "+"\n")
            total_time=time.time()-start_time
            file.write(str(total_time)+"\n")
            file.write("-----------------------------------------------\n")
            print(total_time)
            print("----------------------------------------------------")
    except ValueError:
        print("hatalı veri tipi !")
    except Exception as e:
        print(f"hata oluştu : {e}") 
def kareciz(satir):
    try:
        with open("shapes.txt","a") as file:
            start_time=time.time()
            for i in range(1,satir+1):
                print(" "+satir*"* ")
                file.write(" "+satir*"*  "+"\n")
            total_time=time.time()-start_time
            file.write(str(total_time)+"\n")
            file.write("-----------------------------------------------\n")
            print(total_time)
            print("----------------------------------------------------")

    except ValueError:
        print("hatalı veri tipi !")
    except Exception as e:
        print(f"hata oluştu : {e}") 
def main():
    while True:
        try:
            print("<<<<<<<<<<<<<<<<<<<<SHAPE CREATOR>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("1)ÜÇGEN ÇİZ")
            print("2)DİKDÖRTGEN ÇİZ")
            print("3)KARE ÇİZ")
            print("Q)ÇIKIŞ YAP ! ")
            choice=input("Lütfen seçim yapınız : ").upper().strip()
            if choice=="1":
                satir_sayisi=int(input("üçgenin kaç satır olmasını istersiniz (ekstra boşluklar eklenecektir) : "))
                üçgen_çiz(satir_sayisi)
            elif choice=="2":
                satirs=int(input("dikdörtgenin kaç satır olmasını istersiniz (ekstra boşluklar eklenecektir) : "))
                sutuns=int(input("dikdörtgenin kaç sütun olmasını istersiniz (ekstra boşluklar eklenecektir) : "))
                dikdortgen_ciz(satirs,sutuns)
            elif choice=="3":
                kenar=int(input("Karenin kenarının kaç birim olmasını istersiniz (ekstra boşluklar eklenecektir) : "))
                kareciz(kenar)
            elif choice=="Q":
                break
            else:
                print("hatalı giriş yaptınız ! ")
        except ValueError:
            print("hatalı veri girişi ! ")
        except Exception as e :
            print(f"beklenmedik bir hata : {e}")
        
main()














