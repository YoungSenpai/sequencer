from time import sleep
from luma.core.render import canvas
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont
import subprocess

class Program:
    title = ''
    path = ''
    cursor = False
    x = 0
    y = 0

    def __init__(self, title, path, cursor, x, y):
        self.title = title
        self.path = path
        self.cursor = cursor
        self.x = x
        self.y = y
    
    def getTitle(self):
        return self.title
    def getPath(self):
        return self.path
    def getCursor(self):
        return self.cursor
    def getX(self):
        return self.x
    def getY(self):
        return self.y

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()

programs = [Program('filemanager', '/filemanager/main.py', True, 5, 5), 
            Program('todo-list', '/todo-list/main.py', False, 5, 15)]

running = True

def main():

    cursorY = 5

    while running == True:

        keyboard = input()
        if str(keyboard) == 'up':
            cursorY -= 10
        if str(keyboard) == 'down':
            cursorY += 10
        if str(keyboard) == 'ok':
            for prog in range(len(programs)):
                if cursorY == programs[prog].getY():
                    print(programs[prog].getTitle())
                    subprocess.call(["python3.6", str(programs[prog].getTitle()) + "/main.py"])


        with canvas(device) as draw:
            draw.rectangle((0, cursorY, 75, cursorY+10), outline="white", fill="black")  #cursor

            draw.text((programs[0].getX(), programs[0].getY()),             #filemanager
                    str(programs[0].getTitle()), font=font, fill=255)
            draw.text((programs[1].getX(), programs[1].getY()),             #todo-list
                    str(programs[1].getTitle()), font=font, fill=255)
    
main()





