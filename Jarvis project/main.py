import os
import subprocess as sp
from decouple import config 
import pyttsx3
import speech_recognition as sr
import webbrowser
import keyboard
import psutil
import sys
from datetime import datetime
from random import choice 
from conv import random_text
from online import search_on_google,search_on_wikipedia,youtube,weather_forecast,find_my_ip
from openai import OpenAI
import random
import wikipedia 
import time 
import pyautogui
import pyjokes
import requests
from sympy import sympify
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


# Initialize the text-to-speech engine
def intialise_engine(): 
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-45)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

HOSTNAME = config('BOT')

def speak(audio):
    engine = intialise_engine()
    engine.say(audio)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if hour >= 0 and hour <12:
        speak(f"Good Morning ")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon")
    else:
        speak(f"Good evening ")
    speak(f"{HOSTNAME} here. How may i assist you?")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = str(psutil.sensors_battery())
    speak("cpu is at" + battery)


def solve_math(expression):
    try:
        result = sympify(expression)
        speak(f"The result is {result}")
        print(f"Result: {result}")
        return result
    except Exception as e:
        speak("I couldn't evaluate the expression.")
        return f"Invalid expression: {e}"

def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        speak(f"The result is {result}")
        print(f"Result: {result}")
        return result
    except Exception as e:
        speak("I couldn't evaluate the expression.")
        return f"Error: {e}"


def tell_time():
    now = datetime.now()
    current_time = now.strftime('%I:%M %p')  # Example: 03:45 PM
    response = f"The time is {current_time}"
    print(response)
    speak(response)  # Make Jarvis speak

def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 300  # Adjust as per your environment
            r.dynamic_energy_threshold = False

            r.pause_threshold=1.0
            audio = r.listen(source)
            
            try:
                print("Recognizing.....")
                queri = r.recognize_google(audio, language='en-bri')
                print(f"you said:  {queri}")
                if not 'stop' in queri or 'exit' in queri:
                    speak("")
                else:
                    hour = datetime.now().hour
                    if  hour >= 0 and hour <18:
                        speak(" have a good day, take care!")
                    else:
                        speak("Have a good night, sweet dreams!")
                    exit()

            except Exception:
                speak("sorry i did not understand. can you please repeat that?")
                queri = 'none'
            return queri
          


# Run the application
if __name__ == "__main__":
    greet_me()
    while True:
    
        query = take_command().lower()
        if "hey jarvis" in query:
            speak("jarvis here, how can i assist you")
        
        elif "how are you" in query:
            speak("am absolutely fine, how about you?")

        elif "fine" in query or "good" in query:
            speak("it's good to know that you are fine .")

        elif "who created you" in query:
            speak("i was created by Mr Jackson Godfrey Banda, his my creator ")

        elif "who are you" in query:
            speak("i am Jarvis your personal AI assistant")

        elif "thanks" in query or "thank you" in query:
            speak("most welcome")

        elif "open command prompt" in query:
            speak(choice(random_text))
            speak("Opening command prompt")
            os.system('start cmd')
        
        elif "close command prompt" in query:
            speak(choice(random_text))
            speak("closing command prompt")
            sp.run('taskkill /f /im cmd.exe', shell=True)

        elif "open camera" in query:
            speak(choice(random_text))
            speak("Opening camera")
            sp.run('start microsoft.windows.camera:', shell=True)

        elif "close camera" in query:
            speak(choice(random_text))
            speak("closing camera for")
            sp.run('taskkill /f /im WindowsCamera.exe', shell=True)
        
        elif "open notepad" in query:
            speak(choice(random_text))
            speak("opening notepad for you")
            notepad_path = 'C:\\Windows\\notepad.exe'
            os.startfile(notepad_path)

        elif "close notepad" in query:
            speak(choice(random_text))
            speak("closing notepad for you")
            notepad_path = 'C:\\Windows\\notepad.exe'
            sp.run('taskkill /f /im notepad.exe', shell=True)

        elif "open explorer" in query:
            speak(choice(random_text))
            speak("opening explorer for you")
            explorer_path = 'C:\\Windows\\explorer.exe'
            os.startfile(explorer_path)

        elif "close explorer" in query:
            speak(choice(random_text))
            speak("closing explorer for you")
            explorer_path = 'C:\\Windows\\explorer.exe'
            sp.run('taskkill /f /im explorer.exe', shell=True)

        elif "open vlc" in query:
            speak(choice(random_text))
            speak("opening vlc for you")
            vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
            os.startfile(vlc_path)

        elif "close vlc" in query:
            speak(choice(random_text))
            speak("closing vlc for you")
            vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
            sp.run('taskkill /f /im vlc.exe', shell=True)

        elif "open winrar" in query:
            speak(choice(random_text))
            speak("opening winrar for you")
            WinRAR_path = 'C:\\Program Files\\WinRAR\\WinRAR.exe'
            os.startfile(WinRAR_path)

        elif "close winrar" in query:
            speak(choice(random_text))
            speak("closing winrar for you")
            WinRAR_path = 'C:\\Program Files\\WinRAR\\WinRAR.exe'
            sp.run('taskkill /f /im WinRAR.exe', shell=True)

        elif "open microsoft edge" in query:
            speak(choice(random_text))
            speak("opening microsoft edge for you")
            os.startfile('msedge.exe')

        elif "close microsoft edge" in query:
            speak(choice(random_text))
            speak("closing microsoft edge for you")
            os.system("taskkill /F /IM msedge.exe")

        elif "open chrome" in query: 
            speak(choice(random_text))
            speak("opening chrome for you")
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome_path)

        elif "close chrome" in query:
            speak(choice(random_text))
            speak("closing chrome for you")
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            sp.run('taskkill /f /im chrome.exe', shell=True)

        elif "open microsoft word" in query:
            speak(choice(random_text))
            speak("opening microsoft word for you")
            word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word_path)

        elif "close microsoft word" in query:
            speak(choice(random_text))
            speak("closing microsoft word for you")
            word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            sp.run('taskkill /F /IM WINWORD.EXE', shell=True)
        
        elif "play music" in query or "play songs" in query:
            speak(choice(random_text))
            music_dir = 'C:\\users\\jackson\\music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "open youtube" in query:
            speak(choice(random_text))
            speak("what do you want to play on youtube?")
            video = take_command().lower()
            youtube(video)


        elif "open google" in query:
            speak(choice(random_text))
            speak(f"what do you want to search on google")
            query = take_command().lower()
            search_on_google(query)

        elif "open wikipedia" in query:
            speak(choice(random_text))
            speak(f"what do you want to search on wikipedia")
            search = take_command().lower()
            results = search_on_wikipedia(search)
            speak(f"According to wikipedia, {results}")
            speak("i am printing it on terminal")
            print(results)

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open amazon" in query: 
            speak(choice(random_text))
            speak("opening amazon for you")
            webbrowser.open("https://www.amazon.com")

        elif "open whatsapp" in query:
            speak(choice(random_text))
            speak("opening whatsapp for you")
            webbrowser.open("https://web.whatsapp.com")

        elif "open facebook" in query: 
            speak(choice(random_text))
            speak("opening facebook for you")
            webbrowser.open("https://www.facebook.com")

        elif "open naijaprey" in query: 
            speak(choice(random_text))
            speak("opening naijaprey for you")
            webbrowser.open("https://www.naijaprey.tv")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "the time" in query:
            tell_time()

        elif "shutdown" in query or "turn off" in query:
            speak(choice(random_text))
            speak("hold on a second sir! your system is on its way to shutdown")
            speak("make sure all of your application are closed")
            time.sleep(5)
            sp.call(['shutdown', '/s'])

        elif "restart" in query:
            speak(choice(random_text))
            sp.call(['shutdown','/r'])

        elif "hibernate" in query:
            speak(choice(random_text))
            speak("hibernating .......")
            sp.call(['shutdown','/h'])
        
        elif "switch window" in query:
            speak(choice(random_text))
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "cpu status" in query:
            cpu()

        elif "mathematical calculations" in query:
            speak("Please say the mathematical expression.")
            expression = take_command().lower()
    
            if any(op in expression for op in ["+", "-", "*", "/", "**", "%"]):
              result = calculate_expression(expression)
            else:
              result = solve_math(expression)
              speak(f"The result is {result}")

        elif "solve" in query or "calculate" in query or "evaluate" in query:
            expression = query.replace("solve", "").replace("calculate", "").replace("evaluate", "").strip()
            solve_math(expression)

        elif "ip address" in query:
            speak(choice(random_text))    
            ip_address = find_my_ip()
            speak(f"your ip address is {ip_address}")
            print(f"ip address: {ip_address}")

        
        elif "what is the weather now" in query:
            speak(choice(random_text))
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city").text
            speak(f"getting weather report for your city {city}")
            weather,temp,feels_like = weather_forecast(city)
            speak(f"the current temperature is {temp}, but it feels like {feels_like}")
            speak(f"also the weather report talks about {weather}")
            speak("i am printing the weather info on screen")
            print(f"Description: {weather}\n Temperature: {temp}\n feels like: {feels_like}")

       