import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Ma'am. Please tell me how may I help you")       

def takeCommand(max_retries=3):
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    for attempt in range(max_retries):
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
                speak("I didn't hear anything. Please try again.")
                continue
        try:
            print("Recgnizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again please...")  
    speak("Sorry, I couldn't understand. Let's try again later.")
    return "None"

'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shagunwork29@gmail.com', 'Work_&H@-89')
    server.sendmail('awareindia12@gmail.com', to, content)
    server.close()'''

# Fun data for jokes, facts, and quotes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why was the broom late? It swept in!"
]

fun_facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts."
]

quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "The harder you work for something, the greater  you'll feel when you achieve it."
]

songs = [ 
    # Bollywood Hindi Songs:
    "https://www.youtube.com/watch?v=sUf2PtEZris&list=RDsUf2PtEZris&start_radio=1",  # shaky shaky
    "https://www.youtube.com/watch?v=k4yXQkG2s1E&list=RDk4yXQkG2s1E&start_radio=1",  # Play a music
    "https://www.youtube.com/watch?v=oAVhUAaVCVQ&list=RDoAVhUAaVCVQ&start_radio=1",  # Chamak Challo
    "https://www.youtube.com/watch?v=JWMIlg42pHg&list=RDJWMIlg42pHg&start_radio=1",  # Byee Byee
    "https://www.youtube.com/watch?v=oGneAab3e88&list=RDoGneAab3e88&start_radio=1",  # jai jai shiv shankar
    "https://youtu.be/jADTdg-o8i0?si=QqJaUkhCbBrCjel9",  # Ghungroo - War
    "https://youtu.be/VAdGW7QDJiU?si=b1Q-_nS9rEcXOiDV",  # Jai Jai Shivshankar - War
]

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            if not query:
                speak("Please tell me what you want to search on Wikipedia.")
                print("No search term provided for Wikipedia.")
                continue
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any results on Wikipedia.")
                print(f"Wikipedia error: {e}")
        elif query.startswith("tell me about ") or query.startswith("who is ") or query.startswith("what is "):
            topic = query.replace("tell me about ", "").replace("who is ", "").replace("what is ", "").strip()
            if topic:
                speak(f"Searching Wikipedia for {topic}...")
                try:
                    results = wikipedia.summary(topic, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I couldn't find any results on Wikipedia.")
                    print(f"Wikipedia error: {e}")
            else:
                speak("Please specify what you want to know about.")
                print("No topic provided for Wikipedia search.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
     

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

    
        elif 'joke' in query:
            joke = random.choice(jokes)
            speak(joke)
            print(joke)
        elif 'fun fact' in query:
            fact = random.choice(fun_facts)
            speak(fact)
            print(fact)
        elif 'motivate' in query or 'motivation' in query or 'quote' in query:
            quote = random.choice(quotes)
            speak(quote)
            print(quote)
        elif 'play a song' in query or 'play music' in query or 'play song' in query:
            song_url = random.choice(songs[1:])  # Only Bollywood songs
            speak("Playing a Bollywood hit song on YouTube!")
            webbrowser.open(song_url)
        elif 'flip a coin' in query:
            result = random.choice(['Heads', 'Tails'])
            speak(f"It's {result}!")
            print(f"Coin flip: {result}")
        elif 'roll a dice' in query or 'roll a die' in query:
            dice = random.randint(1, 6)
            speak(f"You rolled a {dice}!")
            print(f"Dice roll: {dice}")
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Ma'am! Have a nice day.")
            break
