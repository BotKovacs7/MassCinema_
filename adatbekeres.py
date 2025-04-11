
from tkinter import *
import sqlite3
import FoglalásMySQL

root = Tk()
root.title("Adatbázis létrehozása")
root.geometry("700x550")

def submit():
    conn = sqlite3.connect("sample_db.db")
    c = conn.cursor()
    c.execute("INSERT INTO foglalasok VALUES (:keresztnev, :vezeteknev)",
        {
            'keresztnev':l_name.get(),
            'vezeteknev':f_name.get(),
        }
    )
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)


def query():
    conn = sqlite3.connect("sample_db.db")
    c = conn.cursor()   
    c.execute("SELECT *, oid FROM cimek")
    records = c.fetchall()
    if records:
        print_records = ''
        for record in records[0]:
            print_records += str(record) + "\n"
        
        query_label = Label(root, text=print_records)
        query_label.grid(row=10, column=0,columnspan=2)
    conn.commit()
    conn.close()




f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

f_name_lbl = Label(root, text="Vezetéknév")
f_name_lbl.grid(row=0, column=0)

l_name_lbl = Label(root, text="Keresztnév")
l_name_lbl.grid(row=1, column=0)



submit_btn = Button(root, text="Hozzáad", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=150)

root.mainloop()