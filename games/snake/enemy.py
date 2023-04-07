from config import SQUARE, WIDTH, HEIGHT
from random import choice, random
from food import Food

class Enemy:
    def __init__(self, snake):
        self.coordinates = [(SQUARE * 2, 0), (SQUARE, 0), (0, 0)]
        self.ids = []
        self.canvas = snake.canvas
        self.direction = "right"
        self.food_list = snake.food_list 
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

        if Food.eat_food(self):
            pass
        else:
            del self.coordinates[-1]
            self.canvas.delete(self.ids[-1])
            del self.ids[-1]

    def choose_direction(self):
        x, y = self.coordinates[0]
        direction = self.direction
        directions = {'up', 'down', 'left', 'right'}
        forbidden = set()

        if direction == 'left':
            forbidden.add('right')
        elif direction == 'right':
            forbidden.add('left')
        if direction == 'up':
            forbidden.add('down')
        elif direction == 'down':
            forbidden.add('up')

        if x == 0:
            forbidden.add('left')
        elif x == (WIDTH - 1) * SQUARE:
            forbidden.add('right')
        if y == 0:
            forbidden.add('up')
        elif y == (HEIGHT - 1) * SQUARE:
            forbidden.add('down')

        possible = directions - forbidden
        if direction in possible:
            if random() < 0.9:
                return direction

        return choice(list(possible)) 