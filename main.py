import speech_recognition as sr
from datetime import date, datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import pyautogui
import smtplib
r = sr.Recognizer()

pyautogui.alert(text='Herhangi bir komut kullandığınızda visual studio ekranda olmazsa çalışmayabilir.', title='https://github.com/recoist1903', button="Tamam");

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım")
        except sr.UnknownValueError:
            speak("sistem çalışmadı")
        return voice

def response(voice):
    if "programdan çık" in voice:
        pyautogui.hotkey('alt','F4')

    if "hata ayıklamayı çalıştır" in voice:
        pyautogui.hotkey('F5')

    if "çalıştır" in voice:
       pyautogui.hotkey('F5')

    if "yeniden adlandır" in voice:
        pyautogui.hotkey('F2')

    if "hata ayıklamayı durdur" in voice:
     pyautogui.hotkey('shift','F5')

    if "çık" in voice:
        speak("çıkış yapıldı")
        exit()

    if "çıkış yap0" in voice:
        speak("çıkış yapıldı")
        exit()    

    if "saat kaç" in voice:
        speak(datetime.now().strftime("%H:%M:&S"))


def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("nasıl yardımcı olabilirim")
time.sleep(1)
while 1:
   voice = record()
   print(voice)
   response(voice)