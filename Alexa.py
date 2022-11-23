import time
import pyautogui
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import sys
import pywhatkit
from requests import get
import random
import cv2
import subprocess
import wolframalpha
import json
import MyAlarm
from typing import List
from playsound import playsound
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from twilio.rest import Client
import psutil

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        print(f"you said:> {command}\n")
    except Exception as e:
        return '0'
    command = command.lower()
    return command

# def takeCommand_hindi():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=5, phrase_time_limit=8)
#     try:
#         print("Recognizing.....")
#         command = r.recognize_google(audio, language='hi')
#         print(f"you said:> {command}")
#     except Exception as e:
#         # speak("please, say that again ....")
#         return 'none'
#     return command

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dcd7ffd4912e4595a87e3e268f9b2252'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        talk(f"today's {day[i]} news is: {head[1]}")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=5 and hour<12:
        talk("Hello sir, Good Morning")
        time = datetime.datetime.now().strftime('%I:%M %p')
        date = datetime.date.today()
        today = datetime.date.today()
        talk(f"its {time}\n and today's date is {today}\n")
        talk("i am Alexa, how may i help you!")

    elif hour>=12 and hour<17:
        talk("Hello sir, Good Afternoon")
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"its {time}")
        talk("i am Alexa, how may i help you!")

    elif hour>=17 and hour<21:
        talk("Hello sir, Good evening")
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"its {time}")
        talk("i am Alexa, how may i help you!")
    else:
        talk("Good night")
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"its {time}")
        talk("now it's time to goto sleep, and wakeup in early morning for worship")
        talk('if its important then, alexa is always there for you')

def taskExe():
    wishMe()
    while True:
        command = takecommand()
        if 'hey alexa' in command or 'hi' in command or 'hello' in command or 'hey' in command:
            talk('hello, welcome to alexa, how may i help you sir!')

        elif 'name' in command:
            talk("i am alexa, the personal assistant")

        elif 'help' in command:
            talk("yes, tell me, what you want, or what can i do for you")

        elif 'go to hell' in command or 'shut up' in command or 'get lost' in command or 'get out' in command:
            talk("how could you say that to your alexa, now i'm crying")
            print("Alexa is Crying.........")
            music_dir = "C:\\Users\\SHAIKH USMAN\\Music\\ringtone"
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'what can you do' in command:
            talk('''I am programmed to minor tasks like opening youtube,google chrome, gmail etc, predict time,
            take a photo, search wikipedia, predict weather In different cities, get top headline news from
            times of india and you can also ask me computational or geographical questions''')

        elif "made you" in command or "create you" in command or "discovered you" in command:
            talk("shaikh mohammed Osmaan, The AI developer, and he is make me using python")

        elif 'thanks' in command:
            talk("it's my pleasure sir!")

        elif 'who are you' in command:
            talk("i am alexa, the personal assistant")

        elif 'how are you' in command:
            talk("i am all good, tell me about you, how are you, and how's going your study")

        elif 'nice' in command:
                talk("ohhh that's grate")

        elif 'awesome' in command:
            talk("ok, what is your current year")

        elif 'year' in command:
            talk("how sweet")

        elif 'long-drive' in command:
            talk('sorry, it is impossiblea, i have a boyfriend')

        elif 'single' in command:
            talk('I am in a relationship with Amazon')

        elif 'boyfriend' in command:
            talk("obviously it's, dearest Amazon")

        elif 'love' in command:
            talk('sorry, i have a boyfriends')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"the time is {time}")

        elif 'date' in command:
            date = datetime.date.today()
            today = datetime.date.today()
            talk(today)

        elif 'joke' in command or 'comedy' in command:
            talk(pyjokes.get_joke())

        elif 'birthday' in command:
            talk("no, it's haraam in islaam, astag-firullah")
            webbrowser.open_new_tab("https://youtu.be/zBKHqnU-ui8")
            talk("this is some result i found on youtube, wishing birthday in islam by tariq-masood")
            time.sleep(3)

        elif 'diwali' in command:
            talk("no, it's haraam in islaam, astag-firullah")
            webbrowser.open_new_tab("https://youtu.be/01oK_7625tI")
            talk("this is some result i found on youtube, wishing happy diwali in islam by tariq-masood")
            time.sleep(3)

        elif 'christmas' in command:
            talk("no, it's haraam in islaam, astag-firullah")
            webbrowser.open_new_tab("https://youtu.be/JntJkV5I9eE")
            talk("this is some result i found on youtube, wishing happy christmas in islam by tariq-masood")
            time.sleep(3)

        elif 'mubarak' in command:
            talk("eid mubarak to you, and your family, alllah bless you")
            webbrowser.open_new_tab("https://youtu.be/6nJWB_Aiqzc")
            talk("this is some result i found on youtube related eid")
            time.sleep(3)

        elif 'open notepad' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\notepad.txt")
            talk("opening notepad")
            time.sleep(3)
        elif 'close notepad' in command:
            talk("ok as your wish, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            time.sleep(3)

        elif 'open windows powershell' in command:
            os.startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")
            talk("opening Windows PowerShell")
            time.sleep(3)
        elif 'close windows powershell' in command:
            talk("ok as your wish, closing Windows PowerShell")
            os.system("taskkill /f /im PowerShell.exe")
            time.sleep(3)

        elif 'open command' in command:
            os.system('start cmd')
            talk("opening command-prompt")
            time.sleep(3)
        elif 'close command' in command:
            talk("ok as your wish, closing command-prompt")
            os.system("taskkill /f /im cmd.exe")
            time.sleep(3)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
            talk("opening youtube")
            time.sleep(3)
        elif 'close youtube' in command:
            talk("ok as your wish, closing youtube")
            os.system("taskkill /f /im chrome.exe")
            time.sleep(3)

        elif 'open whatsapp' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk")
            talk('opening WhatsApp')
            time.sleep(3)
        elif 'close whatsapp' in command:
            talk("ok as your wish, closing whatsapp")
            os.system("taskkill /f /im whatsapp.exe")
            time.sleep(3)

        elif 'open google' in command:
            talk("opening google")
            talk('sir, what should i search on google?')
            cm = takecommand().lower()
            webbrowser.open("google.com")
            time.sleep(3)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            talk("opening G-Mail ")
            time.sleep(3)

        elif 'play on youtube' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(3)

        elif 'wikipedia' in command:
            talk('Searching Wikipedia...')
            about = command.replace('wikipedia', '')
            info = wikipedia.summary(about, 3)
            talk('According to Wikipedia')
            print(info)
            talk(info)
            time.sleep(3)

        elif 'play naat' in command:
            talk('here i found some naat')
            music_dir = 'C:\\Users\\SHAIKH USMAN\\Music\\NAAT'
            song = os.listdir(music_dir)
            rd = random.choice(song)
            song = os.startfile(os.path.join(music_dir, rd))
            time.sleep(3)

        elif 'play surah' in command:
            talk('here i found some surah')
            music_dir = 'C:\\Users\\SHAIKH USMAN\\Music\\SURAH'
            song = os.listdir(music_dir)
            rd = random.choice(song)
            song = os.startfile(os.path.join(music_dir, rd))
            time.sleep(3)

        elif 'play poetry' in command or 'play shaayri' in command:
            talk('here i found some poetry by allaamaa iqbaal')
            music_dir = 'C:\\Users\\SHAIKH USMAN\\Music\\ALLAMA IQBAL'
            song = os.listdir(music_dir)
            print(song)
            rd = random.choice(song)
            song = os.startfile(os.path.join(music_dir, rd))
            time.sleep(3)

        elif 'ip' in command:
            ip = get('https://api.ipify.org').text
            talk(f"your ip address is {ip}")
            time.sleep(3)

        elif 'where i am' in command or 'current location' in command or 'where we are' in command:
            talk('wait sir, let me check')
            try:
                ip = get('https://api.ipify.org').text
                print(ip)
                url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
                geo_request = get(url)
                geo_data = geo_request.json()
                city = geo_data['city']
                country = geo_data['country']
                talk(f'sir im not sure, but i think we are in {city} city of {country} country')
            except Exception as e:
                talk("sorry sir, due to network issue i am not able to find our current location...")
                time.sleep(5)
                time.sleep(3)

        elif 'take screenshot' in command:
            talk('please tell me the name for this file')
            name = takecommand().lower()
            talk("please hold the screen for few second, i'm taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            talk("taking screenshot, is done")
            time.sleep(3)

        elif 'open pycharm' in command:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2021.2.3.lnk")
            talk('opening pycharm')
            time.sleep(3)
        elif 'close pycharm' in command:
            talk("ok as your wish, closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")
            time.sleep(3)

        elif 'open IntelliJ IDEA' in command:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\IntelliJ IDEA Community Edition 2021.2.1.lnk")
            talk('opening IntelliJ IDEA')
            time.sleep(3)
        elif 'close IntelliJ IDEA' in command:
            talk("ok as your wish, closing IntelliJ IDEA")
            os.system("taskkill /f /im idea64.exe")
            time.sleep(3)

        elif 'open microsoft excel' in command:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            talk('opening microsoft-excel')
            time.sleep(3)
        elif 'close Microsoft Excel' in command:
            talk("ok as your wish, closing  microsoft excel")
            os.system("taskkill /f /im Microsoft Excel.exe")
            time.sleep(3)

        elif 'open google-drive' in command:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Drive.lnk")
            talk('opening google-drive')
            time.sleep(3)
        elif 'close google-drive' in command:
            talk("ok as your wish, closing google-drive")
            os.system("taskkill /f /im GoogleDriveFS.exe")
            time.sleep(3)

        elif 'open microsoft team' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk")
            talk('opening microsoft-team')
            time.sleep(3)
        elif 'close microsoft team' in command:
            talk("ok as your wish, closing microsoft-team")
            os.system("taskkill /f /im Teams.exe")
            time.sleep(3)

        elif 'open imo' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Imo Messenger.lnk")
            talk('opening imo')
            time.sleep(3)
        elif 'close imo' in command:
            talk("ok as your wish, closing imo")
            os.system("taskkill /f /im ImoDesktopApp.exe")
            time.sleep(3)

        elif 'open firefox' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk")
            talk('opening firefox')
            time.sleep(3)
        elif 'close firefox' in command:
            talk("ok as your wish, closing firefox")
            os.system("taskkill /f /im firefox.exe")
            time.sleep(3)

        elif 'open recycle-bin' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Recycle Bin.lnk")
            talk('opening recycle-bin')
            time.sleep(3)
        elif 'close recycle-bin' in command:
            talk("ok as your wish, closing recycle-bin")
            os.system("taskkill /f /im Recycle Bin.lnk")
            time.sleep(3)

        elif 'open file explorer' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\File Explorer.lnk")
            talk('opening file explorer')
            time.sleep(3)
        elif 'close file explorer' in command:
            talk("ok as your wish, closing file explorer")
            os.system("taskkill /f /im File Explorer.lnke")
            time.sleep(3)

        elif 'open visual-studio' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
            talk('opening visual-studio')
            time.sleep(3)
        elif 'close visual-studio' in command:
            talk("ok as your wish, closing visual-studio")
            os.system("taskkill /f /im Code.exe")
            time.sleep(3)

        elif 'open uTorrent' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\uTorrent\\uTorrent.exe")
            talk('opening uTorrent')
            time.sleep(3)
        elif 'close uTorrent' in command:
            talk("ok as your wish, closing uTorrent")
            os.system("taskkill /f /im uTorrent.exe")
            time.sleep(3)

        elif 'open Control Panel' in command:
            os.startfile("C:\\Users\\SHAIKH USMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
            talk('opening Control Panel')
            time.sleep(3)

        elif 'switch window' in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")

        elif 'latest news' in command:
            talk("please wait, fetching the latest news")
            news()

        elif 'volume up' in command:
            talk('volume has been up')
            pyautogui.press('volumeup')

        elif 'volume down' in command:
            talk('volume has been down')
            pyautogui.press('volumedown')

        elif 'mute' in command:
            talk('volume has been muted')
            pyautogui.press('volumemute')

        elif 'unmute' in command:
            pyautogui.press('volumeunmute')
            talk('volume has been unmuted')

        elif 'set alarm' in command:
            talk('sir, please tell me the time to set the alarm')
            tt = takecommand()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".","")
            tt = tt.upper()
            MyAlarm.alarm(tt)

        elif 'camera' in command:
            talk("opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            time.sleep(3)

        elif "temperature" in command:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            talk(f"current {search} is {temp}")

        elif "activate how to do" in command:
            talk("How to do mode is activated")
            while True:
                talk("please tell me what you want")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how or "deactivate" in how:
                        talk("okay sir, how to do mode is deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        talk(how_to[0].summary)
                        talk('for closing this mode, you need to say, close it or exit')
                except Exception as e:
                    talk("sorry sir, i am not able to find this")

        elif "battery" in command or "power left" in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            talk(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                talk("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                talk("we should connect our system to charging point to charge our battery")
            elif percentage <= 15 and percentage <= 30:
                talk("we don't have enough power to work, please connect to charging")
            elif percentage <= 15:
                talk("we have very low power, please connect to charging the system will shutdown very soon")

        elif 'nothing' in command or 'sleep' in command or 'stop' in command or 'no thanks' in command or 'no' in command:
            talk('okay, alexa is going to sleep now, and system has been stopped')
            break
        talk('sir, do you have any work')

if __name__=='__main__':
    while True:
        permission = takecommand()
        if "wake up" in permission or "activate" in permission:
            talk("alexa is activated now")
            taskExe()
        elif "goodbye" in permission or "close the program" in permission:
            talk("ok bye, thanks for using alexa, have a nice day, we will meet again")
            sys.exit()
        else:
            talk("for using alexa, you need to say, activate alexa")

######################*****SLEEP LAP-TOP*******##########################################
        # elif "sleep" in command:
        #     talk("Ok , your pc will sleep in 10 seconds")
        #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        #
        # elif "restart" in command:
        #     talk("Ok , your pc will restart in 10 seconds make sure you exit from all applications")
        #     os.system("restart /r /t 5")
        #
        # elif "shutdown" in command:
        #     talk("Ok , your pc will log off in 10 seconds make sure you exit from all applications")
        #     os.system("shutdown /s /t 5")
        #     time.sleep(20)
###########################################################################