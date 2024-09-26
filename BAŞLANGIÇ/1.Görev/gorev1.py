import math
print("denklem ax^2+bx+c olmak üzere ;")
try:
    cont=True
    while cont:
        a=float(input("a katsayısını giriniz "))
        if a==0:
            print("a katsayısı 0'a eşit olamaz!")
        else:
            cont=False
    b=float(input("b katsayısını giriniz "))
    c =float(input("c katsayısını giriniz "))
    diskriminant=math.pow(b,2)-4*a*c
    print(f"diskriminant = {diskriminant}")
    if diskriminant<0:
        print("reel kök yok")
    elif diskriminant > 0:
        
        kok1=(-b+math.sqrt(diskriminant))/(2*a)
        kok2=(-b-math.sqrt(diskriminant))/(2*a) 
        print(kok1)
        print(kok2)
    elif diskriminant == 0:
        kok = -b / (2*a)
        print(kok)
except ValueError:
    print("geçersiz veri girişi ")


