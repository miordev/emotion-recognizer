#Library
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import entrenando, reconocimientoEmociones

#constant
METHOD = ''
WAY = ''
METHODS = ("EigenFaces", "LBPH", "FisherFaces")
WAYS = ("Image", "Video", "Real time")

# Methods
def something():
  canvas.itemconfig(text_canvas, text = "Choose your method")
  WAY = combobox.get()
  
  print("way: ", WAY) #Comprobación
  
  combobox.set('')
  combobox['values'] = METHODS
  button.config(command = menu)

def menu():
  # Elige el método seleccionado
  METHOD = combobox.get()
  combobox.set('')

  ## Eliminamos los elementos de la ventana actual
  canvas.delete("all")
  combobox.place_forget()
  button.place_forget()
  
  print("method: ", METHOD) #Comprobación

  #Entrena los modelos
  entrenando.obtenerModelo(METHOD, entrenando.facesData, entrenando.labels)
  select_way(WAY)
  #Covierte los frame en PhotoImage para mostrarlo por Tkinter
  
  
def select_way(way):
  if WAY == "Image":
    print("No implementado aún")
  if WAY == "Video":
    print("No implementado aún")
  if WAY == "Real time":
    lmain = Label(window, width = windowWidth, height = windowHeight)
    lmain.pack()
    while True:
      frame = reconocimientoEmociones.reconocimiento(METHOD)
      show_frame(frame)


def show_frame(frame):
       frame = cv2.flip(frame, 1)
       cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
       img = Image.fromarray(cv2image)
       imgtk = ImageTk.PhotoImage(image=img)
       lmain.imgtk = imgtk
       lmain.configure(image=imgtk)
       lmain.after(10, show_frame)

#Windows attributes
window = Tk()
window.title("Nombre de la app")
filename = ImageTk.PhotoImage(file = "assets/background.jpg")
windowWidth = filename.width()
windowHeight = filename.height()

#Center the window
x_screen = window.winfo_screenwidth() // 2 - windowWidth // 2
y_screen = window.winfo_screenheight() // 2 - windowHeight // 2

posicion = str(windowWidth) + "x" + str(windowHeight) + "+" + str(x_screen) + "+" + str(y_screen)
window.geometry(posicion)

window.resizable(0,0)

# Window contain
canvas = Canvas(width = windowWidth, height = windowHeight, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

canvas.create_image(0, 0, image = filename, anchor = NW)
text_canvas = canvas.create_text(320, 160, text = "How do you want to do it?", font=("Arial", 16), fill = "#ffffff")
text_canvas

combobox = ttk.Combobox(window)
combobox['values'] = WAYS
combobox.place(x=230, y=180)

button = Button(window, text = "click", command = something, activebackground="#A239CA", bg="#4717F6")
button.place(x=290, y=220)

window.mainloop()