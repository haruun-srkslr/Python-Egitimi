import math
def atan():
    try:
        n=input("hangi değerin karşılık geldiği açıyı öğrenmek istersin : ")
        sonuc=math.atan(int(n))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")