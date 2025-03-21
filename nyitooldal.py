import tkinter as tk
from tkinter import Toplevel, Button
from PIL import Image, ImageTk

# Filmek adatai
movies = [
    {
        "title": "Eredet",
        "duration": "148 perc",
        "release_date": "2010. július 16.",
        "showtimes": ["10:00", "18:00"],
        "image": "movie1.jpg"
    },
    {
        "title": "A remény rabjai",
        "duration": "142 perc",
        "release_date": "1994. szeptember 23.",
        "showtimes": ["12:00", "20:00"],
        "image": "movie2.jpg"
    },
    {
        "title": "A sötét lovag",
        "duration": "152 perc",
        "release_date": "2008. július 18.",
        "showtimes": ["14:00", "22:00"],
        "image": "movie3.jpg"
    },
    {
        "title": "Forrest Gump",
        "duration": "142 perc",
        "release_date": "1994. július 6.",
        "showtimes": ["11:00", "19:00"],
        "image": "movie4.jpg"
    },
    {
        "title": "Vissza a jövőbe",
        "duration": "116 perc",
        "release_date": "1985. július 3.",
        "showtimes": ["13:00", "21:00"],
        "image": "movie5.jpg"
    }
]

# Fő ablak
root = tk.Tk()
root.title("Mozi Kezdőlap")
root.geometry("900x700")
root.config(bg="#f4f4f4")

# Filmek borítóképeinek és információinak megjelenítése
def show_showtimes(movie_title):
    # Új ablak létrehozása a játszási időpontokkal
    show_window = Toplevel(root)
    show_window.title(f"{movie_title} - Játékmenetek")
    show_window.geometry("300x200")
    
    # A film játszási idejeinek kiírása
    movie = next(m for m in movies if m["title"] == movie_title)
    showtimes_text = "\n".join(movie["showtimes"])
    
    label = tk.Label(show_window, text=f"Játékmenetek:\n{showtimes_text}", font=("Arial", 12), justify=tk.LEFT)
    label.pack(padx=20, pady=20)

# Filmek gombokkal
for movie in movies:
    movie_frame = tk.Frame(root, bg="#fff", bd=2, relief="solid", width=180, height=300)
    movie_frame.grid_propagate(False)  # Ne változtassa meg a méretét automatikusan
    movie_frame.grid(row=0, column=movies.index(movie), padx=20, pady=20)
    
    # Film borítókép
    try:
        image = Image.open(movie["image"])  # Helyettesítsd valódi képfájllal
        image = image.resize((180, 240))  # Resize the image to fit into the frame
        movie_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(movie_frame, image=movie_image)
        image_label.image = movie_image  # A hivatkozás megőrzéséhez szükséges
        image_label.pack()
    except Exception as e:
        print(f"Image error: {e}")
    
    # Film cím, időtartam és megjelenési dátum
    details_label = tk.Label(movie_frame, text=f"{movie['title']}\n{movie['duration']}\n{movie['release_date']}", font=("Arial", 10), bg="#fff")
    details_label.pack(pady=10)
    
    # Játékmenetek gomb
    showtimes_button = tk.Button(movie_frame, text="Játékmenetek", command=lambda m=movie: show_showtimes(m["title"]))
    showtimes_button.pack(pady=10)

# A fő ablak futtatása
root.mainloop()