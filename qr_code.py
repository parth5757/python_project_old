import qrcode
# img = qr.make("https://www.candidroot.com/jobs/apply/freshers-interns-for-python-odoo-development-6")
# img.save("parth.png")
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.candidroot.com/jobs/apply/freshers-interns-for-python-odoo-development-6")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("parth.png")
