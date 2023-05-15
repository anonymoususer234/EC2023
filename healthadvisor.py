#import the tkiner module and all the sub-modules that are part of it 
import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
import random


#user discussion with the chatbot 
questions = [
    "what are some healthy breakfast options?",
    "what are the benefits of regular exercise?",
    "how can I lose weight effectively?",
    "what are some high-protein vegetarian meals?",
    "what are the best ways to reduce stress?"
]
answers = [
    "Some healthy breakfast options include cereal with fat free milk, avacado toast, or a greek yogurt and fruits.",
    "Regular exercise has numerous benefits, including improved stamina, fat loss and muscle gain, cardiovascular health, and overall lifespan.",
    "To lose weight effectively, it's important to combine a balanced diet with regular physical activity. Make sure to burn more calories than you consume and whatever you consume has to be rich in nutrients",
    "High-protein vegetarian meals can include options like tofu, lentils, garbanzo beans, and soy meat (vegetarian)",
    "To reduce stress, you can try practicing mindfulness techniques, such as meditation, yoga, engaging in mindfulness seminars and maintaing a calm and cool lifestyle."
]

chatbot_window = None
chatbot_button_added = False  #flag to track if chatbot button is added

def switch_to_main(): #this function would switch the display from the chatbot window to the main by destroying the chatbot window
    global chatbot_window
    chatbot_window.destroy()
    window.deiconify() #de-iconify the main window in order to make sure that it stays 

def switch_to_chatbot():
    window.withdraw()

    #This code creates a new window for the chatbot page
    #It also sets the window dimensions and title
    global chatbot_window
    chatbot_window = tk.Toplevel(window)
    chatbot_window.geometry("800x600")
    chatbot_window.title("Healthbot")

    #this function creates a button in the chatbot window that lets the user switch back to the main page
    back_button = tk.Button(chatbot_window, text="Back", command=switch_to_main)
    back_button.pack()

    #this function creates a text entry box in the chatbot window where the user can enter their question
    question_entry = tk.Entry(chatbot_window, width=50, font=("Arial", 12))
    question_entry.pack(pady=10)

    def get_answer():
        question = question_entry.get().lower()
        if question:
        #if the question is in our list of known questions, we retrieve the corresponding answer
            if question in questions:
                index = questions.index(question)
                answer = answers[index]
            else:
            #if the question is not in our list, we display a default answer
                answer = "I'm sorry, I don't have an answer for that question."

            answer_label = tk.Label(chatbot_window, text=answer, font=("Arial", 12), wraplength=700, justify=tk.LEFT)
            answer_label.pack(pady=10)


            question_entry.delete(0, tk.END) #deleting the entries 

    
    get_answer_button = tk.Button(chatbot_window, text="Get Answer", command=get_answer, font=("Arial", 12)) #create a button to get the answer
    get_answer_button.pack() #pack the button 


def on_submit():
    user_age = age_entry.get() #fetching all the user inputted information
    user_height = height_entry.get()
    user_weight = weight_entry.get()
    user_diet = diet_var.get()
    user_exercise = exercise_var.get()

    if not user_age or not user_height or not user_weight or not user_diet: #checking for empty fields 
        error_message = "Please fill in all the required fields."
        output_label.configure(text=error_message)
        return

    user_age = int(user_age) #casting so that mathematical operations can be completed on it 
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

    if user_height < 60:
        diet_plan += ", Snack: Protein shake"


    if user_exercise == "Cardio": #generates exercise plans for the user based on the exercise type they chose 
        exercise_plan = "30 minutes of running\n10 minutes of jumping jacks: aim for 6 sets of 30 at least\n5 minutes of burpees"
    elif user_exercise == "Strength":
        exercise_plan = "Workout for 1 hour: 3 sets of 10 benchpresses\n3 sets of 10 squats\n3 sets of deadlifts (you can incresae difficulty)"
    elif user_exercise == "Yoga":
        exercise_plan = "30 minutes of yoga, holding one nostril at a time and breathing through the other slowly\nFinally, 10 minutes of stretching"
    else:
        exercise_plan = "No exercise plan available for this selection"

    workaround_plan = "" #workaround plans based on the user's allergies 
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

    workaround_plan = ""
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


    output_label.configure( #configure and display the output widget 
        text=f"Based on your input, here is your customized health advice plan:\n\nDiet plan: {diet_plan}\n\nExercise plan: {exercise_plan}\n\nWorkaround plan: {workaround_plan}"
    )


    global chatbot_button_added #once the user clicks submit, the chatbot button should appear by adding and packing the button right underneath the submit button
    if not chatbot_button_added:
        chatbot_button = tk.Button(window, text="Chatbot", command=switch_to_chatbot, font=("Arial", 12))
        chatbot_button.pack(pady=10)
        chatbot_button_added = True

    
    


window = tk.Tk() #The main window is created, and its dimensions and title are set. 
window.geometry("800x800")
window.title("Health Advisor App")


canvas = tk.Canvas(window) #scrollable frame 
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw") #creates a new canvas by setting the coordinates and the anchor 
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
style = ttk.Style() #creates a custom style for the scrollable frame
style.configure("My.TFrame", background="white")


frame_bg = "white" #set the color to white 
scrollable_frame.configure(style="My.TFrame")
window.configure(bg="lightgray") #configure the background to light gray 


#Here we create all the user input entry widgets 
age_frame = tk.Frame(window, bg=frame_bg)
age_frame.pack(pady=10)
age_label = tk.Label(age_frame, text="What is your age?", font=("Arial", 12), bg=frame_bg) #the age laebsl and entry box 
age_label.pack(side=tk.LEFT, padx=10)
age_entry = tk.Entry(age_frame, width=50, font=("Arial", 12))
age_entry.pack(side=tk.LEFT)

height_frame = tk.Frame(window, bg=frame_bg) #the height input entry location setting and entry box
height_frame.pack(pady=10)
height_label = tk.Label(height_frame, text="What is your height in inches?", font=("Arial", 12), bg=frame_bg)
height_label.pack(side=tk.LEFT, padx=10)
height_entry = tk.Entry(height_frame, width=50, font=("Arial", 12))
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window, bg=frame_bg) #setting the weight frame, label and entry box and packing it 
weight_frame.pack(pady=10)
weight_label = tk.Label(weight_frame, text="What is your weight in lbs?", font=("Arial", 12), bg=frame_bg)
weight_label.pack(side=tk.LEFT, padx=10)
weight_entry = tk.Entry(weight_frame, width=50, font=("Arial", 12))
weight_entry.pack(side=tk.LEFT)


diet_frame = tk.Frame(window, bg=frame_bg) #setting up the frame for the dropdown menu options for diet preference type 
diet_frame.pack(pady=10) 
diet_var = tk.StringVar(window)  #adding his line to define diet_var
diet_label = tk.Label(diet_frame, text="What is your diet preference?", font=("Arial", 12), bg=frame_bg)
diet_label.pack(side=tk.LEFT, padx=10)
diet_options = ["Vegan", "Vegetarian", "Non-veg"]  #defining the diet options list
diet_dropdown = tk.OptionMenu(diet_frame, diet_var, *diet_options)
diet_dropdown.config(width=20, font=("Arial", 12))
diet_dropdown.pack(side=tk.LEFT)


exercise_frame = tk.Frame(window, bg=frame_bg) #here, the exercise preference frame and labels are created and packed 
exercise_frame.pack(pady=10)
exercise_label = tk.Label(exercise_frame, text="What is your exercise preference?", font=("Arial", 12), bg=frame_bg)
exercise_label.pack(side=tk.LEFT, padx=10)
exercise_var = tk.StringVar(window, value="Cardio")  # Add this line to define exercise_var



#the cardio radio button is created, taking in the exercise_frame, text, exercise type, and font as the parameters. 
cardio_radio = tk.Radiobutton(exercise_frame, text="Cardio", variable=exercise_var, value="Cardio", font=("Arial", 12), bg=frame_bg)
cardio_radio.pack(side=tk.LEFT)

#Same as the cardio_radio variable, however this is specifically for the strength_radio variable 
strength_radio = tk.Radiobutton(exercise_frame, text="Strength Training", variable=exercise_var, value="Strength", font=("Arial", 12), bg=frame_bg)
strength_radio.pack(side=tk.LEFT)

#same as above
yoga_radio = tk.Radiobutton(exercise_frame, text="Yoga", variable=exercise_var, value="Yoga", font=("Arial", 12), bg=frame_bg)
yoga_radio.pack(side=tk.LEFT)

#same as above
no_exercise_radio = tk.Radiobutton(exercise_frame, text="No exercise", variable=exercise_var, value="None", font=("Arial", 12), bg=frame_bg)
no_exercise_radio.pack(side=tk.LEFT)


workaround_frame = tk.Frame(window, bg=frame_bg) #workaround checkboxes
workaround_frame.pack(pady=10)
workaround_label = tk.Label(workaround_frame, text="Do you have any allergies or dietary restrictions?", font=("Arial", 12), bg=frame_bg)
workaround_label.pack(side=tk.LEFT, padx=10)

dairy_var = tk.IntVar(window)  #add this line to define dairy_var
dairy_check = tk.Checkbutton(workaround_frame, text="Dairy", variable=dairy_var, font=("Arial", 12), bg=frame_bg)
dairy_check.pack(side=tk.LEFT)

gluten_var = tk.IntVar(window)  #add this line to define gluten_var
gluten_check = tk.Checkbutton(workaround_frame, text="Gluten", variable=gluten_var, font=("Arial", 12), bg=frame_bg)
gluten_check.pack(side=tk.LEFT)

peanut_var = tk.IntVar(window)  #add this line to define peanut_var
peanut_check = tk.Checkbutton(workaround_frame, text="Peanuts", variable=peanut_var, font=("Arial", 12), bg=frame_bg)
peanut_check.pack(side=tk.LEFT)

seafood_var = tk.IntVar(window)  #add this line to define seafood_var
seafood_check = tk.Checkbutton(workaround_frame, text="Seafood", variable=seafood_var, font=("Arial", 12), bg=frame_bg)
seafood_check.pack(side=tk.LEFT)



output_label = tk.Label(scrollable_frame, font=("Arial", 12)) #output label set in the scrollable frame with a font
output_label.grid(row=1, column=0, padx=10, pady=10)
output_label.configure(background=frame_bg)



def generate_meal_plan(user_diet): #generate personalized meal plan 
    user_calories = int(calories_entry.get()) #fetching user input and casting it to an int type 
    user_ingredients = ingredients_entry.get().split(", ")

    #the below will generate meal plan algorithm based on preferences and inputs
    breakfast = ""
    lunch = ""
    dinner = ""
    snacks = []
    #popular ingredient types 
    meat_items = ["beef", "chicken", "pork", "lamb", "turkey"]
    vegetable_items = ["carrots", "broccoli", "spinach", "tomatoes", "peppers"]
    fruit_items = ["apple", "banana", "orange", "grapes", "strawberries"]
    for ingredient in user_ingredients: #processing the user input for ingredients by fetching 
        ingredient_lower = ingredient.lower()

        if ingredient_lower in meat_items: #if the ingrediant is a meat item and is vegan, it continues and randomly selects something vegan for them 
            if user_diet == "Vegan":
                continue
            elif user_diet == "Vegetarian": #if the user is vegeterian but selected a meat item, then we would make their meal vegeterian (e.g. soy substitute)
                lunch = f"Vegetarian curry with {ingredient}"
                dinner = f"Vegetarian stir-fry with {ingredient}"
            else:
                lunch = f"Curry with {ingredient} and rice" #if they are non-veg, then they can hava regular meal 
                dinner = f"Grilled {ingredient} with vegetables"
        elif ingredient_lower in vegetable_items: #processes and outputs the food if they inputted a vegetable 
            breakfast = f"Steamed {ingredient} with rice"
            dinner = f"Stir-fried {ingredient} with soy sauce and rice"
        elif ingredient_lower in fruit_items:
            breakfast = f"Mixed fruit bowl with {ingredient}"
            breakfast = f"Smoothie with {ingredient}"
        else:
            snacks.append(ingredient) #if nothing, then there is an append to the snacks category 


    if not breakfast: #fall back options when the user does not input anything (random choices)
        breakfast_options = ["Oatmeal with mixed berries", "Avocado toast", "Yogurt with granola"]
        breakfast = random.choice(breakfast_options)

    if not lunch:
        lunch_options = ["Grain bowl with roasted vegetables", "Caprese salad", "Vegetable wrap"]
        lunch = random.choice(lunch_options)

    if not dinner:
        dinner_options = ["Pasta with marinara sauce", "Stir-fry tofu with rice and steamed vegetables", "Alfredo noodles that are high in protein"]
        dinner = random.choice(dinner_options)


    dessert_options = ["Chocolate cake", "Ice cream", "Fruit sorbet", "Cheesecake"] #random dessert since balance is important in a healthy diet 
    dessert = random.choice(dessert_options)


    meal_plan_label.configure( #the meal plan is configured and outputted using the f string format for ease 
        text=f"Personalized Meal Plan:\n\n"
             f"Breakfast: {breakfast}\n"
             f"Lunch: {lunch}\n"
             f"Dinner: {dinner}\n"
             f"Snacks: {', '.join(snacks)}\n"
             f"Dessert: {dessert}"
    )

meal_plan_label = tk.Label(window, text="Personalized Meal Planning", font=("Arial", 14), bg=frame_bg) #personalized meal plan section and label creation/packing
meal_plan_label.pack(pady=10)


calories_frame = tk.Frame(window, bg=frame_bg) #creating the user input entry widgets for personalized meal planning
calories_frame.pack(pady=10)
calories_label = tk.Label(calories_frame, text="Enter your daily calorie target:", font=("Arial", 12), bg=frame_bg)
calories_label.pack(side=tk.LEFT, padx=10)
calories_entry = tk.Entry(calories_frame, width=50, font=("Arial", 12))
calories_entry.pack(side=tk.LEFT)

ingredients_frame = tk.Frame(window, bg=frame_bg) #creating the ingrediants frame and text box entry where the user inputs their ingredients 
ingredients_frame.pack(pady=10)
ingredients_label = tk.Label(ingredients_frame, text="Enter ingredients you have (comma-separated):", font=("Arial", 12), bg=frame_bg)
ingredients_label.pack(side=tk.LEFT, padx=10)
ingredients_entry = tk.Entry(ingredients_frame, width=50, font=("Arial", 12))
ingredients_entry.pack(side=tk.LEFT)

generate_button = tk.Button(window, text="Generate Meal Plan", command=lambda: generate_meal_plan(diet_var.get()), font=("Arial", 12)) #this button generates the meal based on the inputs 
generate_button.pack(pady=10)



submit_button = tk.Button(window, text="Submit", command=on_submit, font=("Arial", 12)) #the submit button at the end (the generalized meal and exercise planning section)
submit_button.pack(pady=10)



#window.mainloop is called to run the entire code 
window.mainloop()
