from abc import ABC, abstractmethod
from PointShape import PointShape
from LineShape import LineShape
from RectangleShape import RectangleShape
from EllipseShape import EllipseShape
from CubeShape import CubeShape
from LineOOShape import LineOOShape

class Editor(ABC):
    instance = None

    def __init__(self, canvas=None, shapes=None):
        if Editor.instance is None:
            Editor.instance = self
        self.canvas = canvas
        self.shapes = shapes if shapes is not None else []
        self.current_shape = None

    @staticmethod
    def get_instance():
        if Editor.instance is None:
            Editor.instance = Editor()
        return Editor.instance

    def set_new_shape(self, shape_name, x, y, size=None):
        self.current_shape = self.create_shape(shape_name, x, y, size)

    def create_shape(self, shape_name, x, y, size=None):
        if shape_name == "PointShape":
            return PointShape(x, y)
        elif shape_name == "LineShape":
            return LineShape(x, y, x, y)
        elif shape_name == "EllipseShape":
            return EllipseShape(x, y, x, y)
        elif shape_name == "RectangleShape":
            return RectangleShape(x, y, x, y)
        elif shape_name == "CubeShape":
            return CubeShape(self.canvas, x, y, size)
        elif shape_name == "LineOOShape":
            return LineOOShape(x, y, x, y, self.canvas)

    def touch_start(self, x, y):
        if self.current_shape:
            self.current_shape.x1, self.current_shape.y1 = x, y

    def touch_move(self, x, y):
        if self.current_shape:
            self.current_shape.x2, self.current_shape.y2 = x, y
            if self.current_shape not in self.shapes:
                self.shapes.append(self.current_shape)
            self.draw(self.canvas)

    def touch_up(self):
        self.current_shape = None

    def draw(self, canvas):
        canvas.delete("all")
        for shape in self.shapes:
            shape.draw(canvas)
