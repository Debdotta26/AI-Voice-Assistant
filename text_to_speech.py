import pyttsx3
def text_to_speech(text):
    engine = pyttsx3.init(driverName='sapi5')
    rate =engine.getProperty('rate')
    engine.setProperty('rate', 'rate-70')
    engine.say(text)
    engine.runAndWait()
