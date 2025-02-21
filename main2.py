import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import openai_request as ai


engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    attempts = 3  # Retry limit
    for _ in range(attempts):
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
            content = r.recognize_google(audio)
            print("You said: " + content)
            return content
        except Exception:
            print("Please try again...")
    return ""  # Return empty string if unsuccessful

def main_process():
    jarvis_chat=[]
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can I help you?")
            
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://youtu.be/K4DyBUG242c?si=o-mKjkxYgmaSVW4m")
            elif song == 2:
                webbrowser.open("https://youtu.be/83RUhxsfLWs?si=f7w9Pir0Uo3GNzvr")
            elif song == 3:
                webbrowser.open("https://youtu.be/C5fLxtJH2Qs?si=PcIRHGIH3E2L0601")


        elif "current time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))

        elif "curreny date" in request:
            now_date = datetime.datetime.now().strftime("%d-%m")
            speak("Current date is " + str(now_date))

        elif "add work" in request:
            task = request.replace("new task", "").strip()
            if task:
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt", "r") as file:
                speak("Work we have to do today is: " + file.read())
        elif "show work" in request:
            with open("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title="Today's work",
                message=tasks,
                timeout=10

            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")

        elif "open facebook " in request:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in request:
            webbrowser.open("www.instagram.com")

        elif "open netflix" in request:
            webbrowser.open("www.netflix.com")
            

        elif "open" in request:
            query = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            query = request.replace("search wikipedia", "").strip()
            if query:
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
             
                except Exception as e:
                    speak("Sorry, I couldn't fetch the information.")
            else:
                speak("What should I search on Wikipedia?")


        elif "search google" in request:
            query = request.replace("search google", "").strip()
            if query:
                webbrowser.open("http://www.google.com/search?q=" + query)

       
        elif "send whatsapp" in request:
            speak("To whom should I send the message? please provide the phone number with country code")
            recipient = command()
            speak("What should the message say?")
            message = command()
            try:
               pwk.sendwhatmsg( recipient.strip(), message, 10,10 )
               speak("Message sent successfully.")
            except Exception as e:
               speak("Sorry, I couldn't send the message.")

        
        elif "send email" in request:
            pwk.send_mail("rameshshahi714@gmail.com", user_config.gmail_password,"Hello", "How are you","shahiramesh1717@gmail.com")
            
            speak("Email sent")

        # elif "ask ai" in request:
        #     request=request.replace("jarvis","")
        #     request=request.replace("ask ai")
        #     print(request)
        #     response=ai.send_request(request)
        #     print(response)
        #     speak(response)

        elif "ask ai" in request:
           jarvis_chat=[]
           request = request.replace("jarvis", "").strip() 
           request = request.replace("ask ai", "").strip()
           jarvis_chat.append({"role": "user","content":request})  
        #    print(f"User Query: {request}")
    
           try:
        # Assuming `ai.send_request` is a method to send the request to your AI system
               response = ai.send_request(jarvis_chat)
               speak(response)
           except Exception as e:
               speak("Sorry, I encountered an error while processing your request.")
               print(f"Error: {e}")

        elif "clear chat" in request:
            jarvis_chat=[]
            speak("chat cleared")
    
        
        else:
            
            request=request.replace("jarvis","")

            
            jarvis_chat.append({"role": "user","content":request})
            response=ai.send_request(jarvis_chat)
            

            jarvis_chat.append({"role": "user","content":request})
            speak(response)
            

             




               

        # elif "exit" in request or "quit" in request:
        #     speak("Goodbye!")
        #     break

main_process()
