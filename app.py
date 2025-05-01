import sounddevice as sd
import numpy as np
import whisper
import queue
import sys
import pyttsx3
# import subprocess
import ollama

# settings
model_name = 'mistral:instruct'
samplerate = 16000
duration = 5

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def record_audio(duration=5):
    print('Speak now (ngomong)')
    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
        audio = np.empty((int(duration * samplerate), 1), dtype=np.float32)
        idx = 0
        while idx < len(audio):
            chunk = q.get()
            chunk_len = min(len(chunk), len(audio) - idx)
            audio[idx:idx + chunk_len] = chunk[:chunk_len]
            idx += chunk_len
    print('Recording finished (rekaman berhasil)')
    return audio[:, 0]

def transcribe(audio_data):
    model = whisper.load_model('base')
    print('Transcribing (mengubah suara ke teks)')
    result = model.transcribe(audio_data, fp16=False, language='en')
    print('You said: ', result['text'])
    return result['text']

def ask_ollama(prompt):
    print('Thinking... (berpikir)')
    response = ollama.chat(
        model=model_name,
        messages=[
            # {'role': 'system', 'content': 'Balas dalam Bahasa Indonesia. Jangan menjelaskan terlalu panjang. Jawab singkat dan jelas.'},
            {'role': 'system', 'content': 'Keep replies short and simple.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    reply = response['message']['content'].strip()
    print('AI replied: ', reply)
    return reply

# def ask_ollama(prompt):
#     print('Thinking... (berpikir)')
#     result = subprocess.run(
#         ['ollama', 'run', model_name],
#         input=prompt.encode(),
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         timeout=60
#     )
#     output = result.stdout.decode()
#     lines = output.splitlines()
#     response_lines = [line for line in lines if not line.startswith(prompt)]
#     cleaned = '\n'.join(response_lines).strip()
#     print('AI replied: ', cleaned)
#     return cleaned

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# main loop
while True:
    audio = record_audio(duration)
    text = transcribe(audio)

    if text.lower() in ['exit', 'quit', 'bye']:
        print('Exiting...')
        break

    reply = ask_ollama(text)
    speak(reply)