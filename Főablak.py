import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# MySQL adatbázis kapcsolat létrehozása (nincs jelszó)
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",       # Az adatbázis szerver hostja
        user="root",            # Az adatbázis felhasználó neve
        password="",            # Nincs jelszó
        database="masscinema"   # Az adatbázis neve
    )
    return conn

# Filmek lekérdezése az adatbázisból
def get_films():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Terem_szam, Film_cime, Ev, Mufaj, Jatekido, Kapacitas FROM Termek")
    films = cursor.fetchall()
    conn.close()
    return films

# Filmek részleteinek megjelenítése
def show_film_details(film):
    details = f"Film címe: {film[1]}\n"
    details += f"Év: {film[2]}\n"
    details += f"Műfaj: {film[3]}\n"
    details += f"Játékidő: {film[4]}\n"
    details += f"Terem kapacitása: {film[5]}\n"
    messagebox.showinfo(film[1], details)

# Új ablak, amely a film részleteit mutatja
def open_film_window(film):
    # Az előző ablak bezárása
    root.destroy()

    # Új ablak létrehozása
    film_window = tk.Toplevel()  # Új ablak létrehozása
    film_window.title(film[1])  # A film címével nevezzük el az ablakot
    film_window.geometry("600x400")  # Az új ablak mérete
    film_window.config(bg="lightblue")  # Háttér szín

    # Film címének és adatoknak a megjelenítése
    title_label = ttk.Label(film_window, text=film[1], font=('Arial', 24, 'bold'), background="lightblue")
    title_label.pack(pady=20)

    details_label = ttk.Label(film_window, text=f"Év: {film[2]}\nMűfaj: {film[3]}\nJátékidő: {film[4]}\nTerem kapacitása: {film[5]}",
                              font=('Arial', 16), background="lightblue")
    details_label.pack(pady=10)

    # Vissza gomb
    def go_back():
        film_window.destroy()  # Az új ablak bezárása
        open_main_window()  # A főablak újraindítása

    back_button = ttk.Button(film_window, text="Vissza a filmek listájához", width=30, command=go_back)
    back_button.pack(pady=20)

# Fő ablak létrehozása
def open_main_window():
    global root
    root = tk.Tk()
    root.title("Mozi Filmek")
    root.geometry("600x400")  # Nagyobb méret
    root.config(bg="lightblue")  # Háttér szín

    # ttk stílus alkalmazása
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

    # Filmek lista megjelenítése
    films = get_films()

    # Filmek gombjaival történő megjelenítés
    for film in films:
        button = ttk.Button(root, text=film[1], width=40, command=lambda f=film: open_film_window(f))
        button.pack(pady=10)

    # Alkalmazás futtatása
    root.mainloop()

# A fő ablak indítása
open_main_window()