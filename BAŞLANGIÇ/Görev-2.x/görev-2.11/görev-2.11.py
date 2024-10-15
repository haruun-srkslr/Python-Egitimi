import time
# [3,2,5,9,8]
def bubble_sort(dizi):
    try:
            steps=[]
            start_time=time.time()
            for j in range(len(dizi)):
                for i in range(0,len(dizi)-j-1):
                    if dizi[i]>dizi[i+1]:
                        dizi[i],dizi[i+1] = dizi[i+1],dizi[i]
                steps.append(dizi.copy())
                print(dizi)
                
            toplamsüre=time.time() - start_time
            return steps,toplamsüre    
    except ValueError:
        print("hatalı girdi tipi !")        
    except Exception as e :
        print(f"hata oluştu : {e}")

        
def selection_sort(dizi):
    try:
        steps=[]
        start_time=time.time()
        n=len(dizi)
        for i in range(n):
            
            for j in range(i+1,n):
                if dizi[j]<dizi[i]:
                    dizi[i],dizi[j]=dizi[j],dizi[i]
            steps.append(dizi.copy())
            print(dizi)
        toplamsüre=time.time()-start_time
        return steps,toplamsüre
    except ValueError:
        print("hatalı veri tipi !")
    except Exception as e :
        print(f"hata oluştu : {e}")    

def dosya_kayıt(dizi1,dizi2,süre1,süre2):
    try:
        with open("compare.txt","a",encoding="utf-8") as file:
            file.write("bubble sort\n")
            file.write(f"{dizi1}\n")
            file.write(f"{süre1:.12f}\n")
            file.write("-----------------------------------------------\n")
            file.write("selection sort\n")
            file.write(f"{dizi2}\n")
            file.write(f"{süre2:.12f}\n")
    except Exception as e :
        print(f"hata oluştu : {e}")
def dosyadan_okuma(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            satirlar=file.readline().strip()
            
            # satirlar=satirlar.split(",")
            sayilar=list(map(int,satirlar.split(",")))
            return sayilar
    except FileNotFoundError:
        print("dosya yolunu veya adını kontrol ediniz ! ")
    except Exception as e :
        print(f"hata oluştu : {e}")



def main():
    try:
        filename=input("dosya adı giriniz ! ")
        dizi=dosyadan_okuma(filename)
        bubble=dizi.copy()
        selection=dizi.copy()

        dizi1,süre1=bubble_sort(bubble)
        dizi2,süre2=selection_sort(selection)
        dosya_kayıt(dizi1,dizi2,süre1,süre2)
    except Exception as e :
        print(f"hata oluştu : {e}")

main()