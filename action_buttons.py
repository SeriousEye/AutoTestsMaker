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
#         btn_action.pack(side=LEFT)

#         btn_bed_result = Button(self, text="Фактический результат")
#         btn_bed_result.pack(side=LEFT, padx=5)

#         btn_good_result = Button(self, text="Ожидаемый результат")
#         btn_good_result.pack(side=LEFT, padx=5)

        
# def main():
#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Panel()
#     root.mainloop()  
 
# if __name__ == '__main__':
#     main()

from tkinter import Label, Tk, LEFT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style, Combobox, Entry
from collections import defaultdict
import UI
import weakref
import actions


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

    def print_counter(self):
        print(self.counter)

class Panel(Frame, KeepRefs):
    act = ''
    counter = 1
    tot_text = []
 
    def __init__(self):
        super(Panel, self).__init__()
        # self.count = Counter().counter
        # print(self.count)
        # self.value = value
        self.initUI()

        
    def inc_count(self):
        self.count.inctrement_count()
    
    # def but(self):
    #     self.btn_create = Button(self.parent, text="Добавить", command=self.initUI)
    #     self.btn_create.pack()

    # def print_id(self, visible=False):
    #     if visible:
    #         print("")
    #     else:
    #         print(f"I'm object id: {id(self)}")
    def start_text(self):
        self.tot_text.append(actions.Actions().turn_on_lib())

    def add_action(self):
        text = self.combo_action.get()
        # print(f"text - {text}")
        text = actions.Actions().all_actions[text]
        return text

    def get_action(self):
        text = self.combo_action.get()
        action_text = actions.Actions().all_actions[text]
        return action_text

    def no_text(self):
        self.tot_text = "блок удален"
        
    def instance_id(self):
        return id(self)

    def return_values(self):
        # self.print_id(visible=True)
        self.no_text()
        self.destroy()

    # def panel_standart(self):
    #     self.pack(fill=BOTH, expand=True)
 
    #     lbl_action = Label(self, text="Выберите действие")
    #     lbl_action.pack(side=LEFT, padx=1, expand=True)

    #     self.combo_action = Combobox(self)
    #     self.combo_action['values'] = [act for act in actions.Actions().all_actions]
    #     self.combo_action.current(0)
    #     self.combo_action.pack(side=LEFT, padx=5, expand=True)

    #     btn_bed_result = Button(self, text="Фактический результат")
    #     btn_bed_result.pack(side=LEFT, padx=5, expand=True)

    #     btn_good_result = Button(self, text="Ожидаемый результат")
    #     btn_good_result.pack(side=LEFT, padx=5, expand=True)

    #     btn_del = Button(self, text="Удаляшечки", command=self.return_values)
    #     btn_del.pack(side=LEFT, padx=5, expand=True)

    #     btn_print = Button(self, text="Print", command=self.get_action)
    #     btn_print.pack(side=LEFT, padx=5, expand=True)


    def panel_three(self, action):
        self.pack(fill=BOTH, expand=True)

        lbl_action = Label(self, text="Выберите действие")
        lbl_action.pack(side=LEFT, padx=1, expand=True)

        self.combo_action = Combobox(self)
        self.combo_action['values'] = action
        self.combo_action.current(0)
        self.combo_action.pack(side=LEFT, padx=5, expand=True)

        lbl_x = Label(self, text="x:")
        lbl_x.pack(side=LEFT)
        ent_x = Entry(self, width=4)
        ent_x.pack(side=LEFT, padx=2)

        lbl_y = Label(self, text="y:")
        lbl_y.pack(side=LEFT)
        ent_y = Entry(self, width=4)
        ent_y.pack(side=LEFT, padx=2)

        lbl_duration = Label(self, text="Задержка")
        lbl_duration.pack(side=LEFT)
        ent_duration = Entry(self, width=2)
        ent_duration.pack(side=LEFT)

    def panel_four(self, action):
        self.pack(fill=BOTH, expand=True)

        lbl_action = Label(self, text="Выберите действие")
        lbl_action.pack(side=LEFT, padx=1, expand=True)

        self.combo_action = Combobox(self)
        self.combo_action['values'] = action
        self.combo_action.current(0)
        self.combo_action.pack(side=LEFT, padx=5, expand=True)

        lbl_x = Label(self, text="x:")
        lbl_x.pack(side=LEFT)
        ent_x = Entry(self, width=4)
        ent_x.pack(side=LEFT, padx=2)

        lbl_y = Label(self, text="y:")
        lbl_y.pack(side=LEFT)
        ent_y = Entry(self, width=4)
        ent_y.pack(side=LEFT, padx=2)

        lbl_duration = Label(self, text="Задержка")
        lbl_duration.pack(side=LEFT)
        ent_duration = Entry(self, width=2)
        ent_duration.pack(side=LEFT)

        lbl_button = Label(self, text="Клавиша")
        lbl_button.pack(side=LEFT)
        combo_action = Combobox(self)
        combo_action['values'] = ["Левая кнопка", "Средняя кнопка", "Правая кнопка"]
        combo_action.current(0)
        combo_action.pack(side=LEFT, padx=5, expand=True)

    def panel_five(self, action):
        pass
 
    def initUI(self):
        # !!!выбор действия перенести на основную панель и убрать из добавляющейся
        # действие можно добавить из основной панели в самый низ и из добавляющейся 
        # новую строку под неё 
        if self.act == '':
            self.pack(fill=BOTH, expand=True)

            lbl_action = Label(self, text="Выберите действие")
            lbl_action.pack(side=LEFT, padx=1, expand=True)

            self.combo_action = Combobox(self)
            self.combo_action['values'] = [act for act in actions.Actions().all_actions]
            # self.combo_action.current(0)
            self.combo_action.pack(side=LEFT, padx=5, expand=True)

            self.act = self.combo_action.get()
            self.update()

            # print(self.act)
            self.after(100, self.initUI())

        elif self.act == "Переместить курсор":
            # self.destroy()
            self.pack(fill=BOTH, expand=True)
            # print("PK")
            self.panel_three("Переместить курсор")
            self.act = self.combo_action.get()
            self.after(100, self.initUI())

        elif self.act == "Перетащить мышью":
            self.pack(fill=BOTH, expand=True)
            # print("DM")
            self.panel_three("Перетащить мышью")
            self.act = self.combo_action.get()
            self.after(100, self.initUI())

        # else:
        #     print("2")
        #     btn_bed_result = Button(self, text="Фактический результат")
        #     btn_bed_result.pack(side=LEFT, padx=5, expand=True)

        #     btn_good_result = Button(self, text="Ожидаемый результат")
        #     btn_good_result.pack(side=LEFT, padx=5, expand=True)

        #     btn_del = Button(self, text="Удаляшечки", command=self.return_values)
        #     btn_del.pack(side=LEFT, padx=5, expand=True)

        #     btn_print = Button(self, text="Print", command=self.get_action)
        #     btn_print.pack(side=LEFT, padx=5, expand=True)

        # self.update()

    # нужно описать условие для отображения панели и в конце self.update чтобы панель обновлялась

        


    def print_inst(self):
        print(Panel.get_instances())
        for i in Panel.get_instances():
            print(i)

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class получить все инстансы класса
# https://pythonru.com/primery/primery-raboty-s-klassami-v-python
# https://ru.stackoverflow.com/questions/1053678/%D0%9A%D0%B0%D0%BA-%D1%83%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0-%D0%B8%D0%B7-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%BE%D0%B1%D1%8C%D0%B5%D0%BA%D1%82%D0%BE%D0%B2-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0-python


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