import cv2
import numpy as np
from tensorflow.keras.models import load_model

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

x= load_model('emotion_model.h5')
emotions = ['Angry','Surprise','Happy','Sad','Neutral']

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not open webcam")
    exit()

while True:
    ret,frame=cap.read()

    if not ret:
        print("Error: failed to capture image")
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame,(x, y),(x + w, y + h),(255, 0, 0),2)

    roi_gray= gray[y:y+h, x:x+w]
    roi = roi_gray.astype('float') / 255.0
    roi = np.expand_dims(roi, axis=-1)
    roi = np.expand_dims(roi, axis=0)
    prediction = x.predict(roi,verbose=0)

    label = emotions[np.argmax(prediction)]

    cv2.putText(frame,label,(x, y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0, 255, 0),2)

    cv2.imshow('Emotion Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()