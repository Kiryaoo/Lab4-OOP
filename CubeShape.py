from RectangleShape import RectangleShape
from LineShape import LineShape

class CubeShape(RectangleShape, LineShape):
    def __init__(self, canvas, x1, y1, size):
        x2 = x1 + size
        y2 = y1 + size
        RectangleShape.__init__(self, x1, y1, x2, y2)
        LineShape.__init__(self, x1, y1, x2, y2)

        self.canvas = canvas
        self.temp_front_rectangle = None
        self.temp_back_rectangle = None
        self.temp_edges = []

        # Зменшуємо зсув, щоб куб виглядав більш пропорційно
        self.offset = 15

    def draw(self, finalize=False):
        # Координати переднього та заднього прямокутників
        front_rectangle_coords = (self.x1, self.y1, self.x2, self.y2)
        back_rectangle_coords = (
            self.x1 + self.offset, self.y1 + self.offset,
            self.x2 + self.offset, self.y2 + self.offset
        )

        # Координати ребер
        edges_coords = [
            (self.x1, self.y1, self.x1 + self.offset, self.y1 + self.offset),
            (self.x1, self.y2, self.x1 + self.offset, self.y2 + self.offset),
            (self.x2, self.y1, self.x2 + self.offset, self.y1 + self.offset),
            (self.x2, self.y2, self.x2 + self.offset, self.y2 + self.offset),
        ]

        if not finalize:
            # Видаляємо попередні тимчасові елементи
            if self.temp_front_rectangle:
                self.canvas.delete(self.temp_front_rectangle)
            if self.temp_back_rectangle:
                self.canvas.delete(self.temp_back_rectangle)
            for temp_edge in self.temp_edges:
                self.canvas.delete(temp_edge)
            self.temp_edges.clear()

            # Малюємо задній прямокутник
            self.temp_back_rectangle = self.canvas.create_rectangle(
                *back_rectangle_coords, outline="black", width=2
            )

            # Малюємо ребра
            for edge_coords in edges_coords:
                temp_edge_id = self.canvas.create_line(*edge_coords, fill="black", width=2)
                self.temp_edges.append(temp_edge_id)

            # Малюємо передній прямокутник поверх всього
            self.temp_front_rectangle = self.canvas.create_rectangle(
                *front_rectangle_coords, outline="black", width=2
            )

        else:
            # Малюємо задній прямокутник
            self.canvas.create_rectangle(
                *back_rectangle_coords, outline="black", width=2
            )

            # Малюємо ребра
            for edge_coords in edges_coords:
                self.canvas.create_line(*edge_coords, fill="black", width=2)

            # Малюємо передній прямокутник
            self.canvas.create_rectangle(
                *front_rectangle_coords, outline="black", width=2
            )

    def on_mouse_down(self, event):
        self.is_down = True
        self.set_start_points(event.x, event.y)
        self.set_end_points(event.x, event.y)
        self.draw()

    def on_mouse_move(self, event):
        if not self.is_down:
            return
        self.set_end_points(event.x, event.y)
        self.draw(finalize=False)

    def on_mouse_up(self, event):
        self.is_down = False
        self.set_end_points(event.x, event.y)
        self.draw(finalize=True)

        self.temp_front_rectangle = None
        self.temp_back_rectangle = None
        self.temp_edges.clear()

    @staticmethod
    def get_name():
        return 'Cube'
