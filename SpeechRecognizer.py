import speech_recognition as sr
import time

def recognizeSpeechFromMic(recognizer, mic):

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")



    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Start speaking")
        audio = recognizer.listen(source)


    #try catch in case it can't access the api or can't read the voice
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        response = "Can't reach API"
    except sr.UnknownValueError:
        response = "Can't recognice voice"

    return response



if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while 1 == 1:
        output = recognizeSpeechFromMic(recognizer, mic)
        print(output)
