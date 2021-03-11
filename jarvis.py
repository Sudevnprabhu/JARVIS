import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import pytz 
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
 

def speak(audio):
 engine.say(audio) 
 engine.runAndWait() 
 

def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
        speak("Good Morning!")

   elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

   else:
        speak("Good Evening!")  

   speak("I am Jarvis Sir. Please tell me how may I help you")       



def takeCommand():

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        #speak("Say that again please....")
        print("Say that again please....")
        
        return "None"

    return query


if __name__=="__main__" :
   wishme()
   while True:

      query = takeCommand().lower()

      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'play' in query:
          song = query.replace('jarvis play','')
          speak('playing'+song)
          pywhatkit.playonyt(song)

      elif 'hi' in query:
          speak('hello sir, how can i help you')

      elif 'hello' in query:
          speak('hello sir, how can i help you')

      elif 'thank you' in query:
          speak('you are most welcome sir, i am always there for your help')

      elif 'search' in query:
          result = query.replace('jarvis search','')
          speak('searching'+result)
          pywhatkit.search(result)

      elif 'joke' in query:
          joke = pyjokes.get_joke()
          speak(joke)
          print(joke)

      elif 'date' in query:
          t_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
          speak(t_date.strftime('%d %b, of %Y'))
          print(t_date.strftime('%d %b, of %Y'))

      elif 'time' in query:
          t_now = datetime.datetime.now().strftime('%I:%M %p')
          speak('Sir now the time is' + t_now)
          print(t_now)

      elif 'open youtube' in query:
         webbrowser.open('youtube.com')

      elif 'open my mail' in query:
         webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

      elif 'open classroom' in query:
         webbrowser.open('https://classroom.google.com/u/0/c/NjQyMjM4NTk5MTFa')

      elif 'map' in query:
         webbrowser.open('https://www.google.com/maps/place/Harihar,+Karnataka/@14.5182084,75.7644467,11235m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3bba2bfcac49eab3:0x6e02db5f88c9a1b6!8m2!3d14.5152216!4d75.8071609')

      elif 'open google' in query:
         webbrowser.open('google.com') 

      elif 'open my insta' in query:
         webbrowser.open('https://www.instagram.com/sudev_snp/')  
      
      elif 'open my website' in query:
         webbrowser.open('https://sudevnprabhu.whjr.site/')  
          
      elif 'quit' in query:
         speak('Thank you for using me sir'+quit()) 

          
         
    