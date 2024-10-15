# Roma Rakamı Dönüştürücü

## Proje Tanımı
Bu Python projesi, 0 ile 4000 arasında verilen tam sayıları Roma rakamlarına dönüştürmek için geliştirilmiştir. Kullanıcıdan alınan sayılar bir dosyadan okunur ve sonuçlar başka bir dosyaya yazılır.

## Kullanım
Kullanıcı, bir dosyadan sayıları okuyarak, bu sayıları Roma rakamlarına dönüştürebilir. Dönüştürülen rakamlar belirtilen başka bir dosyaya kaydedilir.

### Adımlar

1. **Sayıların Okunması**:
   - Kullanıcıdan, sayıları içeren bir dosyanın adı veya yolu istenir.
   - Dosyadaki her bir sayı okunur. Geçersiz veriler (sayı olmayan ifadeler) atlanır.

2. **Roma Rakamına Dönüştürme**:
   - Okunan her sayı, `int_to_sayi` fonksiyonu kullanılarak Roma rakamına dönüştürülür.
   - Dönüştürme işlemi sırasında sayı 0 ile 4000 arasında olmalıdır. Aksi halde hata mesajı gösterilir.

3. **Sonuçların Yazılması**:
   - Dönüştürülen Roma rakamları, kullanıcıdan alınan başka bir dosyaya yazılır.

## Fonksiyonlar

### `int_to_sayi(sayi)`
- Verilen tam sayıyı Roma rakamına dönüştürür. 0 ile 4000 arasında olmayan sayılar için hata mesajı gösterir.

### `dosya_okuma(filename)`
- Belirtilen dosyadan sayıları okur ve geçerli sayıları bir liste olarak döndürür. Dosya yoksa yeni bir dosya oluşturur.

### `dosyaya_yazma(romans, filename)`
- Dönüştürülen Roma rakamlarını belirtilen dosyaya yazar.

