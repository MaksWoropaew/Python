from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import log
import function as func
import check

 
 
def save():
    '''
    обрабатывается нажатие кнопки "Сохранить"
    '''
    list_of_data = []
    list_of_data.append(entry_f.get()) # Фамилия
    list_of_data.append(entry_n.get()) # Имя
    list_of_data.append(entry_o.get()) # Отчество
    list_of_data.append(entry_tel.get()) # Телефон
    list_of_data.append(entry_about.get()) # Описание
    log.logger(f"Создали список списков из новых значений {list_of_data}", " ")
    err=0
    new_string = check.check_telephone_number(list_of_data[3])
    if new_string == '':
        print(list_of_data[3])
        entry_tel.delete(0, END)
        entry_tel.insert(0, f'?'+list_of_data[3]+'?') 
        
        err=1
    else:
        list_of_data[3] = new_string

    new_string = check.check_fio(list_of_data[0])
    if new_string == '':
        entry_f.delete(0, END)
        entry_f.insert(0, f'?'+list_of_data[0]+'?')      
        
        err=1
    else:
        list_of_data[0] = new_string
        entry_f.delete(0, END)
        entry_f.insert(0, new_string)
        
    new_string = check.check_fio(list_of_data[1])
    if new_string == '':
        entry_n.delete(0, END)
        entry_n.insert(0, f'?'+list_of_data[1]+'?')      
        
        err=1
    else:
        list_of_data[1] = new_string
        entry_n.delete(0, END)
        entry_n.insert(0, new_string)

    new_string = check.check_fio(list_of_data[2])
    if new_string == '':
        entry_o.delete(0, END)
        entry_o.insert(0, f'?'+list_of_data[2]+'?')      
        
        err=1
    else:
        list_of_data[2] = new_string
        entry_o.delete(0, END)
        entry_o.insert(0, new_string)

    if err == 0:
        log.logger("Записываем их в файл", "Все удовлетворяет требованиям")
        file_exp = drop_down.get()
        if file_exp=='txt':
            func.imp(list_of_data)
        elif file_exp=='csv':
            func.write_csv(list_of_data)
        elif file_exp=='json':
            func.write_json(list_of_data)
        
        entry_f.delete(0, END)
        entry_n.delete(0, END)
        entry_o.delete(0, END)
        entry_tel.delete(0, END)
        entry_about.delete(0, END)
        messagebox.showinfo('Сохранение','Данные сохранены')
    else:
        log.logger(f"Данные введены с ошибками {list_of_data}", "Нужно перезаполнить")

    # print(list_of_data)
    
def show():
    '''
    обрабатывается нажатие кнопки "Показать базу". В переменной текст должен быть список списков
    '''
    file_exp = drop_down.get()
    if file_exp=='txt':
        result = func.read_base()
    elif file_exp=='csv':
        result = func.read_csv()
    elif file_exp=='json':
        result = func.read_json() 
    
    log.logger(f"База данных из файла {file_exp}", "Отобразили")
    # print(file_exp)
    # print(result)

    class Table:
        def __init__(self,root):
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='blue', font=('Arial', 10, 'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
    lst=result    
    total_rows = len(lst)
    total_columns = len(lst[0])
    root = Tk()
    root.title(f"База данных из файла {file_exp}")
    t = Table(root)
    root.mainloop()  

def selected(event):
    '''
    Функция получает выделенный объект из Combobox (выпадающего списка файловых расширений)
    '''
    global file_exp
    file_exp = drop_down.get()    

def find():
    '''
    обрабатывается нажатие кнопки "Найти"
    '''
    # переменная для поиска 
    
    text, result = func.exp(entry_search.get())
    log.logger(f"Ищем запись {text}", "")
    if result != "Данные отсутсвуют":
        entry_f.insert(0, result[0])
        entry_n.insert(0, result[1])
        entry_o.insert(0, result[2])
        entry_tel.insert(0, result[3])
        entry_about.insert(0, result[4])
        log.logger(f"Запись {text} нашлась", "Все отобразилось")
    else:
        log.logger(f"Записи {text} нет", "")
        messagebox.showinfo('Поиск','Такой строки нет')


root = Tk()

root.title('Телефонный справочник')

title = Label(root, text = 'Телефонный справочник')
title.configure(font = ('arial', 10, 'bold')) 
title.grid(row = 0, column = 0, columnspan = 4)

hint = Label(root, text = 'Фамилия:')
hint.grid(row = 1, column = 0, ipadx=10, pady =10) 
entry_f = Entry(root)
entry_f.grid(row = 1, column = 1,columnspan = 1, ipadx=40, pady =10, sticky= W)

hint = Label(root, text = 'Имя:')
hint.grid(row = 2, column = 0, ipadx=0, pady =10)
entry_n = Entry(root)
entry_n.grid(row = 2, column = 1, columnspan = 1, ipadx=40, pady =10, sticky= W)

hint = Label(root, text = 'Отчество:')
hint.grid(row = 3, column = 0, ipadx=10, pady =5)
entry_o = Entry(root)
entry_o.grid(row = 3, column = 1, columnspan = 1, ipadx=40, pady =5, sticky= W)

hint = Label(root, text = 'Телефон:')
hint.grid(row = 4, column = 0, ipadx=10, pady =10)
entry_tel = Entry(root)
entry_tel.grid(row = 4, column = 1, ipadx=10, pady =10, sticky= W)

hint = Label(root, text = 'Описание:')
hint.grid(row = 5, column = 0, ipadx=10, pady =10)
entry_about = Entry(root)
entry_about.grid(row = 5, column = 1, ipadx=40, pady =10, sticky= W)

but_search = Button(root, text = 'Найти', command = find)
but_search.grid(row = 7, column = 2, columnspan = 1, ipadx=10, pady =10)
entry_search = Entry(root)
entry_search.grid(row = 7, column = 0, columnspan = 2, ipadx=100, padx=10, pady =10, sticky=W)

but_save = Button(root, text = 'Сохранить', command=save)
but_save.grid(row = 8, column = 0, padx = 0, ipadx=10, pady =10)

but_show = Button(root, text = 'Показать базу', command=show)
but_show.grid(row = 8, column = 1, padx = 0, ipadx=10, pady =10)

but_exit = Button(root, text = 'Выход', command=exit)
but_exit.grid(row = 8, column = 2, ipadx=10, padx=10, pady =10)

level_list = ['txt', 'csv'] # , 'json'
file_exp = StringVar(value=level_list[1])
drop_down = ttk.Combobox(root, textvariable = file_exp, values = level_list, state="readonly")
drop_down.grid(row = 9, column = 1, columnspan=1, padx=10, pady=10)
drop_down.bind("<<ComboboxSelected>>", selected)


root.mainloop()