#!/usr/bin/env python3
# Simples script para execucao de comandos de voz
# O codigo foi baseado no exemplo presente em
# https://pythonspot.com/en/speech-recognition-using-google-speech-api/
#
# Mateus-n00b, Dezembro 2016
#
# Versao 1.0
#
# Licensa GPL
# -================================================================-

import speech_recognition as sr
import pyttsx,os
import commands
import pyaudio


# To speak
engine = pyttsx.init()
# Record Audio
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        speak("What do you need sir?")
        # print "What do you need sir?"
        audio = r.listen(source)

except Exception as e:
    print "Arggg, something goes wrong!"
    raise e

# Speech recognition using Google Speech Recognition
try:
    # Get the commands from the commands.py
    cmds = commands.Commands()
    cmds = cmds.getCommand()
    for x in cmds.keys():
        if x in str(r.recognize_google(audio)).lower():
            os.system(cmds[x])
            break
        else:
            print "You said "+r.recognize_google(audio)
except sr.UnknownValueError:
    print "What do you said?"
except sr.RequestError as e:
    print "Could not request results from Google Speech Recognition service; {0}".format(e)

def speak(text):
    engine.say(text)
    engine.runAndWait()
