import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as do 
import datetime as dt 
import wikipedia as wp
import pyjokes as pj

listener = sr.Recognizer()
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_command():
    try:
        with sr.Microphone() as source:
            print('listenning...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:   
                command = command.replace('alexa','')         
                
    except:
        pass
    return command

def run_alexa():
    command = input_command()
    print(command)

    if 'play' in command:
        song = command.replace('play','')
        talk('playing your order saheb')
        do.playonyt(song)    
    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+ time)
    elif 'who' in command:
        person = command.replace('who','')
        info = wp.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pj.get_joke())
    else:
        talk('please say the command again.')



run_alexa()