from Shape import Shape

class RectangleShape(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.temp_shape_id = None

    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", fill="grey")

    def on_left_button_down(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.x1, self.y1, self.x2, self.y2 = self.start_x, self.start_y, self.start_x, self.start_y

    def on_mouse_move(self, event, canvas):
        if self.temp_shape_id is not None:
            canvas.delete(self.temp_shape_id)
        self.temp_shape_id = canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline="blue", dash=(4, 2)
        )

    def on_left_button_up(self, event, canvas):
        self.x2, self.y2 = event.x, event.y
        if self.temp_shape_id is not None:
            canvas.delete(self.temp_shape_id)
            self.temp_shape_id = None