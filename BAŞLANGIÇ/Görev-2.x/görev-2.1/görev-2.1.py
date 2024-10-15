def compress(data):
    try:
        i=0
        compressed= []
        while i < len(data) :
            count = 1
            while i+1 < len(data) and data[i] == data[i+1]:
                i+=1
                count+=1
            compressed.append((count,data[i]))
            i+=1
        return compressed
    except Exception as e:
        with open("report.txt","a") as file:
            file.write(f"hata : {e} \n")
            print(f"hata : {e} \n")
def decompressed(data):
    try:
        i=0
        decompressed = ""
        for count,harf in data:
            decompressed += count * harf
        return decompressed
    except Exception as e :
        with open("report.txt","a") as file:
            file.write(f"hata : {e} \n")
            print(f"hata : {e} \n")        
def data_alımı():
    try:
        data=input("Sıkıştırmak istediğiniz datayı giriniz").strip()
        if data:
            return data
        else:
            print("boş data girilemez ! ")
    except Exception as e:
        print(f"hata oluştu : {e}")
def dosya_kayit(data):
    try:
        with open("compressed.txt","a",encoding="utf-8") as file:
            file.write(str(data) + "\n")
            print("compressed.txt dosyasına başarıyla eklendi ! ")
    except Exception as e:
        with open("report.txt","a")as file2:
            file2.write(f"hata : {e} + \n")
def dosya_kayit2(inp):  
    try:
        with open("input.txt","a",encoding="utf-8") as file2:
            file2.write(inp + "\n")
            print("başarıyla eklendi ! ")
    except Exception as e:
        with open("report.txt","a") as file:
            file.write(f"hata : {e} \n")    





def calistir():

    try:
        data = data_alımı()
        
        dosya_kayit2(data)
        
        pressed=compress(data)
        
        dosya_kayit(pressed)
        
        print(f"sıkıştırılmış veri : {pressed}")

        print(f"açılmış hali : {decompressed(pressed)}")
    except Exception as e :
        print(f"hata oluştu : {e}")


calistir()

