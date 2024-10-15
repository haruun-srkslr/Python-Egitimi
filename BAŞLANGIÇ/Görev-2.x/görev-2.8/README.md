# Magic 8 Ball Uygulaması

Bu Python uygulaması, kullanıcılara rastgele yanıtlar veren bir Magic 8 Ball deneyimi sunar. Kullanıcılar sorular sorabilir ve uygulama, önceden tanımlanmış yanıtlar arasından rastgele bir yanıt seçer. Ayrıca, kullanıcılar yeni yanıtlar ekleyebilir ve bu yanıtlar kalıcı olarak kaydedilir.

## Özellikler

- Kullanıcının sorularına rastgele yanıtlar verme.
- Kullanıcıdan yeni yanıtlar alma ve bunları dosyaya ekleme.
- Tüm yanıtları bir dosyada kaydetme.
- Programdan çıkmak için kolay bir yol (Q/q tuşuna basarak çıkma).

## Gereksinimler

- Python 3.x
- `yanitlar.txt` adlı bir dosya, uygulamanın çalışabilmesi için gereklidir. Bu dosya, uygulama çalıştırıldığında yanıtların bulunduğu yerdir.

## Kurulum

1. Python'un en son sürümünü bilgisayarınıza kurun.
2. Bu kodu bir dosyaya (örneğin `magic_8_ball.py`) yapıştırın.
3. Aynı dizinde `yanitlar.txt` adında bir dosya oluşturun ve içine yanıtlar ekleyin. (Örnek yanıtlar: "Evet", "Hayır", "Belki", "Tekrar dene", "Kesinlikle").

## Kullanım

1. Terminal veya komut istemcisine gidin ve dosyanın bulunduğu dizine geçin.
2. Aşağıdaki komutla uygulamayı çalıştırın:
   ```bash
   python magic_8_ball.py
