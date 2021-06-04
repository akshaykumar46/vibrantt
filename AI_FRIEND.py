import pyttsx3
import datetime
import speech_recognition
import wikipedia
import os
import pyjokes
import webbrowser
import random
from googlesearch import *
import pyautogui
#import Command_database
#import table
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def volume_increase(amount):
    speak("increasing volume by{amt}".format(amt=amount))
    if amount%2==0:
        amt=amount/2
    elif amount%2==1:
        amt=(amount+1)/2
    pyautogui.press('volumeup',presses=int(amt))

def volume_decrease(amount):
    speak("decreasing volume by{amt}".format(amt=amount))
    if amount%2==0:
        amt=amount/2
    elif amount%2==1:
        amt=(amount+1)/2
    pyautogui.press('volumedown',presses=int(amt))

def jokes():
    speak(pyjokes.get_joke())

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

def month_name(month_num):
    '''
    (int)->str
    Return name of the month_num.
    >>> month_name(2)
    'Feburary'
    '''
    months_name=["January","Feburary","march","April","May","June","July","August","september","October",\
    "November","December"]

    return months_name[month_num-1]

def date():
    year=int(datetime.datetime.now().year)
    month_number=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)

    month=month_name(month_number)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)

def welcome_greet():
    speak("Welcome back sir!")
    time()
    date()
    speak("I am vibrant how may I help you Sir")

#def volume(set_value):
       # call(["amixer","-D","pulse","sset","master",str(set_value)+"10%"])
        #return None

def take_command():
    recognizer_var=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        recognizer_var.pause_threshold=1
        audio=recognizer_var.listen(source)

    try:
        print("Recognizing...")
        query=recognizer_var.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("I have no Idea of what you are asking about!")
        return ""
    return query

def text_inp():
    command=input(">>")
    return command



if __name__ == "__main__":

   # welcome_greet()
  #  table_num=table.create_table()


    while True:
        while True:
            print("How you wanna continue-\n1. enter 1 for text based input.\2. enter 2 for voice based inputs \n")
            if(int(input()==1)):
                query=text_inp
                break
            elif(int(input())):
                query=take_command().lower()
                break
            else:
                print("Enter a valid choice")
      #  Command_database.add_query(table_num,query)
        if "time now" in query:
            time()

        elif "increase volume" in query:
            speak("How much I  should increse it, Sir?")
            try:
                amt=take_command().replace("increase it to",'').strip()
                amt.replace(" ","")
                while amt.isdigit()==False:
                    speak("speak only numbers")
                    amt=take_command().replace(" ","").strip()
                
            except:
                amt=take_command()
                amt.replace(" ","")
                while amt.isdigit()==False:
                    speak("speak only numbers")
                    amt=take_command().replace(" ","")
            amt=int(amt)
            volume_increase(amt)

        elif "decrease volume" in query:
            speak("How much I should decrease sir?")
            try:
                amt=take_command().replace("decrease it to",'').strip()
                amt.replace(" ","")
                while amt.isdigit()==False:
                    speak("speak only numbers")
                    amt=take_command().replace(" ","").strip()
                
            except:
                amt=take_command()
                amt.replace(" ","")
                while amt.isdigit()==False:
                    speak("speak only numbers")
                    amt=take_command().replace(" ","")
            amt=int(amt)
            volume_decrease(amt)

       # elif "play bhajan" in query:
        #    speak("playing bhajans from your computer")
         #   songs_dir="E:\BHAJANS"
          #  song_index=random.choice(range(1,20,1))
           # songs=os.listdir(songs_dir)
            #os.startfile(os.path.join(songs_dir,songs[song_index]))

       # elif "play song" in query:
        #    speak("playing songs from your computer")
         #   songs_dir="D:\music"
          #  song_index=random.choice(range(1,160,1))
           # print(song_index)
            #songs=os.listdir(songs_dir)
            #os.startfile(os.path.join(songs_dir,songs[song_index]))

        elif "joke" in query:
            jokes()

        elif "search on youtube" in query:
            speak("what should I search sir?")
            input_for_search=take_command()
            input_for_search=input_for_search.replace(" ","+")
            print(input_for_search)
            speak("searching for {var} in youtube".format(var=input_for_search))
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open_new_tab("https://www.youtube.com/results?search_query=%s" % input_for_search)

        elif "today's date" in query:
            date()

        elif "can you hear me" == query:
            speak("yes sir! I can hear you")

        elif "hello"==query:
            speak("hello sir")

        elif "sleep down" in query:
            speak("Good Night Sir!")
            quit()
        elif "search on google" in query:
            speak("what should I search sir?")
            command=take_command().lower()
            print(command)
            speak("searching {var}...".format(var=command))
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open_new_tab("https://google.com/search?q=%s" % command)

        elif "website" in query:
            query=query.replace("website","")
            if "open" in query:
                query=query.replace("open","")
            query=query.strip()
            speak("opening "+query+".com")
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open_new_tab(query+".com")



        elif "hello to me" in query:
            speak("hello sir!")
            speak("can  say it again")
        elif "hello john" in query:
            speak("I am not john, I am vibrant sir")
        elif "yes" in query:
            speak("again, hello sir! ")

        elif "shutdown" in query:
            speak("shuting down the system...")
            quit()
        #elif "hello" in query:
          #  speak("Hello! how may i help YOu")
           # speak("You are glad to know that I knew nothing of anything")
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","").strip()
            try:
                result=wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)
            except:
                speak("specify in more detail!")

