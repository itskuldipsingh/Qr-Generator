import qrcode

def create_qr(data, filename):
  # Create a QR code object with the data
  qr = qrcode.make(data)
  # Sanitize filename (remove special characters)
  sanitized_filename = "".join(c for c in filename if c.isalnum() or c in "_.-").lower() + ".png"
  # Save the QR code image
  qr.save(sanitized_filename)
# Get user input
text = input("Enter link/text to convert to QR: ")
# Extract first 10 characters (or all if less than 10)
filename = text[:10]  # Slice from start (index 0) to index 10 (excluding 10th character)
# Sanitize filename and create QR code
sanitized_filename = create_qr(text, filename)  
print("QR code created successfully! Saved as", sanitized_filename)
