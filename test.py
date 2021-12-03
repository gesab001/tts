import json
import requests
import base64


f = open("payload.json", "r")

payload = json.loads(f.read())
f.close()

v = open("tts_google_voices.txt", "r")
voices = v.readlines()
v.close()
a = open("apikey.txt", "r")
apikey = a.read().strip()
a.close()

for line in range(0, len(voices)):
   print(str(line) +". " + voices[line] ) 
   

def getAudio(payload,apikey):
    print(payload)
    headers = {'Content-Type': 'application/json'}
    url ="https://texttospeech.googleapis.com/v1beta1/text:synthesize?key="+apikey
    r = requests.post(url, headers=headers, json=payload)
    print(r.url)
    a_string = json.loads(r.text)["audioContent"]
    my_str_as_bytes = str.encode(a_string)

    base64_message = a_string
    message_bytes = base64.b64decode(base64_message)

    print(message_bytes)
    with open("hello.mp3", "wb") as out:
            out.write(message_bytes)
            print('Audio content written to file "output.mp3"')

voiceChoice = int(input("voice type: "))
print(voices[voiceChoice])
choice = voices[voiceChoice].split(",")
Language = 	choice[0]
Voicetype = choice[1]	
Languagecode =choice[2]
Voicename= choice[3]	
SSMLGender   = choice[4]

print("Language: " + Language)
print("Voice type: " + Voicetype)
print("Language code: " + Languagecode)
print("Voicename: " + Voicename)
print("SSMLGender: " + SSMLGender)
inputText = input("type text: ")
payload["input"]["text"]= inputText.strip()
payload["voice"]["languageCode"]= Languagecode.strip()
payload["voice"]["ssmlGender"]= SSMLGender.strip()
payload["voice"]["name"]= Voicename.strip()

getAudio(payload, apikey)