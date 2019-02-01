import wikipedia
import time as t
import pyttsx3 
import pylivestream 


#------------------------------------------------------
# get data from wikipedia.

def getRandom():
    def requests():
        for i in range(11):
            ranPageName = wikipedia.random(pages= 10)
            if (i == 10):
                t.sleep(2)
                requests()
            return getData(ranPageName)
    requests()
    return requests()

def getData(ranPageName):
    pagedata = wikipedia.summary(ranPageName)
    saySumm(pagedata)

#------------------------------------------------------
# say the summary using pyttsx

def saySumm(pagedata):
    engine = pyttsx3.init()
    engine.say(pagedata)
    engine.runAndWait()

#------------------------------------------------------
# stream the audio to youtube

def makeLive():
    pylivestream.Screenshare(ini: stream.ini, youtube)
    pylivestream.Screenshare.startlive()



while True:
    getRandom()
    makeLive()