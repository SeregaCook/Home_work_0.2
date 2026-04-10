from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Калькулятор")
root.geometry("250x250+140+20")
root.resizable(False, False)
root.minsize(200, 200)

entry_1 = Entry(root)
entry_1.pack()

entry_2 = Entry(root)
entry_2.pack()

op_var = StringVar(root)
op_var.set("+")
OptionMenu(root, op_var, "+", "-", "*", "/").pack()

label_result = Label(root, text="Результат: ")
label_result.pack()

def button_calk():
    try:
        num1 = float(entry_1.get())
        num2 = float(entry_2.get())
        operation = op_var.get()
        
        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "На ноль делить нельзя!")
                return
            res = num1 / num2
        
        label_result.config(text=f"Результат: {res}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

        

botton_calk = Button(root, text="0",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk.place(x=15, y=50)
botton_calk = Button(root, text="1",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="2",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="3",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="4",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="5",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="6",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="7",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="8",width=5, height=1, command=button_calk)
botton_calk.pack()
botton_calk = Button(root, text="9",width=5, height=1, command=button_calk)
botton_calk.pack()


root.mainloop()