# ISBN Kontrol Uygulaması

Bu Python uygulaması, bir dosyadan ISBN kodlarını okuyarak geçerliliklerini kontrol eder ve sonuçları belirtilen bir dosyaya yazar. Hem ISBN-10 hem de ISBN-13 formatlarını destekler.

## Özellikler

- **ISBN-10 Kontrolü**: ISBN-10 formatındaki kodların geçerliliğini kontrol eder.
- **ISBN-13 Kontrolü**: ISBN-13 formatındaki kodların geçerliliğini kontrol eder.
- **Dosya Okuma/Yazma**: Kullanıcıdan alınan dosya adlarından ISBN kodlarını okur ve sonuçları yeni bir dosyaya yazar.

## Kullanım

### Gereksinimler

- Python 3.x
- Gerekli kütüphaneler yok.

### Kurulum

1. Proje dosyalarını bilgisayarınıza indirin.
2. Bir terminal veya komut istemcisi açın ve proje dizinine gidin.

### Çalıştırma

Aşağıdaki komut ile programı çalıştırın:

### Girdi Formatı:
- Girdi dosyasında her satıra bir ISBN kodu gelecek şekilde düzenleyin. Kodlar, her iki formatta (10 veya 13) olabilir ve - karakteri içerebilir.

### Çıktı Formatı
- Sonuçlar, belirtilen çıkış dosyasına yazılacaktır. Her satırda orijinal ISBN kodu ve geçerlilik durumu gösterilecektir.

### ÖRNEK 
#### Girdi Dosyası (input.txt)
```bash
978-3-16-148410-0
0-306-40615-2
123456789X
```
#### Çıktı Dosyası (output.txt)
```bash
9783161484100 -> geçerli kod!
0306406152 -> geçerli kod!
123456789X -> geçersiz kod!
```