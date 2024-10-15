# VERİ SIKIŞTIRMA VE AÇMA PROGRAMI

## Proje Tanımı
Bu Python projesi, kullanıcıdan alınan veriyi sıkıştırmak (Run-Length Encoding yöntemi ile) ve daha sonra sıkıştırılmış veriyi açmak için geliştirilmiştir. Ayrıca, sıkıştırılmış ve orijinal veri dosyalara kaydedilirken hata durumları bir rapor dosyasına yazılmaktadır.

## Kullanım
Kullanıcıdan sıkıştırılmak istenen veri girdisi alınır ve sıkıştırma işlemi gerçekleştirilir. Sıkıştırılmış veri hem ekrana yazdırılır hem de `compressed.txt` dosyasına kaydedilir. Aynı zamanda, orijinal veri `input.txt` dosyasına kaydedilir. Sıkıştırılmış veri deşifre edilerek eski haline getirilir ve ekrana yazdırılır.

### Adımlar

1. **Veri Girişi**:
   - Kullanıcıdan sıkıştırılacak veri alınır.
   - Boş bir veri girildiğinde, kullanıcı tekrar veri girmeye yönlendirilir.

2. **Veri Sıkıştırma**:
   - Girilen veri, Run-Length Encoding (RLE) algoritması ile sıkıştırılır.
   - Tekrar eden karakterler sayılarak veri formatı şu şekilde oluşturulur: `[(tekrar sayısı, karakter)]`.
   
3. **Veri Kaydı**:
   - Girilen orijinal veri `input.txt` dosyasına kaydedilir.
   - Sıkıştırılmış veri `compressed.txt` dosyasına kaydedilir.

4. **Veri Açma**:
   - Sıkıştırılmış veri, tekrar orijinal haliyle deşifre edilir.

5. **Hata Yönetimi**:
   - Herhangi bir hata durumunda (dosya açma hatası, veri işleme hatası vb.) hata raporu `report.txt` dosyasına kaydedilir.

### GİRDİ 
```python 
Sıkıştırmak istediğiniz datayı giriniz: aaabbcccc
```

### ÇIKTI 
```python 
Sıkıştırılmış veri: [(3, 'a'), (2, 'b'), (4, 'c')]
Açılmış hali: aaabbcccc
```

