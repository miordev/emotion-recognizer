import cv2
import os
import numpy as np
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time as tm
import time
import entrenando

#constant
METHODS = ("EigenFaces", "LBPH", "FisherFaces")
WAYS = ("Image", "Video", "Real time")


root = tk.Tk()
root.title("Nombre de la app")
root.resizable(0,0)
file="assets/frame1_modified2.gif"

info = Image.open(file)
start = ImageTk.PhotoImage(file = "assets/get_started.jpg")
button = ImageTk.PhotoImage(file = "assets/button.jpg")
menu = ImageTk.PhotoImage(file = "assets/menu.jpg")

frames = info.n_frames  # gives total number of frames that gif contains
# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        something()
        return # Para que haga el gif solo una vez
    anim = root.after(20,lambda :animation(count))


def something():
    gif_label.configure(image = start)
    global button_label
    button_label = Button(root, image = button, command = begin, borderwidth = 0)
    button_label.place(x=270, y=410)

def begin():
    button_label.place_forget()
    gif_label.configure(image = menu)

    ## form

    global title_way
    title_way = Label(root, text = "How do you want to do it?")
    title_way.place(x=320, y=150)

    global combobox_ways
    combobox_ways = ttk.Combobox(root)
    combobox_ways['values'] = WAYS
    combobox_ways.place(x=320, y=180)

    global title_method
    title_method = Label(root, text = "Choose your method")
    title_method.place(x=320, y=220)

    global combobox_methods
    combobox_methods = ttk.Combobox(root)
    combobox_methods['values'] = METHODS
    combobox_methods.place(x=320, y=250)

    global button
    button = Button(root, text = "click", command = run, activebackground="#A239CA", bg="#4717F6")
    button.place(x=375, y=280)

def reconocimiento():
  
  NUMBER_RESULT = 0
  # ----------- Métodos usados para el entrenamiento y lectura del modelo ----------

  if method == 'EigenFaces': 
    emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
    NUMBER_RESULT = 5700
  if method == 'FisherFaces': 
    emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
    NUMBER_RESULT = 500
  if method == 'LBPH': 
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()
    NUMBER_RESULT = 60

  emotion_recognizer.read('../models/modelo'+method+'.xml')

  # --------------------------------------------------------------------------------
  dataPath = '../data' #Cambia a la ruta donde hayas almacenado Data
  imagePaths = os.listdir(dataPath)

  faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

  
  ret,frame = cap.read()
  if ret == False: 
    print("No se abrio")
    return
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  auxFrame = gray.copy()

  nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])
  faces = faceClassif.detectMultiScale(gray,1.3,5)

  for (x,y,w,h) in faces:
    rostro = auxFrame[y:y+h,x:x+w]
    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
    result = emotion_recognizer.predict(rostro)

    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

    if method:
      if result[1] < NUMBER_RESULT:
        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
      else:
        cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        nFrame = cv2.hconcat([frame,np.zeros((480,300,3),dtype=np.uint8)])
  title_method.place_forget()
  combobox_methods.place_forget()
  title_way.place_forget()
  combobox_ways.place_forget()
  button.place_forget()
    
  frameCap  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  imgtk = ImageTk.PhotoImage(image = Image.fromarray(frameCap))
  gif_label.configure(image=imgtk)
  root.update()
  gif_label.after(1, reconocimiento())

  

def run():
    way = combobox_ways.get()
    global method
    method = combobox_methods.get()
    print("way: ", way)
    print("method: ", method)
  
    global cap 
    cap = cv2.VideoCapture(-1)
    if way == "Image":
        print("No implementado aún")
    if way == "Video":
        print("No implementado aún")
    if way == "Real time":
        reconocimiento()
        return

gif_label = tk.Label(root)
gif_label.pack()

animation(count)

root.mainloop()

