#    span       id = wob_tm
# vk_bk won-unit

from requests_html import HTMLSession
import requests
import speech_to_text
def weather():
    API_KEY = "11d3e346deb47fa5fda39deed17226cd"  # Your API key
    city = "Rishra"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{temp}degree celcius", desc
    else:
        return None, "City not found or error in fetching data."