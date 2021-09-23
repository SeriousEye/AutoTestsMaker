from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.loadImage()
        self.initUI()
 
    def loadImage(self):
        try:
            self.img = Image.open("temp_screen.png")
        except IOError:
            print("Возникла ошибка во время открытия изображения!")
            sys.exit(1)
 
    def initUI(self):
        self.master.title("Ярлык")
        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)
 
        # Сохраняем ссылку на объект открытого изображения.
        label.image = tatras
 
        label.pack()
        self.pack()
 
    def setGeometry(self):
        w, h = self.img.size
        self.master.geometry(("%dx%d") % (w, h))
 
 
def main():
    root = Tk()
    ex = Example()
    ex.setGeometry()
    root.overrideredirect(True)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()