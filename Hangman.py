import tkinter as tk
from tkinter import messagebox
import random

#List of words for the game
words = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Watermelon","Papaya", "Cherry", 
    "Strawberry", "Blueberry", "Blackberry", "Raspberry","Peach", "Plum", "Pear", "Kiwi", "Fig",
    "Pomegranate", "Guava", "Lychee","Dragonfruit", "Passionfruit", "Coconut", "Avocado", "Lemon",
    "Lime","Tangerine", "Mandarin", "Apricot", "Cantaloupe", "Honeydew", "Cranberry","Date", 
    "Gooseberry", "Jackfruit", "Starfruit", "Durian", "Mulberry","Tamarind", "Sapodilla", "Elderberry",
    "Quince", "Custard Apple","Persimmon", "Rambutan", "Carrot", "Potato", "Tomato", "Onion", "Garlic", 
    "Cabbage", "Cauliflower","Broccoli", "Spinach", "Lettuce", "Kale", "Peas", "Green Beans", "Bell Pepper",
    "Chili Pepper", "Zucchini", "Cucumber", "Pumpkin", "Squash", "Eggplant", "Mushroom", "Corn", 
    "Sweet Potato", "Turnip", "Radish", "Beetroot", "Okra", "Celery", "Asparagus", "Leek", "Parsnip", 
    "Artichoke", "Brussels Sprouts", "Fennel", "Bok Choy", "Collard Greens","Swiss Chard", "Yam", "Arugula",
    "Watercress", "Horseradish", "Chives", "Mustard Greens", "Taro", "Bitter Melon", "Soccer", "Cricket", 
    "Basketball", "Baseball", "Tennis", "Badminton", "Volleyball", "Hockey", "Rugby", "Golf", "Track and Field", 
    "American Football", "Kabaddi", "Ultimate Frisbee", "Softball", "Handball", "Lacrosse", "Table Tennis (outdoor)",
    "Kickball", "Field Hockey", "Throwball", "Dodgeball", "Tag", "Capture the Flag", "Hide and Seek", "Hopscotch",
    "Jump Rope", "Four Square", "Skateboarding", "Cycling", "Roller Skating", "Archery", "Horse Riding", "Rowing", 
    "Kayaking", "Canoeing", "Rock Climbing", "Fishing", "Surfing", "Beach Volleyball", "Bocce", "Croquet","Petanque",
    "Tug of War", "Sparrow", "Pigeon", "Crow", "Parrot", "Peacock", "Eagle", "Hawk", "Owl", "Flamingo", "Penguin", 
    "Kingfisher", "Woodpecker", "Hummingbird", "Swan", "Duck", "Goose", "Turkey", "Rooster", "Hen", "Ostrich", "Emu",
    "Kite", "Falcon", "Seagull", "Canary", "Finch", "Robin", "Blue Jay", "Cardinal", "Magpie", "Cuckoo", "Heron", 
    "Pelican", "Stork", "Albatross", "Dove", "Cockatoo", "Macaw", "Toucan", "Lark", "Quail", "Sandpiper", "Wren", 
    "Raven", "Buzzard", "Ibis", "Kiwi", "Bald Eagle", "Snowy Owl", "Dog", "Cat", "Lion", "Tiger", "Elephant", 
    "Horse", "Zebra", "Giraffe", "Bear", "Wolf", "Glockenspiel", "Steel Drum", "Hang Drum", "Fox", "Deer", "Kangaroo",
    "Panda", "Rabbit", "Monkey", "Chimpanzee", "Gorilla", "Leopard","Cheetah", "Hyena", "Rhinoceros", "Hippopotamus", 
    "Crocodile", "Alligator", "Turtle", "Tortoise", "Snake", "Lizard", "Frog", "Toad", "Eagle", "Hawk", "Owl", "Penguin",
    "Dolphin", "Whale", "Shark", "Octopus", "Jellyfish", "Seal", "Walrus", "Bat", "Squirrel", "Chipmunk", "Raccoon", 
    "Otter", "Armadillo", "Antelope", "Buffalo","Camel", "Donkey", "Goat", "Sheep", "Cow", "Pig", "Moose", "Caribou", 
    "Llama", "Alpaca", "Guitar", "Piano", "Violin", "Drums", "Flute","Saxophone", "Trumpet", "Clarinet", "Cello", "Harp", 
    "Trombone", "Bass Guitar", "Ukulele", "Mandolin","Banjo", "Accordion", "Harmonica", "Oboe", "Tuba", "French Horn", 
    "Keyboard", "Synthesizer", "Xylophone", "Marimba", "Conga", "Bongo", "Tambourine", "Djembe", "Tabla", "Sitar", 
    "Viola", "Bassoon", "Bagpipes", "Didgeridoo", "Kalimba", "Lyre", "Zither", "Pan Flute", "Recorder", "Kazoo", 
    "Triangle", "Castanets", "Snare Drum", "Bass Drum", "Cymbals", "Gong"]
# Ques_hints=["Fruit", "Vegetable","Game","Bird","Animal","Music"]

Ques_hints = (
    ["Fruit"] * 47 +
    ["Vegetable"] * 47 +
    ["Game"] * 47 +
    ["Bird"] * 47 +
    ["Animal"] * 47 +
    ["Music"] * 47
)

sec_hint = ["One a day keeps the doctor away","It is an underground stem",
           "India's most watched game","Sent messages","King of the Jungle",
           "Naughty,cute and lazy","Everyone's favourite","Bull's Eye",
           "Produces sensual and intense sound","Famous for singing",
           "BTS V's favourite","Ball in the ring makes you win",
           "Most popular among the youth"]

#Initialize variables
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6
ind = words.index(word_to_guess)
Ques = Ques_hints[ind]
hints_left = 1

#Create a window
window = tk.Tk()
window.title("Hangman Game")
x1 = int(window.winfo_screenwidth())
y1 = int(window.winfo_screenheight())
x2 = 1000
y2 = 650
x = int(x1/2) - int(x2/2)
y = int(y1/2) - int(y2/2) 
window.geometry(f"{x2}x{y2}+{x}+{y}")
window.resizable(False,False)

#Function to check if the game is over
def is_game_over():
    return check_win() or check_loss()

#Function to check if the player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

#Function to check if the player hs lost
def check_loss():
    return attempts == 0

#Function to handle a letter guess
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter)==1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman",f"You've already guessed'{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo(f"Hangman", f"Congratulations! You win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -=1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman","You lose! The word was: "+ word_to_guess)
                reset_game()
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")
    letter_entry.delete(0,tk.END) 

#Function to reset the game
def reset_game():
    global word_to_guess, guessed_letters, attempts,ind,Ques,hints_left 
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts= 6
    ind = words.index(word_to_guess)
    Ques = Ques_hints[ind]
    hints_left = 1
    update_word_display()
    update_attempts_display()
    draw_hangman()
    update_ques()
    update_hints_left()
    hint_label.config(text ="")  

#Function to update the word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "❤️"
        display_word += " "
    word_label.config(text = display_word)

#Function to update the attempts display
def update_attempts_display():
    attempts_label.config(text = f"Attempts left: {attempts}")

#Function to draw the hangman figure
def draw_hangman():
    canvas.delete("hangman")
    if attempts<6:
        canvas.create_oval(125,125,175,175,width = 4, tags = "hangman") #Head
    if attempts<5:
        canvas.create_line(150,175,150,225,width = 4, tags = "hangman") #Body
    if attempts<4:
        canvas.create_line(150,200,125,175,width = 4, tags = "hangman") #Left Arm
    if attempts<3:
        canvas.create_line(150,200,175,175,width = 4, tags = "hangman") #Right Arm
    if attempts<2:
        canvas.create_line(150,225,125,250,width = 4, tags = "hangman") #Left Leg
    if attempts<1:
        canvas.create_line(150,225,175,250,width = 4, tags = "hangman") #Right Leg

#Function to update ques
def update_ques():
    ques_label.config(text = f"Ques: {Ques}")

#Function to update hints left
def update_hints_left():
    if hints_left ==1:
        hints_left_label.config(text = f"Hint left: 💰")
    else:
        hints_left_label.config(text = f"Hint left: 0")
# Function to get second hint
def get_hint():
    global hints_left
    if hints_left>0:
        hint = sec_hint[ind]
        hint_label.config(text = hint)
        hints_left -=1
        update_hints_left()
    else:
        messagebox.showinfo("Not sufficient hints")

#Create GUI elements
ques_label = tk.Label(window,text ="", font = ("Arial", 15),bg = "#68808B",fg = "white")
hints_left_label = tk.Label(window, text = "",font = ("Arial black", 13), fg = "black", bg = "#FD9797")
word_label = tk.Label(window, text = "", font = ("Arial", 24),fg = "#C70000", bg = "#D9BF18")
attempts_label = tk.Label(window, text = "", font = ("Arial", 16), bg = "#EFC3CA")
letter_entry = tk.Entry(window, width = 5, font=("Arial", 16),bd = 5, bg = "#98F5F9")
guess_button = tk.Button(window, text = "Guess",font = (20), command = guess_letter, bd = 4,bg ="#FFECA1")
reset_button = tk.Button(window, text = "Reset",font = (20), command = reset_game, bd = 4,bg = "#A5FFA4")
next_hint = tk.Button(window,text = "GET HINT",font= ("arial black" ,10),command = get_hint, bg = "#DFD4F7")
hint_label = tk.Label(window,text ="", font = ("Callibri", 14))
canvas = tk.Canvas(window, width = 300, height = 300, bg= "#CDD7E4")
canvas.create_line(50,250,250,250,width = 4) #Base line
canvas.create_line(200,250,200,100,width = 4) #Post
canvas.create_line(100,100,200,100,width = 4) #Beam
canvas.create_line(150,100,150,120,width = 4) #Beam
ques_label.pack()
hints_left_label.pack()
canvas.pack()

#Pack GUI elemets
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()
next_hint.pack()
hint_label.pack()

#Update initial displays
update_word_display()
update_attempts_display()
draw_hangman()
update_ques()
update_hints_left()

#Run the application 
window.mainloop()