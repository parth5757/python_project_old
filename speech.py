# # import pyttsx3
# # friend = pyttsx3.init()
# # friend.say("hi parth aveent love you")
# # friend.runAndWait()







# # import speech_recognition as sr
# # r = sr.Recognizer()
# # with sr.Microphone () as source:
# #     audio = r.listen(source)

# # try:
# #     print("You said " + r.recognize(audio))
# # except LookupError:
# #     print("Could not understand audio")





  
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
import speech_recognition as sr
# dir(sr)
