from tkinter import *


root = Tk()
 
# Create Title
root.title(  "Paint App ")
 
# specify size
root.geometry("500x350")

x_start, y_start = 0, 0
x1_old, y1_old = 0, 0 
# define function when 
# mouse double click is enabled
def paint( event ):
    global x1_old, y1_old, x_start, y_start
    # Co-ordinates.
    x1, y1 = event.x, event.y
    # x1, y1 = event.x, event.y
     
    # Colour
    Colour = "black"
     
    # specify type of display
    # w.create_line( x1, y1, x2,
    #               y2, fill = Colour )
    
    # if x1 >= x1_old and y1 >= y1_old:
    #     x1_old, y1_old = x1, y1
    lx["text"] = x1
    ly["text"] = y1


    if x1 <= x1_old:
        w.create_rectangle(x1, y_start, x1_old, y1_old, outline="black", fill="black")
        x1 = x1_old - x1
        w.create_rectangle(
                x_start, y_start, x1, y1,
                outline="white", fill="white"
            )

        x1, y1 = x1_old, y1_old


    elif y1 <= y1_old:
        y1 = y1_old - y1
        w.create_rectangle(
                x_start, y_start, x1, y1,
                outline="white", fill="white"
            )
        x1, y1 = x1_old, y1_old

    else:
        w.create_rectangle(
                x_start, y_start, x1, y1,
                outline="white", fill="white"
            )
        x1, y1 = x1_old, y1_old
    
def start_point(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def clear_area():
    w.create_rectangle(0, 0, 400, 250, outline="black", fill="black")


 
# create canvas widget.
w = Canvas(root, width = 400, height = 250, background="black")
 
# call function when double
# click is enabled.
w.bind( "<B1-Motion>", paint )
w.bind("<Button-1>", start_point)
 
# create label.
l = Label(root, text = "Double Click and Drag to draw." )

btn = Button(root, text="Clear", command=clear_area)

lx = Label(root, text="")
ly = Label(root, text="")

l.pack()
w.pack()
btn.pack()
lx.pack()
ly.pack()
 
mainloop()

