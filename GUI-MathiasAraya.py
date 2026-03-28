#Se importa tkinder y tambien se importa pygame y se inicia
import tkinter as tk
import pygame
pygame.mixer.init()

# La variable global para controlar que solo exista una ventana secundaria abierta a la vez
ventana_secundaria_activa = None

def abrir_ventana_secundaria(titulo, contenido_fn):
#Abre una ventana secundaria que ya tiene su rol definido. Si ya hay una abierta, la trae al frente en lugar de crear otra. contenido_fn: función que construye el contenido dentro del frame
    global ventana_secundaria_activa
    if ventana_secundaria_activa is not None and ventana_secundaria_activa.winfo_exists():
        ventana_secundaria_activa.lift()
        ventana_secundaria_activa.focus_force()
        return
    secundaria = tk.Toplevel(ventana)
    secundaria.title(titulo)
    secundaria.geometry("600x480")
    secundaria.resizable(False, False)

    ventana_secundaria_activa = secundaria
    #Al cerrar con la X, se ejecuta cerrar_secundaria para limpiar correctamente
    secundaria.protocol("WM_DELETE_WINDOW", lambda: cerrar_secundaria(secundaria))

    #Para que el frame principal tenga el fondo de color
    frame_principal = tk.Frame(secundaria, bg="#2c2c2c")
    frame_principal.pack(fill="both", expand=True)

    #La parte de arriba con el botón de volver y el título de la sección
    frame_header = tk.Frame(frame_principal, bg="#1a1a2e", pady=8)
    frame_header.pack(fill="x")

    tk.Button(frame_header, text="Volver", command=lambda: cerrar_secundaria(secundaria), font=("Arial", 10, "bold"), padx=10, cursor="hand2").pack(side="left", padx=10)
    tk.Label(frame_header, text=titulo, font=("Arial", 14, "bold"), bg="#1a1a2e", fg="white").pack(side="left", padx=10)

    #El área de contenido donde cada sección coloca sus widgets
    frame_contenido = tk.Frame(frame_principal, bg="#2c2c2c", padx=20, pady=20)
    frame_contenido.pack(fill="both", expand=True)

    contenido_fn(frame_contenido)  #Se llama a la función específica de cada sección


def cerrar_secundaria(win):
#Detiene la música, limpia la variable global y destruye la ventana secundaria
    global ventana_secundaria_activa
    pygame.mixer.music.stop()
    ventana_secundaria_activa = None
    win.destroy()

"""
ANÁLISIS DE NÚMEROS
"""
def contenido_analisis(frame):
#Muestra todos los pares de divisores de el número ingresado

    def encontrar_pares(n, a=1, resultado=None):
    #Prueba cada divisor 'a' desde 1 hasta n. Si a divide a n, guarda el par (a, n//a) y se evitan duplicados con a <= b
        if resultado is None:
            resultado = []
        if a > n:
            return resultado
        if n % a == 0:
            b = n // a
            if a <= b:
                resultado.append((a, b))
        return encontrar_pares(n, a + 1, resultado)

    def mostrar_pares(pares, i):
    #Se ejecuta la recursividad y inserta cada par en el widget de texto uno por uno
        if i >= len(pares):
            return
        a, b = pares[i]
        texto_resultado.insert("end", f"  ({a},  {b})\n")
        mostrar_pares(pares, i + 1)

    def calcular():
    #Se valida el número que entra y llama a encontrar_pares para mostrar el resultado
        texto_resultado.config(state="normal")
        texto_resultado.delete("1.0", "end")

        entrada = entry_numero.get().strip()

        #Se verifica que sea un número entero válido
        if not entrada.lstrip("-").isdigit():
            texto_resultado.insert("end", "¡Error! Debes ingresar un número entero positivo.")
            texto_resultado.config(state="disabled")
            return

        n = int(entrada)
        if n <= 0:
            texto_resultado.insert("end", "¡Error! Debes ingresar un número entero positivo.")
            texto_resultado.config(state="disabled")
            return

        pares = encontrar_pares(n)
        texto_resultado.insert("end", f"Los pares de {n} son:\n\n")
        mostrar_pares(pares, 0)
        texto_resultado.config(state="disabled")

    #Widgets de Analisis de números
    tk.Label(frame, text="¿Quieres saber los pares de un número?", font=("Arial", 16, "bold"), bg="#2c2c2c", fg="white").pack(pady=(10, 4))
    tk.Label(frame, text="Ingresa un número entero positivo en el espacio de texto.", font=("Arial", 10), bg="#2c2c2c", fg="#aaaaaa", justify="center").pack(pady=(0, 12))

    frame_entrada = tk.Frame(frame, bg="#2c2c2c")
    frame_entrada.pack()

    entry_numero = tk.Entry(frame_entrada, font=("Arial", 13), width=10, justify="center", bg="#3d3d3d", fg="white", insertbackground="white", relief="flat")
    entry_numero.pack(side="left", padx=(0, 10))
    entry_numero.bind("<Return>", lambda e: calcular())  # Permite calcular con Enter

    tk.Button(frame_entrada, text="Calcular", command=calcular, font=("Arial", 11, "bold"), padx=12, cursor="hand2").pack(side="left")

    #Lugar donde sale el resultado del número ingresado
    frame_resultado = tk.Frame(frame, bg="#2c2c2c")
    frame_resultado.pack(fill="both", expand=True, pady=(14, 0))

    scrollbar = tk.Scrollbar(frame_resultado)
    scrollbar.pack(side="right", fill="y")

    texto_resultado = tk.Text(frame_resultado, font=("Courier", 11), state="disabled", yscrollcommand=scrollbar.set, padx=10, pady=8)
    texto_resultado.pack(fill="both", expand=True)
    scrollbar.config(command=texto_resultado.yview)

#Funciones de acceso desde la ventana principal
def analisis_de_números():
    abrir_ventana_secundaria("Análisis de Números", contenido_analisis)

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
btn1 = tk.Button(ventana, text="Análisis de números", command=analisis_de_números, width=18)
btn2 = tk.Button(ventana, text="Ficha personal",       command=lambda: print("test"), width=18)
btn3 = tk.Button(ventana, text="Animación",            command=lambda: print("test"), width=18)

canva1.create_window(175, 400, window=btn1)
canva1.create_window(350, 400, window=btn2)
canva1.create_window(525, 400, window=btn3)

ventana.mainloop() #Se inicia el bucle principal de la interfaz