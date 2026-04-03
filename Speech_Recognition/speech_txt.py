#pip install pyaudio
#pip install SpeechRecognition

import speech_recognition as sr
def speech_txt():
    r=sr.Recognizer()#class
    while True:
        #source=sr.Microphone()
        with sr.Microphone() as source: 
            print("Speak.....")
            audio=r.listen(source) #recogniser has a function listen() so while speaking ,the capture vouce is stored in source and the it is passed to listen() to recognize it

            #api
            try:
                text=r.recognize_google(audio)#using this api it converts to text 
                print("You said:",text)
                break
            except:
                print("Didn't hear anything please repeat")
speech_txt()

#if the captured voice is not clear it will throw an error in such cases we implement exception handling here
