#importamos las librerias necesarias
import os
import tkinter as tk
from tkinter import Label, OptionMenu, StringVar
from PIL import Image, ImageTk  
from tkinter import messagebox

precio1 = "200"
precio2 = "500"
precio3 = "800"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Catálogo De Relojes")
ventana.resizable(False, False)  # Deshabilitar el redimensionamiento
ventana.configure(bg='black')  # Cambiar el fondo de la ventana a negro

# Calcular el tamaño de la ventana y de la pantalla
ancho_ventana = 700
alto_ventana = 500
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

# Aplicar tamaño y posición centrada a la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Cargar y establecer el ícono de la ventana
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")

# Cargar la imagen
img = Image.open(logo_path)  # Ruta al archivo de imagen
img = img.resize((32, 32))  # Redimensionar la imagen
icon = ImageTk.PhotoImage(img)
ventana.tk.call('wm', 'iconphoto', ventana._w, icon) #establecemos el icono de la ventana

# Diccionario de productos
analogico= {
    "Audi": [
        {"marca": "Audi", "nombre_color": "Nardo Grey", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#7D7E82.jpg"},
        {"marca": "Audi", "nombre_color": "Misano Red", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#B12227.jpg"},
        {"marca": "Audi", "nombre_color": "Grey Red Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#926D54.jpg"}
    ],
    "BMW": [
        {"marca": "BMW", "nombre_color": "Alpine White", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#F8F8F6.jpg"},
        {"marca": "BMW", "nombre_color": "Estoril Blue", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#1F50A5.jpg"},
        {"marca": "BMW", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#DAE8E2.jpg"}
    ],
    "Mercedes-Benz": [
        {"marca": "Mercedes-Benz", "nombre_color": "Silver", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#C0C0C0.jpg"},
        {"marca": "Mercedes-Benz", "nombre_color": "Obsidian Black", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#1C1C1C.jpg"},
        {"marca": "Mercedes-Benz", "nombre_color": "Silver Black Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#888888.jpg"}
    ],
    "Maybach": [
        {"marca": "Maybach", "nombre_color": "Opal Black", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#191919.jpg"},
        {"marca": "Maybach", "nombre_color": "Patagonia Silver", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#A8A8A8.jpg"},
        {"marca": "Maybach", "nombre_color": "Black Silver Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#60606C.jpg"}
    ],
    "Porsche": [
        {"marca": "Porsche", "nombre_color": "Guards Red", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#D21F26.jpg"},
        {"marca": "Porsche", "nombre_color": "Racing Yellow", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#FDE101.jpg"},
        {"marca": "Porsche", "nombre_color": "Red Yellow Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#D25F14.jpg"}
    ],
    "Alfa Romeo": [
        {"marca": "Alfa Romeo", "nombre_color": "Rosso Competizione", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#B83941.jpg"},
        {"marca": "Alfa Romeo", "nombre_color": "Verde Montreal", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#01A049.jpg"},
        {"marca": "Alfa Romeo", "nombre_color": "Red Green Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#8D581C.jpg"}
    ],
    "Ferrari": [
        {"marca": "Ferrari", "nombre_color": "Rosso Corsa", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#D40000.jpg"},
        {"marca": "Ferrari", "nombre_color": "Giallo Modena", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F7E400.jpg"},
        {"marca": "Ferrari", "nombre_color": "Red Yellow Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#CE7200.jpg"}
    ],
    "Lamborghini": [
        {"marca": "Lamborghini", "nombre_color": "Black", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#000000.jpg"},
        {"marca": "Lamborghini", "nombre_color": "Gold", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#D4AF37.jpg"},
        {"marca": "Lamborghini", "nombre_color": "Black Gold Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#6C6C6C.jpg"}
    ],
    "Maserati": [
        {"marca": "Maserati", "nombre_color": "Blu Emozione", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#0E3C82.jpg"},
        {"marca": "Maserati", "nombre_color": "Rosso Trionfale", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#9B1B30.jpg"},
        {"marca": "Maserati", "nombre_color": "Blue Red Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#520E56.jpg"}
    ],
    "Pagani": [
        {"marca": "Pagani", "nombre_color": "Carbon Fiber Black", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#1A1A1A.jpg"},
        {"marca": "Pagani", "nombre_color": "Liquid Silver", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#C0C0C0.jpg"},
        {"marca": "Pagani", "nombre_color": "Black Silver Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#959595.jpg"}
    ],
    "Aston Martin": [
        {"marca": "Aston Martin", "nombre_color": "Aston Martin Racing Green", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#003826.jpg"},
        {"marca": "Aston Martin", "nombre_color": "Skyfall Silver", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#6A7074.jpg"},
        {"marca": "Aston Martin", "nombre_color": "Green Silver Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#364E4D.jpg"}
    ],
    "Bentley": [
        {"marca": "Bentley", "nombre_color": "British Racing Green", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#1A2421.jpg"},
        {"marca": "Bentley", "nombre_color": "Ice White", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F4F4F3.jpg"},
        {"marca": "Bentley", "nombre_color": "Green White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#8A8372.jpg"}
    ],
    "Lotus": [
        {"marca": "Lotus", "nombre_color": "Lotus Yellow", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#FFDA00.jpg"},
        {"marca": "Lotus", "nombre_color": "British Racing Green", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#004225.jpg"},
        {"marca": "Lotus", "nombre_color": "Yellow Green Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#B39B00.jpg"}
    ],
    "McLaren": [
        {"marca": "McLaren", "nombre_color": "McLaren Orange", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#F4C542.jpg"},
        {"marca": "McLaren", "nombre_color": "Onyx Black", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#1D1F20.jpg"},
        {"marca": "McLaren", "nombre_color": "Orange Black Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#B69131.jpg"}
    ],
    "Rolls-Royce": [
        {"marca": "Rolls-Royce", "nombre_color": "English White", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#F4F4F2.jpg"},
        {"marca": "Rolls-Royce", "nombre_color": "Midnight Sapphire", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#0D2345.jpg"},
        {"marca": "Rolls-Royce", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#DAE8E2.jpg"}
    ],
    "Bugatti": [
        {"marca": "Bugatti", "nombre_color": "Bugatti Blue", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#004C99.jpg"},
        {"marca": "Bugatti", "nombre_color": "Black Carbon", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#151515.jpg"},
        {"marca": "Bugatti", "nombre_color": "Blue Black Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#1B3C4B.jpg"}
    ],
    "DS Automobiles": [
        {"marca": "DS Automobiles", "nombre_color": "Whisper Purple", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#3E2535.jpg"},
        {"marca": "DS Automobiles", "nombre_color": "Platinum Grey", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#A6A6A6.jpg"},
        {"marca": "DS Automobiles", "nombre_color": "Purple Grey Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#726A6A.jpg"}
    ],
    "Cadillac": [
        {"marca": "Cadillac", "nombre_color": "Crystal White Tricoat", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#F8F8F7.jpg"},
        {"marca": "Cadillac", "nombre_color": "Stellar Black Metallic", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#222222.jpg"},
        {"marca": "Cadillac", "nombre_color": "White Black Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#D8D8D6.jpg"}
    ],
    "Lincoln": [
        {"marca": "Lincoln", "nombre_color": "Infinite Black", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#1C1C1C.jpg"},
        {"marca": "Lincoln", "nombre_color": "Pristine White", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F3F3F3.jpg"},
        {"marca": "Lincoln", "nombre_color": "Black White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#C8C2C2.jpg"}
    ],
    "Lucid Motors": [
        {"marca": "Lucid Motors", "nombre_color": "Eureka Gold", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#CBB681.jpg"},
        {"marca": "Lucid Motors", "nombre_color": "Stellar White", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#E8E7DF.jpg"},
        {"marca": "Lucid Motors", "nombre_color": "Gold White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#BBAE99.jpg"}
    ],
  "Acura": [
    {"marca": "Acura", "nombre_color": "Platinum White Pearl", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#F2F2F0.jpg"},
    {"marca": "Acura", "nombre_color": "Apex Blue Pearl", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#001E61.jpg"},
    {"marca": "Acura", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#CED8D5.jpg"}
],
"Infiniti": [
    {"marca": "Infiniti", "nombre_color": "Graphite Shadow", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#4B4D50.jpg"},
    {"marca": "Infiniti", "nombre_color": "Majestic White", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F4F3EF.jpg"},
    {"marca": "Infiniti", "nombre_color": "Grey White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#9E8F9D.jpg"}
],
"Lexus": [
    {"marca": "Lexus", "nombre_color": "Ultrasonic Blue Mica", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#0033A0.jpg"},
    {"marca": "Lexus", "nombre_color": "Eminent White Pearl", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F5F5F5.jpg"},
    {"marca": "Lexus", "nombre_color": "Blue White Mix", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#7E99D2.jpg"}
],
"Koenigsegg": [
    {"marca": "Koenigsegg", "nombre_color": "Ghost Grey", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#9D9F9E.jpg"},
    {"marca": "Koenigsegg", "nombre_color": "Swedish Blue", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#004B87.jpg"},
    {"marca": "Koenigsegg", "nombre_color": "Grey Blue Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#6D85A3.jpg"}
],
"Volvo": [
    {"marca": "Volvo", "nombre_color": "Onyx Black Metallic", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#101010.jpg"},
    {"marca": "Volvo", "nombre_color": "Crystal White Pearl", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#E7E9E9.jpg"},
    {"marca": "Volvo", "nombre_color": "Black White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#808080.jpg"}
],
"Spyker": [
    {"marca": "Spyker", "nombre_color": "Brilliant Orange", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#FF6600.jpg"},
    {"marca": "Spyker", "nombre_color": "Silver Grey", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#BEBEBE.jpg"},
    {"marca": "Spyker", "nombre_color": "Orange Silver Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#FF99B0.jpg"}
],
"W Motors": [
    {"marca": "W Motors", "nombre_color": "Crimson Red", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#AF2B2D.jpg"},
    {"marca": "W Motors", "nombre_color": "Matte Black", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#0F0F0F.jpg"},
    {"marca": "W Motors", "nombre_color": "Red Black Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico -#5F1819.jpg"}
],
"Hispano-Suiza": [
    {"marca": "Hispano-Suiza", "nombre_color": "Royal Purple", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#6F2761.jpg"},
    {"marca": "Hispano-Suiza", "nombre_color": "Champagne Silver", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#C1B29F.jpg"},
    {"marca": "Hispano-Suiza", "nombre_color": "Purple Silver Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#8D6D70.jpg"}
],
"Hongqi": [
    {"marca": "Hongqi", "nombre_color": "Imperial Red", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#AA0114.jpg"},
    {"marca": "Hongqi", "nombre_color": "Golden Brown", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#8B5F28.jpg"},
    {"marca": "Hongqi", "nombre_color": "Red Brown Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#751B1E.jpg"}
],
"NIO": [
    {"marca": "NIO", "nombre_color": "NIO Blue", "precio": precio1, "imagen": "relojes analogicos/reloj-analogico-#1F2A44.jpg"},
    {"marca": "NIO", "nombre_color": "Arctic White", "precio": precio2, "imagen": "relojes analogicos/reloj-analogico-#F4F4F3.jpg"},
    {"marca": "NIO", "nombre_color": "Blue White Mix", "precio": precio3, "imagen": "relojes analogicos/reloj-analogico-#8A88A4.jpg"}
]
}
digital = {
    "Audi": [
        {"marca": "Audi", "nombre_color": "Nardo Grey", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#7D7E82.jpg"},
        {"marca": "Audi", "nombre_color": "Misano Red", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#B12227.jpg"},
        {"marca": "Audi", "nombre_color": "Grey Red Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#926D54.jpg"}
    ],
    "BMW": [
        {"marca": "BMW", "nombre_color": "Alpine White", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#F8F8F6.jpg"},
        {"marca": "BMW", "nombre_color": "Estoril Blue", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#1F50A5.jpg"},
        {"marca": "BMW", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#DAE8E2.jpg"}
    ],
    "Mercedes-Benz": [
        {"marca": "Mercedes-Benz", "nombre_color": "Silver", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#C0C0C0.jpg"},
        {"marca": "Mercedes-Benz", "nombre_color": "Obsidian Black", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#1C1C1C.jpg"},
        {"marca": "Mercedes-Benz", "nombre_color": "Silver Black Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#888888.jpg"}
    ],
    "Maybach": [
        {"marca": "Maybach", "nombre_color": "Opal Black", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#191919.jpg"},
        {"marca": "Maybach", "nombre_color": "Patagonia Silver", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#A8A8A8.jpg"},
        {"marca": "Maybach", "nombre_color": "Black Silver Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#60606C.jpg"}
    ],
    "Porsche": [
        {"marca": "Porsche", "nombre_color": "Guards Red", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#D21F26.jpg"},
        {"marca": "Porsche", "nombre_color": "Racing Yellow", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#FDE101.jpg"},
        {"marca": "Porsche", "nombre_color": "Red Yellow Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#D25F14.jpg"}
    ],
    "Alfa Romeo": [
        {"marca": "Alfa Romeo", "nombre_color": "Rosso Competizione", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#B83941.jpg"},
        {"marca": "Alfa Romeo", "nombre_color": "Verde Montreal", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#01A049.jpg"},
        {"marca": "Alfa Romeo", "nombre_color": "Red Green Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#8D581C.jpg"}
    ],
    "Ferrari": [
        {"marca": "Ferrari", "nombre_color": "Rosso Corsa", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#D40000.jpg"},
        {"marca": "Ferrari", "nombre_color": "Giallo Modena", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F7E400.jpg"},
        {"marca": "Ferrari", "nombre_color": "Red Yellow Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#CE7200.jpg"}
    ],
    "Lamborghini": [
        {"marca": "Lamborghini", "nombre_color": "Black", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#000000.jpg"},
        {"marca": "Lamborghini", "nombre_color": "Gold", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#D4AF37.jpg"},
        {"marca": "Lamborghini", "nombre_color": "Black Gold Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#6C6C6C.jpg"}
    ],
    "Maserati": [
        {"marca": "Maserati", "nombre_color": "Blu Emozione", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#0E3C82.jpg"},
        {"marca": "Maserati", "nombre_color": "Rosso Trionfale", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#9B1B30.jpg"},
        {"marca": "Maserati", "nombre_color": "Blue Red Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#520E56.jpg"}
    ],
    "Pagani": [
        {"marca": "Pagani", "nombre_color": "Carbon Fiber Black", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#1A1A1A.jpg"},
        {"marca": "Pagani", "nombre_color": "Liquid Silver", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#C0C0C0.jpg"},
        {"marca": "Pagani", "nombre_color": "Black Silver Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#959595.jpg"}
    ],
    "Aston Martin": [
        {"marca": "Aston Martin", "nombre_color": "Aston Martin Racing Green", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#003826.jpg"},
        {"marca": "Aston Martin", "nombre_color": "Skyfall Silver", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#6A7074.jpg"},
        {"marca": "Aston Martin", "nombre_color": "Green Silver Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#364E4D.jpg"}
    ],
    "Bentley": [
        {"marca": "Bentley", "nombre_color": "British Racing Green", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#1A2421.jpg"},
        {"marca": "Bentley", "nombre_color": "Ice White", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F4F4F3.jpg"},
        {"marca": "Bentley", "nombre_color": "Green White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#8A8372.jpg"}
    ],
    "Lotus": [
        {"marca": "Lotus", "nombre_color": "Lotus Yellow", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#FFDA00.jpg"},
        {"marca": "Lotus", "nombre_color": "British Racing Green", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#004225.jpg"},
        {"marca": "Lotus", "nombre_color": "Yellow Green Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#B39B00.jpg"}
    ],
    "McLaren": [
        {"marca": "McLaren", "nombre_color": "McLaren Orange", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#F4C542.jpg"},
        {"marca": "McLaren", "nombre_color": "Onyx Black", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#1D1F20.jpg"},
        {"marca": "McLaren", "nombre_color": "Orange Black Mix", "precio": precio3, "imagen ": "relojes digitales/reloj-digital-#B69131.jpg"}
    ],
    "Rolls-Royce": [
        {"marca": "Rolls-Royce", "nombre_color": "English White", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#F4F4F2.jpg"},
        {"marca": "Rolls-Royce", "nombre_color": "Midnight Sapphire", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#0D2345.jpg"},
        {"marca": "Rolls-Royce", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#DAE8E2.jpg"}
    ],
    "Bugatti": [
        {"marca": "Bugatti", "nombre_color": "Bugatti Blue", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#004C99.jpg"},
        {"marca": "Bugatti", "nombre_color": "Black Carbon", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#151515.jpg"},
        {"marca": "Bugatti", "nombre_color": "Blue Black Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#2E2E57.jpg"}
    ],
    "DS Automobiles": [
        {"marca": "DS Automobiles", "nombre_color": "Whisper Purple", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#3E2535.jpg"},
        {"marca": "DS Automobiles", "nombre_color": "Platinum Grey", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#A6A6A6.jpg"},
        {"marca": "DS Automobiles", "nombre_color": "Purple Grey Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#726A6A.jpg"}
    ],
    "Cadillac": [
        {"marca": "Cadillac", "nombre_color": "Crystal White Tricoat", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#F8F8F7.jpg"},
        {"marca": "Cadillac", "nombre_color": "Stellar Black Metallic", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#222222.jpg"},
        {"marca": "Cadillac", "nombre_color": "White Black Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#D8D8D6.jpg"}
    ],
    "Lincoln": [
        {"marca": "Lincoln", "nombre_color": "Infinite Black", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#1C1C1C.jpg"},
        {"marca": "Lincoln", "nombre_color": "Pristine White", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F3F3F3.jpg"},
        {"marca": "Lincoln", "nombre_color": "Black White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#C8C2C2.jpg"}
    ],
    "Lucid Motors": [
        {"marca": "Lucid Motors", "nombre_color": "Eureka Gold", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#CBB681.jpg"},
        {"marca": "Lucid Motors", "nombre_color": "Stellar White", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#E8E7DF.jpg"},
        {"marca": "Lucid Motors", "nombre_color": "Gold White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#BBAE99.jpg"}
    ],
    "Acura": [
        {"marca": "Acura", "nombre_color": "Platinum White Pearl", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#F2F2F0.jpg"},
        {"marca": "Acura", "nombre_color": "Apex Blue Pearl", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#001E61.jpg"},
        {"marca": "Acura", "nombre_color": "White Blue Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#CED8D5.jpg"}
    ],
    "Infiniti": [
        {"marca": "Infiniti", "nombre_color": "Graphite Shadow", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#4B4D50.jpg"},
        {"marca": "Infiniti", "nombre_color": "Majestic White", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F4F3EF.jpg"},
        {"marca": "Infiniti", "nombre_color": "Grey White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#9E8F9D.jpg"}
    ],
    "Lexus": [
        {"marca": "Lexus", "nombre_color": "Ultrasonic Blue Mica", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#0033A0.jpg"},
        {"marca": "Lexus", "nombre_color": "Eminent White Pearl", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F5F5F5.jpg"},
        {"marca": "Lexus", "nombre_color": "Blue White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#7E99D2.jpg"}
    ],
    "Koenigsegg": [
        {"marca": "Koenigsegg", "nombre_color": "Ghost Grey", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#9D9F9E.jpg"},
        {"marca": "Koenigsegg", "nombre_color": "Swedish Blue", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#004B87.jpg"},
        {"marca": "Koenigsegg", "nombre_color": "Grey Blue Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#6D85A3.jpg"}
    ],
    "Volvo": [
        {"marca": "Volvo", "nombre_color": "Onyx Black Metallic", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#101010.jpg"},
        {"marca": "Volvo", "nombre_color": "Crystal White Pearl", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#E7E9E9.jpg"},
        {"marca": "Volvo", "nombre_color": "Black White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#808080.jpg"}
    ],
    "Spyker": [
        {"marca": "Spyker", "nombre_color": "Brilliant Orange", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#FF6600.jpg"},
        {"marca": "Spyker", "nombre_color": "Silver Grey", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#BEBEBE.jpg"},
        {"marca": "Spyker", "nombre_color": "Orange Silver Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#FF99B0.jpg"}
    ],
    "W Motors": [
        {"marca": "W Motors", "nombre_color": "Crimson Red", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#AF2B2D.jpg"},
        {"marca": "W Motors", "nombre_color": "Matte Black", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#0F0F0F.jpg"},
        {"marca": "W Motors", "nombre_color": "Red Black Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#5F1819.jpg"}
    ],
    "Hispano-Suiza": [
        {"marca": "Hispano-Suiza", "nombre_color": "Royal Purple", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#6F2761.jpg"},
        {"marca": "Hispano-Suiza", "nombre_color": "Champagne Silver", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#C1B29F.jpg"},
        {"marca": "Hispano-Suiza", "nombre_color": "Purple Silver Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#8D6D 70.jpg"}
    ],
    "Hongqi": [
        {"marca": "Hongqi", "nombre_color": "Imperial Red", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#AA0114.jpg"},
        {"marca": "Hongqi", "nombre_color": "Golden Brown", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#8B5F28.jpg"},
        {"marca": "Hongqi", "nombre_color": "Red Brown Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#751B1E.jpg"}
    ],
    "NIO": [
        {"marca": "NIO", "nombre_color": "NIO Blue", "precio": precio1, "imagen": "relojes digitales/reloj-digital-#1F2A44.jpg"},
        {"marca": "NIO", "nombre_color": "Arctic White", "precio": precio2, "imagen": "relojes digitales/reloj-digital-#F4F4F3.jpg"},
        {"marca": "NIO", "nombre_color": "Blue White Mix", "precio": precio3, "imagen": "relojes digitales/reloj-digital-#8A88A4.jpg"}
    ]
}

# Inicialización
tipo_producto = "digital"  # Opción por defecto
marcas = list(digital.keys())
indice_marca = 0
indice_color = 0

# Crear un marco para los botones y el menú
frame_botones = tk.Frame(ventana, bg='black')
frame_botones.grid(row=0, column=0, columnspan=3, sticky='w', pady=10)

# Crear un marco para los elementos que se deben centrar
frame_central = tk.Frame(ventana, bg='black')
frame_central.grid(row=1, column=0, columnspan=3, pady=20)

# Configurar que las columnas y filas se expandan correctamente
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_rowconfigure(1, weight=1)

# Variable para almacenar la marca seleccionada en el menú
marca_seleccionada = StringVar()
marca_seleccionada.set(marcas[0])  # Valor inicial

# Menú de selección de marcas
menu_marcas = OptionMenu(frame_botones, marca_seleccionada, *marcas, command=lambda marca: seleccionar_marca(marca))
menu_marcas.config(font=("Arial", 8), bg='black', fg='white', width=15)
menu_marcas.grid(row=0, column=0, padx=5)

# Botones para seleccionar el tipo de producto
boton_digital = tk.Button(frame_botones, text="Digital", command=lambda: cambiar_tipo_producto("digital"), bg='black', fg='white')
boton_digital.grid(row=0, column=1, padx= 5)

boton_analogico = tk.Button(frame_botones, text="Analógico", command=lambda: cambiar_tipo_producto("analogico"), bg='black', fg='white')
boton_analogico.grid(row=0, column=2, padx=5)

# Crear etiquetas para mostrar la información del producto
label_imagen = Label(frame_central, bg='black')
label_imagen.grid(row=0, column=1, pady=20)

label_marca = Label(frame_central, font=("Arial", 14), bg='black', fg='white')
label_color = Label(frame_central, font=("Arial", 12), bg='black', fg='white')
label_precio = Label(frame_central, font=("Arial", 12), bg='black', fg='white')

label_marca.grid(row=1, column=1, pady=5)
label_color.grid(row=2, column=1, pady=5)
label_precio.grid(row=3, column=1, pady=5)

# Variables globales
nombre = ""
base_de_datos = {}

# Obtener la ruta absoluta del archivo basado en la ubicación del script
archivo_base_datos = os.path.join(os.path.dirname(__file__), "basedatos.txt")

# Base de datos en memoria
base_de_datos = {}

# Cargar usuarios existentes desde el archivo
def cargar_datos():
    try:
        with open(archivo_base_datos, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:  # Asegúrate de que hay usuario y contraseña
                    usuario = parts[0]
                    contraseña = parts[1]
                    base_de_datos[usuario] = contraseña
    except FileNotFoundError:
        with open(archivo_base_datos, 'w'):  # Crea el archivo si no existe
            pass

# Verificar credenciales
def comprobar(usuario, contraseña):
    return usuario in base_de_datos and base_de_datos[usuario] == contraseña

# Registrar un nuevo usuario
def registrar(usuario, contraseña):
    with open(archivo_base_datos, 'a') as file:
        file.write(f"{usuario},{contraseña}\n")
    base_de_datos[usuario] = contraseña  # Actualizar la base de datos en memoria


# Función para iniciar sesión
def iniciar_sesion():
    global nombre
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()
    if not usuario or not contraseña:
        messagebox.showerror("Error", "Los campos de entrada no pueden estar vacíos.")
        return
    if comprobar(usuario, contraseña):
        nombre = usuario
        ventana.title(f"Catálogo de Relojes [{nombre}]")  # Actualiza el título
        ventana_usuario.destroy()  # Cierra la ventana de usuario
        btn_cuenta.grid_forget()  # Ocultar el botón de "Cuenta"
        btn_cerrar_sesion.grid(row=0, column=1, sticky='ne', padx=(0, 10), pady=(10, 0))  # Mostrar "Cerrar sesión"
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Función para cerrar sesión
def cerrar_sesion():
    global nombre
    nombre = ""
    ventana.title("Catálogo de Relojes")  # Restablece el título original
    btn_cerrar_sesion.grid_forget()  # Ocultar el botón de cerrar sesión
    btn_cuenta.grid(row=0, column=1, sticky='ne', padx=(0, 10), pady=(10, 0))  # Mostrar el botón de "Cuenta"

# Función para abrir la ventana de registro
def abrir_registro():
    registro_window = tk.Toplevel(ventana_usuario)
    registro_window.title("Registro")
    registro_window.configure(bg='black')

    # Calcular el tamaño de la ventana y de la pantalla
    ancho_ventana = 300
    alto_ventana = 300
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Aplicar tamaño y posición centrada a la ventana
    registro_window.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    # Cargar y establecer el ícono de la ventana
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo.png")

    # Cargar la imagen
    img = Image.open(logo_path)  # Ruta al archivo de imagen
    img = img.resize((32, 32))  # Redimensionar la imagen si es necesario
    icon = ImageTk.PhotoImage(img)
    registro_window.tk.call('wm', 'iconphoto', registro_window._w, icon)

    usuario_label = tk.Label(registro_window, text="Usuario:", font=("Arial", 12), bg="black", fg="white")
    usuario_label.pack(pady=5)
    usuario_entry_registro = tk.Entry(registro_window, font=("Arial", 12))
    usuario_entry_registro.pack(pady=5)

    contraseña_label = tk.Label(registro_window, text="Contraseña:", font=("Arial", 12), bg="black", fg="white")
    contraseña_label.pack(pady=5)
    contraseña_entry_registro = tk.Entry(registro_window, show="*", font=("Arial", 12))
    contraseña_entry_registro.pack(pady=5)

    def registrar_usuario():
        usuario = usuario_entry_registro.get()
        contraseña = contraseña_entry_registro.get()
        if not usuario or not contraseña:
            messagebox.showerror("Error", "Los campos de entrada no pueden estar vacíos.")
            return
        if usuario in base_de_datos:
            messagebox.showerror("Error", "El usuario ya existe.")
        else:
            registrar(usuario, contraseña)
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
            registro_window.destroy()

    registrar_button = tk.Button(registro_window, text="Registrar", command=registrar_usuario, font=("Arial", 12), bg="white", fg="black")
    registrar_button.pack(pady=10)

    

# Función para abrir la ventana de usuario
def mostrar_ventana_usuario():
    global ventana_usuario, usuario_entry, contraseña_entry
    ventana_usuario = tk.Toplevel(ventana)
    ventana_usuario.title("Ventana de Usuario")
    ventana_usuario.geometry("300x300")
    ventana_usuario.configure(bg='black')

        # Calcular el tamaño de la ventana y de la pantalla
    ancho_ventana = 700
    alto_ventana = 500
    ancho_pantalla = ventana_usuario.winfo_screenwidth()
    alto_pantalla = ventana_usuario.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Aplicar tamaño y posición centrada a la ventana
    ventana_usuario.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    # Cargar y establecer el ícono de la ventana
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo.png")

    # Cargar la imagen
    img = Image.open(logo_path)  # Ruta al archivo de imagen
    img = img.resize((32, 32))  # Redimensionar la imagen si es necesario
    icon = ImageTk.PhotoImage(img)
    ventana_usuario.tk.call('wm', 'iconphoto', ventana_usuario._w, icon)

    # Etiquetas y entradas para el inicio de sesión
    usuario_label = tk.Label(ventana_usuario, text="Usuario:", font=("Arial", 12), bg="black", fg="white")
    usuario_label.pack(pady=5)
    usuario_entry = tk.Entry(ventana_usuario, font=("Arial", 12))
    usuario_entry.pack(pady=5)

    contraseña_label = tk.Label(ventana_usuario, text="Contraseña:", font=("Arial", 12), bg="black", fg="white")
    contraseña_label.pack(pady=5)
    contraseña_entry = tk.Entry(ventana_usuario, show="*", font=("Arial", 12))
    contraseña_entry.pack(pady=5)

    iniciar_button = tk.Button(ventana_usuario, text="Iniciar sesión", command=iniciar_sesion, font=("Arial", 12), bg="white", fg="black")
    iniciar_button.pack(pady=5)

    registro_button = tk.Button(ventana_usuario, text="Registrarse", command=abrir_registro, font=("Arial", 12), bg="white", fg="black")
    registro_button.pack(pady=5)

# Cargar usuarios existentes
cargar_datos()

# Botón "Cuenta" para abrir la ventana de usuario
btn_cuenta = tk.Button(ventana, text="Cuenta", command=mostrar_ventana_usuario, bg='black', fg='white', font=("Arial", 10))
btn_cuenta.grid(row=0, column=1, sticky='ne', padx=(0, 10), pady=(10, 0))

# Botón "Cerrar sesión", inicialmente oculto
btn_cerrar_sesion = tk.Button(ventana, text="Cerrar sesión", command=cerrar_sesion, bg='black', fg='white', font=("Arial", 10))

# Función para mostrar la nueva ventana
def mostrar_nueva_ventana():
    global texto  # Asegúrate de que 'texto' esté definido
    texto = (
        "En DriveTime nos comprometemos a ofrecerte la mejor calidad y autenticidad en nuestros relojes. "
        "Por eso, cada reloj que vendemos tiene un código único e irrepetible, lo que nos permite garantizar que no se trate de réplicas. "
        "Además, todos nuestros relojes cuentan con una garantía de 3 años para que puedas estar tranquilo ante cualquier percance o inconveniente con el producto. "
        "Si llegas a necesitar asistencia, en cualquiera de nuestras tiendas encontrarás un equipo especializado de reparación listo para ayudarte. "
        "Tu satisfacción es nuestra prioridad."
    )
    # Crear una nueva ventana
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Información Adicional")
    nueva_ventana.resizable(False, False)  # Deshabilitar el redimensionamiento
    nueva_ventana.configure(bg='black')
    # Cargar y establecer el ícono de la ventana
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo.png")

    # Cargar la imagen
    img = Image.open(logo_path)  # Ruta al archivo de imagen
    img = img.resize((32, 32))  # Redimensionar la imagen si es necesario
    icon = ImageTk.PhotoImage(img)
    nueva_ventana.tk.call('wm', 'iconphoto', nueva_ventana._w, icon)
    
    # Calcular el tamaño de la ventana y de la pantalla
    ancho_ventana = 400
    alto_ventana = 300
    ancho_pantalla = nueva_ventana.winfo_screenwidth()
    alto_pantalla = nueva_ventana.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Aplicar tamaño y posición centrada a la ventana
    nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    # Crear un widget Text para mostrar el texto
    texto_nueva_ventana = tk.Text(nueva_ventana, bg="black", fg="white", font=("Arial", 12), wrap="word")
    texto_nueva_ventana.insert(tk.END, texto)
    texto_nueva_ventana.tag_add("justify", "1.0", tk.END)
    texto_nueva_ventana.tag_configure("justify", justify="center")  # Justificar el texto
    texto_nueva_ventana.pack(padx=20, pady=20)

    # Desactivar la edición del texto
    texto_nueva_ventana.config(state=tk.DISABLED)

# Botón para abrir la nueva ventana
boton_nueva_ventana = tk.Button(ventana, text="Política de empresa", command=mostrar_nueva_ventana, font=("Arial", 8), bg='black', fg='white')
boton_nueva_ventana.grid(row=0, column=2, sticky='ne', padx=(0, 10), pady=(10, 0))  # Posicionar en la esquina superior derecha

# Función para actualizar la vista del producto
def mostrar_producto():
    global marcas, tipo_producto
    if tipo_producto == "digital":
        producto_actual = digital[marcas[indice_marca]][indice_color]
    else:
        producto_actual = analogico[marcas[indice_marca]][indice_color]

    try:
        # Obtener el directorio donde se está ejecutando el script o el .exe
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Crear la ruta completa para la imagen del producto usando el directorio actual
        imagen_path = os.path.join(current_dir, producto_actual["imagen"])

        # Intentar cargar la imagen del producto
        imagen_producto = Image.open(imagen_path)
        imagen_producto = imagen_producto.resize((200, 200))  # Redimensionar la imagen
        imagen_producto_tk = ImageTk.PhotoImage(imagen_producto)

        # Actualizar la imagen del producto en el label
        label_imagen.config(image=imagen_producto_tk, bg="white")
        label_imagen.image = imagen_producto_tk  # Guardar la referencia a la imagen
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

    # Actualizar marca, color y precio en líneas separadas
    label_marca.config(text=f"{producto_actual['marca']}")
    label_color.config(text=f"{producto_actual['nombre_color']}")
    precio = producto_actual.get("precio", "No disponible")
    label_precio.config(text=f" ${precio}")

# Función para seleccionar una marca desde el menú
def seleccionar_marca(marca):
    global indice_marca, indice_color
    if marca in marcas:
        indice_marca = marcas.index(marca)
        indice_color = 0  # Reiniciar al primer color de la marca seleccionada
        mostrar_producto()

# Funciones para cambiar de color
def siguiente_color():
    global indice_color
    if indice_color < len(digital[marcas[indice_marca]]) - 1:
        indice_color += 1
    else:
        indice_color = 0  # Volver al primer color
    mostrar_producto()

def anterior_color():
    global indice_color
    if indice_color > 0:
        indice_color -= 1
    else:
        indice_color = len(digital[marcas[indice_marca]]) - 1  # Volver al último color
    mostrar_producto()

# Función para cambiar el tipo de producto y mantener la posición actual si es posible
def cambiar_tipo_producto(nuevo_tipo):
    global tipo_producto, marcas, indice_marca, indice_color
    tipo_producto = nuevo_tipo
    
    nuevas_marcas = list(digital.keys()) if tipo_producto == "digital" else list(analogico.keys())
    marca_actual = marcas[indice_marca] if indice_marca < len(marcas) else None
    if marca_actual in nuevas_marcas:
        indice_marca = nuevas_marcas.index(marca_actual)
    else:
        indice_marca = 0  # Si la marca no existe, reiniciar al primer índice

    colores_disponibles = digital[nuevas_marcas[indice_marca]] if tipo_producto == "digital" else analogico[nuevas_marcas[indice_marca]]
    if indice_color < len(colores_disponibles):
        indice_color = indice_color
    else:
        indice_color = 0

    marcas = nuevas_marcas
    marca_seleccionada.set(marcas[indice_marca])  # Seleccionar la marca actual en el menú desplegable
    mostrar_producto()

# Función para mostrar un mensaje de confirmación
def confirmar():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas continuar?")
    if respuesta:
        messagebox.showinfo("Confirmado", "Has confirmado la compra.")
    else:
        messagebox.showinfo("Cancelado", "La acción ha sido cancelada.")
# Configurar las columnas y filas para el botón de compra
ventana.grid_columnconfigure(0, weight=1)  # Columna izquierda
ventana.grid_columnconfigure(1, weight=1)  # Columna central (donde estará el botón "Comprar")
ventana.grid_columnconfigure(2, weight=1)  # Columna derecha
ventana.grid_rowconfigure(6, weight=1)  # Fila donde está el botón "Comprar"

# Botón para abrir el mensaje de confirmación
btn_confirmar = tk.Button(ventana, text="Comprar", command=confirmar, bg='black', fg='white')
btn_confirmar.grid(row=6, column=1, pady=20)  # Usar grid en lugar de pack

# Botones de navegación
boton_anterior_color = tk.Button(ventana, text="Anterior", command=anterior_color, bg='black', fg='white')
boton_anterior_color.grid(row=1, column=0, padx=(20, 10), pady=10)

boton_siguiente_color = tk.Button(ventana, text="Siguiente", command=siguiente_color, bg='black', fg='white')
boton_siguiente_color.grid(row=1, column=2, padx=(10, 20), pady=10)

# Mostrar el primer producto al iniciar
mostrar_producto()

# Iniciar el bucle principal de la ventana
ventana.mainloop()