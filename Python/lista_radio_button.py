import tkinter
from tkinter import ttk


window = tkinter.Tk()


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Soltero', value='Soltero', variable=selected)
r2 = ttk.Radiobutton(window, text='Casado', value='Casado',variable=selected)
r3 = ttk.Radiobutton(window, text='Divorciado', value='Divorciado', variable=selected)

def reset():
    for widget in window.winfo_children():
        if isinstance(widget, ttk.Radiobutton):
            selected.set(None)   
clear = tkinter.Button(window, text='Clear', command=lambda: reset())

def submit_info():
    print(selected.get())
submit = tkinter.Button(window, text='Submit', command=lambda: submit_info())

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
clear.grid(column=1, row=2, padx=5, pady=5)
submit.grid(column=1, row=3, padx=5, pady=5)

window.mainloop()