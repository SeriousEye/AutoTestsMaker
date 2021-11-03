from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Toplevel
from tkinter.ttk import Frame
import screenshoter as ss
import get_config as gc
 
 
class OpenScreen(Frame):
 
    def __init__(self, parent, cfg_monitor=None):
        """ При объявлении класса, сразу последовательно вызываются методы. """
        Frame.__init__(self, parent)
        self.parent = parent
        self.cfg_monitor = cfg_monitor
        self.make_screen()
        # self.image_size()
        # self.initUI()
        self.start_x, self.start_y, self.x1, self.y1 = 0, 0, 0, 0
        self.imageSize()
        self.initUI()
        self.process_movements()

    def quit(self, arg1):
        self.parent.destroy()
        self.parent.update()

    def paint(self, event):
        self.x1, self.y1 = event.x, event.y

    def start_points(self, event):
        self.start_x, self.start_y = event.x, event.y

    def process_movements(self):
        self.canvas.delete("aaa")
        self.canvas.focus_set()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.start_points)
        self.item = self.canvas.create_rectangle(self.start_x, self.start_y, self.x1, self.y1, tag="aaa",
                                                 outline="black", dash=(1, 1))
        self.after(10, self.process_movements)

    def make_screen(self):
        """ Создается скриншот."""
        screen = ss.ScreenShot()
        screen.fullscreenshot()
        
    def imageSize(self):
        try:
            self.img = Image.open("temp_screen.png")
            self.fillimg = self.img.putalpha(125)
            self.screen = ImageTk.PhotoImage(self.img)
        except IOError:
            print("Возникла ошибка во время открытия изображения!")
        self.wx, self.hy = self.img.size

    def initUI(self):
        """ Открывается изображение в новом окне. """
        self.canvas = Canvas(
            self.parent,
            width=self.wx,
            height=self.hy, 
            highlightthickness=0
            ) # highlightthickness - убирается рамка окна по краям, чтобы открылось только изобаржение.

        image = self.canvas.create_image(0, 0, anchor="nw", image=self.screen)
        self.canvas.grid(column=0, row=0)
        self.canvas.bind("<Escape>", quit)

    def set_geometry(self):
        print(self.cfg_monitor)
        if self.cfg_monitor == 1:
            self.parent.geometry(("%dx%d-0+0") % (self.wx, self.hy))
        else:
            self.parent.geometry(("%dx%d") % (self.wx, self.hy))

 
def main():
    top_window = Toplevel() # создается окно выше уровня основного окна
    ex = OpenScreen(top_window, cfg_monitor=gc.getConfig().PARAMETERS.get("CHANGE_MONITOR")) # изображение загружается в новое окно
    ex.set_geometry()
    top_window.overrideredirect(True) # убирается title у окна
    # top_window.mainloop()
 
# if __name__ == '__main__':
#     main()