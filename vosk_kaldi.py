from vosk import Model, KaldiRecognizer
import pyaudio
import os

# Use a relative path so it works across different computers and operating systems
model_path = "vosk-model-hi-0.22"

if not os.path.exists(model_path):
    print(f"Error: Vosk model folder not found at '{model_path}'. Please download it and place it in the project directory.")
    exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
print("Offline Hindi Speech Recognition Active. Start speaking...")
while True:
    try:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(text)
    except KeyboardInterrupt:
        print("\nStopping speech recognition...")
        break

stream.stop_stream()
stream.close()
mic.terminate()
