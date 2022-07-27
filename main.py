from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Airline Manager")
root.geometry("800x800")

conn = sqlite3.connect('VA')
c = conn.cursor()


class MainWindow:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.grid()
        
        self.pilot_frame = LabelFrame(master, text="Pilot")
        self.pilot_frame.grid(row=0, column=0, padx=10, stick=W)
        
        self.pilot_name_label = ttk.Label(self.pilot_frame, text="Pilot Name: ")
        self.pilot_hours_label = ttk.Label(self.pilot_frame, text="Total Flight Hours: ")
        self.pilot_money_label = ttk.Label(self.pilot_frame, text="Total Money: ")
        
        self.name = ttk.Label(self.pilot_frame, text="Marius Jensch")
        self.hours = ttk.Label(self.pilot_frame, text="140hrs")
        self.money = ttk.Label(self.pilot_frame, text="25.000€")
        
        self.pilot_name_label.grid(row=0, column=0, sticky=W)
        self.pilot_hours_label.grid(row=1, column=0, sticky=W)
        self.pilot_money_label.grid(row=2, column=0, sticky=W)
        
        self.name.grid(row=0, column=3, sticky=E)
        self.hours.grid(row=1, column=3, sticky=E)
        self.money.grid(row=2, column=3, sticky=E)

run = MainWindow(root)

conn.commit()
conn.close()
mainloop()