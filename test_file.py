from tkinter import *
import action_buttons as ab
import gc


class AddDel(Frame):
    new_list = []

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()
        self.a = ab.Counter()
        # self.call_class()
        
    def increment_count(self):
        self.a.inctrement_count
        print(f"increment {self.a.counter}")

    def add_panel(self):
        print(self.a.counter)
        a = ab.Panel(self.a.counter)
        self.increment_count()

    def initUI(self):
        # self.pack(fill=BOTH, expand=True)
        btn_add = Button(self.parent, text="Add buttons", command=self.add_panel)
        btn_add.pack()

        btn_print = Button(self.parent, text="все объекты", command=self.all_obj)
        btn_print.pack()

    def all_obj(self):
        # for obj in gc.get_objects():        
        #     if isinstance(obj, ab.Panel):
        #         print(obj)
        for inst in ab.Panel.get_instances():
            print(inst)


root = Tk()
root.geometry("+500+300")
app = AddDel(root)
root.mainloop()


# from tkinter import *
# from PIL import Image, ImageTk
# import screenshoter as ss

# class OpenScreen(Frame):

#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.start_x, self.start_y, self.x1, self.y1 = 0, 0, 0, 0
#         self.imageSize()
#         self.initUI()
#         self.process_movements()

#     def quit(self, arg1):
#         self.parent.destroy()

#     def paint(self, event):
#         self.x1, self.y1 = event.x, event.y

#     def start_points(self, event):
#         self.start_x, self.start_y = event.x, event.y

#     def process_movements(self):
#         self.canvas.delete("aaa")
#         self.canvas.focus_set()
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.start_points)
#         self.item = self.canvas.create_rectangle(self.start_x, self.start_y, self.x1, self.y1, tag="aaa",
#                                                  outline="black", dash=(1, 1))
#         self.after(10, self.process_movements)

#     def imageSize(self):
#         try:
#             self.img = Image.open("temp_screen.png")
#             self.fillimg = self.img.putalpha(125)
#             self.screen = ImageTk.PhotoImage(self.img)
#         except IOError:
#             print("Возникла ошибка во время открытия изображения!")
#         self.wx, self.hy = self.img.size

#     def initUI(self):
#         self.canvas = Canvas(
#             self.parent, 
#             width=self.wx, 
#             height=self.hy, 
#             highlightthickness=0
#             )
#         image = self.canvas.create_image(0, 0, anchor="nw", image=self.screen)
#         self.canvas.grid(column=0, row=0)
#         self.canvas.bind("<Escape>", quit)


#     def setGeometry(self):
#         self.parent.geometry(f"{self.wx}x{self.hy}")


# https://note.nkmk.me/en/python-pillow-putalpha/
# https://pillow.readthedocs.io/en/stable/
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_rectangle.html
# https://pythonru.com/uroki/canvas-3-tkinter-20
# https://tkdocs.com/tutorial/windows.html закрытие верхних окон

# Нужно чтобы два изображения открывались в двух слоях, затуманенный снизу. 
# Получается, что каждый цикл идет рисование картинки в виде прямоугольника 
# с отступами равными sarts_point

# def main():
#     root = Tk()
#     # root.geometry("3840x1080")
#     app = OpenScreen(root)
#     root.overrideredirect(True)
#     root.mainloop()
    

# if __name__ == '__main__':
#     main()


# ----------------------------------------------------
# import tkinter as tk

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Перемещение элементов холста")

#         self.canvas = tk.Canvas(self, bg="white")
#         self.canvas.pack()
#         self.start_x, self.start_y, self.x1, self.y1 = 0, 0, 0, 0
#         self.update()
#         self.width = self.canvas.winfo_width()
#         self.height = self.canvas.winfo_height()
#         self.pressed_keys = {}
#         self.bind("<KeyPress>", self.key_press)
#         self.bind("<KeyRelease>", self.key_release)


#         self.process_movements()

#     def key_press(self, event):
#         self.pressed_keys[event.keysym] = True

#     def key_release(self, event):
#         self.pressed_keys.pop(event.keysym, None)

#     def paint(self, event):
#         self.x1, self.y1 = event.x, event.y

#     def start_points(self, event):
#         self.start_x, self.start_y = event.x, event.y

#     def process_movements(self):
#         self.canvas.delete("aaa")
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.start_points)
#         self.item = self.canvas.create_rectangle(self.start_x, self.start_y, self.x1, self.y1, tag="aaa",
#                                                  fill="blue")
#         self.canvas.move(self.item, 0, 0)

        
        

#         self.after(10, self.process_movements)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()