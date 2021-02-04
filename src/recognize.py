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
root.title("Odalig")
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
    button_label.place(x=260, y=410)

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
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("JPEG", "*.jpeg")))
    frame = cv2.imread(fln)
    img = Image.open(fln)
    img = img.resize((450, 350), Image. ANTIALIAS)
    img = ImageTk.PhotoImage(image = img)
  elif (way == "Video"): 
    if (not(cap.isOpened())):
      return 
    
    ret, frame = cap.read()
    if (ret == False):
      return                                                                                                                   
  else:
    ret, frame = cap.read()
    if (ret == False):
      return

  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)
  text_emotion = "Indeterminado"
  for (pos_x, pos_y, width, height) in faces:
    current_face = gray_frame[pos_y : pos_y + height, pos_x : pos_x + width]
    current_face = cv2.resize(current_face, constants_recognition.DIMENSIONS, interpolation = cv2.INTER_CUBIC)
    result = model.predict(current_face)

    label = result[0]
    value = result[1]

    text_emotion = constants_recognition.EMOTIONS[label]

    if (way == "Video" or way == "Real time"):
      cv2.putText(frame, '{}'.format(result), (pos_x, pos_y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

      if value < limit:
        cv2.putText(frame, '{}'.format(constants_recognition.EMOTIONS[label]), (pos_x, pos_y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 255, 0), 2)
      else:
        cv2.putText(frame, 'No identificado', (pos_x, pos_y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (pos_x, pos_y), (pos_x + width, pos_y + height), (0, 0, 255), 2)

  if (way == "Image"):
    gif_label.place_forget()
    lb.configure(text = "Emotion: ")
    emotion.configure(text = text_emotion)
    img_label.configure(image = img)
    img_label.update()
    img_label.after(5000)

  if (way == "Real time" or way == "Video"):
    frameCap  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgtk = ImageTk.PhotoImage(image = Image.fromarray(frameCap))
    gif_label.configure(image = imgtk)
    root.update()
    gif_label.after(0, reconocimiento())

def run():
    global way
    way = combobox_ways.get()
    global method
    method = combobox_methods.get()
    print("way: ", way)
    print("method: ", method)

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
    global cap

    if (way == "Image"):
      gif_label.configure(image = "")
      global lb
      lb = tk.Label(root, text = "")
      lb.pack(side=TOP)
      global emotion
      emotion = tk.Label(root, text = "")
      emotion.pack()
      global img_label
      img_label = tk.Label(root)
      img_label.pack()
      btnImage =  tk.Button(root, text="Browse Image", command=reconocimiento)
      btnImage.pack(side=BOTTOM, pady=15)

    if (way == "Video"):
      gif_label.configure(image = "")
      fln = filedialog.askopenfilename()  
      cap = cv2.VideoCapture(fln)
      reconocimiento()

    if (way == "Real time"):
      cap = cv2.VideoCapture(-1)
      reconocimiento()

gif_label = tk.Label(root)
gif_label.pack()

animation(count)

root.mainloop()

# main(constants_recognition.EIGEN_FACES)