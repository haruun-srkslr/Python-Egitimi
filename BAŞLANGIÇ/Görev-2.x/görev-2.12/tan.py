import math
def tan():
    try:
        n=input("hangi tanjant derecesini istersiniz")
        sonuc=math.tan(math.radians(int(n)))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")