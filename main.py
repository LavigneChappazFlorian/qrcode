import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=1
)

qr.add_data('https://florian-lvgchp.netlify.app')
qr.make(fit='True')

img = qr.make_image(fill_color="black", back_color="white")
type(img)
img.save('qrcode/portfolio.png')