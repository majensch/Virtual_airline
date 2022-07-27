from tkinter import *
from PIL import ImageTk, Image
from pyparsing import col

root = Tk()
root.title("Airline Manager")
root.geometry("400x400")


class MainWindow:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.grid()
        
        self.pilot_frame = LabelFrame(master, text="Pilot")
        self.pilot_frame.grid(row=0, column=0, padx = 25, pady=25)
        
        self.pilot_name_label = Label(self.pilot_frame, text="Pilot Name: ")
        self.pilot_hours_label = Label(self.pilot_frame, text="Total Flight Hours: ")
        self.pilot_money_label = Label(self.pilot_frame, text="Total Money: ")
        
        self.pilot_name_label.grid(row=0, column=0, sticky=W)
        self.pilot_hours_label.grid(row=1, column=0, sticky=W)
        self.pilot_money_label.grid(row=2, column=0, sticky=W)


run = MainWindow(root)
mainloop()