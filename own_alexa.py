import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
         with sr.Microphone() as source:
             print('Listening...')
             voice=listener.listen(source)
             command=listener.recognize_google(voice)
             print(command)
             command=command.lower()
             
             if 'alexa' in command:
                engine.say(command) 
                command=command.replace('alexa','')
                print(command)
                talk(command)
    except:
           pass
    return command

def run_alexa():
    command=take_command()
   
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        print('playing..')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk ('current time is' +time)
    elif 'who is the ' in command:
        person=command.replace('who is the ','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk(' NO,I am singal ')
    elif 'joke' in command :
        talk(pyjokes.get_joke())
        return print(pyjokes.birthd_jock())
        # print(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
while True:
    run_alexa()