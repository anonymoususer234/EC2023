import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
import random

window = tk.Tk() #creates the window for the tkinter window 
window.geometry("800x800")
window.title("Health Advisor App")

canvas = tk.Canvas(window)
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind( #configure the scroll wheel using lambda and canvas 
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
style = ttk.Style()
style.configure("My.TFrame", background="white")
