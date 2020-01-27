from gtts import gTTS
from tkinter import filedialog
from tkinter import *
import pytesseract
from PIL import Image
import os
from moviepy.editor import *
import sys
lan = 'en'
if len(sys.argv)==0 :
	path = filedialog.askopenfilenames()[0]
else:
	path= str(sys.argv[1:])[2:-2]
img = Image.open(path)
i2w, i2h = img.size
if i2w%2 != 0:
	i2w = i2w + 1
if i2h%2 != 0:
	i2h = i2h + 1
img2 = img.crop((0,0,i2w,i2h))	
img2.save("image.png")
say = pytesseract.image_to_string(img2);
obj = gTTS(text=say, lang=lan, slow=False)
inp2=path[path.rfind('/')+1:path.rfind('.')]
obj.save(inp2 + ".mp3")
audio = AudioFileClip(inp2 + ".mp3");
dur = int(audio.duration) + 1
os.system('ffmpeg -t '  + str(dur) + ' -loop 1 -r 15 -i ' + "image.png" +' -i ' + inp2+'.mp3 -shortest -pix_fmt yuv420p ' + inp2 + ".mp4")
os.system('rm '+ inp2+'.mp3')
os.system('rm ' + "image.png")
