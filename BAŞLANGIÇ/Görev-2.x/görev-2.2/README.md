# KÜME OPERASYONLARI JSON PROGRAMI

## Proje Tanımı
Bu Python projesi, iki liste içeren bir JSON dosyasını okur ve bu listeler üzerinde küme operasyonları gerçekleştirir. Program, birleştirme (union), kesişim (intersection), ve fark (difference) işlemlerini gerçekleştirir. Sonuçlar bir JSON dosyasına kaydedilir ve işlem süreleri raporlanır.

## Kullanım
Kullanıcıdan, içinde `liste1` ve `liste2` anahtarlarına sahip bir JSON dosyası girişi alınır. Program, bu iki liste üzerinde belirtilen küme işlemlerini gerçekleştirir ve sonuçları başka bir JSON dosyasına yazar.

### Adımlar

1. **JSON Dosyası Okuma**:
   - Kullanıcıdan dosya adı ve konumu istenir.
   - JSON dosyası açılır ve `liste1` ve `liste2` anahtarlarına sahip iki liste alınır.
   - Eğer dosya ya da anahtarlar eksikse hata mesajları yazdırılır.

2. **Küme İşlemleri**:
   - `Union (Birleştirme)` işlemi: `liste1` ve `liste2` kümeleri birleştirilir ve işlem süresi hesaplanır.
   - `Intersection (Kesişim)` işlemi: İki kümenin ortak elemanları bulunur.
   - `Difference (Fark)` işlemi: `liste1`'den `liste2` elemanları çıkarılarak fark kümesi oluşturulur.

3. **Sonuçların JSON Dosyasına Kaydedilmesi**:
   - Tüm işlemlerin sonuçları, kullanıcının belirlediği bir JSON dosyasına kaydedilir.

### ÖRNEK KULLANIM
```python
Dosya adı ve konumunu giriniz! : data.json
Sonuç dosyasının adını yazınız: results.json
```

### data.json İÇERİĞİ
```python
{
    "liste1": [1, 2, 3, 4, 5],
    "liste2": [4, 5, 6, 7, 8]
}

```


### ÇIKTI
```python
{
    "union": {
        "result": [1, 2, 3, 4, 5, 6, 7, 8],
        "time": 0.00012
    },
    "intersection": {
        "result": [4, 5]
    },
    "difference": {
        "result": [1, 2, 3]
    }
}

```