import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")


# contacts = ['a.com'， 'b.com']  #发送给多人

msg = EmailMessage()
msg["Subject"] = "Grab dinner"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "723547242@qq.com"  # contacts
msg.set_content("How about dinner at 6pm this night")

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
# 	smtp.ehlo()
# 	smtp.starttls()
# 	smtp.ehlo()
# 	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# 	subject = 'Grab dinner'
# 	body = 'How about dinner at 6pm this night'

# 	msg = f'Subject:{subject}\n\n{body}'
# 	smtp.sendmail(EMAIL_ADDRESS, '723547242@qq.com', msg)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# 	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# 	subject = 'Grab dinner'
# 	body = 'How about dinner at 6pm this night'

# 	msg = f'Subject:{subject}\n\n{body}'
# 	smtp.sendmail(EMAIL_ADDRESS, '723547242@qq.com', msg)

# with open('Maia - Ori1.jpg', 'rb') as f:
# 	file_data = f.read()
# 	file_type = imghdr.what(f.name)
# 	file_name = f.name

# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

files = ["Maia - Ori1.jpg", "Mia - Ori1.jpg"]
# files = ['resume.pdf']
for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)  # pdf文件时，不需要
        file_name = f.name
    msg.add_attachment(
        file_data, maintype="image", subtype=file_type, filename=file_name
    )
    # pdf文件时，maintype='application', subtype='octet-stream'


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
