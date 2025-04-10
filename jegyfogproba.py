import tkinter as tk
from tkinter import ttk

def create_seat_layout(parent):
    rows = 5
    cols = 8
    seats = {}

    def toggle_seat(seat):
        if seats[seat]['bg'] == 'green':
            seats[seat]['bg'] = 'orange'
        elif seats[seat]['bg'] == 'orange':
            seats[seat]['bg'] = 'green'

    for row in range(rows):
        for col in range(cols):
            seat_id = f"{chr(65 + row)}{col + 1}"
            btn = tk.Button(parent, text=seat_id, width=6, bg='green',
                            command=lambda s=seat_id: toggle_seat(s))
            btn.grid(row=row, column=col, padx=5, pady=5)
            seats[seat_id] = btn

def open():
    foglalas_window = tk.Toplevel()
    foglalas_window.title("Jegyfoglalás")
    foglalas_window.geometry("600x400")
    foglalas_window.config(bg="#ECB189")

    legend_frame = tk.Frame(foglalas_window, bg="#ECB189")
    legend_frame.pack(pady=10)

    tk.Label(legend_frame, text="Elérhető", bg="green", width=10).grid(row=0, column=0, padx=5)
    tk.Label(legend_frame, text="Foglalt", bg="gray", width=10).grid(row=0, column=1, padx=5)
    tk.Label(legend_frame, text="Kiválasztott", bg="orange", width=10).grid(row=0, column=2, padx=5)

    seat_frame = tk.Frame(foglalas_window, bg="#ECB189")
    seat_frame.pack()
    create_seat_layout(seat_frame)

    ttk.Button(foglalas_window, text="Foglalás", command=foglalas_window.destroy).pack(pady=20)
