import math
def cot():
    try:
        n=int(input("hangi kotanjant derecesini istersiniz"))
        sin=math.sin(math.radians(n))
        cos=math.cos(math.radians(n))
        sonuc=cos/sin
        return sonuc 
    except ZeroDivisionError:
        print("sıfıra böldünüz")
    except Exception as e :
        print(f"beklenmedik bir hata ile karşılaşıldı : {e}")