import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def listen_for_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            am_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            am_speak('Sorry, I didn\'t get that.')
        except sr.RequestError:
            am_speak('Sorry, my speech service can\'t connect.')
        return voice_data


def am_speak(audio):
    tts = gTTS(text=audio, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)


def canned_response(voice_data):
    if 'what is your name' in voice_data:
        am_speak(f'My name is {os.name}')
    if 'what time is it' in voice_data:
        am_speak(ctime())
    if 'search the web' in voice_data:
        search = listen_for_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        am_speak(f'Here is what I found for: {search}')
    if 'find location' in voice_data:
        location = listen_for_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        am_speak(f'Here is what I found for: {location}')
    if 'goodbye' in voice_data:
        am_speak('It was good talking to you.')
        exit()
    if 'who rocks the party' in voice_data:
        am_speak('We rock the party, rock the party.')


time.sleep(1)
am_speak('Say something')
while 1:
    voice_data = listen_for_audio()
    canned_response(voice_data)
