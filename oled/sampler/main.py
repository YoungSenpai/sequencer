from luma.core.render import canvas
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import datetime
from pygame import mixer

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
running = True
mixer.pre_init(22050, -8, 2, 512, None)
mixer.init()
font = ImageFont.load_default()

bpm = 1
stepscount = 8
path = 'samples/'
patterns = []

class Track:
    name = ''
    steps = []
    audio = None

    def __init__(self, name):
        self.name = name

class Pattern:
    tracks = [] 


def main():
    kick = Track("kick")
    kick.audio = mixer.Sound(path + kick.name + ".wav")

    snare = Track("snar")
    snare.audio = mixer.Sound(path + snare.name + ".wav")

    kick.steps = ['x','0','0','x','0','0','0','0']
    snare.steps =['0','0','0','0','x','0','0','0']
    
    mid = Pattern()
    mid.tracks = [kick, snare]

    x = 0

    while running == True:
         
        with canvas(device) as draw:
            draw.text((0, 0), kick.name + " " + " ".join(kick.steps), font=font, fill=255)
            
            draw.text((0, 10), snare.name + " " + " ".join(snare.steps), font=font, fill=255)

            for y in range(len(mid.tracks)):
                y1 = y
                y2 = y
                if (len(mid.tracks)-1) > y:
                    y2 = y + 1
                    y1 = y
                else:
                    y2 = y
                    y1 = y - 1
                if stepscount <= x:
                    x = 0
                
                if str(mid.tracks[y1].steps[x]) == 'x':
                    mid.tracks[y1].audio.play()
                    print("kick")
                if str(mid.tracks[y2].steps[x]) == 'x':
                    mid.tracks[y2].audio.play()
                    print("snare")
                x = x + 1
                time.sleep(0.2)

               



main()
