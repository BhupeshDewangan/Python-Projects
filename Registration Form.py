
from tkinter import *
root = Tk()

root.geometry("500x300")

def submit_value():
    print("Your Info. Has Been Saved Successfully")


Label(root, text="Python Registration Form", font= "times 15 bold").grid(row=0, column=3)


name_user = Label(root, text="Student Name")
name_user.grid(row=1, column=2)

branch_user = Label(root, text ="Branch")
branch_user.grid(row=2, column=2)

gender_user = Label(root, text="Gender")
gender_user.grid(row=3, column=2)



country_user = Label(root, text="Country")
country_user.grid(row=5, column = 2)

name_value = StringVar
branch_value = StringVar
gender_value = StringVar
country_value = StringVar
check_value = IntVar

name_box = Entry(root, textvariable = name_value)
name_box.grid(row=1, column=3)

branch_box =Entry(root, textvariable = branch_value)
branch_box.grid(row=2 , column= 3)

gender_box = Entry(root, textvariable = gender_value)
gender_box.grid(row=3, column= 3)


country_box = Entry(root, textvariable = country_value)
country_box.grid(row = 5, column= 3)

check_box = Checkbutton(text ="remember me?", variable = check_value)
check_box.grid(row= 6, column= 3)

Button(text= "Submit", command= submit_value()).grid(row=7, column = 3)

root.mainloop()
