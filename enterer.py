from ast import Return
from tkinter import *
from tkinter import ttk

root = Tk()
#Gives the entry bar
e = Entry(root, width=50)
e.pack()

root.geometry("750x250")
#This is what will be printed on screen
def callback():
    Label(root, text=e.get()).pack()
#What the button will do
btn = ttk.Button(root, text="Show the thing", command=callback)
btn.pack(ipadx=10)
#What key will be bound to the action
root.bind('<Return>',lambda event:callback())

root.mainloop()
