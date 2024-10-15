def dna_tanimlama(dna):
    try:
        dna1=[]
        for i in dna:
            if i not in ["A","T","G","C"]:
                print("hatalı DNA tanımlaması veya yanlış tuşlama ! ")
                return ["HATALI DNA TANIMLAMASI !"]
            else:
                if i == "A":
                    dna1.append("T")
                elif i== "T":
                    dna1.append("A")
                elif i== "G":
                    dna1.append("C")
                elif i== "C":
                    dna1.append("G")       
        return dna1
    except ValueError:
        print("Hatalı veri girişi ")
    except Exception as e :
        print(f"hata oluştu : {e}")            
    
def dosya_okuma(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file :
            satirlar=file.readlines()
            if not satirlar:
                print("boş dosya ! ")
            else:
                dna=[]
                for dizi in satirlar:
                    dizi=dizi.strip().upper()
                    dna.append(dizi)
                return dna
    except FileNotFoundError:
        print("dosya adını veya yolunu hatalı girdiniz ! ")
    except Exception as e:
        print(f"beklenmedik hata : {e}")


def dosya_yazma(filename, islenmemis, islenmis):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            for orijinal, islenmis in zip(islenmemis, islenmis):
                file.write(f"{orijinal} -> {islenmis}\n")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

def main():
    try:
        filename1=input()
        dosya=dosya_okuma(filename1)
        islenmis=[]
        islenmemis=[]
        for i in dosya:
            sonuc = dna_tanimlama(i)
            islenmis.append(sonuc)
            islenmemis.append(i)
        output=input()
        print(islenmemis)
        print(islenmis)
        dosya_yazma(output,islenmemis,islenmis)
    except Exception as e :
        print(f"hata oluştu  : {e}")

main()


















# dna=["T","G","A"]
# sonuc=dna_tanimlama(dna)
# print(sonuc)        
