from tkinter import Menu
from Editor import Editor

class ShapeEditor:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.editor = Editor(canvas=canvas)  # Передаємо canvas при ініціалізації Editor
        self.editor.shapes = []  # Ініціалізуємо масив фігур
        self.current_shape_name = "PointShape"  # Поточний тип фігури за замовчуванням
        self.cube_size = 100  # Розмір куба за замовчуванням
        self.create_menu()

        # Прив'язка подій
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<Expose>", lambda event: self.on_paint())

    def set_shape(self, shape_name):
        self.current_shape_name = shape_name

    def on_mouse_down(self, event):
        # Передаємо тип фігури
        if self.current_shape_name == "CubeShape":
            self.editor.set_new_shape(self.current_shape_name, event.x, event.y, self.cube_size)
        else:
            self.editor.set_new_shape(self.current_shape_name, event.x, event.y)
        self.editor.touch_start(event.x, event.y)

    def on_mouse_move(self, event):

        self.editor.touch_move(event.x, event.y)
        self.canvas.delete("all")
        self.editor.draw(self.canvas)

    def on_mouse_up(self, event):
        self.editor.touch_up()
        self.canvas.delete("all")
        self.editor.draw(self.canvas)

    def on_paint(self):

        self.canvas.delete("all")
        self.editor.draw(self.canvas)

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        shape_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Shapes", menu=shape_menu)

        shape_menu.add_command(label="Point", command=lambda: self.set_shape("PointShape"))
        shape_menu.add_command(label="Line", command=lambda: self.set_shape("LineShape"))
        shape_menu.add_command(label="Rectangle", command=lambda: self.set_shape("RectangleShape"))
        shape_menu.add_command(label="Ellipse", command=lambda: self.set_shape("EllipseShape"))
        shape_menu.add_command(label="Cube", command=lambda: self.set_shape("CubeShape"))
        shape_menu.add_command(label="Line with Circles", command=lambda: self.set_shape("LineOOShape"))

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save as")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        help_menu = Menu(menu, tearoff=1)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About program")
