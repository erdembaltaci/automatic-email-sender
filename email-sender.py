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