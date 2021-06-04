from googlesearch import *
import webbrowser
if "akshay"=="akshay":
    query = input("Input your query:")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)