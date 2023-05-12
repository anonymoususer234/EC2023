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


def on_submit():
    user_age = age_entry.get() #fetches all the variables inputted by the user (using .get())
    user_height = height_entry.get()
    user_weight = weight_entry.get()
    user_diet = diet_var.get()
    user_exercise = exercise_var.get()
    
    if not user_age or not user_height or not user_weight or not user_diet: #checks if the field is empty
        error_message = "Please fill in all the required fields."
        output_label.configure(text=error_message)
        return

    user_age = int(user_age) # casting everything to an int so that mathematical analysis can be completed on it 
    user_height = int(user_height)
    user_weight = int(user_weight)
    
    if user_age < 20:
        if user_diet == "Vegan":
            diet_plan = "Breakfast: Cereal with almond milk or a smoothie bowl made from fresh fruit\nLunch: Rice with vegan cheese curry or quinoa salad\nDinner: Vegan burger with sweet potato fries\nDessert: Dairy free chocolate, mixed berries and non-dairy ice cream"
        elif user_diet == "Vegetarian":
            diet_plan = "Breakfast: Oatmeal with mixed tropical fruits\nLunch: Veggie burger and water/sparking water\nDinner: Grilled vegetable skewers\nDessert: A low calorie fruit popsicle or ice cream bar from brands such as Yasso or Halotop (examples)"
        else:
            diet_plan = "Breakfast: Scrambled eggs with whole wheat toast\nLunch: Grilled chicken sandwich or Caesar salad with caesar dressing, anchovies, and croutons\nDinner: High protein beef curry and rice, or stew\nDessert: Honey-made gummies or low calorie ice cream bars"
    else:
        if user_diet == "Vegan":
             diet_plan = "Breakfast: Avocado toast\nLunch: Quinoa and black bean salad\nDinner: Grilled soy meat rice with vegetables/noodles\nDessert: Chia seed pudding"
        elif user_diet == "Vegetarian":
            diet_plan = "Breakfast: Greek yogurt with granola\nLunch: Lentil soup or Indian high-protein lentil curry\nDinner: Grilled vegetables, tofu, and soy with roasted vegetables\nDessert: Biscuits, milk/white chocolate, or low-calorie ice cream"
        else:
            diet_plan = "Breakfast: Scrambled eggs with whole wheat toast and bacon\nLunch: Grilled chicken sandwich and beef jerky\nDinner: Fish curry and steamed vegetables\nDessert: Mixed fruit sorbet"

    if user_height < 60: #for those less than 5 feet in height, we are adding more protein to their body 
        diet_plan += ", Snack: Protein shake"
