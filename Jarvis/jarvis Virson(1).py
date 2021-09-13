# importing the package to build jarvis
from urllib import request
from wave import Wave_write
import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
from playsound import playsound
import cv2
import time
import psutil
from wikipedia.wikipedia import search
from plyer import notification
import wolframalpha 
import bs4
import requests
  

# making jarvis voice - male 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    # making greeting command from jarvis  

    playsound("wishme.mp3")
    def Wish(title,message):
        notification.notify(
        title = title,
        message = message,
        app_icon = "Jarvis.ico",
        timeout = 25
        )
    Wish("Welome back !",f"Welcome back sir ! Wishes from JARVIS")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<15:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("This is Jarvis your personal virtual friend. How may I help you ?")

def takeCommand():
    # it should take my command through the microphone and respond

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}")
        print()

    except Exception as e:
        print(e)
        return "None"
    query = query.lower()
    return query

def WolRam(query):
    api_key = "L9WWXQ-92VH8J7KQX"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("An string value is not answerable")

def TakeExcecution():
    speak("Jarvis is activated")
    speak("Hello sir there in online for your command !")
    while True:
                query =  takeCommand().lower()

                # making a wikipedia search bar 

                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif 'stop watch' in query:
                    webbrowser.open("https://www.google.com/search?q=stop+watch&rlz=1C1KNTJ_enBH953BH953&oq=stop+watch+&aqs=chrome.0.0i512l2j0i457i512j0i512l5j0i10i512j0i512.2601j0j7&sourceid=chrome&ie=UTF-8")

                elif 'good night' in query:
                    speak("Good night sir")
                    webbrowser.open("https://www.youtube.com/watch?v=7jS9ObvOrZQ")

                elif 'good morning' in query:
                    speak("Good morning sir, it is a good and a great day")
                    webbrowser.open("https://www.youtube.com/watch?v=CuI_p7a9VGs")
                
                elif 'good afternoon' in query:
                    speak("Good afternoon sir")
                    webbrowser.open("https://www.youtube.com/watch?v=GZsYYrTI_nc")

                elif 'good evening' in query:
                    speak("Good evening sir")
                
                elif 'how are you' in query:
                    speak("Fine sir, with your support. What about you ?")
                    myself = takeCommand().lower()
                    if 'fine' in myself:
                        speak("Great sir!")
                    elif 'not fine' in myself:
                        speak("Why sir? It is bright good day. Let me play a song which will make you happy")
                        playsound("D:\music\god_love.mp3")
                    else:
                        speak("Ohh! Ok sir")

                elif 'jarvis' in query:
                    speak("Yes sir! there in online to always server you ")

                elif 'remember that ' in query:
                    remembermsg = query.replace("remember that","")
                    remembermsg = remembermsg.replace("Jarvis","")
                    speak("you tell me to remeber that : " + remembermsg)
                    remember = open('data.txt','w')
                    remember.write(remembermsg)
                    remember.close()

                elif 'reminders ' in query:
                    remember = open('data.txt','r')
                    speak("You told me to remember that " + remember.read())
                
                elif 'appreciate my brother' in query:
                    speak("Excellent Sreejan!")
                
                elif 'temperature' in query:
                   temp =  WolRam("Temperature in bahrain")
                   speak("The temperature in bahrain is "+temp + "updated")
            
                elif 'timer' in query:
                    def countdown(time_sec):
                        while time_sec:
                            mins, secs = divmod(time_sec, 60)
                            timeformat = '{:02d}:{:02d}'.format(mins, secs)
                            print(timeformat, end='\r')
                            time.sleep(1)
                            time_sec -= 1

                        speak("stop")
                    speak("For how much time")
                    sec = int(takeCommand().lower())
                    countdown(sec)
            

                elif 'alarm' in query:
                    speak("Setting alarm, please tell which hour?")
                    hr = int(takeCommand().lower())
                    speak("Minutes please !")
                    minutes = int(takeCommand().lower())
                    speak("AM or PM")
                    am_or_pm = takeCommand().lower()

                    if am_or_pm == "p m":
                        hr+=12

                    while True:
                        if hr==datetime.datetime.now().hour and minutes==datetime.datetime.now().minute:
                            speak("Alarm time up !")
                            playsound("Alarm.mp3")
                            def NotifyMe(title,message):
                                notification.notify(
                                    title = title,
                                    message = message,
                                    app_icon = "clock.ico",
                                    timeout = 10
                                )
                            NotifyMe("Alarm Time up",f"You have set an alarm for {hr}:{minutes}, and the time is up. Thank you ! Regards, JARVIS")
                            break

                elif 'movie' in query:
                    speak("Ok sir ! Please choose the movie you would like to see. 1), Baadhsha , 2) , Seethamma Vakitlo Siramelle chettu")
                    movie_name = takeCommand().lower()
                    if '1' in movie_name:
                        webbrowser.open("https://www.youtube.com/watch?v=k-fT-UF1BOg")
                    elif '2' in movie_name:
                        webbrowser.open("https://www.youtube.com/watch?v=CVCxbun_4Eo")
                    elif 'one' in movie_name:
                        webbrowser.open("https://www.youtube.com/watch?v=k-fT-UF1BOg")
                    elif 'two' in movie_name:
                        webbrowser.open("https://www.youtube.com/watch?v=CVCxbun_4Eo")
                    else:
                        speak("Sorry sir ! No such movie found")
                
                elif 'about you' in query:
                    webbrowser.open("https://ironman.fandom.com/wiki/J.A.R.V.I.S.")
                
                elif 'ask iit' in query:
                    webbrowser.open("www.askiitians.com")
                
                elif 'iit classroom' in query:
                    webbrowser.open("https://classroom.google.com/u/1/h")

                elif 'volume up' in query:
                    pyautogui.press("volumeup")
                
                elif 'volume down' in query:
                    pyautogui.press("volumedown")


                elif 'volume mute' in query:
                    pyautogui.press("volumemute")
                    
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'notepad' in query:
                    os.startfile("notepad.exe")
                
                elif 'Thank you' in query:
                    speak("Always welcome sir , I am always there for helping you")
                
                elif 'take a screenshot' in query:
                    speak("Sir , please do tell the name of the screen shoot of the image")
                    name = takeCommand().lower()
                    speak("Please hold for sometime sir , i will back with the screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("Yes sir I am done with my screen shoot, you can find the screen shoot in the main folder")

                elif 'calculator' in query:
                    webbrowser.open("https://www.google.com/search?q=calculator&rlz=1C1KNTJ_enBH953BH953&oq=calculato&aqs=chrome.1.69i60j0i131i433j69i57j0l5.2569j0j7&sourceid=chrome&ie=UTF-8")

                elif 'open camera' in query:
                    speak("Ok sir, opening the camera. If you want to stop it , then press c")
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret,img = cap.read()
                        cv2.imshow('webcam' , img)
                        k = cv2.waitKey(10)
                        if k==ord('c'):
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif 'play music' in query:
                    speak("Select the song from the list - 1) , Chitti Nee , 2) , Life of Ram , 3) ,Alavaikuntapuramuloo , 4) , Meguvva . Please tell the number , so that I can play the song .. ")
                    song = takeCommand().lower()
                    if song == "number 1":
                        playsound("D:\music\chitti.mp3")

                    # my name is Sujith Sourya Yedia ane nneu 


                    elif song == "number 2":
                        playsound("D:\music\life of ram.mp3")

                    elif song == "number 3":
                        playsound("D:\music\ ala.mp3")

                    elif song == "number 4":
                        playsound("D:\music\magu.mp3")

                    else:
                        speak("Sorry sir ! This song not there in the list")

                
                elif 'Gmail' in query:  
                    webbrowser.open("https://gmail.com")
                    

                elif 'open google' in query:
                    speak("Sir, what should I search for you")
                    cm = takeCommand().lower()
                    webbrowser.open(f"{cm}")

                elif 'tell me a joke' in query:
                    jokes = pyjokes.get_joke()
                    speak(jokes)

                elif 'shutdown the system' in query:
                    os.system("shutdown /s")

                elif 'restart the system' in query:
                    os.system("shutdown /r")
                
                elif 'switch window' in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif 'wish my uncle happy birthday' in query:
                    speak("Name of your uncle please")
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday {name} uncle ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my aunty happy birthday' in query:
                    speak("Name of your aunty please")
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday {name} aunty ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my brother happy birthday' in query:
                    speak("Name of your brother please")
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday {name} bro ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my sister happy birthday' in query:
                    speak("Name of your sister please")
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday {name} ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my friend happy birthday' in query:
                    speak("Name of your friend please")
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday {name} ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my mother happy birthday' in query:
                    name = takeCommand().lower()
                    time.sleep(1)
                    speak(f"Happy birthday Tulasi ma'am ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")

                elif 'wish my father happy birthday' in query:
                    time.sleep(1)
                    speak(f"Happy birthday Sarath sir ! Have a good time , by the way I am Jarvis.. Ok , let me play the birthday song")
                    playsound("D:\music\hpb.mp3")
                elif 'classroom' in query:
                    webbrowser.open("https://classroom.google.com/u/0/h")

                elif 'cloud drive' in query:
                    webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
                
                elif 'time table' in query:
                    speak("Opening timetable")
                    os.open("GRADE.pdf")
                
                elif 'my laptop battery' in query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Sir your laptop charge percentage is {percentage}")

                elif 'sleep' in query:
                    speak("inoperating the modules , exited from the Jarvis Command module, to activte me again you can call me Wake Up Jarvis ! Anytime.")
                    break
                    

# running the code written above

if __name__ == "__main__":
    wishMe()
    while True:
        permission = takeCommand()
        if 'activate' in  permission:
            speak("Activating all modules, opening the system, entering the Jarvis Command Module.")
            TakeExcecution()
        
        elif 'exit' in permission:
            speak("Thank you sir , have a good time.. Shutting down all modules, deactivating the Jarvis module.")
            break

# developed by Sujith Sourya Yedida 

# Jarvis is a voice application which will be your best virtual friend 

# there are many functions in this software

# 1) Can perform google search and also can open exe files
# 2)Can also open camera and play music
# 3)can switch window and also take a screenshoots(unlimited)
# 4)can also wish happy birthday and make you happy
# 5)can also tell your battery level , can increase , decrease and mute the volume
# 6)can also open classroom and time table