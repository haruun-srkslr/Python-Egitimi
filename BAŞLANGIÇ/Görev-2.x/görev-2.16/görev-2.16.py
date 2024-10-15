import time


def sayi_siralama_yazma(filename):
    try:
        start_time=time.time()
        sliste=[]
        with open(filename,"r",encoding="utf-8") as file:
            yazi=file.read().split(",")
            for i in yazi:
                sliste.append(int(i))
            dsliste=sliste.copy()
            dsliste.sort()
            dsliste.reverse()
            enBuyuk=dsliste[0]
            enKucuk=dsliste[-1]
            totalTime=time.time()-start_time
            index1=sliste.index(enBuyuk)
            index2=sliste.index(enKucuk)
            return sliste,enBuyuk,enKucuk,index1,index2,totalTime
    except FileNotFoundError:
        print("dosya adını veya yolunu kontrol ediniz ! ")
    except ValueError :
        print("hatalı veri tipi !")
    except Exception as e :
        print(f"hata oluştu : {e}")

def dosyaislem(sliste,enBuyuk,enKucuk,index1,index2,time):
    try:
        with open("min_max_report.txt","a",encoding="utf=8") as file:
            file.write(str(sliste)+"\n")
            # for i in sliste:
            #     file.write(str(i))
            file.write(f"{enBuyuk} -> indexi : {index1} -> sırası : {index1+1} \n")
            file.write(f"{enKucuk} -> indexi : {index2} -> sırası : {index2+1}\n")
            file.write(f"{time:.12}\n")
            file.write("-----------------------------------------------\n")
    except Exception as e:
        print(f"hata oluştu : {e}")
def main():
    try:
        print("<<<<<<<<<<<<SAYI SIRALAMA PROGRAMI>>>>>>>>>>>>>>>>")
        filename=input("dosyanın içindeki sayılar '1,2,3,4,5,6,7,8,9' şeklinde tırnaklar olmadan yazılmalı sayılar rastgele olabilir ! ")
        liste,enBuyuk,enKucuk,index1,index2,ttime=sayi_siralama_yazma(filename)
        dosyaislem(liste,enBuyuk,enKucuk,index1,index2,ttime)
    except Exception as e: 
        print(f"hata oluştu : {e}")