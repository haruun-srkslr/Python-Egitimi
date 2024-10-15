import random
def menu():
    print("""
    1.Oyna 
    2.Çıkış    
""")
    secim=input("secim yapınız")
    if secim=="1":
        oyna()        
    elif secim=="2":
        quit()
    else:
        print("hatalı seçim yaptınız")


def oyna():
    kullanici=0
    bilgisayar=0
    while True:
        print("""
                    TAŞ-KAĞIT-MAKAS
                    1.TAŞ
                    2.KAĞIT
                    3.MAKAS
            
            """)
        rastgele=random.randint(1,3)
        try:
            s1=int(input("Taş? Kağıt? Makas?(1/2/3)"))
        except ValueError:
            print("hatalı veri tipi girdiniz")
            continue
        while s1 not in [1,2,3]:
            print("hatalı hamle yaptınız!")
            s1=int(input("Taş? Kağıt? Makas?(1/2/3)"))
 
        if s1==rastgele:
            print("beraberlik!")
        elif (s1=="1" and rastgele==3) or \
            (s1=="2" and rastgele==1) or \
            (s1=="3" and rastgele==2) :
            print("kazandın")
            kullanici+=1
        else: 
            bilgisayar+=1
            print("kaybettin")
        print(kullanici)
        print(bilgisayar)
        while True:
            secim=input("devam etmek ister misiniz(e/h)").lower() 
            if secim=="e":
                print("devam ediliyor...")
                break
            elif secim=="h":
                quit()
            else:
                print("hatalı tuşlama yapıldı!")  
            
menu()