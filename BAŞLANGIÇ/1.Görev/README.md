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



