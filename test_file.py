from tkinter import *
from PIL import Image, ImageTk
import screenshoter as ss

class OpenScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.imageSize()
        # self.setGeometry()
        self.initUI()
        self.points()

    def points(self):
        self.x_start, self.y_start = 0, 0
        self.x1_old, self.y1_old = 0, 0

    def start_points(self, event):
        self.x_start, self.y_start = event.x, event.y

    def paint(self, event):
        x1, y1 = event.x, event.y
        self.canvas.create_rectangle(
            self.x_start, self.y_start, x1, y1,
            dash=(3, 5)
        )

        ss.ScreenShot().rectangle_screenshot(self.x_start, self.y_start, x1, y1)
        self.alphaimg = Image.open("temp.png")
        self.fillimg = self.alphaimg.putalpha(50)
    # x1, y1 = x1_old, y1_old


    def imageSize(self):
        try:
            self.img = Image.open("temp_screen.png")
            self.fillimg = self.img.putalpha(125)
            self.screen = ImageTk.PhotoImage(self.img)
        except IOError:
            print("Возникла ошибка во время открытия изображения!")
        self.wx, self.hy = self.img.size

    def initUI(self):
        # canvas = Canvas(self.parent, width=self.wx, height=self.hy)
        self.canvas = Canvas(self.parent, width=self.wx, height=self.hy, highlightthickness=0)

        image = self.canvas.create_image(0, 0, anchor="nw", image=self.screen)
        self.canvas.grid(column=0, row=0)

        self.canvas.bind( "<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.start_points)

    def setGeometry(self):
        self.parent.geometry(f"{self.wx}x{self.hy}")


# https://note.nkmk.me/en/python-pillow-putalpha/
# https://pillow.readthedocs.io/en/stable/
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_rectangle.html

# Нужно чтобы два изображения открывались в двух слоях, затуманенный снизу. 
# Получается, что каждый цикл идет рисование картинки в виде прямоугольника 
# с отступами равными sarts_point

def main():
    root = Tk()
    # root.geometry("3840x1080")
    app = OpenScreen(root)
    root.overrideredirect(True)
    root.mainloop()
    

if __name__ == '__main__':
    main()



    # self.canvas.bind( "<B1-Motion>", self.paint)
    # self.canvas.bind("<Button-1>", self.start_point)


    # def paint(self, event):
    #     self.x1_old, self.y1_old, self.x_start, self.y_start
    #     self.x1, self.y1 = event.x, event.y

    #     self.canvas.create_rectangle(
    #             self.x_start, self.y_start, self.x1, self.y1,
    #             outline="white", fill="white"
    #     )
    #     self.x1, self.y1 = self.x1_old, self.y1_old

    # def start_point(self, event):
    #     self.x_start, self.y_start
    #     self.x_start, self.y_start = event.x, event.y