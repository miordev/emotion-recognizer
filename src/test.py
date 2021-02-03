import recognition_model
import constants_recognition
import os
import cv2
import numpy as np
import csv

SCALE = 1.1
MAX_SCALE = 1.9
SCALE_INCREASE = 0.1

FILTER = 0
MAX_FILTER = 2
FILTER_INCREASE = 1

MIN_FACES = 10

NUM_OF_EMOTIONS = len(constants_recognition.EMOTIONS)

MIN_QUALITY = 8
MAX_IMAGES_NUM = 225

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
      emotion_path = os.path.join(constants_recognition.DATA_TEST_PATH, emotion_file)
      image = cv2.imread(emotion_path, cv2.IMREAD_GRAYSCALE)
      faces_data.append(image)

  return faces_data


def get_labels():
  labels = []
  for i in range(NUM_OF_EMOTIONS):
    for j in range(MAX_IMAGES_NUM):
      labels.append(i)

  return labels


def classify_face(classifier, model, limit, data, result, current_scale, current_filter):
  faces = classifier.detectMultiScale(data, current_scale, current_filter)

  otra = 0
  if (otra in faces):
    [pos_x, pos_y, width, height] = faces[0]
    resize_face = data[pos_y : pos_y + height, pos_x : pos_x + width]
    resize_face = cv2.resize(resize_face, constants_recognition.DIMENSIONS, interpolation = cv2.INTER_CUBIC)

    prediction = model.predict(resize_face)[0]

    # Reconoce
    if(prediction == result):
      return 1
    # No reconoce la emocion 
    return 2
  
  # No hay cara
  return 0


def classify_all_faces(classifier, model, limit, faces_data, labels, current_scale, current_filter):
  count_with_emotion = 0
  count_without_emotion = 0
  total_faces = len(faces_data)

  for i in range(total_faces):
    value = classify_face(
      classifier,
      model,
      limit,
      faces_data[i],
      labels[i],
      current_scale,
      current_filter
    )
    
    if (value == 1):
      count_with_emotion += 1
    elif (value == 2):
      count_without_emotion += 1

  print("CARAS DETECTADAS: ", count_with_emotion + count_without_emotion)
  if (count_with_emotion > MIN_FACES):
    return (count_with_emotion / (count_with_emotion + count_without_emotion)) * 100
  return 0


def get_better_values(method_name):
  classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  model = recognition_model.load(method_name)
  limit = recognition_model.get_limit(method_name)
  
  classification = classify_images()
  faces_data = get_faces_data(classification)
  labels = get_labels()

  best_value = 0
  best_scale = 0
  best_filter = 0
  
  c_scale = SCALE
  while (c_scale <= MAX_SCALE):
    c_filter = FILTER
    while (c_filter <= MAX_FILTER):
      current_value = classify_all_faces(
        classifier,
        model,
        limit,
        faces_data,
        labels,
        c_scale,
        c_filter
      )

      if (current_value > best_value):
        best_value = current_value
        best_scale = c_scale
        best_filter = c_filter

      print('ACTUAL ESCALA: ', c_scale)
      print('ACTUAL FILTRO: ', c_filter)
      print('ACTUAL PORCENTAJE: ', current_value)
      print('--------------------------')

      c_filter += FILTER_INCREASE
    c_scale += SCALE_INCREASE

  print('MEJOR ESCALA: ', best_scale)
  print('MEJOR FILTRO: ', best_filter)
  print('MEJOR PORCENTAJE: ', best_value)
  print('--------------------------')

get_better_values(constants_recognition.LBPH)
