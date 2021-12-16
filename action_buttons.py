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

from tkinter import Label, Tk, LEFT, BOTH, RAISED, Canvas, END, E, W, N, S
from tkinter.ttk import Frame, Button, Style, Combobox, Entry
from collections import defaultdict
from pyautogui import position, press
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
    tot_text = []
    all_args = {}

    all_commands = {
        "ent_x": 1,
        "ent_y": 1,
        "duration": 1,
        "button": 1,
        "clicks": 1,
        "interval": 1,
        "write_text": 1,
        "press_button": 1,
        "wait_time": 1
    }

    action_dict = {
        "Левая кнопка": 'left',
        "Средняя кнопка": 'middle',
        "Правая кнопка": 'right',
        "1": 1,
        "2": 2,
        "3": 3
    }

    buttons = [
        'enter', 'space', 'escape', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
        ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
        'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
        'browserback', 'browserfavorites', 'browserforward', 'browserhome',
        'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
        'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
        'divide', 'down', 'end', 'esc', 'execute', 'f1', 'f10',
        'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
        'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
        'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
        'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
        'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
        'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
        'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
        'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
        'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab',
        'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
        'command', 'option', 'optionleft', 'optionright'
    ]
    
 
    def __init__(self):
        super(Panel, self).__init__()
        # self.count = Counter().counter
        # print(self.count)
        # self.value = value
        self.state_delete = 0
        self.x = 0
        self.y = 0
        self.duration = 0
        self.button = 'left'
        self.clicks = 0
        self.interval = 0
        self.press_button = "enter"
        self.write_text = ""
        self.wait_time = 1
        self.initUI()
        self.bind("<KeyPress>", self.insert_coords)
        
    def inc_count(self):
        self.count.inctrement_count()
    
    def start_text(self):
        self.tot_text.append(actions.Actions().turn_on_lib())

    def add_action(self):
        text = self.combo_action.get()
        # text = actions.Actions().all_actions[text]
        return text

    def delete_panel(self):
        """Удаление текущей панели."""
        self.state_delete = 1
        self.destroy()

    def get_action(self):
        text = self.combo_action.get()
        act  = actions.Actions()
        # action_text = actions.Actions().all_actions[text]
        self.get_values()
        if text == "Переместить курсор":
            return act.move_mouse(x=self.x, y=self.y, duration=self.duration)
        elif text == "Перетащить мышью":
            return act.drag_mouse(x=self.x, y=self.y, duration=self.duration, button=self.button)
        elif text == "Клик мыши":
            return act.click_mouse(x=self.x, y=self.y, button=self.button, clicks=self.clicks, interval=self.interval)
        elif text == "Двойной клик":
            return act.doubleclick_mouse(x=self.x, y=self.y, button=self.button, interval=self.interval)
        elif text == "Ввести текст":
            return act.write_text(text=self.write_text, interval=self.interval)
        elif text == "Нажать клавишу":
            return act.press_button(name_button=self.press_button)
        elif text == "Ждать":
            return act.wait_time(wait=self.wait_time)
        else:
            pass

    def text_to_value(self, dict_value):
        action_list = ["Левая кнопка", "Средняя кнопка", "Правая кнопка", "1", "2", "3"]
        for action in action_list:
            if action == dict_value and action not in "0123456789":
                return self.action_dict[action]
            elif action in "0123456789":
                return self.action_dict[action]

    def get_values(self):
        """Забираются значения из полей, комбобоксов и др."""
        self.x = self.ent_x.get()
        self.y = self.ent_y.get()
        self.duration = self.ent_duration.get()
        self.button = self.text_to_value(self.combo_buttons.get())
        self.clicks = self.combo_clicks.get()
        self.interval = self.ent_interval.get()
        self.write_text = self.ent_write_text.get()
        self.press_button = self.combo_press_button.get()
        self.wait_time = self.ent_wait_time.get()

    def set_command(self, x=None, y=None, duration=None, button=None, clicks=None, interval=None, write_text=None, button_press=None, wait_time=None):
        """
        Нужно добавлять значение для атрибутов в виде кортежа (a, b)
        где a - это ключ словаря all_commands, b - значение 0 или 1,
        т.е. включено или выключено        
        """
        # НУЖНО ПЕРЕДЕЛАТЬ!!!

        tot_list = [x, y, duration, button, clicks, interval, write_text, button_press, wait_time]
        for elem in tot_list:
            if elem:
                self.all_commands[elem[0]] = elem[1]

    def get_coord(self):
        """Возвращает координаты курсора мыши."""
        x, y = position()
        return x, y

    def insert_coords(self, arg):
        """Помещаются координаты курсора в поля x и y"""
        self.ent_x.delete(0, END)
        self.ent_y.delete(0, END)
        x, y = self.get_coord()
        self.ent_x.insert(0, x)
        self.ent_y.insert(0, y)

    def panel_x(self, value):
        if value:
            self.lbl_x.grid(column=6, row=1)
            self.ent_x.grid(column=7, row=1)
        else:
            self.lbl_x.grid_forget()
            self.ent_x.grid_forget()

    def panel_y(self, value):
        if value:
            self.lbl_y.grid(column=8, row=1)
            self.ent_y.grid(column=9, row=1)
        else:
            self.lbl_y.grid_forget()
            self.ent_y.grid_forget()

    def panel_duration(self, value):
        if value:
            self.lbl_duration.grid(column=10, row=1)
            self.ent_duration.grid(column=11, row=1)
        else:
            self.lbl_duration.grid_forget()
            self.ent_duration.grid_forget()

    def panel_button(self, value):
        if value:
            self.combo_buttons.grid(column=12, row=1)
            self.combo_buttons.grid(column=13, row=1)
        else:
            self.combo_buttons.grid_forget()
            self.combo_buttons.grid_forget()
    
    def panel_clicks(self, value):
        if value:
            self.combo_clicks.grid(column=14, row=1)
            self.combo_clicks.grid(column=15, row=1)
        else:
            self.combo_clicks.grid_forget()
            self.combo_clicks.grid_forget()
    
    def panel_interval(self, value):
        if value:
            self.lbl_interval.grid(column=16, row=1)
            self.ent_interval.grid(column=17, row=1)
        else:
            self.lbl_interval.grid_forget()
            self.ent_interval.grid_forget()

    def panel_w_text(self, value):
        if value:
            self.ent_write_text.grid(column=18, row=1)
        else:
            self.ent_write_text.grid_forget()

    def panel_p_button(self, value):
        if value:
            self.lbl_press.grid(column=19, row=1)
            self.combo_press_button.grid(column=20, row=1)
        else:
            self.lbl_press.grid_forget()
            self.combo_press_button.grid_forget()

    def panel_w_time(self, value):
        if value:
            self.lbl_wait_time.grid(column=21, row=1)
            self.ent_wait_time.grid(column=22, row=1)
        else:
            self.lbl_wait_time.grid_forget()
            self.ent_wait_time.grid_forget()           

    def on_off(self):
        """Включает или выключает виджеты в соответствии с параметрами словаря all_commands"""

        # self.lbl_action.pack()
        # self.combo_action.pack()
        # self.btn_refresh.pack()
        for command in self.all_commands:
            if command == "ent_x":
                self.panel_x(self.all_commands[command])
            elif command == "ent_y":
                self.panel_y(self.all_commands[command])
            elif command == "duration":
                self.panel_duration(self.all_commands[command])
            elif command == "button":
                self.panel_button(self.all_commands[command])
            elif command == "clicks":
                self.panel_clicks(self.all_commands[command])
            elif command == "interval":
                self.panel_interval(self.all_commands[command])
            elif command == "write_text":
                self.panel_w_text(self.all_commands[command])
            elif command == "press_button":
                self.panel_p_button(self.all_commands[command])
            elif command == "wait_time":
                self.panel_w_time(self.all_commands[command])

    def show_panel_widgets(self):
        self.set_command(
            x=("ent_x", 0),
            y=("ent_y", 0),
            duration=("duration", 0),
            button=("button", 0),
            clicks=("clicks", 0),
            interval=("interval", 0),
            write_text=("write_text", 0),
            button_press=("press_button", 0),
            wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_move_mouse(self):
        self.show_panel_widgets()
        self.set_command(
            x=("ent_x", 1),
            y=("ent_y", 1),
            duration=("duration", 1)
            # button=("button", 0),
            # clicks=("clicks", 0),
            # interval=("interval", 0),
            # write_text=("write_text", 0),
            # button_press=("press_button", 0),
            # wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_drag_mouse(self):
        self.show_panel_widgets()
        self.set_command(
            x=("ent_x", 1),
            y=("ent_y", 1),
            duration=("duration", 1),
            button=("button", 1)
            # clicks=("clicks", 0),
            # interval=("interval", 0),
            # write_text=("write_text", 0),
            # button_press=("press_button", 0),
            # wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_click_mouse(self):
        self.show_panel_widgets()
        self.set_command(
            x=("ent_x", 1),
            y=("ent_y", 1),
            # duration=("duration", 0),
            button=("button", 1),
            clicks=("clicks", 1),
            interval=("interval", 1)
            # write_text=("write_text", 0),
            # button_press=("press_button", 0),
            # wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_doubleclick_mouse(self):
        self.show_panel_widgets()
        self.set_command(
            x=("ent_x", 1),
            y=("ent_y", 1),
            # duration=("duration", 0),
            button=("button", 1),
            # clicks=("clicks", 0),
            interval=("interval", 1)
            # write_text=("write_text", 0),
            # button_press=("press_button", 0),
            # wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_write_text(self):
        self.show_panel_widgets()
        self.set_command(
            # x=("ent_x", 0),
            # y=("ent_y", 0),
            # duration=("duration", 0),
            # button=("button", 0),
            # clicks=("clicks", 0),
            interval=("interval", 1),
            write_text=("write_text", 1)
            # button_press=("press_button", 0),
            # wait_time=("wait_time", 0)
            )
        self.on_off()
        self.focus()

    def panel_press_button(self):
        self.show_panel_widgets()
        self.set_command(
            # x=("ent_x", 0),
            # y=("ent_y", 0),
            # duration=("duration", 0),
            # button=("button", 0),
            # clicks=("clicks", 0),
            # interval=("interval", 0),
            # write_text=("write_text", 0),
            button_press=("press_button", 1)
            # wait_time=("wait_time", 0)            
            )
        self.on_off()
        self.focus()

    def panel_wait_time(self):
        self.show_panel_widgets()
        self.set_command(
            # x=("ent_x", 0),
            # y=("ent_y", 0),
            # duration=("duration", 0),
            # button=("button", 0),
            # clicks=("clicks", 0),
            # interval=("interval", 0),
            # write_text=("write_text", 0),
            # button_press=("press_button", 0),
            wait_time=("wait_time", 1)
            )
        self.on_off()
        self.focus()

    def refresh_panel(self):
        text = self.combo_action.get()
        if text == "Переместить курсор":
            self.panel_move_mouse()
        elif text == "Перетащить мышью":
            self.panel_drag_mouse()
        elif text == "Клик мыши":
            self.panel_click_mouse()
        elif text == "Двойной клик":
            self.panel_doubleclick_mouse()
        elif text == "Ввести текст":
            self.panel_write_text()
        elif text == "Нажать клавишу":
            self.panel_press_button()
        elif text == "Ждать":
            self.panel_wait_time()
        else:
            pass
 
    def initUI(self):
        # self.pack(fill=BOTH, expand=True)

        self.btn_delete = Button(self, text= "X", command=self.delete_panel, width=5)
        self.btn_delete.grid(column=1, row=1)
        
        self.lbl_action = Label(self, text="Выберите действие")
        self.lbl_action.grid(column=2, row=1)

        self.combo_action = Combobox(self)
        self.combo_action['values'] = [act for act in actions.Actions().all_actions]
        self.combo_action.current(0)
        self.combo_action.grid(column=3, row=1)

        self.btn_refresh = Button(self, text="Обновить", command=self.refresh_panel)
        self.btn_refresh.grid(column=4, row=1)

        self.ent_write_text = Entry(self, width=40)

        self.lbl_x = Label(self, text="x:")
        self.ent_x = Entry(self, width=4)
        self.ent_x.insert(0, self.x)

        self.lbl_y = Label(self, text="y:")
        self.ent_y = Entry(self, width=4)
        self.ent_y.insert(0, self.y)

        self.lbl_duration = Label(self, text="Задержка")
        self.ent_duration = Entry(self, width=2)
        self.ent_duration.insert(0, 0)

        self.lbl_interval = Label(self, text="Интервал")
        self.ent_interval = Entry(self, width=2)
        self.ent_interval.insert(0, 0)

        self.lbl_clicks = Label(self, text="Нажатий")
        self.combo_clicks = Combobox(self)
        self.combo_clicks['values'] = ["1", "2", "3"]
        self.combo_clicks.current(0)

        self.lbl_button = Label(self, text="Клавиша")
        self.combo_buttons = Combobox(self)
        self.combo_buttons['values'] = ["Левая кнопка", "Средняя кнопка", "Правая кнопка"]
        self.combo_buttons.current(0)
        
        self.lbl_press = Label(self, text="Выберите клавишу")
        self.combo_press_button = Combobox(self)
        self.combo_press_button['values'] = self.buttons
        self.combo_buttons.current(0)

        self.lbl_wait_time = Label(self, text="Ожидание")
        self.ent_wait_time = Entry(self, width=2)
        self.ent_wait_time.insert(0, 1)

        self.focus()


    # реализовать панель через метод скрытия виджетов https://www.delftstack.com/ru/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/

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