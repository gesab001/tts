# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
import json
import subprocess  
import keyboard
import time

# The text that you want to convert to audio
history = []

"""

Language Name	Language Code
Afrikaans	af
Irish	ga
Albanian	sq
Italian	it
Arabic	ar
Japanese	ja
Azerbaijani	az
Kannada	kn
Basque	eu
Korean	ko
Bengali	bn
Latin	la
Belarusian	be
Latvian	lv
Bulgarian	bg
Lithuanian	lt
Catalan	ca
Macedonian	mk
Chinese Simplified	zh-CN
Malay	ms
Chinese Traditional	zh-TW
Maltese	mt
Croatian	hr
Norwegian	no
Czech	cs
Persian	fa
Danish	da
Polish	pl
Dutch	nl
Portuguese	pt
English	en
Romanian	ro
Esperanto	eo
Russian	ru
Estonian	et
Serbian	sr
Filipino	tl
Slovak	sk
Finnish	fi
Slovenian	sl
French	fr
Spanish	es
Galician	gl
Swahili	sw
Georgian	ka
Swedish	sv
German	de
Tamil	ta
Greek	el
Telugu	te
Gujarati	gu
Thai	th
Haitian Creole	ht
Turkish	tr
Hebrew	iw
Ukrainian	uk
Hindi	hi
Urdu	ur
Hungarian	hu
Vietnamese	vi
Icelandic	is
Welsh	cy
Indonesian	id
Yiddish	yi
"""

def getHistory():
  fopen = open("tts_history.json", "r")
  history = json.loads(fopen.read())
  return history
def saveHistory(history):
  with open("tts_history.json", "w") as outfile:
    json.dump(history, outfile, sort_keys=True, indent=4)
def play(mytext):
      language = 'en'
      #mytext = "[1 Corinthians,13,4] Ang pag-ibig ay nagtitiis ng mahabang panahon, [at] mabait; ang pag-ibig sa kapwa ay hindi naiinggit; ang pag-ibig sa kapwa ay hindi nagmamapuri, hindi nagmamataas,Hindi kumikilos ng hindi karapat-dapat, hindi hinahanap ang kanyang sarili, hindi madaling magalit, hindi nag-iisip ng masama; Hindi nagagalak sa kasamaan, kundi nagagalak sa katotohanan;Tinitiis ang lahat ng bagay, pinaniniwalaan ang lahat ng bagay, lahat ng bagay ay inaasahan, lahat ng bagay ay tinitiis.  John Asher, please pray. repeat"
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
      
count = 0
mytext = "" 


def confirmRepeat(mytext):
  command = input("command: ")
  if command=="r":
    play(mytext)
  

def repeat(_mytext):
  mytext = _mytext
  print("repeat texxt")
  keyboard.on_press_key("ctrl", lambda _:confirmRepeat(mytext))
  counter = 1
  while True:
  
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed q Key!')

            break  # finishing the loop
    except:
      print("continue")
    play(mytext + " " + str(counter))
    counter = counter + 1
    time.sleep(1)
    
  
     
while True:
    options = ["history"] 
    print(options)
    mytext = input('input: ')
    if mytext=="history":
      history = getHistory ()
      print(history)
      for x in range(0, len(history)):
        print(str(x) + " " + history[x])
    elif mytext.isdigit():
        print(mytext)    
        mytext = history[int(mytext)]  
        if "repeat" in mytext:
           mytext = mytext.replace("repeat", "")
           repeat(mytext)
        else:
           play(mytext)   
    else:
      history.append(mytext)  
      history.sort()
      saveHistory(history)
      if "repeat" in mytext:

       mytext = mytext.replace("repeat", "")
       repeat(mytext)
      else:
        play(mytext)      
      # Language in which you want to convert


