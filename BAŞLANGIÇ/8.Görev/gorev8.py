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