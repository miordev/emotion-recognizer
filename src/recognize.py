import recognition_model
import cv2
import constants


def main(method_name):
  print('Reconociendo ( ' + method_name + ' )...')
  model = recognition_model.load(method_name)
  limit = recognition_model.get_limit(method_name)

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
      current_face = cv2.resize(current_face, constants.DIMENSIONS, interpolation = cv2.INTER_CUBIC)
      result = model.predict(current_face)

      label = result[0]
      value = result[1]

      cv2.putText(frame, '{}'.format(result), (pos_x, pos_y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

      if value < limit:
        cv2.putText(frame, '{}'.format(constants.EMOTIONS[label]), (pos_x, pos_y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
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


# main(constants.EIGEN_FACES)