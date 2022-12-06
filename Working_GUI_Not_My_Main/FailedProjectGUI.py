import tkinter
from tkinter import *
import random
from ProjectCode2 import *
import os

root = Tk()
root.title('Project')
root.geometry('1000x2400')
def button_function():
    global my_Text
    output = simulate_game()
    my_Text.insert(END,output)
    print("button pressed")
    button['state'] = DISABLED

def button_function2():
    my_Text.delete(1.0,END)
    button['state'] = NORMAL

button = Button(root, text="Click Me!!!", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button2 = Button(root, text="Reset!!!", command=button_function2)
button2.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
my_Text = Text(root,width = 40, height = 10, font=('Helvetica',12))
my_Text.pack(pady=30)
root.mainloop()
