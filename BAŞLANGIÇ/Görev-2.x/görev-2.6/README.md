# DNA Dönüştürücü

## Proje Tanımı
Bu Python projesi, DNA dizilerini tanımlamak ve bunları tamamlayıcı dizilere dönüştürmek için geliştirilmiştir. Kullanıcıdan alınan DNA dizileri, belirtilen bir dosyadan okunur ve sonuçlar başka bir dosyaya yazılır.

## Kullanım
Kullanıcı, bir dosyadan DNA dizilerini okuyarak, bu dizileri tamamlayıcı dizilere dönüştürebilir. Dönüştürülen diziler belirtilen başka bir dosyaya kaydedilir.

### Adımlar

1. **DNA Dizilerinin Okunması**:
   - Kullanıcıdan, DNA dizilerini içeren bir dosyanın adı veya yolu istenir.
   - Dosyadaki her bir DNA dizisi okunur. Geçersiz karakterler içeren diziler için hata mesajı gösterilir.

2. **DNA Tanımlaması**:
   - Okunan her DNA dizisi, `dna_tanimlama` fonksiyonu kullanılarak tamamlayıcı dizisine dönüştürülür. 
   - DNA dizileri yalnızca "A", "T", "G" ve "C" karakterlerini içermelidir. Aksi halde hata mesajı gösterilir.

3. **Sonuçların Yazılması**:
   - Dönüştürülen tamamlayıcı DNA dizileri, kullanıcıdan alınan başka bir dosyaya yazılır.

## Fonksiyonlar

### `dna_tanimlama(dna)`
- Verilen DNA dizisini tamamlayıcı dizisine dönüştürür. Geçersiz karakterler için hata mesajı gösterir.

### `dosya_okuma(filename)`
- Belirtilen dosyadan DNA dizilerini okur ve geçerli dizileri bir liste olarak döndürür.

### `dosya_yazma(filename, islenmemis, islenmis)`
- Orijinal DNA dizilerini ve tamamlayıcı dizilerini belirtilen dosyaya yazar.

## Örnek Kullanım

### Giriş Dosyası:
#### dna.txt` adlı dosyada aşağıdaki DNA dizileri bulunabilir:
```bash
 ATGC GATTACA XYZ
```

### Çıktı dosyası:
```bash
ATGC -> TACG GATTACA -> CTAATGT
```