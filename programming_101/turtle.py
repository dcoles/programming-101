import math
from turtle import Vec2D

from programming_101.canvas import Canvas


class Turtle:
    DEFAULT_WIDTH = 512
    DEFAULT_HEIGHT = 512

    def __init__(self, canvas=None):
        self.canvas = canvas or Canvas(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
        self.origin = Vec2D(self.canvas.width // 2, self.canvas.height // 2)
        self.position = Vec2D(0.0, 0.0)
        self.heading = 0.0
        self.pendown = True

        self.canvas.begin_path()
        self.canvas.move_to(self.origin[0], self.origin[1])

    @property
    def stroke_color(self):
        """Stroke color."""
        return self.canvas.stroke_style

    @stroke_color.setter
    def stroke_color(self, color: str):
        """Set the stroke color."""
        self.canvas.stroke_style = color

    @property
    def fill_color(self):
        """Fill color."""
        return self.canvas.fill_style

    @fill_color.setter
    def fill_color(self, color: str):
        """Set the fill color."""
        self.canvas.fill_style = color

    def left(self, deg: float):
        """Turn left by a number of degrees."""
        self.heading += deg

    def right(self, deg: float):
        """Turn right by a number of degrees."""
        self.heading -= deg

    def forward(self, distance: float):
        """Move forward by a number of pixels."""
        dx = distance * math.cos(math.radians(self.heading))
        dy = distance * math.sin(math.radians(self.heading))

        self.position += Vec2D(dx, dy)

        p = self.origin + self.position
        if self.pendown:
            self.canvas.line_to(*p)
        else:
            self.canvas.move_to(*p)

    def stroke(self):
        """Stroke the path."""
        self.canvas.stroke()

    def fill(self):
        """Fill the path."""
        self.canvas.fill('evenodd')
