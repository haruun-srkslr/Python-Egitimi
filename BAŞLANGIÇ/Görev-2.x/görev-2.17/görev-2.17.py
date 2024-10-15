def dosya_okuma(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            satirlar=file.readlines()
            kelimeler=[]
            ters=[]
            polindrom=[]
            
            for yazi in satirlar:    
                düzelt=yazi.strip().replace("\n","" )
                if düzelt:
                    kelimeler.append(düzelt)
            for i in kelimeler:
                if i[::-1]==  i :
                    ters.append(i[::-1])
                    polindrom.append(i[::-1])
                else:            
                    ters.append(i[::-1])
        return ters,polindrom 
    except FileNotFoundError:
        print("dosya yolunu veya adını kontrol ediniz !")
    except Exception as e: 
        print(f"hata oluştu : {e}")
def dosya_yazma(ters,polindrom):
    try:
        with open("report.txt","w",encoding="utf-8") as file:
            for kelimeler in ters:
                file.write(kelimeler+"\n")
            file.write("------------------------------\n")
            for i in polindrom:
                file.write(f"polindrom kelimeler : {i}\n")
    except Exception as e:
        print(f"hata oluştu : {e}")





def main():
    try:
        dosya_adi=input("dosya adini giriniz ! ")
        ters,polindrom=dosya_okuma(dosya_adi)
        dosya_yazma(ters,polindrom)
    except Exception as e:
        print(f"hata oluştu : {e} ")

main()