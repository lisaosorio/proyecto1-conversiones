import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def ventana_longitud():
    ventana= tk.Toplevel()
    ventana.title("Longitud")
    ventana.geometry("250x300")
    ventana.configure(bg="#edf582")

    tk.Label(ventana, text="Ingresa el valor a convertir",bg="#edf582",font=("Arial", 14)).pack()
    entry=tk.Entry(ventana)
    entry.pack(padx=5, pady=5)

    eleccion=tk.StringVar(value="Metro a Kilómetro")
    combo = ttk.Combobox(ventana, textvariable=eleccion, values=["Metro a Kilómetro", "Pulgada a Metro"])
    combo.pack(padx=5, pady=5)

    etiqueta_unidad = tk.Label(ventana, text=" " ,bg="#edf582",font=("Arial", 10))
    etiqueta_unidad.pack(padx=5,pady=5) 

    etiqueta_resultado=tk.Label(ventana, text="Resultado", bg="#edf582", font=("Arial", 12))
    etiqueta_resultado.pack()

    def convertir():
        try:
            inicial=float(entry.get())
            if eleccion.get()== "Metro a Kilómetro":
                resultado= inicial/1000
                etiqueta_unidad.config(text="Conversión de Metro a Kilómetro")
                unidad= " Km"

            else:
                resultado= inicial *0.0254
                etiqueta_unidad.config(text="Conversión de Pulgada a Metro")
                unidad= " M"

            etiqueta_resultado.config(text=f"Resultado: {resultado:.3f}{unidad}", bg="#edf582", font=("Arial", 13))
        except ValueError:
            #mostrar error si no se ingresan números
            etiqueta_resultado.config(text="¡Error, ingresa números válidos!", fg="red")
    boton= tk.Button(ventana, text="Convertir", command=convertir, font=("Arial", 13), bg="#b0fffc")
    boton.pack(padx=5, pady=5)


def ventana_masa():
    ventana= tk.Toplevel()
    ventana.title("Masa")
    ventana.geometry("250x300")
    ventana.configure(bg="#edf582")

    tk.Label(ventana, text="Ingresa el valor a convertir",bg="#edf582",font=("Arial", 14)).pack()
    entry=tk.Entry(ventana)
    entry.pack(padx=5, pady=5)

    eleccion=tk.StringVar(value="Kilogramo a Gramo")
    combo = ttk.Combobox(ventana, textvariable=eleccion, values=["Kilogramo a Gramo", "Libra a Kilogramo"])
    combo.pack(padx=5, pady=5)

    etiqueta_unidad = tk.Label(ventana, text=" " ,bg="#edf582",font=("Arial", 10))
    etiqueta_unidad.pack(padx=5,pady=5)

    etiqueta_resultado=tk.Label(ventana, text="Resultado", bg="#edf582", font=("Arial", 12))
    etiqueta_resultado.pack(padx=5, pady=5)

    def convertir():
        try:
            inicial=float(entry.get())
            if eleccion.get()== "Kilogramo a Gramo":
                resultado= inicial*1000
                unidad= " G"
                etiqueta_unidad.config(text="Conversión de Kilogramo a Gramo")

            else:
                resultado= inicial *0.453592
                unidad= " Kg"
                etiqueta_unidad.config(text="Conversión de Libra a Kilogramo")

            etiqueta_resultado.config(text=f"Resultado: {resultado:.3f} {unidad}", font=("Arial", 13))
        except ValueError:
            #mostrar error si no se ingresan números
            etiqueta_resultado.config(text="¡Error, ingresa números válidos!", fg="red")
    boton= tk.Button(ventana, text="Convertir", command=convertir, font=("Arial", 13), bg="#b0fffc")
    boton.pack(padx=5, pady=5)

def ventana_tiempo():
    ventana = tk.Toplevel()
    ventana.title("Tiempo")
    ventana.geometry("250x300")
    ventana.configure(bg="#edf582")

    tk.Label(ventana, text="Ingresa el valor a convertir",bg="#edf582",font=("Arial", 14)).pack()
    entry = tk.Entry(ventana)
    entry.pack(padx=5, pady=5)

    eleccion = tk.StringVar(value="Segundo a Minuto")
    combo = ttk.Combobox(ventana, textvariable=eleccion, values=["Segundo a Minuto", "Hora a Día"])
    combo.pack(padx=5, pady=5)

    etiqueta_unidad = tk.Label(ventana, text=" " ,bg="#edf582",font=("Arial", 10))
    etiqueta_unidad.pack(padx=5,pady=5)

    etiqueta_resultado=tk.Label(ventana, text="Resultado", bg="#edf582", font=("Arial", 12))
    etiqueta_resultado.pack(padx=5, pady=5)

    def convertir():
        try:
            inicial = float(entry.get())
            if eleccion.get() == "Segundo a Minuto":
                resultado = inicial / 60
                unidad= " Min"
                etiqueta_unidad.config(text="Conversión de Segundo a Minuto")
            else:
                resultado = inicial / 24
                unidad= " D"
                etiqueta_unidad.config(text="Conversión de Hora a Día")
            etiqueta_resultado.config(text=f"Resultado: {resultado:.3f} {unidad}",font=("Arial", 13))
        except ValueError:
            etiqueta_resultado.config(text="¡Error, ingresa números válidos!", fg="red")

    boton = tk.Button(ventana, text="Convertir", command=convertir,font=("Arial", 13), bg="#b0fffc" )
    boton.pack(padx=5, pady=5)

ventana = tk.Tk()
ventana.title("Conversiones")
ventana.geometry("450x300")
ventana.configure(bg="#b0fffc")

etiqueta= tk.Label(ventana, text="¿Qué tipo de conversión deseas hacer?",bg="#b0fffc", font=("Arial", 16))
etiqueta.pack(padx=5, pady=5)

boton_longitud=tk.Button(ventana, text="Longitud", bg="white", font=("Arial", 13), command=ventana_longitud)
boton_longitud.pack(padx=5, pady=5)

boton_masa=tk.Button(ventana, text="Masa", bg="white", font=("Arial", 13), command=ventana_masa)
boton_masa.pack(padx=5, pady=5)

boton_tiempo=tk.Button(ventana, text="Tiempo", bg="white", font=("Arial", 13), command=ventana_tiempo)
boton_tiempo.pack(padx=5, pady=5)

ventana.mainloop()