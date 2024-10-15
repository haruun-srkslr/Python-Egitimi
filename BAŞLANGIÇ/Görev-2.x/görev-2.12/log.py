import math
def log():
    try:
        y=int(input("logaritması tabanını giriniz ! "))
        x=int(input("logaritmanın üssünü giriniz ! "))
        sonuc=math.log(x,y)
        return sonuc
    except Exception as e :
        print(f"hata oluştu : {e}")