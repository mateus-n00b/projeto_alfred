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
from subprocess import Popen, PIPE
import commands,time
import pyaudio


# To speak
engine = pyttsx.init()
# Record Audio
r = sr.Recognizer()
# Audio var
global audio

# +==============================+
#          FUNCTIONS
# +==============================+
def speak(text):
    engine.say(text)
    engine.runAndWait()

def addCommand(cmd):
        os.system('sed -i "s/#,/,\'%s\':\'%s\'\\n#,/" commands.py' % (cmd[0],cmd[1]))

def listen():
    with sr.Microphone() as source:
        speak("I'm ready to help you")
        print "I'm ready to help you"
        audio = r.listen(source)
    return str(r.recognize_google(audio)).lower()
# +==============================+
#              MAIN
# +==============================+
try:
    with sr.Microphone() as source:
        speak("What do you need sir?")
        print "What do you need sir?"
        audio = r.listen(source)

except Exception as e:
    speak("Arggg, something goes wrong!")
    raise e

# Speech recognition using Google Speech Recognition
try:
    # Get the commands from the commands.py
    cmds = commands.Commands().getCommand()
    for x in cmds.keys():
        if x in str(r.recognize_google(audio)).lower():
            os.system(cmds[x])
            speak("Executing %s" % (x))
            break

        elif 'addiction' in str(r.recognize_google(audio)).lower():
             print ("What is the nick of the command?")
             nick = listen()
             print ("What is the command?")
             cmd = listen()

             tp = (nick,cmd)
             addCommand(tp)

        elif 'search' in str(r.recognize_google(audio)).lower():
            search = listen()
            cmd = Popen(["bash engine.sh {0}".format(search)], stdout=PIPE, shell=True)
            saida, erro = cmd.communicate()
            speak("Showing the results")
            print saida,erro

        else:
            print ("You said "+r.recognize_google(audio))

except sr.UnknownValueError:
    print ("What do you said?")
except sr.RequestError as e:
    print "Could not request results from Google Speech Recognition service; {0}".format(e)
    time.sleep(1)
