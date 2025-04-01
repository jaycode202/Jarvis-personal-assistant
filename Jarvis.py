import os
import subprocess as sp
from decouple import config 
import pyttsx3
import speech_recognition as sr
import webbrowser
import keyboard
import psutil
import sys
from datetime import date
from datetime import datetime
from random import choice 
import random
import wikipedia 
import time 
import pyautogui
import pyjokes
import requests
from sympy import sympify, solve
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
from tkinter import Tk, Label
import google.generativeai as genai
import sympy 
import smtplib
import re
from gnews import GNews
from bs4 import BeautifulSoup
import wikipedia
import pywhatkit as kit 
from decouple import config
import json
import geocoder
from bs4 import BeautifulSoup
import lxml 


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
    speak("JARVIS here. How may i assist you?")


def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)



API_KEY = "a6f7817cc546fa8b76ca4c26f4933685"

def get_weather():
    # Get location (city name)
    g = geocoder.ip('me')
    city = g.city

    if not city:
        return "Sorry, I couldn't determine your location."

    # Fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=a6f7817cc546fa8b76ca4c26f4933685&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return "Sorry, I couldn't fetch the weather data."

    # Extract weather details
    weather_desc = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # Format response
    weather_report = f"The weather in {city} is {weather_desc}. The temperature is {temperature}°C with {humidity}% humidity."

    return weather_report


random_text = [
    "Right away",
    "just a moment",
    "awesome, getting on it",
    "Affirmative",

]

    
def increase_volume():
    pyautogui.press("volumeup")

def decrease_volume():
    pyautogui.press("volumedown")

def play_pause():
    pyautogui.hotkey('ctrl', 'p')  # Play/Pause
    time.sleep(3)

def stop():
    pyautogui.hotkey('ctrl', 's')  # Stop
    time.sleep(3)

def next():
    pyautogui.hotkey('ctrl', 'f')  #Next 
    time.sleep(3)

def prev():
    pyautogui.hotkey('ctrl', 'b')  #Previous 
    time.sleep(3)

def get_cpu_usage():
    """Returns CPU usage percentage."""
    usage = psutil.cpu_percent(interval=1)
    return f"Current CPU usage is {usage}%."

def get_memory_usage():
    """Returns RAM usage percentage."""
    memory = psutil.virtual_memory()
    return f"Current memory usage is {memory.percent}%."

def get_disk_usage():
    """Returns disk usage percentage."""
    disk = psutil.disk_usage('/')
    return f"Current disk usage is {disk.percent}%."

def get_network_usage():
    """Returns network usage (sent and received data)."""
    net_io = psutil.net_io_counters()
    return f"Sent data: {net_io.bytes_sent / (1024 * 1024):.2f} MB, Received data: {net_io.bytes_recv / (1024 * 1024):.2f} MB."

def get_battery_status():
    """Returns battery percentage and power status."""
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged = "plugged in" if battery.power_plugged else "not plugged in"
        return f"Battery is at {percent}%, and it is {plugged}."
    else:
        return "Battery information is not available."
    
def close_browser_tab():
    """Closes the current browser tab by first bringing it to focus."""
    try:
        time.sleep(1)  # Allow time to switch focus
        pyautogui.click(x=500, y=50)  # Adjust (x, y) to click on the browser tab
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')  # Close tab shortcut
        return "Closed the current browser tab."
    except Exception as e:
        return f"Error: {e}"

def get_today_date():
    """
    Returns today's date in a readable format.
    """
    today = date.today() 
    return today.strftime("%A, %B %d, %Y")  # Example: "Saturday, March 30, 2025"


def weather_report():
    report = get_weather()
    
    # Ensure UI update function exists
    try:
        app.update_output(report)  # Update UI (text box)
    except NameError:
        print(report)  # Fallback to print if UI method is not found

    speak(report)  # Make Jarvis speak


def get_news():
    """Fetches top 10 headlines from BBC and GNews API."""
    try:
        headlines = []

        bbc_url = "http://feeds.bbci.co.uk/news/rss.xml"
        response_bbc = requests.get(bbc_url, headers={"User-Agent": "Mozilla/5.0"})
        soup_bbc = BeautifulSoup(response_bbc.content, "xml")

        bbc_headlines = soup_bbc.find_all("title")[1:11]  # Skip the first one (it's the title of the feed)
        for headline in bbc_headlines:
            headlines.append(f"BBC: {headline.text.strip()}")

        gnews_url = "https://gnews.io/api/v4/top-headlines?token=7ede4071b18edd990e6a7a870cef2543&lang=en&max=10"
        response_gnews = requests.get(gnews_url)
        gnews_data = response_gnews.json()

        if "articles" in gnews_data:
            for article in gnews_data["articles"][:10]:
                headlines.append(f"GNews: {article['title']}")

        if not headlines:
            return "No news found at the moment."

        news_report = "\n".join(headlines)
        return news_report

    except Exception as e:
        return f"Error fetching news: {e}"

def solve_advanced_math(query):
    try:
        expression = sympy.sympify(query)  # Converting query into a math expression
        result = solve(expression)  # Solving the equation
        response = f"The solution is {result}"
    except Exception as e:
        response = "I couldn't solve that. Please try again."
    
    app.update_output(response)  # Shows in the UI
    speak(response)  # Speak the answer

def solve_math(expression):
    """Handles basic math calculations safely using SymPy."""
    try:
        result = sympify(expression)  # Converts input into a SymPy expression
        last_response = f"The answer is {result}"
        return last_response
    except Exception:
        return "Invalid mathematical expression."

    
# Set up the Gemini AI API
genai.configure(api_key="AIzaSyAjyd2SWljVm5CguR0naoEPPQzG6izVkIE")  # Replace with your actual API key
    
def ask_gemini(question):
    """Send a question to Gemini AI and get an answer."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(question)
        return response.text if response else "I'm not sure about that."
    except Exception as e:
        return f"Error: {str(e)}"


def tell_time():
    now = datetime.now()
    current_time = now.strftime('%I:%M %p')  # Example: 03:45 PM
    response = f"The time is {current_time}"
    app.update_output(response)  # Show in UI
    speak(response)  # Make Jarvis speak
        

def take_command():
        """Recognizes user voice input and updates the UI accordingly."""
        global app  # Make sure we can access `app` inside this function
       
        r = sr.Recognizer()
        with sr.Microphone() as source:
            app.show_listening()  # Show listening indicator

            r.adjust_for_ambient_noise(source, duration=1)
            r.energy_threshold = 500  # Adjust as per your environment
            r.dynamic_energy_threshold = False

            r.pause_threshold=1.0
            audio = r.listen(source)
            
            try:
                print("Recognizing.....")
                queri = r.recognize_google(audio, language='en')
                app.update_output(f"You Said: {queri}")
                if not 'stop' in queri or 'exit' in queri:
                    speak("")
                else:
                    hour = datetime.now().hour
                    if  hour >= 0 and hour < 18:
                        app.update_output("have a great day, take care!")
                        speak("have a great day, take care!")
                    else:
                        app.update_output("Have a good night, sweet dreams!")
                        speak("Have a good night, sweet dreams!")
                    root.destroy()  # Closes the UI
                    sys.exit()  # Exits the script completely


            except Exception:
                speak("sorry i did not understand. can you please repeat that?")
                queri = 'none'

            app.hide_listening()  # Hide the indicator after listening
            return queri

            

def voice_loop():
        greet_me()
        global last_response
        while True:
            query = take_command().lower()
            if "what is your name" in query:
                speak("My name is Jarvis, i am your personal assistant")

            elif "hey jarvis" in query:
                speak("hello Jarvis here")
            
            elif "how are you" in query:
                speak("am absolutely fine, how about you?")

            elif "fine" in query or "good" in query or "awesome" in query:
                speak("it's good to know that you are fine .")

            elif "i'm not fine" in query or "i'm not feeling well" in query or "i'm under the weather" in query:
                speak("sorry thats bad to hear kindly visit the nearest clinic for medical help")

            elif "who created you" in query:
                app.update_output("i was created by Mr Jackson Godfrey Banda, his my creator. ")
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

            elif "open vlc" in query:
                speak(choice(random_text))
                speak("opening vlc for you")
                vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
                os.startfile(vlc_path)

            elif "close vlc" in query:
                speak(choice(random_text))
                speak("closing vlc for you")
                vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
                sp.run('taskkill /F /IM vlc.exe', shell=True)

            elif "open windows media player" in query:
                speak(choice(random_text))
                speak("opening windows media player for you")
                wmp_path = 'C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe'
                os.startfile(wmp_path)

            elif "close windows media player" in query:
                speak(choice(random_text))
                speak("closing windows media player for you")
                wmp_path = 'C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe'
                sp.run('taskkill /f /im wmplayer.exe', shell=True)


            elif "open smadav" in query:
                speak(choice(random_text))
                speak("opening smadav for you")
                smadav_path = 'C:\\Program Files (x86)\\SMADAV\\SMΔRTP.exe'
                os.startfile(smadav_path)

            elif "close smadav" in query:
                speak(choice(random_text))
                speak("closing smadav for you")
                smadav_path = 'C:\\Program Files (x86)\\SMADAV\\SMΔRTP.exe'
                sp.run('taskkill /f /im SMΔRTP.exe', shell=True)

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
       
            elif "open microsoft excel" in query:
                speak(choice(random_text))
                speak("opening microsoft excel for you")
                excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                os.startfile(excel_path)

            elif "close microsoft excel" in query:
                speak(choice(random_text))
                speak("closing microsoft excel for you")
                excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                sp.run('taskkill /F /IM EXCEL.EXE', shell=True)

            elif "open microsoft publisher" in query:
                speak(choice(random_text))
                speak("opening microsoft publisher for you")
                publisher_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE'
                os.startfile(publisher_path)

            elif "close microsoft publisher" in query:
                speak(choice(random_text))
                speak("closing microsoft publisher for you")
                publisher_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE'
                sp.run('taskkill /F /IM MSPUB.EXE', shell=True)

            elif "open microsoft powerpoint" in query:
                speak(choice(random_text))
                speak("opening microsoft power point for you")
                pp_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                os.startfile(pp_path)

            elif "close microsoft powerpoint" in query:
                speak(choice(random_text))
                speak("closing microsoft power point for you")
                pp_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                sp.run('taskkill /F /IM POWERPNT.EXE', shell=True)
            
            elif "open microsoft access" in query:
                speak(choice(random_text))
                speak("opening microsoft access for you")
                access_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE'
                os.startfile(access_path)

            elif "close microsoft access" in query:
                speak(choice(random_text))
                speak("closing microsoft access for you")
                access_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE'
                sp.run('taskkill /F /IM MSACCESS.EXE', shell=True)
            
            elif "open microsoft onenote" in query:
                speak(choice(random_text))
                speak("opening microsoft one note for you")
                onenote_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE'
                os.startfile(onenote_path)

            elif "close microsoft onenote" in query:
                speak(choice(random_text))
                speak("closing microsoft one note for you")
                onenote_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE'
                sp.run('taskkill /F /IM ONENOTE.EXE', shell=True)

            elif "open microsoft outlook" in query:
                speak(choice(random_text))
                speak("opening microsoft out look for you")
                outlook_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
                os.startfile(outlook_path)

            elif "close microsoft outlook" in query:
                speak(choice(random_text))
                speak("closing microsoft outlook for you")
                outlook_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
                sp.run('taskkill /F /IM OUTLOOK.EXE', shell=True)

            elif "open calculator" in query: 
                speak(choice(random_text))
                speak("opening calculator for you")
                calculator_path = 'C:\\Windows\\system32\\calc.exe'
                os.startfile(calculator_path)

            elif "close calculator" in query or "dismiss calculator" in query:
                speak(choice(random_text))
                speak("closing calculator for you")
                calculator_path = 'C:\\Windows\\system32\\calc.exe'
                sp.run('taskkill /f /im CalculatorApp.exe', shell=True)

            elif "open settings" in query:
                speak(choice(random_text))
                speak("opening windows system settings for you")
                settings_path = 'C:\\Windows\\ImmersiveControlPanel\\SystemSettings.exe'
                os.system("start ms-settings:")

            elif "close settings" in query:
                speak(choice(random_text))
                speak("closing windows system settings for you")
                settings_path = 'C:\\Windows\\ImmersiveControlPanel\\SystemSettings.exe'
                sp.run('taskkill /f /im SystemSettings.exe', shell=True)

            elif "open microsoft store" in query:
                speak(choice(random_text))
                speak("opening microsoft store")
                os.system("start ms-windows-store:")

            elif "close microsoft store" in query:
                speak(choice(random_text))
                speak("closing microsoft store")
                sp.run("taskkill /F /IM WinStore.App.exe", shell=True)

            
            elif "play music" in query:
                speak(choice(random_text))
                music_dir = 'C:\\users\\jackson\\music'
                jams = os.listdir(music_dir)
                rd = random.choice(jams)
                os.startfile(os.path.join(music_dir, rd))

            elif "play movie" in query or "put a movie on" in query:
                speak(choice(random_text))
                movie_dir = 'C:\\users\\jackson\\videos'
                film = os.listdir(movie_dir)
                rd = random.choice(film)
                os.startfile(os.path.join(movie_dir, rd))

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
                app.update_output(results)  # Show in UI

            elif "wikipedia" in query:
                speak("searching wikipedia.....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=4)
                speak("according to wikipedia")
                app.update_output(results)  # Show in UI
                speak(results)
                

            elif "open amazon" in query: 
                speak(choice(random_text))
                speak("opening amazon for you")
                webbrowser.open("https://www.amazon.com")

            elif "open instagram" in query: 
                speak(choice(random_text))
                speak("opening instagram for you")
                webbrowser.open("https://www.instagram.com/")

            elif "open whatsapp" in query:
                speak(choice(random_text))
                speak("opening whatsapp for you")
                webbrowser.open("https://web.whatsapp.com")

            elif "open gmail" in query:
                speak(choice(random_text))
                speak("opening gmail for you")
                webbrowser.open("https://mail.google.com/")

            elif "open facebook" in query: 
                speak(choice(random_text))
                speak("opening facebook for you")
                webbrowser.open("https://www.facebook.com")

            elif "open netflix" in query: 
                speak(choice(random_text))
                speak("opening netflix for you")
                webbrowser.open("https://www.netflix.com/zm/")

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                app.update_output(joke)  # Show in UI
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

            #elif "cpu status" in query:
                #cpu()

            elif "cpu" in query:
                response = get_cpu_usage()
                app.update_output(response)
                speak(response)

            elif "memory" in query:
                response = get_memory_usage()
                app.update_output(response)
                speak(response)

            elif "battery" in query:
                response = get_battery_status()
                app.update_output(response)
                speak(response)

            elif "disc" in query or "disk" in query:
                response = get_disk_usage()
                app.update_output(response)
                speak(response)

            elif "network" in query:
                response = get_network_usage()
                app.update_output(response)
                speak(response)


            elif "solve" in query or "evaluate" in query:
                equation = query.replace("solve", "").strip()
                solve_advanced_math(equation)  # Use SymPy for equation

            elif "find" in query:
                expression = query.replace("find", "").strip()  
                response = solve_math(expression)  # Call function with user input
                app.update_output(response)  # Print or send to UI
                speak(response)  # Speak the result

            elif "ip address" in query:
                speak(choice(random_text))    
                ip_address = find_my_ip()
                response = f"Your IP Address: {ip_address}"
                app.update_output(response)  # Show in UI
                speak(response)
                
            elif "weather" in query:
                weather_report()

            elif "today's date" in query or "what is the date" in query:
                date_info = get_today_date()
                app.update_output(date_info)
                speak(date_info)  # Make Jarvis speak

            elif "news" in query:
                news = get_news()
                app.update_output(news)
                speak(news)

                                            
            elif "increase volume" in query:
                increase_volume()

            elif "decrease volume" in query:
                decrease_volume()

            elif "play" in query or "pause" in query:
                play_pause()

            elif "next" in query:
                next()

            elif "previcious" in query:
                prev()

            elif "where is" in query:
                location = query.replace("where is", "").strip()  # Remove "where is" and clean spaces
                if location:  
                    app.update_output("Locating .......")
                    speak(f"Locating {location}")
                    formatted_location = location.replace(" ", "+")  # Convert spaces to '+' for URL
                    time.sleep(1)  # Pause before opening
                    webbrowser.open(f"https://www.google.co.in/maps/place/{formatted_location}")
                else:
                    speak("I didn't catch the location. Can you repeat?")

            elif "close tab" in query or "close browser tab" in query:
                app.update_output("closing tab")
                speak("closing tab")
                close_browser_tab()

            elif "what is" in query or "explain" in query or "define" in query or "calculate" in query:
                response = ask_gemini(query)
                app.update_output(response)
                speak(response)
                 
            
# User Interface UI
class JarvisUI:
    def __init__(self, root, gif_path = "Jarvis.gif"):
        self.root = root
        icon_path = "favicon.ico"
        try:
                root.iconbitmap(icon_path)
        except Exception as e:
                print(f"Error setting icon: {e}")
        self.root.title("Jarvis Your Personal Assistance ")
        self.root.geometry("1020x600")
        self.root.configure(bg="#1e1e1e")  # Dark background
        
        
        # Allow the UI to resize professionally
        self.root.columnconfigure(0, weight=3)  # Left side (GIF + Text)
        self.root.columnconfigure(1, weight=1)  # Right side (Listening Indicator)
        self.root.rowconfigure(0, weight=1)

        # Main Frame
        main_frame = tk.Frame(root, bg="#1e1e1e")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

         # Left Frame (GIF + Text Box)
        left_frame = tk.Frame(main_frame, bg="#1e1e1e")
        left_frame.pack(side="left", fill="both", expand=True)

        # Load and Display GIF
        self.image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.image)]
        self.frame_index = 0
        self.gif_label = tk.Label(left_frame, image=self.frames[self.frame_index], bg="#1e1e1e")
        self.gif_label.pack()

        # Output Text Box (Inside a Frame)
        output_frame = tk.Frame(left_frame, bg="#1e1e1e")
        output_frame.pack(pady=10, fill="both", expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(output_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Output Text Area
        self.output_text = tk.Text(
            output_frame, height=10, wrap="word",
            font=("Consolas", 12), bg="#2d2d2d", fg="#00ffcc",
            insertbackground="white", relief="flat", padx=5, pady=5
        )
        self.output_text.pack(side="left", fill="both", expand=True)
        self.output_text.config(state="disabled")  # Read-only
        self.scrollbar.config(command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)

        # Right Side (Listening Indicator)
        # Right Frame (Listening Indicator)
        right_frame = tk.Frame(main_frame, bg="#1e1e1e")
        right_frame.pack(side="bottom", fill="y", padx=20)

        # "Listening" Label (Above the Indicator)
        self.listening_label = tk.Label(right_frame, text="Listening...", fg="white", font=("Arial", 11, "bold"), bg="#1e1e1e")
        self.listening_label.pack(pady=10)
        self.listening_label.pack_forget()  # Hide initially

        # "Listening" Indicator (Red Circle)
        self.indicator_canvas = tk.Canvas(right_frame, width=35, height=35, bg="#1e1e1e", highlightthickness=0)
        self.indicator_canvas.pack()
        self.indicator = self.indicator_canvas.create_oval(5, 5, 35, 35, fill="#1e1e1e")  # Hidden by default

        # Start GIF Animation
        self.update_gif()


    def update_gif(self):
        """Update the GIF animation."""
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.gif_label.config(image=self.frames[self.frame_index])
        self.root.after(100, self.update_gif)

    def update_output(self, text):
        """Update the output text box with Jarvis responses."""
        self.output_text.config(state="normal")
        self.output_text.insert("end", text + "\n", "tag")
        self.output_text.config(state="disabled")
        self.output_text.see("end")  # Auto-scroll
        self.output_text.tag_config("tag", spacing1=5, spacing3=5)

    def show_listening(self):
        """Turn on the listening indicator."""
        self.listening_label.pack()  # Show "Listening..."
        self.indicator_canvas.itemconfig(self.indicator, fill="red")  # Turn red

    def hide_listening(self):
        """Turn off the listening indicator."""
        self.listening_label.pack_forget()  # Hide "Listening..."
        self.indicator_canvas.itemconfig(self.indicator, fill="#1e1e1e") 

# Run the application
if __name__ == "__main__":  
    root = tk.Tk()
    app = JarvisUI(root, "Jarvis.gif")  # Replace with your GIF file path

   # Start voice assistant in a separate thread
    threading.Thread(target=voice_loop, daemon=True).start()
    
    root.mainloop()
