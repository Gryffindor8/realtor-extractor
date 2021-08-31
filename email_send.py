import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


def sent_mail(mail_content, sender_address, receiver_address, sender_pass):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Shopify new order recieved'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com')
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def inventry(product_title, product_sku, order_number, info, product_inventory, vendors=" ", vendor_web=" ",
             quantity=0):
    sender_address = "@gmail.com"
    sender_pass = ""
    if product_inventory >= 0:
        receiver_address = "1@gmail.com"
        mail_content = '''Hi,
        The {} sku {} in order {} is in stock and needs to be shipped out 
        to: {} '''.format(product_title, product_sku, order_number, info)
        sent_mail(mail_content, sender_address, receiver_address, sender_pass)
    if product_inventory < 0 and vendors == " ":
        receiver_address = "2@gmail.com"
        mail_content = '''Hi,Please send via usps or cheapest shipping method:,
        {} of {} item # {}
        to:{}
        Thank You!AviBoca Online Judaica '''.format(quantity, product_title,
                                                    product_sku, info)
        sent_mail(mail_content, sender_address, receiver_address, sender_pass)
    if vendors == "Artscroll" or vendors == "A&M Judaica":
        receiver_address = "3@gmail.com"
        mail_content = '''Hi,
        {} SKU {} in order {} is wholesaled with {} and needs you to place the 
        order through {} '''.format(product_title, product_sku, order_number, vendors, vendor_web)
        sent_mail(mail_content, sender_address, receiver_address, sender_pass)


# inventry("with > 0", "sku=1", "12132123", "its dummy order", 0)
# inventry("with > 0", "sku=1", "12132123", "its dummy order", -1, quantity=2)
# inventry("with > 0", "sku=1", "12132123", "its dummy order", -1, vendors="Artscroll", vendor_web="google.com")
data = requests.get(
    "https://steemd.com/@streetstyle?page=874").content
# fix_bytes_value = data.replace(b"'", b'"')
# my_json = json.load(io.BytesIO(fix_bytes_value))
# print(my_json)
print(data)
