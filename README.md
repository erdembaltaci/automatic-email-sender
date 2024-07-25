# automatic-email-sender

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
4. Oluşturulan uygulama şifresini not edin(bu adımda 16 haneli  random şifre oluşturulacak ve gerçek mail şifrenizi güvenle saklamaya devam edebileceksiniz), bu şifreyi Python betiğinde kullanacaksınız.

## Kullanım-1

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

<br>

3. Alıcı listenizi hazırlayın:
- Masaüstünüzde alıcılar.txt adında bir metin dosyası oluşturun ve göndermek istediğiniz e-posta adreslerini her satıra bir tane olacak şekilde listeleyin.```
- Dosyanın yolu aşağıdaki gibi olmalıdır:
- C:\\Users\\x\\OneDrive\\Masaüstü\\alıcılar.txt

 <br>

4. Betiği çalıştırın:
- python email_sender.py

## Kullanım-2

Kodu manuel olarak kopyalayarak:
- 'email_sender.py' dosyasını oluşturun ve aşağıdaki kodu yapıştırın:
   <br>
  ```bash
   import smtplib
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText

   def send_email(smtp_server, smtp_port, smtp_user, smtp_password, to_email, subject):
       msg = MIMEMultipart()
       msg['From'] = smtp_user
       msg['To'] = to_email
       msg['Subject'] = subject

       # HTML E-posta gövdesi
       email_body = f"""
       <html>
       <body>
           <p>Mail Başlığı</p>
           <p>
               Mail Gövdesi
           </p>
           <p>Teşekkür veya mail sonu</p>
       </body>
       </html>
       """
    
       msg.attach(MIMEText(email_body, 'html'))

       try:
           server = smtplib.SMTP(smtp_server, smtp_port)
           server.starttls()
           server.login(smtp_user, smtp_password)
           server.sendmail(smtp_user, to_email, msg.as_string())
           server.quit()
           print(f'E-posta başarıyla gönderildi: {to_email}')
       except Exception as e:
           print(f'E-posta gönderilemedi: {to_email}, Hata: {str(e)}')

   def main():
       # Mail gönderme platformunuzun SMTP sunucusu bilgileri örneğin 'Gmail'
       smtp_server = 'smtp.gmail.com'  # Gmail SMTP sunucu adresi
       smtp_port = 587  # genellikle SMTP portu 587'dir, ancak değişiklik gösterebilir
       smtp_user = 'your_gmail_account@gmail.com'  # gmail hesabınızın kullanıcı adı
       smtp_password = '**********'  # gmail 'uygulama şifresi'

       # recipients.txt dosyasının yeni yolu
       recipients_file_path = 'C:\\Users\\x\\OneDrive\\Masaüstü\\alıcılar.txt'  # Masaüstünde olduğunu varsayıyoruz

        try:
           with open(recipients_file_path, 'r') as f:
               recipients = f.read().splitlines()
        except FileNotFoundError:
           print(f'Dosya bulunamadı: {recipients_file_path}')
           return

       subject = 'Hello I am Developer'
       # E-posta gövdesi oluşturulduğu için `body` değişkenine gerek yok.

       for recipient in recipients:
           send_email(smtp_server, smtp_port, smtp_user, smtp_password, recipient, subject)

   if __name__ == '__main__':
       main()
- Betiği SMTP sunucu bilgilerinizle güncelleyin:
  email_sender.py dosyasını düzenleyin ve aşağıdaki değişkenleri kendi bilgilerinizle güncelleyin:
   <br>
   ```bash
      smtp_server = 'smtp.gmail.com'
      smtp_port = 587
      smtp_user = 'your_gmail_account@gmail.com'
      smtp_password = 'your_app_password'  # Gmail uygulama şifreniz
- Alıcı listenizi hazırlayın:
  Masaüstünüzde alıcılar.txt adında bir metin dosyası oluşturun ve göndermek istediğiniz e-posta adreslerini her satıra bir tane olacak şekilde listeleyin. Dosyanın    yolu aşağıdaki gibi olmalıdır:
   <br>
   ```bash
     C:\\Users\\x\\OneDrive\\Masaüstü\\alıcılar.txt
   
- Betiği çalıştırın:
 <br>
  Betiği herhangi bir Python IDE'sinde (PyCharm, VS Code, vb.) veya komut satırında çalıştırabilirsiniz.
