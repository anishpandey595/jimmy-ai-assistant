### Important Note on Facial Recognition
The `face_recoginition.py` module uses OpenCV's LBPH algorithm to identify the user. For privacy and file-size reasons, the pre-trained model is not included in this repository. 

To use the facial recognition feature, you must:
1. Create a folder named `face_recoginition/` in the root directory.
2. Download the `haarcascade_frontalface_default.xml` file from the official OpenCV repository and place it in that folder.
3. Write a short OpenCV script to capture your own face data and train the LBPH recognizer.
4. Save your output model as `trainer/trainer.yml` inside the `face_recoginition/` folder.
5. Update the `names` array in `face_recoginition.py` to match your trained ID.
