import qrcode

# taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

# Formate of upi id
# upi://pay?pa=UPI_ID&pn=Name&mc=MerchantCode&tid=TransactionId&tr=RefId&tn=Note&am=Amount&cu=Currency

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR code for each UPI ID
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code in image
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR code (you need to install pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
