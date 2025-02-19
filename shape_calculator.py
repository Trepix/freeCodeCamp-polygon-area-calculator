class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return "\n".join(["*" * self.width] * self.height) + "\n"

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)
