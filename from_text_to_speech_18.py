# pip install pyttsx3
# engine - подача

import pyttsx3
engine  =  pyttsx3.init()
engine.say("Привет мир!")
engine.runAndWait()