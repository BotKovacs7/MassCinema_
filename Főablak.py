import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import jegyfoglalas
from PIL import Image, ImageTk

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
    film_window.geometry("1000x800")
    film_window.config(bg="#ECB189")

    ttk.Label(film_window, text=film[1], font=('Arial', 24, 'bold'), background="#ECB189").pack(pady=20)
    ttk.Label(film_window, text=f"Megjelenés: {film[2]}\nMűfaj: {film[3]}\nJátékidő: {film[4]} perc\nTerem kapacitása: {film[5]} fő",
              font=('Arial', 16), background="#ECB189").pack(pady=10)

    def go_back():
        film_window.destroy()
        root.deiconify() 

    def foglalas():
        film_window.destroy()
        jegyfoglalas.open() 

    ttk.Button(film_window, text="Foglalás", width=30, command=foglalas).pack(pady=20)
    ttk.Button(film_window, text="Vissza a filmekhez", width=30, command=go_back).pack(pady=20)

def open_main_window():
    global root
    root = tk.Tk()
    root.title("Mozi Filmek")
    root.geometry("1000x800")
    root.config(bg="#ECB189")

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
    films_col1 = films[:mid]
    films_col2 = films[mid:]

    def load_resized_image(image_path):
        image = Image.open(image_path)
        image = image.resize((125, 200), Image.LANCZOS) 
        return ImageTk.PhotoImage(image)

    for idx, film in enumerate(films_col1):
        image = load_resized_image(f"./images/movie{idx+1}.jpg")
        btn = tk.Button(col1, image=image, width=125, height=200, command=lambda f=film: open_film_window(f))
        btn.image = image 
        btn.pack(pady=10)

    for idx, film in enumerate(films_col2):
        image = load_resized_image(f"./images/movie{idx+mid+1}.jpg")
        btn = tk.Button(col2, image=image, width=125, height=200, command=lambda f=film: open_film_window(f))
        btn.image = image 
        btn.pack(pady=10)

    root.mainloop()

open_main_window()