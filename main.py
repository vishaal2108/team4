import speech_recognition as sr
import pyttsx3
import paho.mqtt.client as mqtt

# MQTT setup
broker = "localhost"  # Change this if using external MQTT broker
port = 1883
topic = "home/device/control"

try:
    client = mqtt.Client()
    client.connect(broker, port)
    print("✅ Connected to MQTT broker.")
except Exception as e:
    print("❌ MQTT Connection Error:", e)

# Initialize voice engine
try:
    engine = pyttsx3.init()  # You can try engine = pyttsx3.init('sapi5') on Windows
except Exception as e:
    print("❌ TTS Engine Initialization Error:", e)

def speak(text):
    print("Assistant:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("❌ Speech error:", e)

# Listen for voice command
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        try:
            audio = recognizer.listen(source, timeout=5)
        except Exception as e:
            speak("Microphone error.")
            print("❌ Mic error:", e)
            return ""
    try:
        command = recognizer.recognize_google(audio)
        print("🎤 You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
    except sr.RequestError:
        speak("Network error.")
    return ""

# Process and send command
def process_command(command):
    if "light on" in command:
        client.publish(topic, "light_on")
        speak("Turning on the light.")
    elif "light off" in command:
        client.publish(topic, "light_off")
        speak("Turning off the light.")
    elif "fan on" in command:
        client.publish(topic, "fan_on")
        speak("Turning on the fan.")

    elif "fan off" in command:
        client.publish(topic, "fan_off")
        speak("Turning off the fan.")

    else:
        speak("Command not recognized.")

# Main loop
try:
    while True:
        cmd = listen_command()
        if cmd:
            process_command(cmd)
except KeyboardInterrupt:
    print("\n🛑 Program stopped by user.")
