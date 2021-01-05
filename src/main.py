import reconocimientoEmociones

METHOD = ''

def menu():
  print("Elija el método de entrenamiento")
  print("1 -> EigenFaces")
  print("2 -> LBPH")
  print("3 -> FisherFaces")

  option_method = int(input())
  if option_method == 1:
      METHOD = "EigenFaces"
  if option_method == 2:
      METHOD = "LBPH"
  if option_method == 3:
      METHOD = "FisherFaces"
  
  # entrenando.obtenerModelo(METHOD, entrenando.facesData, entrenando.labels)

  reconocimientoEmociones.reconocimiento(METHOD)


menu()