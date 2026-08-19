🤖 Jimmy AI Assistant

A modular, multi-modal personal voice assistant built with Python. It integrates offline speech recognition, computer vision face verification, system automation, and cloud AI capabilities.
🛠️ System Prerequisites & Dependencies

Before running the assistant, ensure you have Python 3.8+ installed on your system.
1. System-Level Dependencies (Linux / Fedora)

If you are running on Linux, install the required audio and GUI packages first by running:
sudo dnf install espeak-ng python3-tkinter scrot -y
2. Python Packages

Install all required libraries via pip by running:
pip install pyttsx3 speechrecognition psutil scikit-learn requests opencv-python opencv-contrib-python pyautogui
🚀 Installation & Setup

    Clone the repository:
    git clone https://github.com/anishpandey595/jimmy-ai-assistant.git
    cd jimmy-ai-assistant

    Add Optional Offline Models (If using Vosk):

        Download the Hindi Vosk model (vosk-model-hi-0.22) from the Official Vosk Models Website.

        Extract the folder directly into your project root directory.

    Run the Master Assistant:
    python3 main.py

📂 Project Architecture

    main.py — The master orchestration script (handles startup, face verification, greeting, and main voice command loop).

    features.py — Utility module for system monitoring (CPU usage), timers/reminders, and live weather reporting.

    face_recoginition.py — Biometric security module using OpenCV.

    vosk_kaldi.py — Offline speech recognition engine for local voice processing.

    friday_meta_LL2.py — Cloud integration module for advanced AI processing.

### Important Note on Facial Recognition
The `face_recoginition.py` module uses OpenCV's LBPH algorithm to identify the user. For privacy and file-size reasons, the pre-trained model is not included in this repository. 

To use the facial recognition feature, you must:
1. Create a folder named `face_recoginition/` in the root directory.
2. Download the `haarcascade_frontalface_default.xml` file from the official OpenCV repository and place it in that folder.
3. Write a short OpenCV script to capture your own face data and train the LBPH recognizer.
4. Save your output model as `trainer/trainer.yml` inside the `face_recoginition/` folder.
5. Update the `names` array in `face_recoginition.py` to match your trained ID.


### Important Note on Offline Hindi Voice Recognition (Vosk)
The `vosk_kaldi.py` script uses the Vosk offline speech recognition engine with a local Hindi model. For file-size reasons, the model folder is not included in this repository.

To use offline Hindi recognition:
1. Download the Hindi Vosk model (`vosk-model-hi-0.22`) from the [Official Vosk Models Website](https://alphacephei.com/vosk/models).
2. Extract the model folder directly into your project root directory.
3. Ensure the folder name matches `"vosk-model-hi-0.22"` or update the path variable inside `vosk_kaldi.py`.
