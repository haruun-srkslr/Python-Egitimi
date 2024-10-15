# 3216
# 3216//1000= 3

def int_to_sayi(sayi):
    try:
        roman_numerals = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),(50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')]

        if sayi<0 or sayi>4000:
            print("lütfen seçtiğiniz sayının 0 ile 4000 arasında olmasına dikkat ediniz ! ")
            return ""
        roman_num=""
        while sayi>0:
            for value,romans in roman_numerals:
                count=sayi//value
                roman_num+=romans*count
                sayi-=value*count
        return roman_num
    except Exception as e: 
        print(f"hata oluştu : {e}")    



def dosya_okuma(filename):
    try:
        
        with open(filename,"r",encoding="utf-8") as file:
            satirlar=file.readlines()
            if not satirlar:
                print("henüz bir sayi girilmedi ! ")
            else:
                sayilar=[]
                for yazi in satirlar:
                    yazi=yazi.strip()
                    if yazi.isdigit():
                        sayilar.append(int(yazi))
                    else:
                        print(f"uyarı geçersiz {yazi} atlanıyor ")
                return sayilar 
    except FileNotFoundError:
        with open(filename,"w",encoding="utf-8") as file:
            print("dosya oluşturuldu ! ")
            file.close()
            return []
    except Exception as e:
        print(f"beklenmeyen bir hata oluştu {e}")
        return []

def dosyaya_yazma(romans,filename):
    try:
        with open(filename,"a",encoding="utf-8") as file:
            for i in romans:
                file.write(i+"\n")
            print(f"roma rakamları başarıyla {filename} adlı dosyaya eklendi ! ")
    except Exception as e:
        print(f" hata oluştu : {e} ! ")
def main():
    try:

        print("""
    ------------------------ROMA RAKAMI DÖNÜŞTÜRÜCÜ--------------------------------------""")
        rfilename=input("lütfen sayıların olduğu dosyanın adını veya yolunu giriniz")
        sayilar=dosya_okuma(rfilename)
        wfilename=input("lütfen roma rakamı eklenecek dosyanın adını veya yolunu giriniz")

        if not sayilar:
            print("işlenecek sayi bulunamadı ! ")
        romans=[]
        for sayi in sayilar:
            roman=int_to_sayi(sayi)
            if roman:
                romans.append(roman)
        dosyaya_yazma(romans,wfilename)
    except Exception as e:
        print(f"hata oluştu: {e} !")

main()










