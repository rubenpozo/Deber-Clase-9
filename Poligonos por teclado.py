from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_rectangle(10, 80, 50, 130, width=5, fill= 'black')
canvas.create_oval(10, 150, 50, 200,width=5, fill='black')

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        canvas.move(2, 0, -6)
        canvas.move(3, 0, -9)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        canvas.move(2, 0, 6)
        canvas.move(3, 0, 9)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        canvas.move(2, -6, 0)
        canvas.move(3, -9, 0)
    else:
        canvas.move(1, 3, 0)
        canvas.move(2, 6, 0)
        canvas.move(3, 9, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
