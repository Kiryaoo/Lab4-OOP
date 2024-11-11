from EllipseShape import EllipseShape
from LineShape import LineShape


class LineOOShape(LineShape, EllipseShape):
    def __init__(self, x1, y1, x2, y2, canvas, circle_radius=5):
        LineShape.__init__(self, x1, y1, x2, y2)
        EllipseShape.__init__(self, x1, y1, x2, y2)

        self.canvas = canvas
        self.temp_shape_id = None
        self.circle_radius = circle_radius

    def on_left_button_down(self, event):
        # Зберігаємо початкову точку для лінії
        self.start_x, self.start_y = event.x, event.y

    def on_mouse_move(self, event):
        # Видаляємо попередню тимчасову лінію, якщо вона існує
        if self.temp_shape_id is not None:
            self.canvas.delete(self.temp_shape_id)

        # Малюємо нову тимчасову лінію з пунктиром
        self.temp_shape_id = self.canvas.create_line(
            self.start_x, self.start_y, event.x, event.y,
            fill="blue", dash=(2, 2)
        )

    def on_left_button_up(self, event):
        # Зберігаємо кінцеві координати та малюємо постійну лінію з кругами на кінцях
        self.x2, self.y2 = event.x, event.y

        # Видаляємо тимчасову лінію
        if self.temp_shape_id is not None:
            self.canvas.delete(self.temp_shape_id)
            self.temp_shape_id = None

        # Малюємо постійний LineOOShape
        self.draw(self.canvas)

    def draw(self, canvas):
        # Малюємо основну лінію
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

        # Малюємо круги на кінцях лінії
        canvas.create_oval(
            self.x1 - self.circle_radius, self.y1 - self.circle_radius,
            self.x1 + self.circle_radius, self.y1 + self.circle_radius,
            outline="black", fill="black"
        )
        canvas.create_oval(
            self.x2 - self.circle_radius, self.y2 - self.circle_radius,
            self.x2 + self.circle_radius, self.y2 + self.circle_radius,
            outline="black", fill="black"
        )
