import tkinter


window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
lista = ['Python', 'Java', 'C#', 'Javascript', 'PHP', 'R', 'C++']
lista_box = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_box)
listbox.grid(column=0, row=1, sticky=tkinter.W)

label1 = tkinter.Label(window, text='Lenguajes de programacion')
label1.grid(column=0, row=0, sticky=tkinter.N)


window.mainloop()