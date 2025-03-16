import requests
import wikipedia
import pywhatkit as kit 
from email.message import EmailMessage
import smtplib
from decouple import config
import json



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

def weather_forecast(city):
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7655debd7c6b07e7b80e7d96c53dca15"
    ).json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]['feels_like']
    return weather,f"{temp}""C",f"{feels_like}""C"