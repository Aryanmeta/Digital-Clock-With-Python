from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')

def time():
    string1 = strftime('%F\n%r\n%c\n%j Day\n%z\n%H:%M:%S %p\n%m/%d/%y %a')
    label.config(text=string1)
    label.after(1000,time)

label = Label(root,font=('A Iranian Sans',40),background='black',foreground='pink')
label.pack(anchor='center')

time()
mainloop()