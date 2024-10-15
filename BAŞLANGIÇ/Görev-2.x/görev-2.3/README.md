# Sayıları Yazıyla Yazma Programı

## Proje Tanımı
Bu Python projesi, bir dosyada bulunan sayıları okur ve bu sayıları Türkçe olarak yazıya çevirir. Program, sayıları kelimelere dönüştürdükten sonra sonuçları başka bir dosyaya yazar.

## Kullanım
Kullanıcı, programın çalıştırılacağı sayıların bulunduğu dosyanın adını girdikten sonra, program dosyadaki sayıları okur, her sayıyı Türkçe kelimelere çevirir ve sonuçları `kelime.txt` dosyasına yazar.

### Adımlar

1. **Dosya Okuma**:
   - Kullanıcıdan bir dosya adı istenir.
   - Dosya içinde bulunan sayılar okunur ve bir listeye alınır.
   - Her satırda bir sayı olmalıdır. Hatalı girdi varsa kullanıcıya uyarı verilir.

2. **Sayıları Yazıya Çevirme**:
   - Okunan sayılar, Türkçe kelimelere dönüştürülür. Örneğin `123` sayısı "yüz yirmi üç" şeklinde yazıya çevrilir.
   - Hem pozitif hem de negatif sayılar desteklenir. Negatif sayılar "eksi" kelimesiyle başlar.

3. **Sonuçları Dosyaya Yazma**:
   - Her sayının karşısında yazıya çevrilmiş hali olacak şekilde sonuçlar `kelime.txt` dosyasına yazılır.

## Örnek Kullanım
### Girdi:
```python
Dosya adını giriniz: sayilar.txt
```

### sayilar.txt İÇERİĞİ:
```python
123
456
789
```
### kelime.txt İÇERİĞİ:
```python
123 --> yüz yirmi üç
-------------
456 --> dört yüz elli altı
-------------
789 --> yedi yüz seksen dokuz
-------------
```

