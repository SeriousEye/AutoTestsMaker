# from PIL import Image, ImageTk
# from tkinter import Tk
# from tkinter.ttk import Frame, Label
# import sys
 
 
# class Example(Frame):
 
#     def __init__(self):
#         super().__init__()
#         self.loadImage()
#         self.initUI()


#     # def loadImage(self):
#     #     try:
#     #         self.img = Image.open("temp_screen.png")
#     #         self.img.show()
#     #     except IOError:
#     #         print("Возникла ошибка во время открытия изображения!")
#     #         sys.exit(1)  
 
#     def loadImage(self):
#         try:
#             self.img = Image.open("tatras.jpg")
#         except IOError:
#             print("Возникла ошибка во время открытия изображения!")
#             sys.exit(1)    
 
#     def initUI(self):
#         self.master.title("Ярлык")
#         tatras = ImageTk.PhotoImage(self.img)
#         label = Label(self, image=tatras, state='normal')
 
#         # Сохраняем ссылку на объект открытого изображения.
#         label.image = tatras
 
#         label.pack()
#         self.pack()
 
#     def setGeometry(self):
#         w, h = self.img.size
#         self.master.geometry(("%dx%d") % (w, h))
 
 
# def main():
#     root = Tk()
#     ex = Example()
#     ex.setGeometry()
#     root.overrideredirect(True)
#     root.mainloop()
 
 
# if __name__ == '__main__':
#     main()

# import tkinter
# from tkinter.constants import ANCHOR, BOTH, YES
# from PIL import Image, ImageTk
# import sys

# root = tkinter.Tk()
# root.geometry("3840x1080-0+0")

# # создаем рабочую область
# frame = tkinter.Frame(root)
# frame.pack(expand=YES, fill=BOTH)

# #Добавим изображение
# canvas = tkinter.Canvas(frame, highlightthickness=0)
# image = Image.open("temp_screen.png")

# photo = ImageTk.PhotoImage(image)
# image = canvas.create_image(0, 0, image=photo)
# canvas.pack()
# root.overrideredirect(True)
# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("3840x1080-0+0")

frame = Frame(root)
frame.pack()

# create the canvas, size in pixels
canvas = Canvas(frame, width=3840, height=1080, highlightthickness=0)

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='temp_screen.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0, 0, image=gif1, anchor=NW)
root.overrideredirect(True)

# run it ...
# test line

mainloop()