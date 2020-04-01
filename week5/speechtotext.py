# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 02:16:12 2020

@author: user
"""

import speech_recognition as s
Audio=("B.wav")
#use audio as file  source

r=s.Recognizer()
#initialise the recorder

with s.AudioFile(Audio) as source:
    audio=r.record(source)
    
#reads the audio file
    try:
        print("Audio File contains:", r.recognize_google(audio))
    except s.UnknownValueError:
        print("Google speech recogniser couldnot understand audio.")
    except s.RequestError:
        print("couldn't get the results.")
