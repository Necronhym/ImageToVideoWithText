from gtts import gTTS
from tkinter import filedialog
from tkinter import *
import pytesseract
from PIL import Image
import os
from moviepy.editor import *
lan = 'en'
path = filedialog.askopenfilenames()[0]
say = pytesseract.image_to_string(Image.open(path));
obj = gTTS(text=say, lang=lan, slow=False)
inp2=path[path.rfind('/')+1:path.rfind('.')]
obj.save(inp2 + ".mp3")
audio = AudioFileClip(inp2 + ".mp3");
dur = int(audio.duration) + 1
os.system('ffmpeg -t '  + str(dur) + ' -loop 1 -r 15 -i ' +path +' -i ' + inp2+'.mp3 -shortest -pix_fmt yuv420p ' + inp2 + ".mp4")
os.system('rm '+ inp2+'.mp3')
