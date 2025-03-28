import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Importáljuk a szükséges könyvtárat
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="masscinema"
    )

def get_films():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Terem_szam, Film_cime, Ev, Mufaj, Jatekido, Kapacitas FROM Termek")
    films = cursor.fetchall()
    conn.close()
    return films

def open_film_window(film):
    root.withdraw()  

    film_window = tk.Toplevel()
    film_window.title(film[1])
    film_window.geometry("600x400")
    film_window.config(bg="lightblue")

    ttk.Label(film_window, text=film[1], font=('Arial', 24, 'bold'), background="lightblue").pack(pady=20)
    ttk.Label(film_window, text=f"Megjelenés: {film[2]}\nMűfaj: {film[3]}\nJátékidő: {film[4]} perc\nTerem kapacitása: {film[5]} fő",
              font=('Arial', 16), background="lightblue").pack(pady=10)

    def go_back():
        film_window.destroy()
        root.deiconify()  

    ttk.Button(film_window, text="Vissza a filmekhez", width=30, command=go_back).pack(pady=20)

def load_image(image_name):
    """Kép betöltése a fájlból."""
    try:
        img = Image.open(f"images/{image_name}.jpg")  # Betöltés az 'images' mappából
        img = img.resize((150, 225), Image.ANTIALIAS)  # Átméretezés
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Hiba a kép betöltésekor: {e}")
        return None

def open_main_window():
    global root
    root = tk.Tk()
    root.title("Mozi Filmek")
    root.geometry("1000x800")
    root.config(bg="lightblue")

    style = ttk.Style()
    style.configure("TButton",
                    font=('Arial', 18, 'bold'),
                    background="skyblue",
                    foreground="black",
                    padding=10)
    
    style.configure("TLabel",
                    font=('Arial', 18),
                    background="lightblue",
                    foreground="black")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    col1 = tk.Frame(root, bg="#ECB189", width=500, height=800)
    col1.grid(row=0, column=0, sticky="nsew")
    tk.Label(col1, bg="#ECB189", font=("Arial", 16)).pack(pady=10)

    col2 = tk.Frame(root, bg="#ECB189", width=500, height=800)
    col2.grid(row=0, column=1, sticky="nsew")
    tk.Label(col2,  bg="#ECB189", font=("Arial", 16)).pack(pady=10)

    films = get_films()
    mid = len(films) // 2   
    films_col1 = films[:mid+1]
    films_col2 = films[mid:]

    # Első oszlopba a gombok
    for index, film in enumerate(films_col1):
        image_name = f"movie{index + 1}"  # A képek neve movie1, movie2, stb.
        image = load_image(image_name)
        
        if image:  # Ha sikerült betölteni a képet
            button = ttk.Button(col1, text=film[1], image=image, compound="top", width=30, command=lambda f=film: open_film_window(f))
            button.image = image  # Megőrizzük a hivatkozást
            button.pack(pady=10)

    # Második oszlopba a gombok
    for index, film in enumerate(films_col2):
        image_name = f"movie{index + len(films_col1) + 1}"  # A képek neve movie1, movie2, stb.
        image = load_image(image_name)
        
        if image:  # Ha sikerült betölteni a képet
            button = ttk.Button(col2, text=film[1], image=image, compound="top", width=30, command=lambda f=film: open_film_window(f))
            button.image = image  # Megőrizzük a hivatkozást
            button.pack(pady=10)

    root.mainloop()

open_main_window()
