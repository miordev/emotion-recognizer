import os
import constants_recognition
import cv2
import time
import numpy as np


def train(method_name, model, faces_data, labels):
  print('Entrenando ( ' + method_name + ' )...')
  
  initial_time = time.time()
  model.train(faces_data, np.array(labels))
  final_time = time.time()

  train_time = final_time - initial_time
  print('Tiempo de entrenamiento: ', train_time)


def save(method_name, model):
  if not os.path.exists(constants_recognition.MODELS_PATH):
    os.mkdir(constants_recognition.MODELS_PATH)
  
  filename = 'model' + method_name + '.xml'
  specific_model_path = os.path.join(constants_recognition.MODELS_PATH, filename)
  model.write(specific_model_path)


def load(method_name):
  model = create(method_name)

  filename = 'model' + method_name + '.xml'
  specific_model_path = os.path.join(constants_recognition.MODELS_PATH, filename)
  print(specific_model_path)
  model.read(specific_model_path)
  return model


def create(method_name):
  if (method_name == constants_recognition.EIGEN_FACES):
    return cv2.face.EigenFaceRecognizer_create()

  if (method_name == constants_recognition.FISHER_FACES):
    return cv2.face.FisherFaceRecognizer_create()

  if (method_name == constants_recognition.LBPH):
    return cv2.face.LBPHFaceRecognizer_create()


def get_limit(method_name):
  if (method_name == constants_recognition.EIGEN_FACES):
    return constants_recognition.LIMIT_EIGEN_FACES

  if (method_name == constants_recognition.FISHER_FACES):
    return constants_recognition.LIMIT_FISHER_FACES

  if (method_name == constants_recognition.LBPH):
    return constants_recognition.LIMIT_LBPH