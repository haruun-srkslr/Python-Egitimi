import json 
import time
def read_json_file(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data = json.load(file)
            return data["liste1"], data["liste2"]
    except FileNotFoundError:
        print(f"{filename} adında bir dosya yok !")
        return None,None
    except KeyError as e:
        print(f"{filename} eksik anahtar {e}")
    except json.JSONDecodeError :
        print(f"{filename} adlı dosya gerekli json formatında değil ! ")

def write_json_file(filename,result):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(result,file,indent=4)
    except Exception as e:
        print(f"{filename} adlı dosyaya yazılırken hata oluştu : {e}")


def main():
    try:
        # dosya okuma işlemi yapıldı 
        file_name=input("dosya adı ve konumunu giriniz ! ")
        liste1,liste2 = read_json_file(file_name)
        if liste1 is None or liste2 is None:
            print("boş dosya !")
            return

        set1=set(liste1)
        set2=set(liste2)

        results={}

        # küme birleştirme
        start_time = time.time()
        union_set=set1|set2
        union_time= time.time() - start_time
        results["union"]={
            'result' : list(union_set),
            'time ' : union_time
        }

        # küme kesişimi 
        intersection_set=set1.intersection(set2)
        results["intersection"] = {
            'result' : list(intersection_set)

        }


        # fark alma
        difference_set=set1.difference(set2)
        results["difference"]={
            'result':list(difference_set)

        }

        output_file_name= input("sonuç dosyasının adını yazınız")
        write_json_file(output_file_name,results)

        print(f"sonuçlar {output_file_name} dosyasına kaydedildi")
    except ValueError:
        print("veri girişi hatası ! ")
    
    
    
    except Exception as e:
        print(f"hata oluştu : {e} !")



main()
