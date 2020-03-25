from gtts import gTTS
import os, requests
from playsound import playsound
import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    playsound('call.mp3',True)
    print("Tell the Location : ",end='')
    audio=r.listen(source)
    
    try:
        city=r.recognize_google(audio)
        print(city+'\n')
    except:
        print("NOT PROPERLY AUDIBLE")

weather_url = "'http://api.openweathermap.org/data/2.5/weather"
ap_id = #Enter your app id here

#temp = requests.put(weather_url,data={"q":city,"appid":ap_id})
temp = requests.get('http://api.openweathermap.org/data/2.5/weather?q={0}&appid={ap_id}'.format(city, ap_id)).json()

feels = temp['weather'][0]['description']
temprature = temp['main']['temp']
temprature_new = 'Current Temperature is '+str(round((temprature-273.16), 1))+' degree celsius, '
feels_new = "and, outside, it is "+feels

weather = temprature_new+feels_new

language = 'en-us'
obj = gTTS(text=weather, lang=language, slow=False)

obj.save("welcome.mp3")
print(weather)
playsound('Welcome.mp3',True)
