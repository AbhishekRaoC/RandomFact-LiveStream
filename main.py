import wikipedia
import pyttsx3 
import pylivestream 


#------------------------------------------------------
# get data from wikipedia.

def getRandom():
    ranPageName = wikipedia.random()
    getData(ranPageName)

def getData(ranPageName):
    pagedata = wikipedia.summary(ranPageName)
    for i in len(pagedata):
        # parse through the data and remove the pronounciation letters
    saySumm(pagedata)

#------------------------------------------------------
# say the summary using pyttsx

def saySumm(pagedata):
    engine = pyttsx3.init()
    engine.say(pagedata)
    engine.runAndWait()

#------------------------------------------------------
# stream the audio to youtube




while True:
    getRandom()