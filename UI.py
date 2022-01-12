from tkinter import *
import actions
import show_screenshot as ss
import get_config as gc
import action_buttons as ab



class Example(Frame):
    row_count = 1
    # row_dict = {} # Словарь думаю не нужен, т.к. есть списко row_list актуальных позиций панелей из которого по порядку тянем действия
    row_list = [0]
    button_up = [0]
    button_down = [0]

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.menu_frame = Frame(master=parent)
        self.menu_frame.grid(column=1, row=0, sticky=W, pady=(0, 20))
        self.parent = parent
        # self.initUI()
        self.buttons()

    def add_panel(self):
        self.add_to_panel()
        pan = ab.Panel()
        pan.grid(column=1, row=self.row_count, sticky=W)
        self.row_list.append(pan)
        self.row_count += 1

    def add_to_panel(self):
        self.btn_up = Button(self.parent, text="^")
        self.btn_up.bind("<1>", self.f)
        self.btn_up.grid(column=2, row=self.row_count)
        self.button_up.append(self.btn_up)

        self.btn_down = Button(self.parent, text="v")
        self.btn_down.bind("<1>", self.f)
        self.btn_down.grid(column=3, row=self.row_count)
        self.button_down.append(self.btn_down)

    def panels_up(self, position):
        panel_current = self.row_list[position]
        panel_before = self.row_list[position-1]

        btn_up_cur = self.button_up[position]
        btn_up_bef = self.button_up[position-1]

        btn_down_cur = self.button_down[position]
        btn_down_bef = self.button_down[position-1]

        panel_before.grid_forget()
        btn_up_bef.grid_forget()
        btn_down_bef.grid_forget()
        panel_current.grid_forget()
        btn_up_cur.grid_forget()
        btn_down_cur.grid_forget()

        self.row_list[position - 1], self.row_list[position] = self.row_list[position], self.row_list[position - 1]
        self.button_up[position - 1], self.button_up[position] = self.button_up[position], self.button_up[position - 1]
        self.button_down[position - 1], self.button_down[position] = self.button_down[position], self.button_down[position - 1]

        panel_before.grid(column=1, row=position, sticky=W)
        btn_up_bef.grid(column=2, row=position)
        btn_down_bef.grid(column=3, row=position)
        panel_current.grid(column=1, row=position-1, sticky=W)
        btn_up_cur.grid(column=2, row=position-1)
        btn_down_cur.grid(column=3, row=position-1)

    def panels_down(self, position):
        panel_current = self.row_list[position]
        panel_after = self.row_list[position+1]

        btn_up_cur = self.button_up[position]
        btn_up_aft = self.button_up[position+1]

        btn_down_cur = self.button_down[position]
        btn_down_aft = self.button_down[position+1]

        panel_after.grid_forget()
        btn_up_aft.grid_forget()
        btn_down_aft.grid_forget()
        panel_current.grid_forget()
        btn_up_cur.grid_forget()
        btn_down_cur.grid_forget()

        self.row_list[position + 1], self.row_list[position] = self.row_list[position], self.row_list[position + 1]
        self.button_up[position + 1], self.button_up[position] = self.button_up[position], self.button_up[position + 1]
        self.button_down[position + 1], self.button_down[position] = self.button_down[position], self.button_down[position + 1]

        panel_after.grid(column=1, row=position, sticky=W)
        btn_up_aft.grid(column=2, row=position)
        btn_down_aft.grid(column=3, row=position)
        panel_current.grid(column=1, row=position+1, sticky=W)
        btn_up_cur.grid(column=2, row=position+1)
        btn_down_cur.grid(column=3, row=position+1)

    def f(self, event):
        caller = event.widget
        if caller in self.button_up:
            position = self.button_up.index(caller)
        else:
            position = self.button_down.index(caller)
        if caller in self.button_up and position > 1:
            self.panels_up(position)

        if caller in self.button_down and position < (len(self.button_down) - 1):
            self.panels_down(position)

    # def all_obj(self):
    #     """Словарь строк очищается от экземпляров удаленных панелей."""
    #     temp_row_dict = self.row_dict.copy()
    #     for act in temp_row_dict:
    #         if act.state_delete == 0:
    #             self.row_dict[act] = act.get_action()
    #         else:
    #             del self.row_dict[act]

    def initUI(self):
        self.parent.title("Simple")
        # self.pack(fill=BOTH, expand=1)

    def print_dict(self):
        # temp_row_dict = self.row_dict.copy()
        # for act in temp_row_dict:
        #     if act.state_delete == 0:
        #         self.row_dict[act] = act.get_action()
        #     else:
        #         del self.row_dict[act]
        print(self.row_list)

    def save_file(self):
        # self.all_obj()
        with open("test_save.py", "w", encoding="utf-8")as wf:
            text_import = actions.Actions().turn_on_lib()
            wf.write(text_import)
            for act in self.row_list[1:]:
                wf.write(act.get_action())

    def buttons(self):
        btn_add = Button(master=self.menu_frame, text="Добавить", command=self.add_panel)
        btn_add.grid(column=0, row=0)

        btn_screenshot = Button(master=self.menu_frame, text="Скриншот", command=ss.main)
        btn_screenshot.grid(column=1, row=0)

        btn_settings = Button(master=self.menu_frame, text="Настроить монитор", command=gc.getConfig().change_monitor_cfg())
        btn_settings.grid(column=2, row=0)

        btn_print = Button(master=self.menu_frame, text="Print", command=self.print_dict)
        btn_print.grid(column=3, row=0)

        btn_save = Button(master=self.menu_frame, text="Сохранить", command=self.save_file)
        btn_save.grid(column=4, row=0)

# Нужно доработать отображение(удаление) панели оберки в виде кнопок вверх и вниз

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class посмотреть все инстансы класса

# ПОРЯДОК ДОДЕЛКИ ПРИЛОЖЕНИЯ ДО СОСТОЯНИЯ РАБОЧЕГО!!! 
# 1. Сделать кнопку сохранения файла в определенную директорию и с указанием названия 
#   - https://pythonru.com/uroki/dialogovye-vsplyvajushhie-okna-tkinter-9 
#   - https://younglinux.info/tkinter/dialogbox
# 2. Допилить к панели, в виде флага включения, сохранение скриншота  после выполнения действия 
#   - https://pythonru.com/uroki/polja-vybora-znachenij-tkinter-3 
#   - https://younglinux.info/tkinter/variable
# 3. Добавить действий из puautogui https://pyautogui.readthedocs.io/en/latest/
# 4. Написать мини-программу для последовательного запуска файлов автотестов с возможностью выбора стенда для запуска и сверки с эталонами 
# 5. Рефакторинг/оптимизация кода и добавление комментов к методам.




# def main():
if __name__ == '__main__':
    root = Tk()
    root.geometry("+300+300")
    app = Example(root)
    root.mainloop()  
 
# if __name__ == '__main__':
#     main()