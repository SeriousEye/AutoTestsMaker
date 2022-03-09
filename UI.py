import re
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from os import path, makedirs, listdir, remove, rmdir
from turtle import pos
# from PIL import ImageGrab
# from functools import partial
import actions
import show_screenshot as ss
import screenshoter as scr
import get_config as gc
import action_buttons as ab
import json



class Example(Frame):
    row_count = 1
    # row_dict = {} # Словарь думаю не нужен, т.к. есть списко row_list актуальных позиций панелей из которого по порядку тянем действия
    row_list = [0]
    button_up = [0]
    button_down = [0]
    screenshots = [0]
    delete_widgets = [0]
    step_to_save = [0]
    screenshot_state = [0]

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
        # print(self.row_list[self.row_count-1])

    def delete_row(self, event):
        """Обработчик события при нажатии кнопки удаления панели. Также удаляет из списков соответствующие кнопки и основную панель."""
        caller = event.widget
        if caller in self.delete_widgets:
            position = self.delete_widgets.index(caller)
            # print(f"row_list - {self.row_list}\nbutton_up - {self.button_up}\nbutton_down - {self.button_down}\ndel_widget - {self.delete_widgets}")
            self.row_list.pop(position).delete_panel()
            self.button_up.pop(position).grid_forget()
            self.button_down.pop(position).grid_forget()
            self.delete_widgets.pop(position).grid_forget()

    def add_to_panel(self):
        """В окно добавляются кнопки вверх, вниз и удаление, также за каждой кнопкой закрепляется обработчик по нажатию кнопки"""
        self.btn_up = Button(self.parent, text=" ^ ")
        self.btn_up.bind("<1>", self.f)
        self.btn_up.grid(column=2, row=self.row_count, padx=(15, 2))
        self.button_up.append(self.btn_up)

        self.btn_down = Button(self.parent, text=" v ")
        self.btn_down.bind("<1>", self.f)
        self.btn_down.grid(column=3, row=self.row_count, padx=2)
        self.button_down.append(self.btn_down)

        self.btn_delete = Button(self.parent, text= "X", width=5)
        self.btn_delete.bind("<1>", self.delete_row)
        self.btn_delete.grid(column=4, row=self.row_count, padx=(20, 0))
        self.delete_widgets.append(self.btn_delete)

    def f(self, event):
        """Обработчик нажатия кнопки панели. Понимает, какая кнопка нажата и вызывает определенный метод, который меняет панели."""
        caller = event.widget
        if caller in self.button_up:
            position = self.button_up.index(caller)
        else:
            position = self.button_down.index(caller)
        if caller in self.button_up and position > 1:
            self.panels_up(position)

        if caller in self.button_down and position < (len(self.button_down) - 1):
            self.panels_down(position)

    def panels_up(self, position):
        """Определяем подрядок отключения, смены и включения панелей при нажатии кнопки вверх ' ^ ' """
        panel_current = self.row_list[position]
        panel_before = self.row_list[position - 1]

        btn_up_cur = self.button_up[position]
        btn_up_bef = self.button_up[position - 1]

        btn_down_cur = self.button_down[position]
        btn_down_bef = self.button_down[position - 1]

        del_wgt_cur = self.delete_widgets[position]
        del_wgt_bef = self.delete_widgets[position - 1]

        panel_before.grid_forget()
        btn_up_bef.grid_forget()
        btn_down_bef.grid_forget()
        del_wgt_bef.grid_forget()

        panel_current.grid_forget()
        btn_up_cur.grid_forget()
        btn_down_cur.grid_forget()
        del_wgt_cur.grid_forget()
        
        self.row_list[position - 1], self.row_list[position] = self.row_list[position], self.row_list[position - 1]
        self.button_up[position - 1], self.button_up[position] = self.button_up[position], self.button_up[position - 1]
        self.button_down[position - 1], self.button_down[position] = self.button_down[position], self.button_down[position - 1]
        self.delete_widgets[position - 1], self.delete_widgets[position] = self.delete_widgets[position], self.delete_widgets[position - 1]

        panel_before.grid(column=1, row=position, sticky=W)
        btn_up_bef.grid(column=2, row=position, padx=(15, 2))
        btn_down_bef.grid(column=3, row=position, padx=2)
        del_wgt_bef.grid(column=4, row=position, padx=(20, 0))

        panel_current.grid(column=1, row=position-1, sticky=W)
        btn_up_cur.grid(column=2, row=position-1, padx=(15, 2))
        btn_down_cur.grid(column=3, row=position-1, padx=2)
        del_wgt_cur.grid(column=4, row=position-1, padx=(20, 0))

    def panels_down(self, position):
        """Определяем подрядок отключения, смены и включения панелей при нажатии кнопки вниз ' v ' """
        panel_current = self.row_list[position]
        panel_after = self.row_list[position + 1]

        btn_up_cur = self.button_up[position]
        btn_up_aft = self.button_up[position + 1]

        btn_down_cur = self.button_down[position]
        btn_down_aft = self.button_down[position + 1]

        del_wgt_cur = self.delete_widgets[position]
        del_wgt_aft = self.delete_widgets[position + 1]

        panel_after.grid_forget()
        btn_up_aft.grid_forget()
        btn_down_aft.grid_forget()
        del_wgt_aft.grid_forget()

        panel_current.grid_forget()
        btn_up_cur.grid_forget()
        btn_down_cur.grid_forget()
        del_wgt_cur.grid_forget()

        self.row_list[position + 1], self.row_list[position] = self.row_list[position], self.row_list[position + 1]
        self.button_up[position + 1], self.button_up[position] = self.button_up[position], self.button_up[position + 1]
        self.button_down[position + 1], self.button_down[position] = self.button_down[position], self.button_down[position + 1]
        self.delete_widgets[position + 1], self.delete_widgets[position] = self.delete_widgets[position], self.delete_widgets[position + 1]

        panel_after.grid(column=1, row=position, sticky=W)
        btn_up_aft.grid(column=2, row=position, padx=(15, 2))
        btn_down_aft.grid(column=3, row=position, padx=2)
        del_wgt_aft.grid(column=4, row=position, padx=(20, 0))

        panel_current.grid(column=1, row=position+1, sticky=W)
        btn_up_cur.grid(column=2, row=position+1, padx=(15, 2))
        btn_down_cur.grid(column=3, row=position+1, padx=2)
        del_wgt_cur.grid(column=4, row=position+1, padx=(20, 0))

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
        """Выбор дериктории и задания названия файла для сохранения."""
        file_name = asksaveasfilename(
            filetypes=(("Python file", "*.py"),
                       ("All files", "*.*")    
            )
        )
        # Выполняется сохранение файла, если не нажата кнопка отмена и задано имя файла   
        if file_name:

            path_name = file_name.replace('/', '\\') if '/' in file_name else file_name

            all_files = listdir(path.split(path_name)[0])
            if path.split(path_name)[1] in all_files:
                remove(path_name)
                rmdir(path.splitext(path_name)[0])
            
            screenshot_folder = path.splitext(file_name)[0].replace('/', '\\')
            makedirs(screenshot_folder)


            with open(file_name, "w", encoding="utf-8")as wf:
                text_import = actions.Actions().turn_on_lib()
                wf.write(text_import)

                for act in self.row_list[1:]:
                    screen = act.screenshot_state.get()

                    wf.write(act.get_action())

                    """Если установлен флаг "скриншот", то делается снимок того экрана в которм находятся указанные координаты"""
                    if screen:
                        act.get_values()
                        filename = f"{act}".strip(".!")
                        second_name = self.row_list.index(act)
                        wx, hy = scr.ScreenShot().screen_resolution()
                        half_screen = int(wx/2)
                        left_region = (0, 0, 1920, 1080)
                        right_region = (half_screen, 0, half_screen, hy)

                        if act.choose_screen_state == 'Левый экран':
                            screen_resolution = actions.Actions().screenshot(region=left_region, name1=screenshot_folder, name2=f"Screen_step_{second_name}")
                            wf.write(screen_resolution)
                        elif act.choose_screen_state == 'Правый экран':
                            screen_resolution = actions.Actions().screenshot(region=right_region, name1=screenshot_folder, name2=f"Screen_step_{second_name}")
                            wf.write(screen_resolution)
                        # scr.ScreenShot().screen_size(x, y, path, file_name, path.basename(filename))

    def save_schema(self):
        filename = asksaveasfilename(
            filetypes=(("json file", "*.json"),
                       ("All files", "*.*")    
            )
        )
        if filename:
            self.step_to_save.clear()
            self.step_to_save.append(0)
            # print(path.basename(filename))
            for act in self.row_list[1:]:
                step = act.save_datas()
                self.step_to_save.append(step)

            # print(self.step_to_save)

            with open(filename, "w", encoding="utf-8")as wf:
                json.dump(self.step_to_save, wf)


    def load_file(self):
        filename = askopenfilename()
        if filename:
            with open(filename)as of:
                temp = json.load(of)
                for dic in temp[1:]:
                    for key, val in dic.items():
                        self.add_to_panel()
                        pan = ab.Panel()
                        pan.load_panel(key)
                        pan.set_values(x=val[0], 
                                       y=val[1],
                                       duration=val[2],
                                       button=val[3],
                                       clicks=val[4],
                                       interval=val[5],
                                       button_press=val[6],
                                       write_text=val[7],
                                       wait_time=val[8],
                                       scroll=val[9],
                                       screenshot_state=val[10],
                                       choose_screen_state=val[11])

                        pan.grid(column=1, row=self.row_count, sticky=W)
                        self.row_list.append(pan)
                        self.row_count += 1

    def buttons(self):
        btn_add = Button(master=self.menu_frame, text="Добавить", command=self.add_panel)
        btn_add.grid(column=0, row=0)

        # btn_screenshot = Button(master=self.menu_frame, text="Скриншот", command=ss.main)
        # btn_screenshot.grid(column=1, row=0)

        # btn_settings = Button(master=self.menu_frame, text="Настроить монитор", command=gc.getConfig().change_monitor_cfg())
        # btn_settings.grid(column=2, row=0)

        # btn_print = Button(master=self.menu_frame, text="Print", command=self.print_dict)
        # btn_print.grid(column=3, row=0)

        btn_save = Button(master=self.menu_frame, text="Сохранить тест", command=self.save_file)
        btn_save.grid(column=4, row=0)

        btn_save_schema = Button(master=self.menu_frame, text="Сохранить схему", command=self.save_schema)
        btn_save_schema.grid(column=5, row=0)

        btn_load = Button(master=self.menu_frame, text="Загрузить схему", command=self.load_file)
        btn_load.grid(column=6, row=0)


# Нужно доработать отображение(удаление) панели оберки в виде кнопок вверх и вниз

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class посмотреть все инстансы класса

# ПОРЯДОК ДОДЕЛКИ ПРИЛОЖЕНИЯ ДО СОСТОЯНИЯ РАБОЧЕГО!!! 
# READY 1. Сделать кнопку сохранения файла в определенную директорию и с указанием названия 
#   - https://pythonru.com/uroki/dialogovye-vsplyvajushhie-okna-tkinter-9 
#   - https://younglinux.info/tkinter/dialogbox
# READY 2. Допилить к панели, в виде флага включения, сохранение скриншота  после выполнения действия 
#   - https://pythonru.com/uroki/polja-vybora-znachenij-tkinter-3 
#   - https://younglinux.info/tkinter/variable
# READY 2.5 Допилить удаление кнопок вверх/вниз после удаления панели!!! 
# 3. Добавить действий из puautogui https://pyautogui.readthedocs.io/en/latest/
# READY 4. Нужно сделать возможность загрузки файла автотеста в программу, чтобы была возможность редактировать.
# READY 4.5 Нужно чтобы дописывалось сохранение скриншота после выполнения действия, при установленном чек-боксе
# 5. Написать мини-программу для последовательного запуска файлов автотестов с возможностью выбора стенда для запуска и сверки с эталонами 
# 6. Сделать через декораторы или в самих методах, чтобы подсвечивалось поле или нельзя было ввести не валидное значение. https://pythonru.com/uroki/sozdanie-izmenenie-i-proverka-teksta-tkinter-2
#    или обернуть в try/except, там где может быть ошибка. Или сделать так, чтобы кнопку Сохранить нельзя было нажать пока в поле 
#    не валидное значение
# 6.5 Сделать полосу прокрутки для основного окна
# 7. Сделать логирование (чтобы можно было отлавливать ошибки)
# 8. Рефакторинг/оптимизация кода и добавление комментов к методам.




# def main():
if __name__ == '__main__':
    root = Tk()
    root.geometry("+300+300")
    app = Example(root)
    root.mainloop()  
 
# if __name__ == '__main__':
#     main()