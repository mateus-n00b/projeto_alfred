#!/usr/bin/env python
#coding: UTF-8


import pyttsx,os
import speech_recognition as sr
import time,sys

engine = pyttsx.init()
# GAMBIS
hour = time.asctime().split(' ')[3].split(':')[0]

if int(hour) < 12:
   engine.say('Good morning, Mr. '+os.getenv("USER"))
elif int(hour) >= 12 and int(hour) < 18:
    engine.say('Good aftermoon, Mr. '+os.getenv("USER"))
elif int(hour) >= 18 and int(hour) < 00:
    engine.say('Good night, Mr. '+os.getenv("USER"))

def readABook(book):
    a = open(book, 'r')
    for x in a.readlines():
        engine.say(x)
        time.sleep(0.3)
    engine.runAndWait()

def checkSystem():
     speak = pyttsx.init()
     os.system('bash check.sh')
     try:
        # speak.say('Ok, now checking memory usage')
        a = open("/tmp/outLogs", 'r')
        for x in a.readlines():
            speak.say(x)
            time.sleep(0.3)
        sys.exit()
     except:
            speak.say("Arggg, something goes wrong!")
     speak.runAndWait()


engine.runAndWait()
# readABook("/tmp/outLogs")
checkSystem()
