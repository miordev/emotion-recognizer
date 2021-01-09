import cv2
import os
import numpy as np
import time

import methods
import emotions
import paths


def train_emotion_recognizer(method_name, model, faces_data, labels):
  print('Entrenando ( ' + method_name + ' )...')
  
  initial_time = time.time()
  model.train(faces_data, np.array(labels))
  final_time = time.time()

  train_time = final_time - initial_time
  print('Tiempo de entrenamiento: ', train_time)


def save_emotion_recognizer(method_name, model):
  if not os.path.exists(paths.MODELS_PATH):
    os.mkdir(paths.MODELS_PATH)
    
  specific_model_path = paths.MODELS_PATH + '/modelo' + method_name + '.xml'
  model.write(specific_model_path)


def create_model(method_name, faces_data, labels):
  # Dependiendo del nombre del método, crea un modelo
  model = methods.get_emotion_recognizer(method_name)

  # Hace el entranamiento con el conjunto de imágenes (escala de grises) y etiquetas
  train_emotion_recognizer(method_name, model, faces_data, labels)

  # Guarda el modelo en un archivo 'xml'
  save_emotion_recognizer(method_name, model)


def define_data(faces_data, labels):
  label = 0
  for nameDir in emotions.ALL:
    emotions_path = paths.DATA_PATH + '/' + nameDir

    for filename in os.listdir(emotions_path):
      labels.append(label)

      face_path = emotions_path + '/' + filename      
      image = cv2.imread(face_path, cv2.IMREAD_GRAYSCALE)
      faces_data.append(image)

    label += 1


# Conjunto de caras y etiquetas, clasificados según su emoción
labels = []
faces_data = []

define_data(faces_data, labels)
create_model(methods.LBPH, faces_data, labels)