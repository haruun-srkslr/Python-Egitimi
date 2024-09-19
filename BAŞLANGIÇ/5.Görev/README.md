# Stok Yönetim Sistemi 

## PROJE TANIMI
Bu Python tabanlı stok yönetim sistemi, kullanıcıların ürün eklemesine, mevcut ürünleri listelemesine, ürün çıkarmasına ve az olan ürünleri görüntülemesine olanak tanır. Basit bir menü arayüzü ile kullanıcı dostu bir deneyim sunmaktadır.

## KULLANIM
Kullanıcı, aşağıdaki seçeneklerden birini seçerek stok yönetim sistemine erişebilir:

1. **Ürün Ekle**: Stokta olmayan yeni bir ürün ekler.
2. **Ürünleri Listele**: Mevcut tüm ürünleri ve adetlerini listeler.
3. **Ürünleri Çıkar**: Stoktan belirli bir ürünü çıkarır.
4. **Az Olan Ürünleri Listele**: Stokta az kalan (5 veya daha az) ürünleri görüntüler.
5. **Çıkış**: Programdan çıkış yapar.




```python
stok = {}

def menü():
    while True:
        print("""
    1.ÜRÜN EKLE
    2.ÜRÜNLERİ LİSTELE
    3.ÜRÜNLERİ ÇIKAR
    4.AZ OLAN ÜRÜNLERİ LİSTELE
    Q.ÇIKIŞ
        """)
        secim = input("---SEÇİM YAPINIZ(1-4/Q)---")
        # Diğer fonksiyonlar burada çağrılmaktadır.

def urunEkle():
    ad = input("Eklenecek ürünü giriniz: ").strip()
    # Ürün ekleme işlemleri

def urunListele():
    if not stok:
        print("Ürün bulunamadı")
    else:
        for urun, adet in stok.items():
            print(f"{urun}: {adet}")

def urunCıkar():
    urunListele()
    # Ürün çıkarma işlemleri

def AzOlan():
    # Az kalan ürünleri listeleme işlemleri

menü()

