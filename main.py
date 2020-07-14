import pyqrcode
import png

# * The data
data = "https://www.youtube.com/channel/UC9X19m2Zugqi6b9Fw7TVkXw"
# * Making the code
QRC = pyqrcode.create(data)
# * The image
QRC.png("QR.png", scale=6)