#Program name:python code for alexa to siya.

#Programmers Name :Adhav Vrushali Abasaheb.
#Date : 6 oct 2022
import playsound


from gtts import gTTS

fd = open('arti.txt','r')


#mytext = fd.read()


#sp = gTTS(text=mytext,lang='en')

#sp.save('python.mp3')

playsound.playsound('python.mp3')

fd.close()
