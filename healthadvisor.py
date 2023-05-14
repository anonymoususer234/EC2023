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
