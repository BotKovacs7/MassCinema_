import adatbekeres 
import tkinter as tk
from tkinter import ttk

def open():
    foglalas_window = tk.Toplevel()
    foglalas_window.title("Jegyfoglalás")
    foglalas_window.geometry("600x400")
    foglalas_window.config(bg="#ECB189")

    legend_frame = tk.Frame(foglalas_window)
    legend_frame.pack()

    tk.Label(legend_frame, text="Elérhető", bg="green", width=10).grid(row=0, column=0)
    tk.Label(legend_frame, text="Foglalt", bg="gray", width=10).grid(row=0, column=1)
    tk.Label(legend_frame, text="Kiválasztott", bg="orange", width=10).grid(row=0, column=2)

    seat_frame = tk.Frame(foglalas_window)
    seat_frame.pack()
    create_seat_layout(seat_frame)

    def on_booking():
        foglalas_window.destroy()
        adatbekeres.open()  # <- adatbekérés megnyitása

    ttk.Button(foglalas_window, text="Foglalás", command=on_booking).pack(pady=20)

    foglalas_window.mainloop()
