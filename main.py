import pyttsx3

if __name__ == '__main__':
    print("*****ROBOTALKS******")
    engine = pyttsx3.init()

    current_rate = engine.getProperty('rate')  # Get current rate
    print(f"Default rate: {current_rate}")  # Optional: see what it was
    engine.setProperty('rate', 125)  # Set to slower rate (try 125–150)
    while True:
        speak = input("Enter what you want me to speak: ")
        if speak.lower() == "roboends":
            engine.say("Bye! have a good time")
            engine.runAndWait()
            break
        engine.say(speak)
        engine.runAndWait()
