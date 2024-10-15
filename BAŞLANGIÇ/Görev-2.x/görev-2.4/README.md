# Bütçe Takip Programı

## Proje Tanımı
Bu Python projesi, kişisel bütçenizi takip etmek için bir araç sağlar. Kullanıcı, gelir ve gider işlemlerini kaydedebilir, belirli tarih aralıklarında işlemleri filtreleyebilir ve toplam gelir, gider ve mevcut bakiyeyi görüntüleyebilir.

## Kullanım
Kullanıcı, işlemleri bir JSON dosyasına kaydedebilir. Program, işlemler üzerinde çeşitli fonksiyonlar sunar: gelir/gider ekleme, toplamları görüntüleme ve belirli tarih aralığında işlemleri filtreleme.

### Adımlar

1. **İşlem Ekleme**:
   - Kullanıcıdan işlem türü (`income` veya `expense`), miktar, kategori ve tarih bilgisi alınır.
   - İşlemin gerçekleşme süresi (saniye cinsinden) otomatik olarak hesaplanır ve kaydedilir.
   - İşlemler `budget.json` dosyasına kaydedilir.

2. **Toplamları Görüntüleme**:
   - Program, tüm gelir ve giderleri toplar ve kullanıcının mevcut bakiyesini hesaplar.

3. **Tarih Filtresi ile İşlemleri Görüntüleme**:
   - Kullanıcı, belirli bir başlangıç ve bitiş tarihi girerek bu tarihler arasındaki işlemleri görüntüleyebilir.

## Fonksiyonlar

### `read_json(filename)`
- Belirtilen JSON dosyasını okur ve işlemleri bir liste olarak döndürür. Dosya bulunamazsa yeni bir liste oluşturur.

### `write_json(transactions, filename)`
- İşlemleri belirtilen JSON dosyasına yazar.

### `add_transactions(transactions)`
- Yeni bir işlem ekler. Kullanıcıdan işlem türü, miktar, kategori ve tarih bilgisi istenir. İşlem süresi otomatik olarak hesaplanır.

### `total_budget(transactions)`
- Tüm gelir ve giderleri hesaplar ve mevcut bakiyeyi gösterir.

### `filter_date(transactions)`
- Belirli bir tarih aralığı içindeki işlemleri filtreler ve ekranda gösterir.

## Dosya
- **`budget.json`**: Tüm gelir ve gider işlemlerinin saklandığı JSON dosyasıdır.

## Örnek Kullanım

### Program Menüsü:
```bash
--- Bütçe Takip Programı ---
1. İşlem Ekle
2. Toplamları Görüntüle
3. Tarih Filtresi ile İşlemleri Görüntüle
4. Çıkış
Bir seçenek giriniz (1-4):
```

### İşlem Ekleme:
```bash
İşlem türünü seçiniz (income/expense): income
Para miktarı: 5000
Para harcadığınız kategoriyi giriniz: Salary
Tarih giriniz (YYYY-AA-GG): 2024-04-25
```

### Toplamları Görüntüleme:
```bash
Gelir : 5000
Gider : 2000
Bakiye : 3000
```
### Tarih Filtresi ile İşlemleri Görüntüleme:
```bash
Başlangıç tarihi giriniz (YYYY-AA-GG): 2024-01-01
Bitiş tarihi giriniz (YYYY-AA-GG): 2024-12-31
2024-04-25 - Income - 5000 - Salary saniye
```
