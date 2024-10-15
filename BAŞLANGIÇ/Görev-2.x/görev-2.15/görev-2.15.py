import time
def frekans(girdi):
    try:
        frekans1={}
        start_time=time.time()
        for harf in girdi:
            if harf.isalpha():
                if harf in frekans1:
                    frekans1[harf]+=1
                else:
                    frekans1[harf]=1
        
        siralanmis=sorted(frekans1.items(), key=lambda x:x[1], reverse=True)
        
        
        total_time=time.time() - start_time    
        return siralanmis,total_time
    except ValueError:
        print("hatalı veri tipi !")    
    except Exception as e :
        print(f"hata oluştu : {e}")
def dosya_yazma(sonuc,time):
    try:
        with open("frequency_analysis.txt","a",encoding="utf-8") as file:
            for i in sonuc:
                file.write(f"{i} \n")
            file.write(f"{time:.12f}"+"\n")
            file.write("--------------------------------------\n")
    except Exception as e:
        print(f"beklenmedik bir hata oluştu : {e} ")




def main():
    try:
        metin=input("  ").upper().strip()
        siralanmis,ttime=frekans(metin)
        dosya_yazma((siralanmis),ttime)
    except Exception as e :
        print(f"beklenmedik bir hata : {e}")

