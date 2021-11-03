from tkinter import *
import show_screenshot as ss
import get_config as gc
import action_buttons as ab


class Example(Frame):
    list_lines = []    

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        # self.list_lines = []
        self.list_id = 0
        self.initUI()
        self.buttons()
        # self.update()
    
    def id_button(self):
        self.list_id += 1

    # def add_panel(self):
    #     print(id(a))
    #     self.list_lines.append(id(a))
    #     print(self.list_lines)

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

    # def print_list(self):
    #     self.txt_field.insert("1.0", "".join(str(self.list_lines)))

    def buttons(self):
        # self.txt_field = Text()
        # self.txt_field.pack()

        btn_screenshot = Button(self, text="Скриншот", command=ss.main)
        btn_screenshot.pack(side=LEFT)

        btn_settings = Button(self, text="Настроить монитор", command=gc.getConfig().change_monitor_cfg())
        btn_settings.pack(side=LEFT)

        btn_add = Button(self, text="Добавить", command=ab.Panel)
        # self.list_lines.append(btn_add)
        btn_add.pack(side=LEFT)

        # btn_print = Button(self, text="Print", command=self.print_list)
        # btn_print.pack(side=LEFT)

# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class посмотреть все инстансы класса
        
def main():
    root = Tk()
    root.geometry("+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()