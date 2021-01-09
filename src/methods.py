import cv2

EIGEN_FACES = 'EigenFaces'
FISHER_FACES = 'FisherFaces'
LBPH = 'LBPH'

LIMIT_EIGEN_FACES = 5700
LIMIT_FISHER_FACES = 500
LIMIT_LBPH = 600


def get_emotion_recognizer(method_name):
  if (method_name == EIGEN_FACES):
    return cv2.face.EigenFaceRecognizer_create()

  if (method_name == FISHER_FACES):
    return cv2.face.FisherFaceRecognizer_create()

  if (method_name == LBPH):
    return cv2.face.LBPHFaceRecognizer_create()


def get_limit_emotion_recognizer(method_name):
  if (method_name == EIGEN_FACES):
    return LIMIT_EIGEN_FACES

  if (method_name == FISHER_FACES):
    return LIMIT_FISHER_FACES

  if (method_name == LBPH):
    return LIMIT_LBPH