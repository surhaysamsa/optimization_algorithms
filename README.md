# Optimizasyon Algoritmaları Ödevi

Bu depo, Optimizasyona Giriş dersi kapsamında öğrencilerin atanan optimizasyon algoritmalarını Python dilinde uygulamaları ve katkıda bulunmaları için oluşturulmuştur.

## Amaç

- Atanan algoritmanın orijinal makalesini incelemek ve anlamak.
- Algoritmanın Python kodunu yazmak ve bu depoya katkıda bulunmak.
- Algoritmanın temel özelliklerini ve çalışma mekanizmalarını açıklayan bir dokümantasyon hazırlamak.
- Git ve GitHub kullanarak gerçek bir yazılım geliştirme sürecini deneyimlemek.

## Depo Yapısı

```
OptimizationAlgorithms/
├── README.md
├── algorithms/
│   ├── ogrenci1_algoritmasi/
│   │   ├── algorithm.py
│   │   └── documentation.md
│   ├── ogrenci2_algoritmasi/
│   │   ├── algorithm.py
│   │   └── documentation.md
│   └── ...
```

## Katkıda Bulunma Adımları

1. **Depoyu Fork Edin**
   - GitHub hesabınıza giriş yapın.
   - Bu depoyu kendi hesabınıza fork edin.

2. **Depoyu Klonlayın**
   - Terminal veya komut satırını açın.
   - Fork’ladığınız depoyu bilgisayarınıza klonlayın:

   ```bash
   git clone https://github.com/kullanici_adiniz/OptimizationAlgorithms.git
   ```

3. **Yeni Bir Branch Oluşturun**
   - Kendi çalışmanızı yapmak için yeni bir branch oluşturun:

   ```bash
   git checkout -b kullanici_adiniz-algoritma
   ```

4. **Kendi Klasörünüzü Oluşturun**
   - `algorithms` klasörü altında kendi kullanıcı adınızı ve algoritma adınızı içeren bir klasör oluşturun:

   ```bash
   mkdir algorithms/kullanici_adiniz_algoritmasi
   ```

5. **Kodunuzu ve Dokümantasyonunuzu Ekleyin**
   - Klasörünüzün içine aşağıdaki dosyaları ekleyin:
     - `algorithm.py`: Algoritmanızın Python kodu.
     - `documentation.md`: Algoritmanın dokümantasyonu.

6. **Kod Başlığı**
   - `algorithm.py` dosyanızın başına aşağıdaki formatta bir bilgilendirme yazısı ekleyin (kendi bilgilerinizle güncelleyin):

   ```
   The original version of: [Algoritma Adı]

   # Created by "[Adınız]" on [Tarih] -----------------------------%
   #       Email: [Email Adresiniz]                                %
   #       Github: https://github.com/kullanici_adiniz             %
   # --------------------------------------------------------------%

   Links:
       1. [Orijinal yayının linki]
   References:
       [1] [Orijinal yayının tam referansı]
   ```

7. **Dokümantasyon Hazırlama**
   - `documentation.md` dosyanızda aşağıdaki bölümleri yazın:
     - Giriş
     - Temel Özellikler
     - Konum Güncelleme Denklemleri
     - Keşif ve Sömürü Mekanizmaları
     - Referanslar

8. **Değişikliklerinizi Commit Edin**
   - Değişikliklerinizi kaydedin ve commit edin:

   ```bash
   git add .
   git commit -m "Added [Algoritma Adı] by [Adınız]"
   ```

9. **Fork’unuza Push Edin**
   - Değişikliklerinizi kendi fork’unuza gönderin:

   ```bash
   git push origin kullanici_adiniz-algoritma
   ```

10. **Pull Request Oluşturun**
    - GitHub üzerinde fork’unuza gidin.
    - Ana depoya (hocanın deposuna) pull request gönderin.
    - Pull request açıklamasına çalışmalarınız hakkında bilgi ekleyin.

## Kodlama Standartları ve Kurallar

- **Kod Kalitesi**
  - Temiz, okunabilir ve yorum satırlarıyla desteklenmiş kod yazın.
  - PEP 8 Python kodlama standartlarına uygun hareket edin.
  - Değişken ve fonksiyon isimlerini anlamlı seçin.

- **Dosya ve Klasör Yapısı**
  - Kendi klasörünüzü `algorithms` klasörü altında oluşturun.
  - Dosya isimlendirmelerinde küçük harf ve alt çizgi kullanın ("algorithm.py" gibi).

- **Dokümantasyon**
  - Algoritmanın matematiksel denklemlerini ve çalışma prensiplerini detaylı bir şekilde açıklayın.
  - Gerekli görselleri veya denklemleri eklemek için uygun formatlar kullanın (Markdown formatında LaTeX kullanabilirsiniz).
  - Kullandığınız kaynakları ve referansları eklemeyi unutmayın.

- **Uyumluluk**
  - Kodunuzun, gerektiğinde mevcut test fonksiyonlarıyla uyumlu çalışabilmesini sağlayın.
  - Gerekli kütüphane ve bağımlılıkları belirtin.

## Git ve GitHub Kullanımı

- **Fork Etme ve Branch Oluşturma**
  - Depoyu fork ederek kendi GitHub hesabınıza kopyalayın.
  - Her öğrenci kendi branch’inde çalışmalıdır.

- **Commit Mesajları**
  - Anlamlı ve açıklayıcı commit mesajları kullanın ("Added Particle Swarm Optimization by Ahmet Demir" gibi).

- **Pull Request**
  - Pull request açıklamasında yaptığınız çalışmaları ve eklediğiniz özellikleri belirtin.
  - Gerekirse kodunuz hakkında notlar veya açıklamalar ekleyin.

## Kaynaklar

- **Git ve GitHub Rehberleri**
  - Git Başlangıç Rehberi
  - GitHub Pull Request Oluşturma

- **Markdown ve Dokümantasyon**
  - Markdown Kılavuzu
  - LaTeX Matematik Denklemleri

- **EvoloPy Projesi**
  - EvoloPy GitHub Deposu

## Teslim Tarihi

- Çalışmalarınızı [Teslim Tarihi] tarihine kadar gönderiniz.

## İletişim

- **Öğretim Görevlisi**: [İsminiz]
- **E-posta**: [E-posta Adresiniz]
- **Ofis Saatleri**: [Ofis Saatleri Bilgisi]

Herhangi bir sorunuz veya sorununuz olursa, lütfen iletişime geçmekten çekinmeyin.

## Notlar

- **Akademik Dürüstlük**
  - Tüm çalışmalarınız size ait olmalıdır. Alıntı yaptığınız veya referans verdiğiniz kaynakları mutlaka belirtin.
  - Plagiarizm ve intihal kabul edilmeyecektir.

- **İşbirliği**
  - Algoritmanın kavramlarını tartışabilirsiniz, ancak kod ve dokümantasyon bireysel olarak hazırlanmalıdır.

- **Teknik Destek**
  - Git ve GitHub kullanımıyla ilgili sorunlar yaşarsanız, belirtilen kaynakları inceleyin veya öğretim görevlisiyle iletişime geçin.

## Başarılar!

Çalışmalarınızda başarılar dilerim. Bu ödev, optimizasyon algoritmalarını derinlemesine anlamanız ve yazılım geliştirme sürecinde deneyim kazanmanız için harika bir fırsatır.
