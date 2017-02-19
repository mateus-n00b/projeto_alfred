#!/usr/bin/env python
#coding: UTF-8


import pyttsx,os
import speech_recognition as sr
import time,sys

engine = pyttsx.init()
# GAMBIS
hour = time.asctime().split(' ')[3].split(':')[0]

def speak(text):
    engine.say(text)
    engine.runAndWait()

if int(hour) < 12:
   speak('Good morning, Mr. '+os.getenv("USER"))
elif int(hour) >= 12 and int(hour) < 18:
    speak('Good aftermoon, Mr. '+os.getenv("USER"))
elif int(hour) >= 18 and int(hour) < 23 :
    speak('Good night, Mr. '+os.getenv("USER"))

def readABook(book):
    fala = pyttsx.init()
    a = open(book, 'r')
    for x in a.readlines():
        fala.say(x)
        time.sleep(0.3)
    sys.exit()

def checkSystem():
     fala = pyttsx.init()
    #  os.system('bash check.sh')
     try:
        a = open("/tmp/outLogs", 'r')
        for x in a.readlines():
            fala.say(x)
            time.sleep(0.3)
        # sys.exit()
        engine.runAndWait()        
     except:
            speak("Arggg, something goes wrong!")

def addCommand(cmd):
    # Ugly command to add commands
    # os.system('sed -i "s/#,/,\'%s\':\'%s\'\\n#,/" commands.py' % (cmd.split(':')[0],cmd.split(':')[1]))
    os.system('sed -i "s/#,/,\'%s\':\'%s\'\\n#,/" commands.py' % (cmd[0],cmd[1]))

# readABook("/tmp/outLogs")
checkSystem()
