import text_to_speech
import datetime
import webbrowser
import weather
import speech_to_text

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hey , maam how can i help you")
        return "hey , maam how can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning ma'am")
        return "good morning ma'am"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour:",(str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok, shutting down")
        return "ok, shutting down"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube is now ready for you")
        return "youtube is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google is now ready for you")
        return "google is now ready for you"

    elif "open instagram" in user_data:
        webbrowser.open("https://instagram.com/")
        text_to_speech.text_to_speech("instagram is now ready for you")
        return "instagram is now ready for you"

    elif "play spotify" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify is now ready for you")
        return "spotify is now ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand")