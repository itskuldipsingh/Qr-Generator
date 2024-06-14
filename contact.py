import qrcode

first_name = "First name"
last_name = "Last name"
email = "name@email.com"
phone_number = "+91 1234567890"

vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=CELL:{phone_number}
END:VCARD"""

img = qrcode.make(vcard)
img.save('contact.png')
