#!/usr/bin/env python3


import speech_recognition as sr
import os
import commands


# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # print("You said: " + r.recognize_google(audio))

    cmds = commands.Commands()
    cmds = cmds.getCommand()
    for x in cmds.keys():
        if x in str(r.recognize_google(audio)).lower():
            os.system(cmds[x])
            break
        else:
            print r.recognize_google(audio)
            # print x
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
