from tkinter import *

window = Tk()
window.title("Welcome to fun facts")
window.geometry('1200x600')

lbl = Label(window, text="person 1")
lbl.grid(column=0, row=0)

label = Label(window, text="person 2")
label.grid(column=0, row=1)

def clicked():
    lbl.configure(text="1. His favorite coding languages are java and python.\n"
                       "2. His favorite color is red.\n "
                       "3. His favorite video game is minecraft.\n "
                       "4. His favorite sports are football, baseball and formula 1.\n "
                       "5. His favorite food is sushi \n")
    btn1.destroy()

def pressed():
    label.configure(text="1. His favorite coding languages are c++ and assembly\n"
                         "2. His favorite color is yellow\n"
                         "3. his favorite game is FIFA 26 \n"
                         "4. his favorite sport is vollyball\n"
                         "5. his favorite food is thini")
    btn2.destroy()

btn1 = Button(window, text="Person 1", command=clicked)
btn1.grid(column=1, row=0)

btn2 = Button(window, text="Person 2", command=pressed)
btn2.grid(column=1, row=1)

window.mainloop()
