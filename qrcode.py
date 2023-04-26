# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import os

# enter the qr code value in the qrvalue.ini file and place in the same path of tool
qrvalue = "qrvalue.ini"

# if ini file not available in the tool path, then error log should be created
text_file = "error.log"

if os.path.exists(qrvalue):
	pass
else:
	print("\n qrvalue.ini is missing")
	f = open(text_file, "a+")
	f.write(str("qrvalue.ini is missing\n"))
	f.close()
	exit()

# String which represents the QR code
with open(qrvalue) as f:   # open the ini file
	ini = f.read()       # read the ini file

# Generate QR code
qr = pyqrcode.create(ini)

# Create and save the svg file naming "qrcode.svg"
qr.svg("qrcode.svg", scale = 8)

# Create and save the png file naming "qrcode.png"
qr.png('qrcode.png', scale = 6)

