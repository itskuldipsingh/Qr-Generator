import qrcode

first_name = input("First name:")
last_name = input("Last name:")
email = input("Email:")
phone_number = input("Number:")

vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=CELL:{phone_number}
END:VCARD"""

img = qrcode.make(vcard)
img.save(first_name+"_Vcard.png")
print(f"QR code created successfully! Saved as {first_name}_Vcard.png")
