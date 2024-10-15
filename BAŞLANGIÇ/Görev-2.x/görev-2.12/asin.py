import math
def asin():
    try:
        n=input("hangi değerin karşılık geldiği açıyı öğrenmek istersin : ")
        sonuc=math.asin(int(n))
        return sonuc 
    except Exception as e :
        print(f"hata oluştu : {e}")