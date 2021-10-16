from time import sleep, time
from types import new_class
import pyttsx3 
import speech_recognition as sr   
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokescli
import pyautogui
import news_module
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("happy to see to you again") 
     

def takeCommand():
  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f" you said: {query}\n")
        

    except Exception as e:
        print(e)    
        speak("i am sorry sir,i didn't get that,can you Say that again please...")  
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karunsharma1920@gmail.com', 'FLiCKFTW1920@#$')
    server.sendmail('karunsharma1920@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
         
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if 'go on ' in query:
            result = wikipedia.summary(query,nextsentences=2)
            speak(result)    

        elif ' open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif ' open google' in query:
            speak("opening google sir...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening satckoverflow sir..")
            webbrowser.open("stackoverflow.com")   


        elif 'friday play music' in query:
            
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'friday what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif ' open code' in query:
            speak("for sure sir..")
            codePath = "C:\\Users\\acer1.OMG\\AppData\\Local\\Programs\\Microsoft VS Code.exe"
            os.startfile(codePath)
       

        elif ' I want to send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("to whom do you want to email ,sir...")
                to = content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 
        elif 'how are you' in query:
            speak('i am fine sir, what about you sir')
                    
        elif  'goodbye friday' in query:
               speak('good night sir , i am going to sleep, if you need me , you can call me anytime')
               break
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            sleep(5)
            pyautogui.keyUp("alt")   
             
        #close program
        elif "close it" in query:
            speak("as your wish sir")
            os.system("TASKKILL /f /im iexplore.exe")    

        #jokes
        elif "tell me a joke" in query:
            joke = pyjokescli.get_joke()    
            speak(joke)

        elif "tell me news"    in query:
            speak("please wait sir ,today's headlines are ")
            query = news()