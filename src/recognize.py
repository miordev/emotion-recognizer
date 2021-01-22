import recognition_model
import cv2
import constants_recognition
import os
import numpy as np
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from io import BytesIO

#constant
METHODS = ("EigenFaces", "LBPH", "FisherFaces")
WAYS = ("Image", "Video", "Real time")


root = tk.Tk()
root.title("Nombre de la app")
#root.resizable(0,0)
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
  if (way == "Image"):
    frame = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
  else:
    ret, frame = cap.read()
    if (ret == False):
      return

  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)

  for (pos_x, pos_y, width, height) in faces:
    print("Estoy entrando en el for")
    current_face = gray_frame[pos_y : pos_y + height, pos_x : pos_x + width]
    current_face = cv2.resize(current_face, constants_recognition.DIMENSIONS, interpolation = cv2.INTER_CUBIC)
    result = model.predict(current_face)

    label = result[0]
    value = result[1]

    cv2.putText(frame, '{}'.format(result), (pos_x, pos_y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

    if value < limit:
      cv2.putText(frame, '{}'.format(constants_recognition.EMOTIONS[label]), (pos_x, pos_y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
      cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 255, 0), 2)
    else:
      cv2.putText(frame, 'No identificado', (pos_x, pos_y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
      cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 0, 255), 2)

  frameCap  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  imgtk = ImageTk.PhotoImage(image = Image.fromarray(frameCap))
  gif_label.configure(image = imgtk)
  if (way == "Real time"):
    root.update()
    gif_label.after(1, reconocimiento())
  
def browse(): 
  fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
  global image_bytes
  imgUp = Image.open(fln)
  buf = BytesIO()

  # Save the image as jpeg to the buffer
  imgUp.save(buf, 'jpeg')

  # Rewind the buffer's file pointer
  buf.seek(0)

  # Read the bytes from the buffer
  image_bytes = buf.read()

  # Close the buffer
  buf.close()

  reconocimiento()

def run():
    global way
    way = combobox_ways.get()
    global method
    method = combobox_methods.get()
    print("way: ", way)
    print("method: ", method)
  
    
    global cap 
    cap = cv2.VideoCapture(-1)

    title_method.place_forget()
    combobox_methods.place_forget()
    title_way.place_forget()
    combobox_ways.place_forget()
    button.place_forget()

    global face_classifier
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    global model 
    model = recognition_model.load(method)
    global limit
    limit = recognition_model.get_limit(method)

    if way == "Image":
      gif_label.place_forget()
      label = Label(root)
      label.pack(side=TOP)
      btn =  tk.Button(root, text="Browse Image", command=browse)
      btn.pack(side=BOTTOM, pady=15)
    if way == "Video":
        print("No implementado aún")
    if way == "Real time":
        # Detector de rostros
        reconocimiento()
        return

gif_label = tk.Label(root)
gif_label.pack()

animation(count)

root.mainloop()

# main(constants_recognition.EIGEN_FACES)