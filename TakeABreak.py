import time
import webbrowser

totalBreaks = 4
currentBreaks = 0

print('This program started running on ' + time.ctime())

while(currentBreaks < totalBreaks):
    time.sleep(3600) #parameter for sleep is in seconds
    webbrowser.open('www.google.com') #set string to whatever link you want
    currentBreaks = currentBreaks + 1
    print(str(currentBreaks) + " break(s) were taken on " + time.ctime())
