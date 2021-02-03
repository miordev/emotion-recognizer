from os import system
import sys

def help():
  print('Run the program with one of the following arguments')  
  print('\t-h --help \t\t Help to run the programme')  
  print('\t-i --interface\t\t Run the program interface')  
  print('\t-t --test\t\t Execute the validation of the models')  

def main():
  if len(sys.argv) != 2:
    return help()

  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    return help()
  
  elif sys.argv[1] == "--test" or sys.argv[1] == "-t":
    system('python test.py')
  
  elif sys.argv[1] == "--interface" or sys.argv[1] == "-i":
    system('python3 recognize.py')

  else:
    return help()  
    
main()