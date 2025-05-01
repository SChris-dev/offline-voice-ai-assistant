# 🎙️ Offline Voice AI Assistant

This is a fully offline voice assistant project using:

- 🧠 Ollama + Mistral (for text-based AI)
- 🗣️ Whisper (for speech-to-text)
- 🔊 pyttsx3 (for text-to-speech)

Speak into your mic, the assistant replies with generated responses — all **without internet**.

## 📦 Features

- 🎧 Real-time voice input using `sounddevice`
- 🧠 AI response via locally run Mistral (through Ollama)
- 🔤 Converts your voice to text using `Whisper`
- 🔊 Speaks the AI’s response with `pyttsx3`
- 🌐 Supports **Bahasa Indonesia** and other languages!
- 📡 100% works offline (no API keys needed)

## 🛠 Requirements

- Python 3.10+
- Ollama installed (`https://ollama.com`)
- Whisper model (auto-downloaded)
- TTS voice engine (pyttsx3 uses system voices)

## 📥 Install dependencies

```bash
pip install sounddevice numpy openai-whisper pyttsx3
```

## 🚀 How to Run

1. Install Ollama if you haven't yet (`https://ollama.com`)
2. Pull the Mistral Model (this will download ~4GB):
```bash
ollama pull mistral:instruct
```
3. Run the script:
```bash
python app.py
```
4. Speak when prompted. The assistant will:
- Convert your voice to text
- Think with Mistral
- Speak back to you with TTS

🛑 Say “exit”, “bye”, or “quit” to close the program.

## 🎙 Notes

- Background noise can confuse Whisper — a headset mic helps a lot!
- Responses may be slower in non-English languages (but it still works!)
- Voice output might sound robotic depending on your system voices.