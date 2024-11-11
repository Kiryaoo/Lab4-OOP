import tkinter as tk
from ShapeEditor import ShapeEditor
from Tools import Toolbar

class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("600x600")

        # Створення полотна для малювання
        self.canvas = tk.Canvas(self.root, width=600, height=550, bg="white")
        self.canvas.pack()

        # Передаємо self.canvas у ShapeEditor
        self.editor = ShapeEditor(self.canvas, self.root)
        self.switch = ShapeEditor(self.canvas, self.root)
        self.switch.create_menu()

        # Створюємо Toolbar і передаємо необхідні аргументи
        self.toolbar = Toolbar(self.root, self.canvas)

        self.root.mainloop()

mainWindow()