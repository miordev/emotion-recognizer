import recognition_model
import constants_recognition
import os
import cv2
import numpy as np

def get_data_to_validate():
  faces_data = []
  labels = []
  
  index_label = 0
  for emotion_name in constants_recognition.EMOTIONS:
    emotion_path = os.path.join(constants_recognition.DATA_TEST_PATH, emotion_name)

    for face_name in os.listdir(emotion_path):
      labels.append(index_label)

      face_path = os.path.join(emotion_path, face_name)
      image = cv2.imread(face_path, cv2.IMREAD_GRAYSCALE)
      faces_data.append(image)

    index_label += 1

  return [faces_data, labels]


def classify(classifier, model, limit, data, result):
  # Estos valores permiten detectar más caras o no (NO tiene nada que ver con las emociones)
  faces = classifier.detectMultiScale(data, 1.03, 3)

  if (otra in faces):
    [pos_x, pos_y, width, height] = faces[0]
    resize_face = data[pos_y : pos_y + height, pos_x : pos_x + width]
    resize_face = cv2.resize(resize_face, constants_recognition.DIMENSIONS, interpolation = cv2.INTER_CUBIC)

    prediction = model.predict(resize_face)[0]

    # Reconoce
    if(prediction == result):
      return 1
  
  return 0



def main(method_name):
  classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  model = recognition_model.load(method_name)
  limit = recognition_model.get_limit(method_name)
  
  caras = 0
  todas = 0

  [faces_data, labels] = get_data_to_validate()
  for i in range(len(faces_data)):
    todas += 1
    caras += classify(classifier, model, limit, faces_data[i], labels[i])

  print(todas)
  print(caras)


# Descomenta esta línea con el modelo que quieres
# main(constants_recognition.LBPH)
