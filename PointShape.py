from Shape import Shape

class PointShape(Shape):
    def __init__(self, x1, y1):
        super().__init__(x1, y1)

    def draw(self, canvas):
        radius = 5
        canvas.create_oval(self.x1 - radius, self.y1 - radius, self.x1 + radius, self.y1 + radius, fill="black")

    def on_left_button_down(self, event):
        self.x1, self.y1 = event.x, event.y

    def on_mouse_move(self, event):
        pass

    def on_left_button_up(self, event):
        pass
