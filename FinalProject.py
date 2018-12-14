from tkinter import*
import random

tk = Tk()
canvas = Canvas(tk, width=500,  height=500)
tk.title("Drawing")

#Score Board
root = Tk()


def R():
    canvas.move(circ, (250, 250), (250, 250))


#Reset to middle
rButton = Button(root, text="Reset", command=R).grid(row=1, column=0)




# Moving ball
circ = canvas.create_oval(0, 0, 20, 20, fill="green")
canvas.move(circ, random.randint(250, 250), random.randint(200, 250))

x = random.randint(-10, 10)
y = random.randint(-5, 5)


# Paddle movement

def move_up(event):
    yright = 10
    print(yright)
    xmove(right, yright)
    yleft = 10
    print(yleft)
    xmove(left, yleft)


def move_down(event):
    xright = -10
    print(xright)
    xmove(right, xright)
    xleft = -10
    print(xleft)
    xmove(left, xleft)


def xmove(object,x):
    canvas.move(object, y, 0)


canvas.bind("<Up>", move_up)
canvas.bind("<Down>", move_down)




canvas.pack()

right = canvas.create_rectangle(470, 200,  480, 300, fill="green")
left = canvas.create_rectangle(10, 200, 20, 300, fill="black")


def fx():
    global x, y
    canvas.move(circ, x, y)
    ax0, ay0, ax1, ay1 = canvas.coords(right)
    bx0, by0, bx1, by1 = canvas.coords(left)
    cx0, cy0, cx1, cy1 = canvas.coords(circ)
    if cy1 >= 500 or cy0 <= 0:
        y *= -1
    if cx1 == ax1 or cx0 == bx1:
        x *= -1
    tk.after(100, fx)


tk.after(100, fx)
tk.mainloop()
canvas.mainloop()