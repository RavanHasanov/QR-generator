import pyqrcode

url = input("enter url to generate qr code:")

qrCode = pyqrcode.create(url)
qrCode.svg("CRcode.svg",10)