from tkinter import *
from textblob import TextBlob

def check_spelling():
    a = TextBlob(spell_check.get())
    spell = Label(window, text = "The Correct Spelling is:", font=('Poppins bold', 30))
    spell.pack()
    correct_text = Label(window, text = str(a.correct()), font=('Poppins bold', 25), bg = "lightpink")
    correct_text.pack()

window = Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background = "lightgreen")

text_heading = Label(window, text= "Spelling Checker", font = ("Arial", 40, "bold"), bg="black", fg = "pink")
text_heading.pack()

text_check = Label(window, text= "Enter The Spelling", font = ("Arial", 35), bg="yellow", fg = "red")
text_check.pack(pady = 10)

spell_check = Entry(window, font= ("Arial", 25), width= 250, bg = "skyblue")
spell_check.pack()


Check_button = Button(window, text= "Check !!", font=('Poppins bold', 25), fg= "white", bg ="red", command = check_spelling)
Check_button.pack(pady= 10)

window.mainloop()
