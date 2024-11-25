import os
import PyPDF2
from PyPDF2 import PdfReader
import fitz
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import time
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
from win11toast import toast
import pyautogui
import json
from pytube import YouTube
import instaloader



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print((audio))
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listnening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}")
        return query

    except Exception as e:
        speak("Sorry Sir I can not understand...")
        return "none"

def news():
    # a61c267016124732bc178b1dc51fd025
    speak("which type of news you want?")
    type = takecommand().lower()
    mainUrl = f"https://newsapi.org/v2/everything?q={type}&apiKey=a61c267016124732bc178b1dc51fd025"
    speak("please sir wait, i am fetching the latest news...")
    mainPage =requests.get(mainUrl).json()
    article = mainPage["articles"]
    head = []
    day = ["first","second","third" ,"fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} about {type} news : {head[i]}")
def newsHeadlines():
    mainUrl = "https://newsapi.org/v2/top-headlines?country=us&apiKey=a61c267016124732bc178b1dc51fd025"
    speak("please sir wait, i am fetching the latest news...")
    mainPage = requests.get(mainUrl).json()
    article = mainPage["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} headline is : {head[i]}")

def PdfReader():
    def get_number_of_pages(pdf_path):
        pdf_document = fitz.open(pdf_path)
        num_pages = pdf_document.page_count
        pdf_document.close()
        return num_pages
    def read_specific_page(pdf_path, page_number):
        pdf_document = fitz.open(pdf_path)
        if page_number < 1 or page_number > pdf_document.page_count:
            pdf_document.close()
            error = speak("Invalid page number")
            return error
        page = pdf_document.load_page(page_number - 1)
        page_content = page.get_text()
        pdf_document.close()
        return page_content
    speak("Sir, please enter the PDF name and its path correctly.")
    pdf_path = input("Enter the path to the PDF file: ")
    num_pages = get_number_of_pages(pdf_path)
    speak(f"The PDF has {num_pages} pages.")
    speak("Sir, please enter the page number i have to read...")
    page_number = int(input(f"Enter a page number: "))
    page_content = read_specific_page(pdf_path, page_number)
    speak(f"Content of page {page_number}:\n{page_content}")

def instagram():
    speak("Please sir enter the username correctly.")
    name = input("Enter username here : ")
    webbrowser.open(f"www.instagram.com/{name}")
    speak(f"Sir,here is the profile of user {name}")
    time.sleep(8)
    speak("would you like to download profile picture of tis account?")
    cnm = takecommand().lower()
    if "yes" in cnm:
        mod = instaloader.Instaloader()
        mod.download_profile(name, profile_pic_only=True)
        speak("Sir, the profile picture is downloaded. Now I am ready for next command")
    else:
        pass
def ytDownloader():
    def on_progress(stream, chunk, bytes_remaining):
        speak("the file is downloading...")

    def on_complete(stream, file_path):
        speak("the file is successfully downloaded. Now I am ready for next command")

    speak("Sir,please enter the URL")
    url = input("enter URL : ")

    yt = YouTube(
            url,
            on_progress_callback=on_progress,
            on_complete_callback=on_complete,
            use_oauth=False,
            allow_oauth_cache=True
        )

    yt.streams.filter(file_extension='mp4', res="720p").first().download()

def sendEmail(to,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('arabasauda@gmail.com', 'naveedahmad12345')
    server.sendmail('arabasauda@gmail.com',to ,message)
    server.close()

def stonePaperScissor():
    while True:
        Choices = ["Stone", "Paper", "Scissors"]
        speak("Let's play the game...")
        speak("Sir,please chose one")
        speak("Stone, Paper, or Scissor")
        print("1 = Stone \n2 = Paper \n3 = Scissor")
        user = int(input("Enter Your Choice : "))
        if user == 1:
            print("You Choose Rock")
        elif user == 2:
            print("You Choose Paper")
        elif user == 3:
            print("You Choose Scissor")
        else:
            speak("Sir,please chose 1 or 2 or 3 only.")
        comp = random.choice([1, 2, 3])
        choices_dict = {1: "Computer Chose Stone", 2: "Computer Chose Paper", 3: "Computer Chose Scissors"}
        print(choices_dict[comp])

        def game(user, comp):
            if user == comp:
                rs = speak("Draw")
                return rs
            elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
                rsl = speak("Computer Wins, better luck next time.")
                return rsl
            else:
                rsw = speak("Congratilation Sir, you win")
                return rsw

        result = game(user, comp)
        print(result)
        speak("Sir do you want to play again?")
        play_again = input("Enter 'yes' to play again or 'no' to quit: ")
        if play_again.lower() != "yes":
            break

def date():
    crndate = time.strftime("%d %B, %Y")
    speak(f"Today, the date is {crndate}")
def day():
    day = time.strftime("%A")
    speak(f"Today is {day}")
def localtime():
    currenttime = time.strftime("%I:%M%p")
    speak(f"The time is {currenttime} ")
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >12  and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How can i help you,Sir")

def MainFunction():
   while True:

       query = takecommand().lower()
       sites = [["my website","https://naveedahmad.netlify.app/"],["facebook","https://www.facebook.com/"],["youtube","https://www.youtube.com/"],["gmail","https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],["instagram","https://www.instagram.com/?hl=en"],["w3school","https://www.google.com/search?q=w3schools+python&oq=w3&gs_lcrp=EgZjaHJvbWUqEggDEAAYQxiDARixAxiABBiKBTIRCAAQRRg5GEMYsQMYgAQYigUyEggBEAAYQxiDARixAxiABBiKBTISCAIQLhhDGMcBGNEDGIAEGIoFMhIIAxAAGEMYgwEYsQMYgAQYigUyEggEEAAYQxiDARixAxiABBiKBTIYCAUQLhhDGIMBGMcBGLEDGNEDGIAEGIoFMgwIBhAAGEMYgAQYigUyDAgHEAAYQxiABBiKBTIHCAgQABiPAtIBCTYxMzNqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.org/"],["stack overflow","https://stackoverflow.com/"]]
       for site in sites:
           if f"open {site[0]}" in query:
               webbrowser.open(site[1])
               speak(f"Opening {site[0]} Sir...")

       if "instagram profile" in query or "profile on instagram" in query:
           instagram()

       elif "set a alarm" in query:
           speak("Sir, can you please tell me, which time you want to set for alarm?")
           alarmTime = int(input("Enter hour : "))
           atn = int(datetime.datetime.now().hour)
           if atn == alarmTime:
               os.startfile("E:\\Alarm Tone\\videoplayback.m4a")
               toast("Alarm", "Remind Sir you set an alarm",buttons= ["Ok","No"] )
       elif "let's play" in query:
           speak("which game you want to play?")
           print("1 = Stone Paper Scissor")
           gm = int(input("enter here : "))
           if gm == 1:
               stonePaperScissor()
           else:
               speak("sorry sir,this game is not available")

       elif "how are you" in query:
           speak("i am good Sir, How are you")
           time.sleep(3)
           speak("Sounds good")
       elif "what is your name" in query or "who are you" in query:
           speak("My name is lucy")
       elif "thank you" in query or "thanks" in query or "thank u" in query:
           speak("Sir, its my pleasure.")
       elif "who i am" in query or "who am i"in query:
           speak("You are my boss Sir, and i am your assistant")
       elif "what is my name" in query:
           speak("Your name is : Muahmmad Naveed Ahmad")

       elif "tell me a joke" in query:
           joke = pyjokes.get_joke(language=ur-pk ,category=neutral)
           speak(joke)

       apps = [["control panel" ,"C:\\Users\\Mr.M.N.A\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"] , ["visual studio" , "C:\\Users\\Mr.M.N.A\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"], ["pycharm" , "C:\\Users\\Mr.M.N.A\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains Toolbox\\PyCharm Community.lnk"] , ["cap cut" ,"C:\\Users\\Mr.M.N.A\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CapCut\\CapCut.lnk" ] , ["screen recorder" ,"C:\\Users\\Mr.M.N.A\\Desktop\\Screen Recorder.lnk"] ,["live wallpaper" ,"C:\\Users\\Mr.M.N.A\\Desktop\\Lively Wallpaper.lnk"] , ["replit" , "C:\\Users\\Mr.M.N.A\\Desktop\\Replit.lnk"]]
       for app in apps:
           if f"open {app[0]}" in query:
               os.startfile(app[1])
               speak(f"Opening {app[0]} Sir...")

       folders = [["my pics" , "E:\\Mr.M.N.A"] , ["pyhton","D:\\Python"]]
       for folder in folders :
           if f"open {folder[0]} folder" in query:
               os.startfile(folder[1])
               speak(f"Opening {folder[0]} folder Sir...")

       if "what is time" in query or "tell me time" in query:
           localtime()
       elif "what is date" in query or "tell me date" in query:
           date()
       elif "what is day" in query:
           day()

       elif"download a file" in query:
           ytDownloader()

       elif "read pdf" in query or "read a pdf" in query:
           PdfReader()

       elif "open command prompt" in query:
           os.system("start cmd")
       elif "open camera" in query:
           cap = cv2.VideoCapture(0)
           while True:
               ret , img = cap.read()
               cv2.imshow('webcam',img)
               k = cv2.waitKey(50)
               if k == 27:
                   break;
               cap.release()
               cv2.destroyAllWindows()
       elif "play music" in query or "play a music" in query:
           music_dir = "E:\\My Mbl\\A s"
           songs = os.listdir(music_dir)
           rd = random.choice(songs)
           os.startfile(os.path.join(music_dir, rd))
       elif "ip address" in query:
           ip = get('https://api.ipify.org').text
           speak(f"Your ip address is {ip}")

       elif "where i am" in query or "where we are" in query or "what is my location" in query:
           speak("Please wait sir, let me check...")
           try:
               ip = requests.get('https://api.ipify.org').text
               url = "https://get.geojs.io/v1/ip/geo/" + ip +".json"
               geoRequest = requests.get(url)
               geoData = geoRequest.json()
               city = geoData['city']
               country = geoData['country']
               speak(f"Sir i am not sure, but we are in {city} city of {country} country")
           except Exception as e:
               speak("Sorry sir, i am not be able to find your location due to network problem")

       elif "search on wikipedia" in query:
           speak("searching wikipeida......")
           query = query.replace("wikipedia", input(""))
           results = wikipedia.summary(query,sentences = 2)
           speak("according to wikipedia....")
           speak(results)

       elif "open browser" in query:
           speak("Sir, What should i search on browser")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")

       if "send a message" in query:
           speak("Sir, please enter number without zero ")
           num = int(input("Enter number here : "))
           speak("Sir, please enter message what you want to send ")
           msg = input("enter message : ")
           kit.sendwhatmsg(f"+92 {num}", msg ,1,31)

       elif "send a email" in query :
           try:
               speak("What should i send?")
               message = takecommand().lower()
               to = "ugee633@gmail.com"
               sendEmail(to,message)
               speak("Email sent successfully")
           except Exception as e:
               print(e)
               speak("Sorry sir, Email did not sent")

       elif "switch the window" in query :
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
       elif "close the window" in query or "close window" in query:
           pyautogui.keyDown("alt")
           pyautogui.press("f4")
           time.sleep(1)
           pyautogui.keyUp("alt")
       elif "open settings" in query :
           pyautogui.keyDown("win")
           pyautogui.press("i")
           time.sleep(1)
           pyautogui.keyUp("win")
       elif "minimise" in query or "minimize" in query :
           pyautogui.keyDown("win")
           pyautogui.press("m")
           time.sleep(1)
           pyautogui.keyUp("win")
       elif "screenshot" in query:
           speak("sir,what name do you want to save this file?")
           name = takecommand().lower()
           speak("Sir,please hold the screen for few seconds, i am taking screenshot")
           time.sleep(3)
           img = pyautogui.screenshot()
           img.save(f"{name}.jpg")
           speak("the screenshot is save in our main folder")

       elif "tell me news" in query:
           speak("Sir, you want headlines or news?")
           cmo = takecommand().lower()
           if "headlines" in cmo:
               newsHeadlines()
           elif"news" in cmo:
               news()

       elif "hide" in query or "visible" in query:
           speak("Sir, tell me you want to hide this folder or make it visible for everyone")
           cmo = takecommand().lower()
           if "hide" in cmo :
               folderPath = "/d"
               os.system(f"attrib +h {folderPath}")
               speak("Sir, all files in this directory are now hidden")
           elif "visible" in cmo :
               folderPath = "/d"
               os.system(f"attrib -h {folderPath}")
               speak("Sir, all files in this directory are now visible for everyone")
           elif "leave" in cmo :
               speak("Okay Sir.")

       elif "shutdown" in query:
           os.system("shutdown /s /t 5")

       elif "restart the system" in query:
           os.system("shutdown /r /t 5")

       elif "sleep the system" in query:
           os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

       elif "lock my computer" in query:
           os.system("rundll32.exe user32.dll, LockWorkStation")

       elif "wait" in query:
           speak("Okay sir,I am waiting....")
           time.sleep(10)
       elif "you can sleep" in query or "no" in query or "nothing" in query:
           speak("Thanks for using me Sir, have a good day")
           sys.exit()
       time.sleep(2)
       speak("Sir do you want anyother work? ")

if __name__ == '__main__':
   speak("Hello boss, I am lucy")
   wish()
   MainFunction()
