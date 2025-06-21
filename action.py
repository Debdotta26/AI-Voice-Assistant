import text_to_speech
import datetime
import webbrowser
import weather
import knowledge
import speech_to_text

def Action(data):
    user_data=data.lower()

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

    elif "aditya" in user_data:
        text_to_speech.text_to_speech("good night adi, love u a lot and thank u for always being there for me")
        return "good night adi, love u a lot and thank u for always being there for me"


    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    elif  "tell me a joke" in user_data:
        joke = knowledge.tell_joke()
        text_to_speech.text_to_speech(joke)
        return joke

    elif "tell me a fact" in user_data:
        fact = knowledge.tell_fact()
        text_to_speech.text_to_speech(fact)
        return fact

    elif "what is" in user_data or "who is" in user_data or "tell me about" in user_data:
        topic = (
            user_data.replace("what is", "")
            .replace("who is", "")
            .replace("tell me about", "")
            .strip()
        )
        info = knowledge.get_knowledge(topic)
        text_to_speech.text_to_speech(info)
        return info

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"
   
