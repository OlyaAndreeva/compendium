from random import randint
from config import WIDTH, HEIGHT, SQUARE, FOOD_NUMBER


class Food:
    def __init__(self, canvas, snake_coordinates) -> None:
        x = randint(0, WIDTH-1) * SQUARE
        y = randint(0, HEIGHT-1) * SQUARE
        while (x, y) in snake_coordinates:
            x = randint(0, WIDTH-1) * SQUARE
            y = randint(0, HEIGHT-1) * SQUARE
        self.coordinates = (x, y)
        self.id = canvas.create_oval(
            x, y, x + SQUARE, y + SQUARE, fill="#f0d011", tags="food")

    def __eq__(self, other) -> bool:
        return self.coordinates == other.coordinates

    def __hash__(self) -> int:
        return hash(self.coordinates)


def get_food(snake):
    food_list = []
    while len(food_list) < FOOD_NUMBER:
        new_food = Food(snake.canvas, snake.coordinates)
        if new_food in food_list:
            snake.canvas.delete(new_food.id)
        else:
            food_list.append(new_food)
    return food_list


def eat_food(snake):
    for food in snake.food_list:
        if snake.coordinates[0] == food.coordinates:
            index = snake.food_list.index(food)
            snake.canvas.delete(snake.food_list[index].id)
            del snake.food_list[index]
            if len(snake.food_list) == 0:
                snake.food_list = get_food(snake)
            return True
    return False
