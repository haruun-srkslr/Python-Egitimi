# Collatz Simülasyonu

Bu Python uygulaması, Collatz Conjecture (Collatz Teoremi) üzerine bir simülasyon gerçekleştirir. Kullanıcıdan pozitif bir tam sayı alır ve bu sayıyı belirli kurallara göre dönüştürerek sonuca ulaşır. Her adımda üretilen sayılar ve adım sayısı bir dosyaya kaydedilir.

## Özellikler

- Kullanıcının girdiği pozitif tam sayılar için Collatz simülasyonu yapma.
- Her adımda elde edilen sayıları ve adım numarasını kaydetme.
- Kullanıcı çıkış yapmak için "q" tuşunu kullanabilir.

## Gereksinimler

- Python 3.x
- Yazma izinleri olan bir dosya konumu (çünkü sonuçlar `collatz.txt` dosyasına kaydedilecektir).

## Kurulum

1. Python'un en son sürümünü bilgisayarınıza kurun.
2. Bu kodu bir dosyaya (örneğin `collatz_simulation.py`) yapıştırın.

## Kullanım

1. Terminal veya komut istemcisine gidin ve dosyanın bulunduğu dizine geçin.
2. Aşağıdaki komutla uygulamayı çalıştırın:
```bash
python collatz_simulation.py
```
3.Uygulama, pozitif bir tam sayı girmenizi isteyecektir. Pozitif bir sayı girin.

4.Eğer programdan çıkmak isterseniz "q" tuşuna basın.

5.Uygulama, girilen sayıya göre adım adım dönüşümleri hesaplayacak ve sonuçları collatz.txt dosyasına kaydedecektir.