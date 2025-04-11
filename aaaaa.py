import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import jegyfoglalas

# ------------------ Adatbázis kapcsolat ------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="masscinema"
    )

# ------------------ Filmek lekérése ------------------
def get_films():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Terem_szam, Film_cime, Ev, Mufaj, Jatekido, Kapacitas FROM Termek")
    films = cursor.fetchall()
    conn.close()
    return films

# ------------------ Foglalt ülések lekérdezése ------------------
def get_foglalt_ulesek(film_cime):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ules FROM foglalasok WHERE film_cime = %s", (film_cime,))
    foglalt = cursor.fetchall()
    conn.close()
    return {sor[0] for sor in foglalt}

# ------------------ Jegyfoglaló ablak ------------------
def open_jegyfoglalas(film):
    film_title = film[1]
    terem_szam = film[0]
    kapacitas = film[5]
    sorok = 6
    oszlopok = kapacitas // sorok

    foglalas_window = tk.Toplevel()
    foglalas_window.title(f"{film_title} - Jegyfoglalás")
    foglalas_window.geometry("700x650")
    foglalas_window.config(bg="#ECB189")

    frame = tk.Frame(foglalas_window, bg="#ECB189")
    frame.pack(pady=20)

    tk.Label(frame, text=f"Válassz ülőhelyet a(z) {film_title} filmhez!",
             font=("Arial", 16, "bold"), bg="#ECB189").pack(pady=10)

    ulesek_frame = tk.Frame(frame, bg="#ECB189")
    ulesek_frame.pack()

    selected = set()
    foglalt_ulesek = get_foglalt_ulesek(film_title)
    ules_gombok = {}

    for sor in range(sorok):
        for oszlop in range(oszlopok):
            ules = f"{sor+1}-{oszlop+1}"
            btn = tk.Button(ulesek_frame, text=ules, width=5, height=2,
                            bg="green", fg="white")

            if ules in foglalt_ulesek:
                btn.config(state="disabled", bg="red")

            def click(b=btn, u=ules):
                if u in selected:
                    selected.remove(u)
                    b.config(bg="green")
                else:
                    selected.add(u)
                    b.config(bg="blue")

            btn.config(command=click)
            btn.grid(row=sor, column=oszlop, padx=5, pady=5)
            ules_gombok[ules] = btn

    def foglalas_mentes():
        if not selected:
            messagebox.showwarning("Nincs kiválasztás", "Kérlek, válassz legalább egy ülőhelyet!")
            return

        conn = connect_db()
        cursor = conn.cursor()

        for ules in selected:
            cursor.execute(
                "INSERT INTO foglalasok (film_cime, ules) VALUES (%s, %s)",
                (film_title, ules)
            )

        conn.commit()
        conn.close()
        messagebox.showinfo("Sikeres foglalás", "A foglalás sikeresen mentve lett.")
        foglalas_window.destroy()

    tk.Button(frame, text="Foglalás mentése", command=foglalas_mentes,
              font=("Arial", 14)).pack(pady=20)

# ------------------ Film adatlap ablak ------------------
def open_film_window(film):
    root.withdraw()
    film_window = tk.Toplevel()
    film_window.title(film[1])
    film_window.geometry("600x400")
    film_window.config(bg="#ECB189")

    ttk.Label(film_window, text=film[1], font=('Arial', 24, 'bold'), background="#ECB189").pack(pady=20)
    ttk.Label(film_window, text=f"Megjelenés: {film[2]}\nMűfaj: {film[3]}\nJátékidő: {film[4]} perc\nTerem kapacitása: {film[5]} fő",
              font=('Arial', 16), background="#ECB189").pack(pady=10)

    def go_back():
        film_window.destroy()
        root.deiconify()

    def foglalas():
        film_window.destroy()
        open_jegyfoglalas(film)

    ttk.Button(film_window, text="Foglalás", width=30, command=foglalas).pack(pady=20)
    ttk.Button(film_window, text="Vissza a filmekhez", width=30, command=go_back).pack(pady=20)

# ------------------ Főablak ------------------
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

# ------------------ Futtatás ------------------
if __name__ == "__main__":
    open_main_window()
