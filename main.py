import wikipedia
import pyttsx3 
import pylivestream 


#------------------------------------------------------
# get data from wikipedia.

def getRandom():
    for i in range(11):
        if (i < 10):
            ranPageName = wikipedia.random()
            getData(ranPageName)
            i = 0

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

# def capAudio():




while True:
    getRandom()