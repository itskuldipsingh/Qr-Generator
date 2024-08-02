import qrcode
import re

def create_qr(data):
    # Create a QR code object with the data
    qr = qrcode.make(data)
    # Sanitize filename (remove special characters)
    sanitized_data = re.sub(r'[^\w\-_. ]', '', data)
    sanitized_filename = f"qr_{sanitized_data[:10]}.png".lower()
    # Save the QR code image
    qr.save(sanitized_filename)
    return sanitized_filename

while True:
    # Get user input
    text = input("Enter link/text to convert to QR (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    # Create QR code and sanitize filename
    sanitized_filename = create_qr(text)
    print("QR code created successfully! Saved as", sanitized_filename)
