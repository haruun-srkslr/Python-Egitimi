import math
def cos():
    try:
        n=input("hangi cosinus derecesini istersiniz")
        sonuc=math.cos(math.radians(int(n)))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")