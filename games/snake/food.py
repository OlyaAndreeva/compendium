from random import randint

class Food: 
    def __init__(self, canvas) -> None:
        x = randint(0, 29) * 30
        y = randint(0, 19) * 30
        self.coordinates = (x, y)
        canvas.create_oval(x, y, x + 30, y + 30, fill = "#f0d011", tags="food") 