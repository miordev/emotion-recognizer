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

root = tk.Tk()

label = tk.Label(root)
label.pack()

fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))

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

frame = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
frameCap  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
imgtk = ImageTk.PhotoImage(image = Image.fromarray(frameCap))

label.configure(image = imgtk)
root.update()

root.mainloop()