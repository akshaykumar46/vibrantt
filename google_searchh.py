import webbrowser
query="akshay"
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open_new_tab("https://google.com/search?q=%s" % query)