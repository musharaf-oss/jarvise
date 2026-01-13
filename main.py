import os
from os import mkdir
import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import pygame
from google import genai
from apikey import api_key
import random

# def ai(prompt):
#     client = genai.Client(api_key=api_key)
#     ans = f"gemini respone :{prompt} \n**************************************\n\n"
#
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt,
#     )
#     answer = response.text  # store Gemini reply
#     print(answer)  # print it
#     ans += answer  # add to string
#
#     if not os.path.exists("gemini"):
#         mkdir("gemini")
#     with open(f"gemini{''.join(prompt.split('intelligence')[0:30])}.txt") as f:
#         f.write(ans)

def ai(prompt):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer = response.text
    print(answer)

    # Create folder if it doesn't exist
    if not os.path.exists("gemini"):
        # os.
        mkdir("gemini")

    # Make prompt safe for filename
    safe_prompt = "".join(c for c in prompt if c.isalnum() or c in (" ", "_")).strip()
    safe_prompt = safe_prompt.replace(" ", "_")[:40]

    # Add timestamp to always create NEW file
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    filename = f"gemini/{safe_prompt}_{timestamp}.txt"

    # Write response to new file
    with open(filename, "w", encoding="utf-8") as f:
        f.write("PROMPT:\n")
        f.write(prompt + "\n\n")
        f.write("GEMINI RESPONSE:\n")
        f.write(answer)


def play_music(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception:
        return ""



if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis A I ")

    while True:
        print("Listening...")
        text = takecommand()

        sites=[["youtube","http://youtube.com"],["google","http://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
               say(f"opening {site[0]} sir...")
               webbrowser.open(site[1])

        locations=[["music",r"C:\Users\star zz\Desktop\Fevicol Se Dabangg 2 128 Kbps.mp3"]]
        for location in locations:
          if f"play {location[0]}".lower() in text.lower():
             say(f"Playing {location[0]} sir")
             play_music(location[1])

        if "stop music" in text.lower():
            pygame.mixer.music.stop()
            say("Music stopped")
        apps=[["wps",r"C:Users\star zz\AppData\Local\Kingsoft\WPS Office\12.2.0.23196\office6\wpsoffice"]]
        for app in apps:
            if f"open {app[0]}".lower() in text.lower():
               say(f"opening {app[0]} sir")
               os.startfile(app[1])
        if f"using AI".lower() in text.lower():
            ai(prompt=text)

        if text == "":
            continue

        if text.lower() == "exit" or text.lower() == "stop":
            say("Goodbye")
            break

        say(text)
        time.sleep(0.6)



