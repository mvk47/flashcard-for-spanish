from tkinter import *
import pandas as pd
import random
word = {"Spanish": None, "English": None}


BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Times New Roman", 30, "bold")

# Flipping the card

words = pd.read_csv("data/spanish_words.csv")
dict_of_words = words.to_dict(orient="records")
word = {"Spanish": "Empty", "English": "Empty"}


def flip_card():
    canvas.itemconfig(canvas_background, image=back_background)
    canvas.itemconfig(canvas_title, text="English", font=FONT_TITLE)
    canvas.itemconfig(canvas_word, text=word["English"])
#  Word change




def change_word():
    global word
    canvas.itemconfig(canvas_title, text="Spanish", font=FONT_TITLE)
    word = dict_of_words[random.randint(0, len(dict_of_words))]
    canvas.itemconfig(canvas_word, text=word["Spanish"], font=FONT_WORD)
    # window.after(3000, flip_card())

window = Tk()

window.title("Spanish learner")

window.minsize(height=720, width=800)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# front card

front_background = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=528, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(400, 263, image=front_background)
back_background = PhotoImage(file="images/card_back.png")


canvas_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
canvas_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


window.after(3000, func=flip_card())
# Tick button
my_image = PhotoImage(file="images/right.png")
tick_button = Button(image=my_image, highlightthickness=0, command=change_word)
tick_button.grid(row=1, column=0)

# Cross button
my_image2 = PhotoImage(file="images/wrong.png")
cross_button = Button(image=my_image2, highlightthickness=0, command=change_word)
cross_button.grid(row=1, column=1)




change_word()

window.mainloop()
