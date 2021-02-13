import speech_recognition as sr

def voiceTtext(file1):
    r=sr.Recognizer()
    R=sr.Recognizer()
    with sr.AudioFile(file) as source:
       audio=R.record(source)
    text1=r.recognize_google(audio)
    return text1