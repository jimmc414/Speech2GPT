import openai
import speech_recognition as sr
import pyttsx3
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    # Set up the speech recognizer
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Wait for the user to speak
    print("Listening...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    # Convert the audio to text
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print(f"Error connecting to the service: {e}")

def speak(text):
    # Speak the text
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        text = listen()
        if text:
           # Use the OpenAI API to generate a response
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"User: {text}",
                max_tokens=1024,
                n = 1,
                stop=None,
                temperature=0.5,
            )

            # Extract the generated text from the API response
            generated_text = response["choices"][0]["text"]

            # Print the generated text
            print(f"ChatGPT: {generated_text}")
            speak(generated_text)
        else:
            print("Sorry, I didn't hear anything.")

if __name__ == "__main__":
    main()
