import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import winsound
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)         # to listen
            command = listener.recognize_google(voice)  # to listen and convert it into words
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)                                   # to talk to anything
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("Playing " + song)
        pywhatkit.playonyt(song)            # to play on youtube. song could be name
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%P')
        print(time)
        talk("Current time is " + time)
    elif 'wikipedia' or 'who' or 'search' in command:
        person = command
        info = wikipedia.summary(person,10)
        print(info)
        talk(ifo)
    elif 'date' in command:

        winsound.PlaySound('masti.wav', winsound.SND_ASYNC)  # to play any windows music file
    elif 'joke' in command:
        talk(pyjokes.get_joke())
# run_alexa()
# talk('chal jaw pan yakka.......kum kur jaw kay')
