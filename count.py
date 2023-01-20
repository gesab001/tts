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
      
count = 20
mytext = "" 


      
while count>0:
    play(str(count))
    count = count - 1
    time.sleep(1)

play("Ready or not, here I come")
 


