
# speech recognition
# installation requirements: SpeechRecognition, PyAudio
import speech_recognition as sr 
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("speak anything...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
    except :
        print("Sorry! couldn't able to hear your voice")    


# speech recognition from audio file 

filepath = "C:\\Users\\LOKESH\\Downloads\\OSR_us_000_0010_8k.wav"

r = sr.Recognizer()
jackhammer = sr.AudioFile(filepath)

with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    print("let's record.......")
    audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print("File says : {}".format(text))
    except :
        print("Sorry! Unable to print the text from audio file")    



























