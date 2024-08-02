import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Application")

        self.brush_color = "black"
        self.brush_size = 5
        self.eraser_on = False

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        # Tool buttons
        self.pen_button = tk.Button(root, text="Pen", command=self.use_pen)
        self.pen_button.pack(side=tk.LEFT)

        self.brush_button = tk.Button(root, text="Brush", command=self.use_brush)
        self.brush_button.pack(side=tk.LEFT)

        self.color_button = tk.Button(root, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        self.size_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT)

        self.canvas.bind("<B1-Motion>", self.paint)

    def use_pen(self):
        self.eraser_on = False
        self.brush_size = 1

    def use_brush(self):
        self.eraser_on = False
        self.brush_size = self.size_scale.get()

    def choose_color(self):
        self.eraser_on = False
        color = colorchooser.askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color

    def use_eraser(self):
        self.eraser_on = True

    def change_size(self, val):
        self.brush_size = int(val)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)

        if self.eraser_on:
            self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

root = tk.Tk()
app = PaintApp(root)
root.mainloop()