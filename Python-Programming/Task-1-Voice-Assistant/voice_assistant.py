import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


# Initialize text-to-speech engine
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    """Speak the given text and display it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the user's voice through the microphone."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:
            speak("I did not hear anything.")
            return ""

    try:
        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


def process_command(command):

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "your name" in command:
        speak("My name is OIBSIP Voice Assistant.")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


def main():

    print("=" * 60)
    print("             OIBSIP VOICE ASSISTANT")
    print("=" * 60)

    speak("Hello! I am your voice assistant.")
    speak("You can ask me for the time, date, or open websites.")
    speak("Say exit when you want to stop.")

    running = True

    while running:

        command = listen()

        if command:
            running = process_command(command)


if __name__ == "__main__":
    main()