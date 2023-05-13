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

        
    if user_exercise == "Cardio":
        exercise_plan = "30 minutes of running\n10 minutes of jumping jacks: aim for 6 sets of 30 at least\n5 minutes of burpees"
    elif user_exercise == "Strength":
        exercise_plan = "Workout for 1 hour: 3 sets of 10 benchpresses\n3 sets of 10 squats\n3 sets of deadlifts (you can incresae difficulty)"
    elif user_exercise == "Yoga":
        exercise_plan = "30 minutes of yoga, holding one nostril at a time and breathing through the other slowly\nFinally, 10 minutes of stretching"
    else:
        exercise_plan = "No exercise plan available for this selection"


    workaround_plan = "" #depending on allergies there is a workaround plan to prevent any contamination 
    if dairy_var.get() == 1:
        workaround_plan += "Avoid dairy products. "
    if gluten_var.get() == 1:
        workaround_plan += "Avoid gluten-containing products. "
    if peanut_var.get() == 1:
        workaround_plan += "Avoid peanuts and peanut butter. "
    if seafood_var.get() == 1:
        workaround_plan += "Avoid seafood. "
    if len(workaround_plan) == 0:
        workaround_plan = "No workaround plan required."


    output_label.configure( #display widget
        text=f"Based on your input, here is your customized health advice plan:\n\nDiet plan: {diet_plan}\n\nExercise plan: {exercise_plan}\n\nWorkaround plan: {workaround_plan}"
    )

    
 #setting all the colors, labels and frames and then packing it using y coordinates 
frame_bg = "white"
scrollable_frame.configure(style="My.TFrame")
window.configure(bg="lightgray")
age_frame = tk.Frame(window, bg=frame_bg)
age_frame.pack(pady=10)
age_label = tk.Label(age_frame, text="What is your age?", font=("Arial", 12), bg=frame_bg)
age_label.pack(side=tk.LEFT, padx=10)
age_entry = tk.Entry(age_frame, width=50, font=("Arial", 12))
age_entry.pack(side=tk.LEFT)
height_frame = tk.Frame(window, bg=frame_bg)
height_frame.pack(pady=10)
height_label = tk.Label(height_frame, text="What is your height in in?", font=("Arial", 12), bg=frame_bg)
height_label.pack(side=tk.LEFT, padx=10)
height_entry = tk.Entry(height_frame, width=50, font=("Arial", 12))
height_entry.pack(side=tk.LEFT)
weight_frame = tk.Frame(window, bg=frame_bg)
weight_frame.pack(pady=10)
weight_label = tk.Label(weight_frame, text="What is your weight in lbs?", font=("Arial", 12), bg=frame_bg)
weight_label.pack(side=tk.LEFT, padx=10)
weight_entry = tk.Entry(weight_frame, width=50, font=("Arial", 12))
weight_entry.pack(side=tk.LEFT)
diet_frame = tk.Frame(window, bg=frame_bg) #diet menu
diet_frame.pack(pady=10)



diet_var = tk.StringVar(window)  # Add this line to define diet_var
diet_label = tk.Label(diet_frame, text="What is your diet preference?", font=("Arial", 12), bg=frame_bg)
diet_label.pack(side=tk.LEFT, padx=10)
diet_options = ["Vegan", "Vegetarian", "Non-veg"]  # Define the diet options list
diet_dropdown = tk.OptionMenu(diet_frame, diet_var, *diet_options)
diet_dropdown.config(width=20, font=("Arial", 12))
diet_dropdown.pack(side=tk.LEFT)
exercise_frame = tk.Frame(window, bg=frame_bg) #exercise button
exercise_frame.pack(pady=10)
exercise_label = tk.Label(exercise_frame, text="What is your exercise preference?", font=("Arial", 12), bg=frame_bg)
exercise_label.pack(side=tk.LEFT, padx=10)
exercise_var = tk.StringVar(window, value="Cardio")  # Add this line to define exercise_var

cardio_radio = tk.Radiobutton(exercise_frame, text="Cardio", variable=exercise_var, value="Cardio", font=("Arial", 12), bg=frame_bg)
cardio_radio.pack(side=tk.LEFT)
strength_radio = tk.Radiobutton(exercise_frame, text="Strength Training", variable=exercise_var, value="Strength", font=("Arial", 12), bg=frame_bg)
strength_radio.pack(side=tk.LEFT)
yoga_radio = tk.Radiobutton(exercise_frame, text="Yoga", variable=exercise_var, value="Yoga", font=("Arial", 12), bg=frame_bg)
yoga_radio.pack(side=tk.LEFT)
no_exercise_radio = tk.Radiobutton(exercise_frame, text="No exercise", variable=exercise_var, value="None", font=("Arial", 12), bg=frame_bg)
no_exercise_radio.pack(side=tk.LEFT)


workaround_frame = tk.Frame(window, bg=frame_bg) # this is the area where there is a workaround 
workaround_frame.pack(pady=10)
workaround_label = tk.Label(workaround_frame, text="Do you have any allergies or dietary restrictions?", font=("Arial", 12), bg=frame_bg)
workaround_label.pack(side=tk.LEFT, padx=10)
dairy_var = tk.IntVar(window)  # Add this line to define dairy_var
dairy_check = tk.Checkbutton(workaround_frame, text="Dairy", variable=dairy_var, font=("Arial", 12), bg=frame_bg)
dairy_check.pack(side=tk.LEFT)
gluten_var = tk.IntVar(window)  # Add this line to define gluten_var
gluten_check = tk.Checkbutton(workaround_frame, text="Gluten", variable=gluten_var, font=("Arial", 12), bg=frame_bg)
gluten_check.pack(side=tk.LEFT)
peanut_var = tk.IntVar(window)  # Add this line to define peanut_var
peanut_check = tk.Checkbutton(workaround_frame, text="Peanuts", variable=peanut_var, font=("Arial", 12), bg=frame_bg)
peanut_check.pack(side=tk.LEFT)
