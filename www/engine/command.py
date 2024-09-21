import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174) 
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)
        

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
           
    except Exception as e:
        return ""

    return query.lower()


# Ensure allCommands is only exposed once
if "allCommands" not in eel._exposed_functions:
    @eel.expose
    def allCommands(message=1):
        if message == 1:
            query = takecommand()
            print(query)
            eel.senderText(query)
        else:
            query = message

        try:
            if "open" in query:
                from www.engine.features import openCommand
                openCommand(query)

            elif "on youtube" in query:
                from www.engine.features import PlayYoutube
                PlayYoutube(query)

            elif any(kw in query for kw in ["send message", "phone call", "video call", "call", 
                                            "send whatsapp message", "whatsapp call", "whatsapp video call"]):
                from www.engine.features import findContact, whatsApp
                flag = ""
                contact_no, name = findContact(query)

                if contact_no != 0:
                    if "send message" in query:
                        flag = 'message'
                        speak("What message to send?")
                        query = takecommand()

                    elif "call" in query:
                        flag = 'call'

                    elif "send whatsapp message" in query:
                        flag = 'message'
                        speak("What message to send?")
                        query = takecommand()

                    elif "whatsapp call" in query:
                        flag = 'call'

                    elif "whatsapp video call" in query:
                        flag = 'call'

                    elif "phone call" in query:
                        flag = 'call'

                    else:
                        flag = 'video call'

                    whatsApp(contact_no, query, flag, name)

            else:
                print("not run")
                

        except Exception as e:
            print(f"Error occurred: {e}")
        eel.ShowHood()

