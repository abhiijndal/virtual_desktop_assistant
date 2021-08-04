import speech_recognition as sr 
import pyttsx3
import webbrowser
import wikipedia
import datetime
import pyjokes

def speak(audio):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        print('listening.........')

        r.pause_threshold=0.7

        audio=r.listen(source)

    try:
        print('recognizing.......')
        Query=r.recognize_google(audio,language='en')

        print(f'the command is:{Query}')

    except Exception as e:
        print(e)
        print('say that again')

        speak("I don't understand! please repeat")
        return 'None'

    return Query


def hey():
    print('hello sir/mam')
    #speak('tell me how may  I help you?')

def wish_me():
    hours=int(datetime.datetime.now().hour)

    if hours>0 and hours <12:
        speak("good morning sir")

    elif hours>=12 and hours<=18:
        speak("good afternoon sir")

    else:
        speak('good evening sir')

def time():
    hour=int(datetime.datetime.now().hour)
    Minutes=int(datetime.datetime.now().minute)  

    speak(f'{hour} hour and {Minutes} minutes')
    print(F'{hour} hour and {Minutes} minutes')
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)

    speak(F'current date is{day}-{month}-{year}')

if __name__== "__main__":
    wish_me()
    hey()
    #hello()
    while(True):
        
        query=takecommand().lower()

        if  "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")
            continue
        elif "hello" in query :
            speak('hello there! So good to talk to you, tell me how may I help you')
        
       
        elif 'open google'in query:
            speak("öpening google")
            webbrowser.open('www.google.com')
            continue

        elif 'open stackoverflow'in query:
           #speak("ópening stack overflow")
            webbrowser.open("www.stackoverflow.com")
            continue
        elif 'open duckduckgo' in query:
            speak('ópening duckduckgo')
            webbrowser.open('duckduckgo.com')
            continue

        elif 'open brave'in query:
            speak('opening brave')
            webbrowser.open('brave')
            continue

        elif 'goodbye'in query:
            speak('thankyou sir ')
            exit()

        elif 'wikipedia'in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia',"")
            res=wikipedia.summary(query,sentences=3)
            speak('according to wikipedia...')
            speak(res)
            print(res)
            continue

        elif 'tell me the time' in query:
            time()
            continue
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'tell me the  date' in query:
            date()
            continue
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            continue

        
        elif 'tell me your name' in query:
            speak("im, maxi sir your virtual desktop assistant")
            print("im, maxi sir your virtual desktop assistant")
            continue
    

        elif "how are you"in query:
            speak('Iam fine sir and you?')
            continue
        
       
        elif 'Iam fine'in query or 'Iam good ' in query:
            speak("its good to know that you are fine.")
            
        