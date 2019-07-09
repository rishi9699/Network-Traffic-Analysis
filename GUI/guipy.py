import tkinter
from tkinter.ttk import *
from tkinter import messagebox
 
window=tkinter.Tk()
# to rename the title of the window window.title("GUI")
window.title("GUI")
 
# pack is used to show the object in the window
window.geometry('400x200')
l1 = tkinter.Label(window, text = "Hello World!")
l1.grid(column=0, row=0)
txt = tkinter.Entry(window,width=10)
txt.grid(column=0, row=2)
def triggrd():
    txt.get()
    l1.configure(text=int(txt.get())/2)
    messagebox.showinfo("Message title", "Message content")
bt = (tkinter.Button (window, text="Enter", bg="green", fg="black", command=triggrd)).grid(column=0, row=1)
chk = tkinter.Checkbutton(window, text="Select")
chk.grid(column=0, row=3)
rad1 = Radiobutton(window, text="Python", value=1)
rad2 = Radiobutton(window, text="Java", value=2)
rad3 = Radiobutton(window, text='Scala', value=3)
rad1.grid(column=0, row=6)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=4)
window.mainloop()