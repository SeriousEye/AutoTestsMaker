from tkinter import *
import show_screenshot as ss
import get_config as gc


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
        self.buttons()
    
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

    def buttons(self):
        btn_screenshot = Button(self, text="Скриншот", command=ss.main)
        btn_screenshot.pack()

        btn_settings = Button(self, text="Настроить монитор", command=gc.getConfig().change_monitor_cfg())
        btn_settings.pack()
        
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()