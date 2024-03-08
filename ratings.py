import sqlite3
import time
import tkinter as tk
import datetime
#import current user id


ratings = sqlite3.connect("ratings.db")
r = ratings.cursor()
r.execute("""CREATE TABLE IF NOT EXISTS ratings 
        (rating INT,
        poster INT,
        year INT)""")

# current user needs to be inputed here
def insertRating():
    #user = imported id
    currentDate = datetime.now()
    strDate = currentDate.strftime("%Y")
    numberOutOfTen = int(textBox.get())
    if numberOutOfTen >= 1:
        if numberOutOfTen <= 10:
            inserted = [
            (numberOutOfTen , user , strDate),
            ]
            b.executemany("""
                INSERT INTO ratings (rating ,poster ,year) VALUES (?,?,?)
                """,inserted)
            ratings.commit()
        


def start():
    #window
    window = tk.Tk()
    window.geometry("700x700")
    window.title("ratings")
    label1 = tk.Label(window, text="Enter how you rate the program out of ten", font=("Arial",18))
    label1.pack()
    textbox = tk.Entry(window)
    textbox.pack()
    buttI = tk.Button(window, text="input rating",font = ("Arial",14),command = insertRating)
    buttI.pack()
    buttC = tk.Button(window, text="close",font=("Arial",14),command = window.destroy)
    buttC.pack()
    window.mainloop()


start()
