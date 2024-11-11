from tkinter import *
from PIL import Image, ImageTk
from Editor import Editor

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)  # Активуємо цей обробник подій

    def show_tooltip(self, event):
        if self.tooltip_window or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx()
        y = y + self.widget.winfo_rooty()
        self.tooltip_window = Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = Label(self.tooltip_window, text=self.text, background="yellow", relief=SOLID, borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


class Toolbar:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.editor = Editor.get_instance()
        self.editor.canvas = canvas
        self.selected_shape = None
        self.create_toolbar()

    def create_toolbar(self):
        self.toolbar_frame = Frame(self.root, bd=1, relief=RAISED)

        # Завантаження іконок для кнопок
        self.rect_icon = ImageTk.PhotoImage(Image.open("rectangle.png").resize((26, 26)))
        self.ellipse_icon = ImageTk.PhotoImage(Image.open("ellipse.png").resize((21, 21)))
        self.line_icon = ImageTk.PhotoImage(Image.open("line.png").resize((21, 21)))
        self.point_icon = ImageTk.PhotoImage(Image.open("point.png").resize((21, 21)))
        self.cube_icon = ImageTk.PhotoImage(Image.open("Cube.png").resize((26, 26)))  # Іконка для Cube
        self.lineoo_icon = ImageTk.PhotoImage(Image.open("Dumbell.jpg").resize((26, 26)))  # Іконка для LineOO

        # Створення кнопок для панелі інструментів
        rect_button = Button(self.toolbar_frame, image=self.rect_icon, command=lambda: self.select_shape("RectangleShape"))
        rect_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(rect_button, "Rectangle")

        ellipse_button = Button(self.toolbar_frame, image=self.ellipse_icon, command=lambda: self.select_shape("EllipseShape"))
        ellipse_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(ellipse_button, "Ellipse")

        line_button = Button(self.toolbar_frame, image=self.line_icon, command=lambda: self.select_shape("LineShape"))
        line_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(line_button, "Line")

        point_button = Button(self.toolbar_frame, image=self.point_icon, command=lambda: self.select_shape("PointShape"))
        point_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(point_button, "Point")

        cube_button = Button(self.toolbar_frame, image=self.cube_icon, command=lambda: self.select_shape("CubeShape"))
        cube_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(cube_button, "Cube")

        lineoo_button = Button(self.toolbar_frame, image=self.lineoo_icon, command=lambda: self.select_shape("LineOOShape"))
        lineoo_button.pack(side=LEFT, padx=2, pady=2)
        ToolTip(lineoo_button, "Dumbell")

        self.toolbar_frame.pack(side=LEFT, fill=X)
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def select_shape(self, shape_type):
        self.selected_shape = shape_type

    def on_mouse_down(self, event):
        if self.selected_shape:
            self.editor.set_new_shape(self.selected_shape, event.x, event.y, size=50)  # Встановлюємо розмір для CubeShape
            self.editor.touch_start(event.x, event.y)

    def on_mouse_move(self, event):
        if self.selected_shape:
            self.editor.touch_move(event.x, event.y)

    def on_mouse_up(self, event):
        if self.selected_shape:
            self.editor.touch_up()
            self.editor.draw(self.canvas)
