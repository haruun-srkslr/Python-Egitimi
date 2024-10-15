import math
def sin():
    try:
        n=input("hangi sinüs derecesini istersiniz")
        sonuc=math.sin(math.radians(int(n)))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")