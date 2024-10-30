import tkinter as tk
from time import strftime

#timer
def timer():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, timer)

#window
window=tk.Tk()
window.title("Clock")


#label
label=tk.Label(window, font=("Arial",40), fg="white", bg="orange")
label.pack()
timer()

window.mainloop()