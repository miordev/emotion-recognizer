from os import system
import sys

def help():
  print('Ejecute el programa con uno de los siguientes argumentos')  
  print('\t-t --help \t\t Ayuda para ejecutar el programa')  
  print('\t-i --interface\t\t Ejecutar la interface del programa')  
  print('\t-t -test\t\t Ejecutar la validación de los modelos')  

def main():
  if len(sys.argv) != 2:
    return help()

  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    return help()
  
  elif sys.argv[1] == "--test" or sys.argv[1] == "-t":
    system('python test.py')
  
  elif sys.argv[1] == "--interface" or sys.argv[1] == "-i":
    system('python prueba2.py')

  else:
    return help()  

    
main()