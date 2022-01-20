from tkinter import *
from pyautogui import *
from tkinter.filedialog import askopenfilenames

class Panel(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.button_frame = Frame(master=parent)
        self.button_frame.grid(column=0, row=0, sticky=W, pady=(0, 10))

        self.files_frame = Frame(master=parent)
        self.files_frame.grid(column=0, row=1)
        self.parent = parent
        # self.initUI()
        self.buttons()

    def choose_file(self):
        pass

    def buttons(self):
        frame = Frame(self, borderwidth=1)
        frame.pack()
        btn_action = Button(self.button_frame, text="Выберите файл", command=self.choose_file)
        btn_action.grid(column=0, row = 0)

        # btn_bed_result = Button(self, text="Фактический результат")
        # btn_bed_result.pack(side=LEFT, padx=5)

        # btn_good_result = Button(self, text="Ожидаемый результат")
        # btn_good_result.pack(side=LEFT, padx=5)

        files_field = Text(self.files_frame, width=50, height=20)
        files_field.grid(column=0, row=0)

        
def main():
    root = Tk()
    root.geometry("+300+300")
    app = Panel(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()


# import re
# import tkinter as tk

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.pattern = re.compile("\d{0,4}$")
#         self.label = tk.Label(self, text="Введите логин")
#         vcmd = (self.register(self.validate_username), "%i", "%P")
#         self.entry = tk.Entry(self, validate="key",
#                               validatecommand=vcmd,
#                               invalidcommand=self.print_error)
#         self.label.pack()
#         self.entry.pack(anchor=tk.W, padx=10, pady=10)

#     def validate_username(self, index, username):
#         print("Проверка символа" + index)
#         return self.pattern.match(username) is not None

#     def print_error(self):
#         print("Запрещенный символ в логине")

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # https://pythonru.com/uroki/sozdanie-izmenenie-i-proverka-teksta-tkinter-2
# # https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python