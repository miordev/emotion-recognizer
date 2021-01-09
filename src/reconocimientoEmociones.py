import cv2
import os
import numpy as np

import methods
import emotions
import paths

def load_model(method_name):
  model = methods.get_emotion_recognizer(method_name)
  specific_model_path = paths.MODELS_PATH + '/modelo' + method_name + '.xml'
  model.read(specific_model_path)
  return model

  
def recognition(method_name):
  print('Reconociendo ( ' + method_name + ' )...')
  model = load_model(method_name)
  limit = methods.get_limit_emotion_recognizer(method_name)

  # Cámara por defecto
  camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  # Detector de rostros
  face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

  while (True):
    ret, frame = camera.read()
    if (ret == False):
      break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)

    for (pos_x, pos_y, width, height) in faces:
      current_face = gray_frame[pos_y : pos_y + height, pos_x : pos_x + width]
      current_face = cv2.resize(current_face, emotions.DIMENSIONS, interpolation = cv2.INTER_CUBIC)
      result = model.predict(current_face)

      label = result[0]
      value = result[1]

      cv2.putText(frame, '{}'.format(result), (pos_x, pos_y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

      if value < limit:
        cv2.putText(frame, '{}'.format(emotions.ALL[label]), (pos_x, pos_y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 255, 0), 2)
      else:
        cv2.putText(frame, 'No identificado', (pos_x, pos_y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 0, 255), 2)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    ESCAPE_KEY = 27
    if key == ESCAPE_KEY:
      break

  camera.release()
  cv2.destroyAllWindows()


recognition(methods.LBPH)