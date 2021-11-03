# from tkinter import *
# from pyautogui import *

# class Panel(Frame):
#     def __init__(self):
#         Frame.__init__(self)   
#         self.buttons()

#     def buttons(self):
#         frame = Frame(self, borderwidth=1)
#         frame.pack()
#         btn_action = Button(self, text="Выберите действие")
#         btn_action.pack(side=RIGHT)

#         btn_bed_result = Button(self, text="Фактический результат")
#         btn_bed_result.pack(side=RIGHT, padx=5)

#         btn_good_result = Button(self, text="Ожидаемый результат")
#         btn_good_result.pack(side=RIGHT, padx=5)

        
# def main():
#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Panel()
#     root.mainloop()  
 
# if __name__ == '__main__':
#     main()

from tkinter import Label, Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from collections import defaultdict
import weakref


class KeepRefs(object):
    __refs__ = defaultdict(list)
    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class Counter():

    def __init__(self):
        self.counter = 1

    def inctrement_count(self):
        self.counter +=1

class Panel(Frame, KeepRefs):
    counter = 1
 
    def __init__(self):
        super(Panel, self).__init__()
        self.count = Counter()
        self.initUI()
        
    def inc_count(self):
        self.count.inctrement_count()
    
    # def but(self):
    #     self.btn_create = Button(self.parent, text="Добавить", command=self.initUI)
    #     self.btn_create.pack()
 
    def initUI(self):
        # self.master.title("Кнопки в kinter")
        # self.style = Style()
        # self.style.theme_use("default")
 
        # frame = Frame(self, relief=RAISED, borderwidth=1)
        # frame.pack(fill=BOTH, expand=True)
 
        self.pack(fill=BOTH, expand=True)
 
        # closeButton = Button(self, text="Закрыть")
        # closeButton.pack(side=RIGHT, padx=5, pady=5)
        # okButton = Button(self, text="Готово")
        # okButton.pack(side=RIGHT)
        btn_action = Button(self, text="Выберите действие")
        btn_action.pack(side=RIGHT, expand=True)

        btn_bed_result = Button(self, text="Фактический результат")
        btn_bed_result.pack(side=RIGHT, padx=5, expand=True)

        btn_good_result = Button(self, text="Ожидаемый результат")
        btn_good_result.pack(side=RIGHT, padx=5, expand=True)

        btn_del = Button(self, text="Удаляшечки", command=self.destroy)
        btn_del.pack(side=RIGHT, padx=5, expand=True)

        btn_print = Button(self, text="Print", command=self.print_inst)
        btn_print.pack(side=RIGHT, padx=5, expand=True)

        lbl_count = Label(self, text=f"{self.counter}")
        lbl_count.pack(side=RIGHT, padx=5, expand=True)

        self.inc_count()

    def print_inst(self):
        print(Panel.get_instances())
        for i in Panel.get_instances():
            print(i)

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class получить все инстансы класса

# def main():
 
#     root = Tk()
#     root.geometry("+300+300")
#     app = Panel("a")
#     app1 = Panel("b")
#     app2 = Panel("c")
#     root.mainloop()
 
 
# if __name__ == '__main__':
#     main()
#     for i in Panel.get_instances():
#         print(i)