# 🗣️ Voice-Controlled Home Automation Using MQTT (Software-Only)

This is a Python-based voice assistant project that listens for voice commands and publishes messages to an MQTT broker to control smart home devices like lights and fans.

> ⚠️ Note: This project is currently software-only and does not include physical hardware integration.

---

## 📌 Features

- 🎤 Voice command recognition using Google Speech API
- 🔈 Text-to-speech feedback via `pyttsx3`
- 🔗 MQTT protocol integration via `paho-mqtt`
- 💡 Supports simple commands: `"light on"`, `"light off"`, `"fan on"`, `"fan off"`
- 🧠 Can be extended to control real IoT hardware

---

## 🛠️ Technologies Used

- Python 3
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-mqtt-assistant.git
cd voice-mqtt-assistant
