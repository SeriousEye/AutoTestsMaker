from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Toplevel
from tkinter.ttk import Frame
import screenshoter as ss
 
 
class OpenScreen(Frame):
 
    def __init__(self, parent):
        """ При объявлении класса, сразу последовательно вызываются методы. """
        Frame.__init__(self, parent)
        self.parent = parent
        self.make_screen()
        self.image_size()
        self.initUI()

    def make_screen(self):
        """ Создается скриншот."""
        screen = ss.ScreenShot()
        screen.fullscreenshot()
        
    def image_size(self):
        """ Загружается изображение и сохраняются его размеры. """
        try:
            self.img = Image.open("temp_screen.png")
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
 
 
def main():
    root = Toplevel() # создается окно выше уровня основного окна
    ex = OpenScreen(root) # изображение загружается в новое окно
    root.overrideredirect(True) # убирается title у окна
    # root.mainloop()
 
# if __name__ == '__main__':
#     main()
    