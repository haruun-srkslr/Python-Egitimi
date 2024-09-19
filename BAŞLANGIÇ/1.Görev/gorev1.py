import math
print("denklem ax^2+bx+c olmak üzere ;")
try:
    cont=True
    while cont:
        a=int(input("a katsayısını giriniz "))
        if a==0:
            cont=True
            print("a katsayısı 0'a eşit olamaz!")
        else:
            cont=False
    b=int(input("b katsayısını giriniz "))
    c =int(input("c katsayısını giriniz "))
    diskriminant=math.pow(b,2)-4*a*c
    print(diskriminant)

    kok1=(-b+math.sqrt(diskriminant))/2*a
    kok2=(-b-math.sqrt(diskriminant))/2*a 
    print(kok1)
    print(kok2)
except ValueError:
    print("kök yok!")


