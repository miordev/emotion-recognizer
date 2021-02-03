import recognition_model
import constants_recognition
import os
import cv2
import csv
import numpy as np

NUM_OF_EMOTIONS = len(constants_recognition.EMOTIONS)

MIN_QUALITY = 7
MAX_IMAGES_NUM = 1200

def classify_images():
  classification = []

  for i in range(NUM_OF_EMOTIONS):
    classification.append([])

  faces_count = 0

  with open(constants_recognition.CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      
      # Ignora los headers
      if (line_count != 0):  
        # Solo fotos de entranamiento
        if (row[0] != 'Training'):
          break

        faces_count += 1

        for index_emotion in range(NUM_OF_EMOTIONS):
          column_index = 3 + index_emotion
          value = int(row[column_index])

          if ((value >= MIN_QUALITY) and (len(classification[index_emotion]) < MAX_IMAGES_NUM)):
            image_name = row[1]
            classification[index_emotion].append(image_name)
            break

      line_count += 1

  # Resultados
  print("CARAS: ", faces_count)
  print("FELICIDAD: ", len(classification[0]))
  print("SORPRESA: ", len(classification[1]))
  print("TRISTEZA: ", len(classification[2]))
  print("MOLESTO: ", len(classification[3]))

  return classification


def get_faces_data(classification):
  faces_data = []
  
  for emotion_array in classification:
    for emotion_file in emotion_array:
      emotion_path = os.path.join(constants_recognition.DATA_TRAIN_PATH, emotion_file)
      image = cv2.imread(emotion_path, cv2.IMREAD_GRAYSCALE)
      faces_data.append(image)

  return faces_data


def get_labels():
  labels = []
  for i in range(NUM_OF_EMOTIONS):
    for j in range(MAX_IMAGES_NUM):
      labels.append(i)

  return labels


def main(method_name):
  # Dependiendo del nombre del método, crea un modelo
  model = recognition_model.create(method_name)

  # Conjunto de caras y etiquetas, clasificados según su emoción
  classification = classify_images()
  
  faces_data = get_faces_data(classification)
  labels = get_labels()

  # Hace el entranamiento con el conjunto de imágenes (escala de grises) y etiquetas
  recognition_model.train(method_name, model, faces_data, labels)

  # Guarda el modelo en un archivo 'xml'
  recognition_model.save(method_name, model)


main(constants_recognition.FISHER_FACES)