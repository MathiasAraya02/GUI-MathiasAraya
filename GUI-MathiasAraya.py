#Se importa tkinder y tambien se importa pygame y se inicia
import tkinter as tk
import pygame
pygame.mixer.init()

"""
VENTANA PRINCIPAL
"""
ventana = tk.Tk()
ventana.title("Proyecto de interfaz grafica Mathi")
ventana.geometry("700x580")
ventana.resizable(False, False)

#El canvas que ocupa toda la ventana para poder poner imagen de fondo y botones encima
canva1 = tk.Canvas(ventana, bg="white", width=700, height=580)
canva1.pack()

#Cargar la imagen de fondo en el canvas principal
img = tk.PhotoImage(file="paisaje_naranja.png")
canva1.create_image(0, 0, image=img, anchor="nw")
canva1.image = img  #Para evitar que la imagen se borre

canva1.create_text(350, 80, text="¡Bienvenido! Elige una de las 3 opciones", font=("Arial", 18, "bold"), fill="white")

#Los botones de la ventana principal
btn1 = tk.Button(ventana, text="Análisis de números", command=lambda: print("test"), width=18)
btn2 = tk.Button(ventana, text="Ficha personal",       command=lambda: print("test"), width=18)
btn3 = tk.Button(ventana, text="Animación",            command=lambda: print("test"), width=18)

canva1.create_window(175, 400, window=btn1)
canva1.create_window(350, 400, window=btn2)
canva1.create_window(525, 400, window=btn3)

ventana.mainloop() #Se inicia el bucle principal de la interfaz