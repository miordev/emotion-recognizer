import recognition_model
import constants
import os
import cv2


def get_data():
  faces_data = []
  labels = []
  
  index_label = 0
  for emotion_name in constants.EMOTIONS:
    emotion_path = os.path.join(constants.DATA_PATH, emotion_name)

    for face_name in os.listdir(emotion_path):
      labels.append(index_label)

      face_path = os.path.join(emotion_path, face_name)
      image = cv2.imread(face_path, cv2.IMREAD_GRAYSCALE)
      faces_data.append(image)

    index_label += 1

  return [faces_data, labels]


def main(method_name):
  # Dependiendo del nombre del método, crea un modelo
  model = recognition_model.create(method_name)

  # Conjunto de caras y etiquetas, clasificados según su emoción
  [faces_data, labels] = get_data()
  # Hace el entranamiento con el conjunto de imágenes (escala de grises) y etiquetas
  recognition_model.train(method_name, model, faces_data, labels)

  # Guarda el modelo en un archivo 'xml'
  recognition_model.save(method_name, model)


# main(constants.FISHER_FACES)