from random import randint
from config import WIDTH, HEIGHT, SQUARE


class Food:
    def __init__(self, canvas, snake_coordinates) -> None:
        x = randint(0, WIDTH-1) * SQUARE
        y = randint(0, HEIGHT-1) * SQUARE
        while (x, y) in snake_coordinates:
            x = randint(0, WIDTH-1) * SQUARE
            y = randint(0, HEIGHT-1) * SQUARE
        self.coordinates = (x, y)
        canvas.create_oval(x, y, x + SQUARE, y + SQUARE, fill="#f0d011", tags="food")
