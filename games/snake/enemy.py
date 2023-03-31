from config import SQUARE


class Enemy:
    def __init__(self, snake):
        self.coordinates = [(SQUARE * 2, 0), (SQUARE, 0), (0, 0)]
        self.ids = []
        self.canvas = snake.canvas
        self.direction = "right"
        self.draw()

    def draw(self):
        for x, y in self.coordinates:
            id = self.canvas.create_rectangle(
                x, y, SQUARE + x, SQUARE + y, fill="#ff5040")
            self.ids.append(id)

    def moves(self):
        x, y = self.coordinates[0]
        self.direction = self.choose_direction()
        if self.direction == "right":
            x = x + SQUARE
        elif self.direction == "down":
            y = y + SQUARE
        elif self.direction == "up":
            y = y - SQUARE
        else:
            x = x - SQUARE
        self.coordinates.insert(0, (x, y))
        id = self.canvas.create_rectangle(
            x, y, SQUARE + x, SQUARE + y, fill="#ff5040")
        self.ids.insert(0, id)

        del self.coordinates[-1]
        self.canvas.delete(self.ids[-1])
        del self.ids[-1]

    def choose_direction(self):
        return "right"
