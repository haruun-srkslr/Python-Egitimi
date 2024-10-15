import sin
import cos
import tan
import cot
import log
import asin
import acos
import atan

def c_screen():
    while True:
        print("""

        <<<<<<<<<<<<<<<<<<<-------HESAP MAKİNESİ------->>>>>>>>>>>>>>>>>>>
                1)SİN(X) HESAPLAMA
                2)COS(X) HESAPLAMA
                3)TAN(X) HESAPLAMA 
                4)COT(X) HESAPLAMA
                5)LOGARİTMA HESAPLAMA
                6)ARC SİN(X) 
                7)ARC COS(X)
                8)ARC TAN(X)
                Q)MENÜYE DÖN
                

                
                """)
        choice=input("lütfen seçim yapınız : ").lower().strip()
        if choice == '1':
            sonuc=sin.sin()
            print("Sonuç:",sonuc)
        elif choice == '2':
            sonuc=cos.cos()
            print("Sonuç:",sonuc)
        elif choice == '3':
            print("Sonuç:", tan.tan())
        elif choice == '4':
            print("Sonuç:",cot.cot())
        elif choice == '6':
            try:
                print("Sonuç:", asin.asin())
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif choice == '7':
            try:
                print("Sonuç:", acos.acos())
            except ValueError:
                print("hatalı veri tipi girdiniz")
        elif choice == '8':
            print("Sonuç:",atan.atan() )
        elif choice == '5':
            print("sonuç : ",log.log())
        elif choice=="q":
            print("MENÜYE DÖNÜLÜYOR  ...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


