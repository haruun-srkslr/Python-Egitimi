# Metin Analiz Programı

## Proje Açıklaması
Bu proje, verilen bir metnin kelime sayısını, en sık kullanılan kelimeyi, cümle sayısını ve ortalama kelime uzunluğunu analiz eden bir programdır.

## Özellikler
- **Kelime Sayısı:** Metindeki toplam kelime sayısını hesaplar.
- **En Sık Kullanılan Kelime:** Metinde en sık geçen kelimeyi ve tekrar sayısını belirler.
- **Cümle Sayısı:** Metindeki toplam cümle sayısını hesaplar.
- **Ortalama Kelime Uzunluğu:** Metindeki kelimelerin ortalama uzunluğunu hesaplar.

## Kullanım
1. Programı çalıştırmak için Python ortamında kodu çalıştırın.
2. Konsolda metni girin.
3. Program, metin analiz sonuçlarını konsola yazdıracaktır.


## Fonksiyonlar
- `kelime_sayisi(metin)`: Verilen metindeki toplam kelime sayısını döndürür.
- `enSikKelime(metin)`: Metinde en sık geçen kelimeyi ve sayısını döndürür.
- `cumle_sayisi(metin)`: Metindeki toplam cümle sayısını döndürür.
- `ort_kelime_uzunlugu(metin)`: Metindeki kelimelerin ortalama uzunluğunu döndürür.


```python
import re
from collections import Counter

def kelime_sayisi(metin):
    kelimeler=re.findall(r'\b\w+\b',metin)
    return len(kelimeler)

def enSikKelime(metin):
    kelimeler=re.findall(r'\b\w+\b',metin.lower())
    kelime_sayilari=Counter(kelimeler)
    en_sik=kelime_sayilari.most_common(1)
    return en_sik[0] if en_sik else("yok",0)
def cumle_sayisi(metin):
    cumleler=re.split(r'[.!?]',metin)
    return len([cumle for cumle in cumleler if cumle.strip()])
def ort_kelime_uzunlugu(metin):
    kelimeler=re.findall(r'\b\w+\b',metin)
    top_uzunluk=sum(len(kelime) for kelime in kelimeler)
    top_kelime=len(kelimeler)
    return top_uzunluk/top_kelime if top_kelime>0 else 0





def menü():
    print("metin analiz programı")
    metin=input("metni giriniz")
    toplam_kelime=kelime_sayisi(metin)
    en_sik=enSikKelime(metin)
    cumle_sayi=cumle_sayisi(metin)
    ortalama_uzunluk=ort_kelime_uzunlugu(metin)
    print(f"toplam kelime sayısı : {toplam_kelime}")
    print(f"en sık kullanılan kelime : {en_sik}")
    print(f"cümle sayisi : {cumle_sayi}")
    print(f"ortalama kelime uzunluğu : {ortalama_uzunluk}")


menü()