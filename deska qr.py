import qrcode

# Define the data you want to encode as a QR code
data = 'https://shopdeska.com/en-ca'

# Generate QR code
img = qrcode.make(data)

# Save the QR code as a PNG file
img.save('shopdeska_qr.png')