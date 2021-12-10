from tkinter import *
import actions
import show_screenshot as ss
import get_config as gc
import action_buttons as ab



class Example(Frame):
    row_dict = {}  

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
        self.buttons()

    def add_panel(self):
        b = ab.Panel()
        self.row_dict[b] = b.add_action()

    def all_obj(self):
        temp_row_dict = self.row_dict.copy()
        for act in temp_row_dict:
            if act.state_delete == 0:
                self.row_dict[act] = act.get_action()
            else:
                del self.row_dict[act]

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

    def print_dict(self):
        temp_row_dict = self.row_dict.copy()
        for act in temp_row_dict:
            if act.state_delete == 0:
                self.row_dict[act] = act.get_action()
            else:
                del self.row_dict[act]
        print(self.row_dict)

    def save_file(self):
        self.all_obj()
        # for act in self.row_dict:
        #     self.row_dict[act] = act.get_action()
        with open("test_save.py", "w", encoding="utf-8")as wf:
            text_import = actions.Actions().turn_on_lib()
            wf.write(text_import)
            for act in self.row_dict.values():
                wf.write(act)

    def buttons(self):
        btn_screenshot = Button(self, text="Скриншот", command=ss.main)
        btn_screenshot.pack(side=LEFT)

        btn_settings = Button(self, text="Настроить монитор", command=gc.getConfig().change_monitor_cfg())
        btn_settings.pack(side=LEFT)

        btn_add = Button(self, text="Добавить", command=self.add_panel)
        btn_add.pack(side=LEFT)

        btn_print = Button(self, text="Print", command=self.print_dict)
        btn_print.pack(side=LEFT)

        btn_save = Button(self, text="Сохранить", command=self.save_file)
        btn_save.pack(side=LEFT)

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class посмотреть все инстансы класса
        
def main():
    root = Tk()
    root.geometry("+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()