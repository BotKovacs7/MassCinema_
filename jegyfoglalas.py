import tkinter as tk
from tkinter import ttk
import adatbekeres

def select_seat(row, col):
    current_color = buttons[row][col].cget("bg")
    if current_color == "green":
        buttons[row][col].config(bg="orange")
    elif current_color == "orange":
        buttons[row][col].config(bg="green")

def create_seat_layout(root):
    global buttons
    buttons = []
    rows, cols = 9, 16
    occupied_seats = [(8, 10)]  # Foglalt szék példaként

    for r in range(rows):
        row_buttons = []
        for c in range(cols):
            if c < 12 or r == 8:  # Kétszekciós elrendezés
                bg_color = "green" if (r, c) not in occupied_seats else "gray"
                btn = tk.Button(root, text=f"{c+1}", width=3, height=1, bg=bg_color,
                                command=lambda r=r, c=c: select_seat(r, c))
                btn.grid(row=r, column=c, padx=2, pady=2)
                row_buttons.append(btn)
        buttons.append(row_buttons)

def bekeres():
    adatbekeres.open()

def open():
    foglalas_window = tk.Toplevel()
    foglalas_window.title("Jegyfoglalás")
    foglalas_window.geometry("600x400")
    foglalas_window.config(bg="#ECB189")

    legend_frame = tk.Frame(foglalas_window, bg="#ECB189")
    legend_frame.pack()

    tk.Label(legend_frame, text="Elérhető", bg="green", width=10).grid(row=0, column=0)
    tk.Label(legend_frame, text="Foglalt", bg="gray", width=10).grid(row=0, column=1)
    tk.Label(legend_frame, text="Kiválasztott", bg="orange", width=10).grid(row=0, column=2)

    seat_frame = tk.Frame(foglalas_window, bg="#ECB189")  # <-- EZ az egyetlen változás
    seat_frame.pack()
    create_seat_layout(seat_frame)

    ttk.Button(foglalas_window, text="Foglalás", command= bekeres).pack(pady=20)

    foglalas_window.mainloop()
