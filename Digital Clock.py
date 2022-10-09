from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')

def time():
    string1 = strftime('%F\n%r\n%c')
    label.config(text=string1)
    label.after(1000,time)

label = Label(root,font=('A Iranian Sans',40),background='black',foreground='pink')
label.pack(anchor='center')

time()
mainloop()