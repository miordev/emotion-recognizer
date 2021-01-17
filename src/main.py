import recognize
import constants

def menu():
  print("Elija el método de entrenamiento")
  print("1 -> EigenFaces")
  print("2 -> LBPH")
  print("3 -> FisherFaces")

  option_method = int(input())
  METHOD = ''

  if option_method == 1:
    METHOD = constants.EIGEN_FACES
  if option_method == 2:
    METHOD = constants.LBPH
  if option_method == 3:
    METHOD = constants.FISHER_FACES
  
  recognize.main(METHOD)


menu()