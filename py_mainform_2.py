# main form
import tkinter as tk
from tkinter import *

w = 1200
h = 650

class mainform:
    def __init__(self, master):
        self.master = master
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))


        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.master.config(bg="#2A2C2B")
        self.lbl = tk.Label(self.master, text='Main Form', font=('verdana',50, 'bold'), fg='#ecf0f1',bg="#2A2C2B")
        self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)