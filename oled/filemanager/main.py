from luma.core.render import canvas
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont
from time import sleep
import os

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
font = ImageFont.load_default()

directory = os.listdir(os.getenv('HOME'))

count = 0

with canvas(device) as draw:
    for i in range(len(directory)):
        draw.text((0, count), str(directory[i]), font=font, fill=255)
        count = count + 10;


sleep(5)
device.command(0xAE) #off
