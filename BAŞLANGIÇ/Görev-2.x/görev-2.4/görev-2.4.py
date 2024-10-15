import json
import time
from datetime import datetime 

# "transactions": [
#     {
#         "id": 1,
#         "type": "income", // "income" veya "expense"
#         "amount": 5000,
#         "category": "Salary",
#         "date": "2024-04-25",
#         "duration": 0.002 // İşlem ekleme süresi (saniye cinsinden)
#     }
# ]

def read_json(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data = json.load(file)
            return data["transactions"]
    except FileNotFoundError:
        print("böyle bir dosya yok dosya oluşturulacak ")
        return []
    except json.JSONDecodeError:
        print("geçerli json formatında değil")
        return []
        

def write_json(transactions,filename):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump({"transactions" :transactions},file,indent=2)
    except Exception as e :
        print(f"hata oluştu : {e}")

def add_transactions(transactions) :
    start_time=time.time()
    while True:
        try:
            type1 = input("işlem türünü seçiniz (income/expense)").strip().lower()
            if type1 == "expense" or type1 == "income":
                break
            else:
                print("hatalı işlem türü girdiniz !")
        except Exception as e:
            print(f"beklenmedik bir hata oluştu : {e}")
    while True:
        try:     
            amount = int(input("para miktarı ! "))
            if amount <=0:
                print("sıfırdan küçük bir para ekleyemezsiniz")
            else:
                break
        except Exception as e:
            print(f"beklenmedik bir hata oluştu : {e}")
    while True:
        try:
            category = input("para harcadığınız kategoriyi giriniz ! ")
            if category :
                break
            else:
                print("boş kategori girilemez")      
        except Exception as e:
            print(f"beklenmedik bir hata oluştu : {e}")
    while True:
        try:

            date_1 = input("tarih giriniz (YYYY-AA-GG)").strip()
            date = datetime.strptime(date_1,"%Y-%M-%d").date()
            break
        except ValueError:
            print("hatalı tarih formatı (YYYY-AA-GG) şeklinde yazınız ! ")
            return
        except Exception as e :
            print(f"hata oluştu : {e} ! ") 
    endTime=time.time()
    duration=round(endTime-start_time,4)
    transaction = {
        "type": type1,
        "amount": amount,
        "category": category,
        "date":date.isoformat(),
        "duration":duration
    }
    transactions.append(transaction)

def total_budget(transactions):
    try:
        sonuc1=0
        sonuc2=0
        for t in transactions:
            if t["type"] == "income":
                income=int(t["amount"])
                sonuc1+=income
        print(f"Gelir : {sonuc1}")
        for i in transactions:
            if i["type"] == "expense":
                expense=int(i["amount"])
                sonuc2+=expense
        print(f"Gider : {sonuc2}")

        balance=sonuc1-sonuc2
        print(f"Bakiye : {balance}")
    except ValueError:
        print("veri girişi hatası ! ")
    except Exception as e:
        print(f"hata oluştu : {e} !")
def filter_date(transactions):
    while True:
        try:
            start_date1= input("Başlangıç tarihi giriniz (YYYY-AA-GG)").strip()
            end_date1 =  input("Bitiş tarihi giriniz (YYYY-AA-GG)").strip()
            break
        except ValueError:
            print("Tarihi '(YYYY-AA-GG)' şeklinde giriniz ")
        except Exception as e:
            print(f"bilinmeyen bir hata oluştu : {e}")
    while True:    
        try:
            start_date=datetime.strptime(start_date1,"%Y-%M-%d").date()
            end_date=datetime.strptime(end_date1,"%Y-%M-%d").date()
            break
        except Exception as e :
            print(f"hata oluştu : {e}")
    try:
        if start_date > end_date:
            print("başlangıç tarihi bitiş tarihinden büyük olamaz ! ")
            return
        for t in transactions:
            if start_date<=datetime.strptime(t["date"],"%Y-%M-%d").date()<=end_date:
                print(f"{t['date']} - {t['type'].capitalize()} - {t['amount']} - {t['category']} saniye")
                print()
    except Exception as e:
        print(f"hata oluştu : {e} !")    






def main():
    try:    
        filename="budget.json"
        transactions = read_json(filename)
        while True:
            print("\n--- Bütçe Takip Programı ---")
            print("1. İşlem Ekle")
            print("2. Toplamları Görüntüle")
            print("3. Tarih Filtresi ile İşlemleri Görüntüle")
            print("4. Çıkış")
            choice = input("Bir seçenek giriniz (1-4): ").strip()

            if choice == "1":
                add_transactions(transactions)
                write_json(transactions, filename)
            elif choice == "2":
                total_budget(transactions)
            elif choice == "3":
                filter_date(transactions)
            elif choice == "4":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçenek! Lütfen 1 ile 4 arasında bir sayı giriniz.")
    except ValueError:
        print("hatalı veri girişi")
    except Exception  as e :
        print(f"hata oluştu : {e} !")
    



main()