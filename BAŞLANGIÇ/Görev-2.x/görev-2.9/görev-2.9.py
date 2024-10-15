def collatz_sim(n):
    try:
        steps=[]
        step_num = 1
        start_num=n

        while start_num != 1:

            if start_num % 2 == 0:
                new_num=start_num//2
            else:
                new_num=3*start_num+1

            steps.append(new_num)
            start_num=new_num
            step_num+=1
        print(steps,step_num-1)
        return steps,step_num
    except ValueError:
        print("hatalı veri girişi")
    except Exception as e:
        print(f"hata oluştu : {e}")
def dosyaya_yaz(steps,stepsNum,input1):
    try:
        with open("collatz.txt","a",encoding="utf-8") as file:
            for i in range(1,stepsNum):
                file.write(f"{input1} --> {steps[i-1]} --> {i} . adım  \n ")
            file.write("---------------------------------------------------\n")
            file.close()
    except Exception as e:
        print(f"hata oluştu : {e}")





def main():
    while True:
        try:
            sayi=input("Pozitif bir tam sayı giriniz (çıkmak için 'q'): ").lower()
            if sayi=="q":
                print("programdan çıkılıyor ! ")
                break
            if int(sayi)<=0 :
                print("sayı 0'dan küçük olamaz!")
                continue
            steps,step_num=collatz_sim(int(sayi))
            dosyaya_yaz(steps,step_num,sayi)
        except ValueError:
            print("geçerli bir sayı giriniz")
        

main()