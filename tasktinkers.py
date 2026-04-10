from tkinter import *
from tkinter.ttk import Progressbar, Combobox

root = Tk()
root.title("Tkinter App")
root.geometry("250x250+140+20")
root.resizable(False, False)
root.minsize(200, 200)

label = Label(root, text="Text")
label.pack()

button = Button(root, text="Button")
button.pack()

entry = Entry(root)
entry.pack()

text = Text(root, height=2)
text.pack()

listbox = Listbox(root, height=3)
listbox.pack()

combo = Combobox(root, values=["Item 1"])
combo.pack()

main_menu = Menu(root)
root.config(menu=main_menu)
sub_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Menu", menu=sub_menu)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

progress = Progressbar(root, length=100)
progress.pack()

root.mainloop()