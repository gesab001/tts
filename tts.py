# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
import json
import subprocess  
import keyboard
# The text that you want to convert to audio
history = []
keyboard.on_press_key("enter", lambda _:print("You pressed enter"))


def getHistory():
  fopen = open("tts_history.json", "r")
  history = json.loads(fopen.read())
  return history
def saveHistory():
  with open("tts_history.json", "w") as outfile:
    json.dump(history, outfile, sort_keys=True, indent=4)
def play(mytext):
      language = 'en'
      
      # Passing the text and language to the engine, 
      # here we have marked slow=False. Which tells 
      # the module that the converted audio should 
      # have a high speed
      myobj = gTTS(text=mytext, lang=language, slow=False)
      
      # Saving the converted audio in a mp3 file named
      # welcome 
    
      myobj.save("welcome.mp3")
      
      # Playing the converted file
      command = "ffplay -autoexit -nodisp welcome.mp3"
      subprocess.call(command, shell=False)
      

      
while True:
    mytext = input('input: ')
    if len(mytext)==0:
      history = getHistory ()
      print(history)
      for x in range(0, len(history)):
        print(str(x) + " " + history[x])
    elif mytext.isdigit():
        print(mytext)    
        mytext = history[int(mytext)]  
        play(mytext)
    else:
      history.append(mytext)  
      history.sort()
      saveHistory()
      play(mytext)
      # Language in which you want to convert


