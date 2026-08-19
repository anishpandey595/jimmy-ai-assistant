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
