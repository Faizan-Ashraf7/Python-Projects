import qrcode
from PIL import Image
details = "Name: Faizan Ashraf\nCourse: BCA\nRoll Number: 18\n"
qr = qrcode.QRCode(
  version =1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4
)
qr.add_data(details)
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("my_det.png")
img.show()
print('QR created successfully')