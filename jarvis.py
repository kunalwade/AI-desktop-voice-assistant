import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Good morning Sir!!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("This is jarvis at your service sir!!")

def takeCommand():
    #it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)

        print("Pardon sir . Can you say that again!!")
        return None
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('wadekunal1234@gmail.com','hello')
    server.sendmail('wadekunal1234@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    speak("Hello Sir!! How you doing")
    wishMe()
    while True:
        if 1:
            query = takeCommand().lower()
            #logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia ")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("Youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
        
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
        
            elif 'play music' in query:
                music_dir = 'C:\\Users\\HP\\Music'
                songs = os.listdir(music_dir)
            
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
                os.startfile(codePath)

            elif 'email to kunal' in query:
                try:
                    speak("what should I say?")
                    content = takeCommand()
                    to = "wadekunal1234@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry sir there seems to be some problem")





