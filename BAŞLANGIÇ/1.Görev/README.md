# İKİNCİ DERECEDEN DENKLEM ÇÖZME

## PROJE TANIMI
Bu Python projesi, ikinci dereceden bir denklemin köklerini hesaplamak için geliştirilmiştir. Kullanıcıdan denklemin katsayılarını alarak, denklemin köklerini bulur.

## KULLANIM
Kullanıcı, denklemin katsayılarını `a`, `b` ve `c` olarak girdikten sonra program, denklemin köklerini hesaplar. Program, geçerli bir `a` değeri girmediği sürece kullanıcıdan giriş alır.

### ADIMLAR

1. **Katsayı Girişi**:
   - Kullanıcıdan `a`, `b`, ve `c` katsayıları istenir.
   - `a` katsayısı sıfıra eşit olamaz; bu durumda kullanıcıdan tekrar giriş istenir.

2. **Diskriminant Hesabı**:
   - Diskriminant (`D = b^2 - 4ac`) hesaplanır.
   - Eğer `D` pozitifse iki gerçek kök bulunur; `D` sıfırsa bir gerçek kök bulunur; `D` negatifse kök yoktur.

3. **Kök Hesabı**:
   - Gerçek kökler `(-b ± √D) / (2a)` formülü ile hesaplanır.

### KOD ÖRNEKLERİ

```python
import math
print("Denklem ax^2 + bx + c olmak üzere;")
try:
    cont = True
    while cont:
        a = int(input("a katsayısını giriniz: "))
        if a == 0:
            cont = True
            print("a katsayısı 0'a eşit olamaz!")
        else:
            cont = False
    b = int(input("b katsayısını giriniz: "))
    c = int(input("c katsayısını giriniz: "))
    diskriminant = math.pow(b, 2) - 4 * a * c
    print(diskriminant)

    kok1 = (-b + math.sqrt(diskriminant)) / (2 * a)
    kok2 = (-b - math.sqrt(diskriminant)) / (2 * a) 
    print(kok1)
    print(kok2)
except ValueError:
    print("Kök yok!")