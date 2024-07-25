# automatic-email-sender

# Email Sender

Bu proje, SMTP protokolünü kullanarak toplu e-posta göndermek için bir Python betiğidir. Betik, alıcıların e-posta adreslerini bir metin dosyasından okur ve her bir alıcıya önceden tanımlanmış bir HTML e-postası gönderir.

## Özellikler

- HTML formatında e-posta gönderir
- Alıcı e-posta adreslerini bir metin dosyasından okur
- E-posta göndermek için SMTP kullanır

## Gereksinimler

- Python 3.x
- `smtplib` (Python standart kütüphanesinde bulunur)
- `email` (Python standart kütüphanesinde bulunur)

## Gmail'den Uygulama Şifresi Alma

1. Google hesabınıza giriş yapın ve [Güvenlik Ayarları](https://myaccount.google.com/security) sayfasına gidin.
2. "Google'da oturum açma" bölümünde, "Uygulama şifreleri"ni seçin. (Bu seçenek, iki adımlı doğrulamayı etkinleştirmeniz gerekebilir.)
3. "Uygulama şifreleri" sayfasında, "Uygulama seç" ve "Cihaz seç" menülerinden uygun seçenekleri belirleyin ve "Oluştur" butonuna tıklayın.
4. Oluşturulan uygulama şifresini not edin, bu şifreyi Python betiğinde kullanacaksınız.

## Kullanım

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/erdembaltaci/automatic-email-sender.git
   cd email-sender
   
2. Betiği SMTP sunucu bilgilerinizle güncelleyin:
 - email_sender.py dosyasını düzenleyin ve aşağıdaki değişkenleri kendi bilgilerinizle güncelleyin:
 - smtp_server = 'smtp.gmail.com'
 - smtp_port = 587
 - smtp_user = 'your_gmail_account@gmail.com'
 - smtp_password = 'your_app_password'  # Gmail uygulama şifreniz


3. Alıcı listenizi hazırlayın:

  - Masaüstünüzde alıcılar.txt adında bir metin dosyası oluşturun ve göndermek istediğiniz e-posta adreslerini her satıra bir tane olacak şekilde listeleyin.
  - Dosyanın yolu aşağıdaki gibi olmalıdır:
  - C:\\Users\\x\\OneDrive\\Masaüstü\\alıcılar.txt


4. Betiği çalıştırın:
  - python email_sender.py
