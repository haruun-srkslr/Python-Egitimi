import math
def acos():
    try:
        n=input("hangi değerin karşılık geldiği açıyı öğrenmek istersin : ")
        sonuc=math.acos(int(n))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")