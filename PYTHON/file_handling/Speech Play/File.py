import playsound
from gtts import gTTS

fd = open('arti.txt','r')
mytext = fd.read()
sp = gTTS(text=mytext,lang='en')

sp.save('python.mp3')

playsound.playsound('python.mp3')

fd.close()