from tkinter import *
from tkinter.ttk import Progressbar, Combobox  # Дополнительные модули для современных виджетов

# --- ИНИЦИАЛИЗАЦИЯ И НАСТРОЙКИ ОКНА ---
root = Tk()
root.title("Конспект по Tkinter")

# Настройка геометрии: размер 400x500, появление в точке X=140, Y=20
root.geometry("400x500+140+20")

# Запрет на изменение размеров окна (как указано в "Don.")
root.resizable(False, False)

# Установка минимального размера (на случай, если resizable будет True)
root.minsize(300, 300)


# --- ГРАФИЧЕСКИЕ ЭЛЕМЕНТЫ (ВИДЖЕТЫ) ---

# Label — Текст в окне
label = Label(root, text="Пример работы всех элементов:")
label.pack()

# Button — Кнопка
button = Button(root, text="Нажми меня")
button.pack()

# Entry — Однострочное поле ввода
entry = Entry(root)
entry.pack()

# Text — Многострочное поле ввода
text_area = Text(root, height=3, width=30)
text_area.pack()

# Listbox — Список
listbox = Listbox(root, height=3)
listbox.insert(1, "Элемент 1")
listbox.insert(2, "Элемент 2")
listbox.pack()

# Combobox — Выпадающий список
combo = Combobox(root, values=["Вариант А", "Вариант Б"])
combo.pack()

# Menu — Элемент меню (создается отдельно и привязывается к root)
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Меню", menu=file_menu)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Выход", command=root.quit)

# Scrollbar — Полоса прокрутки
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Progressbar — Шкала загрузки
progress = Progressbar(root, length=100, mode='determinate')
progress.pack()
progress['value'] = 50  # Установим для примера на 50%


# --- ЗАПУСК ПРИЛОЖЕНИЯ ---
# Метод mainloop всегда должен быть в самом конце
root.mainloop()