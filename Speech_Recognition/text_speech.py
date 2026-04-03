import pyttsx3

txt_sp = pyttsx3.init() ##define a class init()

# correct method name (small 'g')
voices = txt_sp.getProperty('voices')

# select voice
txt_sp.setProperty('voice', voices[1].id)  # try 0 or 1

# volume
txt_sp.setProperty('volume', 1.0)

#speed
txt_sp.setProperty('rate',0.5)

text = input("Enter the Text: ")

txt_sp.say(text) #converting text to voice
txt_sp.runAndWait()