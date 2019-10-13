from time import sleep
from luma.core.render import canvas
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import Image

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)

with canvas(device) as draw:
    pic = Image.open('image.png')
    draw.bitmap((0, 0), pic, fill=255)


sleep(3)               # Wait 3 seconds.
device.command(0xAE)   # Display OFF.
sleep(1)               # Wait 1 second.
device.command(0xAF)   # Display ON.
sleep(1)
device.command(0xAE)
sleep(1)
device.command(0xAF)
