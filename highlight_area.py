from tkinter import *


root = Tk()
 
# Create Title
root.title(  "Paint App ")
 
# specify size
root.geometry("500x350")

x1_old, y1_old = 0, 0 
# define function when 
# mouse double click is enabled
def paint( event ):
    global x1_old, y1_old
    # Co-ordinates.
    x1, y1, x2, y2 = ( event.x - 2 ),( event.y - 2 ), ( event.x + 2 ),( event.y + 2 )
    # x1, y1 = event.x, event.y
     
    # Colour
    Colour = "black"
     
    # specify type of display
    # w.create_line( x1, y1, x2,
    #               y2, fill = Colour )
    
    # if x1 >= x1_old and y1 >= y1_old:
    #     x1_old, y1_old = x1, y1
    w.create_rectangle(
            x1_old, y1_old, x1, y1,
            outline="white", fill="white"
        )
    
def start_point(event):
    global x1_old, y1_old
    x1_old, y1_old = event.x, event.y


 
# create canvas widget.
w = Canvas(root, width = 400, height = 250, background="black")
 
# call function when double
# click is enabled.
w.bind( "<B1-Motion>", paint )
w.bind("<Button-1>", start_point)
 
# create label.
l = Label( root, text = "Double Click and Drag to draw." )


l.pack()
w.pack()
 
mainloop()

