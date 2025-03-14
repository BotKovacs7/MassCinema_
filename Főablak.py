import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",       
        user="root",            
        password="",            
        database="masscinema"   
    )
    return conn

def get_films():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Terem_szam, Film_cime, Ev, Mufaj, Jatekido, Kapacitas FROM Termek")
    films = cursor.fetchall()
    conn.close()
    return films

def show_film_details(film):
    details = f"Film címe: {film[1]}\n"
    details += f"Év: {film[2]}\n"
    details += f"Műfaj: {film[3]}\n"
    details += f"Játékidő: {film[4]}\n"
    details += f"Terem kapacitása: {film[5]}\n"
    messagebox.showinfo(film[1], details)

def open_film_window(film):

    root.destroy()

    film_window = tk.Toplevel()
    film_window.title(film[1])
    film_window.geometry("600x400")
    film_window.config(bg="lightblue")

    title_label = ttk.Label(film_window, text=film[1], font=('Arial', 24, 'bold'), background="lightblue")
    title_label.pack(pady=20)

    details_label = ttk.Label(film_window, text=f"Megjelenés: {film[2]}\nMűfaj: {film[3]}\nJátékidő: {film[4]}\nTerem kapacitása: {film[5]}",
                              font=('Arial', 16), background="lightblue")
    details_label.pack(pady=10)

    def go_back():
        film_window.destroy()
        open_main_window()

    back_button = ttk.Button(film_window, text="Vissza a filmek listájához", width=30, command=go_back)
    back_button.pack(pady=20)

def open_main_window():
    global root
    root = tk.Tk()
    root.title("Mozi Filmek")
    root.geometry("600x400")
    root.config(bg="lightblue")


    style = ttk.Style()
    style.configure("TButton",
                    font=('Arial', 12, 'bold'),
                    background="skyblue",
                    foreground="black",
                    padding=10)
    style.configure("TLabel",
                    font=('Arial', 12),
                    background="lightblue",
                    foreground="black")

    films = get_films()

    for film in films:
        button = ttk.Button(root, text=film[1], width=40, command=lambda f=film: open_film_window(f))
        button.pack(pady=10)

    root.mainloop()

open_main_window()