from luma.core.render import canvas
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import datetime
from pygame import mixer
import threading

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
running = True
mixer.init()
font = ImageFont.load_default()

thread = threading.Thread()


bpm = 1
stepscount = 8
path = 'samples/'
patterns = []

class Track:
    name = ''
    steps = []
    audio 

    def __init__(self, name):
        self.name = name
        audio = mixer.Sound(path + self.name + ".wav")
    

class Pattern:
    tracks = []


def render(pattern, el):
    print("start" + str(el))
    for x in range(0, len(pattern.tracks[el].steps)):
        if pattern.tracks[el].steps[x] == 'x':
            pattern.tracks[el].audio.play()
            print(str(pattern.tracks[el].name) + " | x")
        time.sleep(bpm / 120)



def main():
    kick = Track("kick")
    snare = Track("snar")
    kick.steps = ['x','0','0','0','x','0','0','0']
    snare.steps =['0','0','x','0','0','0','x','0']
    kick = mixer.Sound(path + kick.name + ".wav")
    snare = mixer.Sound(path + snare.name + ".wav")

    mid = Pattern()
    mid.tracks = [kick, snare]

    while running == True:
         
        with canvas(device) as draw:
            draw.text((0, 0), kick.name + " " + " ".join(kick.steps), font=font, fill=255)
            
            for x in range(0, len(mid.tracks)):
                thread = threading.Thread(target=render, name="Thread", args=(mid, x))
                thread.start()



main()