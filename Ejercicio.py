<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Conversiones")
ventana.geometry("450x300")
ventana.configure(bg="#e38dbc")

etiqueta = tk.Label(ventana, text="Escoge una opción")

boton_longitud=tk.Button(ventana, text="Longitud", bg="white")
boton_longitud.pack()

boton_masa=tk.Button(ventana, text="Masa", bg="white")
boton_masa.pack()

boton_tiempo=tk.Button(ventana, text="Tiempo", bg="white")
boton_tiempo.pack()
=======
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Conversiones")
ventana.geometry("450x300")
ventana.configure(bg="#e38dbc")
>>>>>>> 6486bb9 (Correccion de nombre de archivo)
ventana.mainloop()