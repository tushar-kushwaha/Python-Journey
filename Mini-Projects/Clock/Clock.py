import tkinter as tk 
from time import strftime

display = tk.Tk()
display.title("Clock")

label = tk.Label(display,font = ('DS-Digital', 50 , 'bold' ), background = 'black' , foreground = 'white' )
label.pack(anchor = 'center')

def clock():
    string = strftime('%H:%M:%S \n%D')
    label.config(text = string)
    label.after(1000 , clock)

clock()

display.mainloop()

