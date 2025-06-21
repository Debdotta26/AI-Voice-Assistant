Of course! Here's a refined version of your GitHub README content for the **AI Voice Assistant** project:

---

# 🧠 AI Voice Assistant

A voice-activated virtual assistant built with Python and a graphical user interface (GUI). It can respond to both voice and text input, performing tasks like telling jokes, sharing fun facts, fetching information from Wikipedia, reporting the weather, opening websites, and more—all using speech synthesis.

---

## 💡 Features

- 🎙️ Voice input using microphone  
- 🗣️ Text-to-speech responses  
- 🌦️ Weather updates  
- 🌐 Opens websites like Google, YouTube, Gaana  
- ⏰ Tells the current time  
- 🧠 Answers general knowledge questions via Wikipedia  
- 😂 Tells programming jokes using `pyjokes`  
- 📚 Shares fun facts  
- 💬 Greets the user and responds to basic inputs  
- 🖼️ GUI built with `Tkinter` and image rendering via `Pillow`

---

## 🛠️ Technologies Used

- Python 3  
- `Tkinter` – GUI interface  
- `SpeechRecognition` – Speech-to-text  
- `pyttsx3` – Text-to-speech  
- `pyjokes` – Programming jokes  
- `wikipedia` – Knowledge retrieval  
- `requests-html` – Weather scraping  
- `Pillow` – Image handling in GUI

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Debdotta26/AI-Voice-Assistant.git
cd AI-Voice-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the assistant:

```bash
python GUI.py
```

---

## 📁 File Structure

```
AI-Voice-Assistant/
├── action.py             # Handles voice commands and logic
├── gui.py                # Main GUI interface
├── knowledge.py          # Jokes, facts, and Wikipedia queries
├── speech_to_text.py     # Converts microphone input to text
├── text_to_speech.py     # Converts text to speech
├── weather.py            # Scrapes weather info
├── download (1).jpg      # Image used in the GUI
├── requirements.txt      # Required packages
└── README.md             # Project documentation
```

---

## 🧪 Sample Commands

Try saying:

- “What is your name?”  
- “Tell me a joke”  
- “What is Python?”  
- “Open Google”  
- “What’s the weather?”  
- “Good morning”

---

## 📸 Screenshot

Here’s a preview of the AI Assistant GUI:

![AI Assistant GUI](AI%20Assistant%20output.jpg)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it—with credit.

---

## 🙋‍♂️ Author

Created by [**Debdotta Bhattacharya**](https://github.com/Debdotta26/AI-Voice-Assistant)  
Contributions, feedback, and forks are warmly welcomed!

---

