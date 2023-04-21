from tkinter import BooleanVar
from food import Food
from config import WIDTH, HEIGHT, SQUARE, SPEED, TIME
from enemy import Enemy
from time import perf_counter


class Snake:
    def __init__(self, window, canvas):
        self.coordinates = [(WIDTH//2*SQUARE, SQUARE*2),
                            (WIDTH//2*SQUARE, SQUARE),
                            (WIDTH//2*SQUARE, 0)]
        self.ids = []
        self.window = window
        self.canvas = canvas
        self.direction = "down"
        self.pause = BooleanVar()  # False by default
        self.draw()
        self.food_list = Food.get_food(self)

        self.enemy_left = Enemy(self,
                                [(SQUARE * 2, 0), (SQUARE, 0), (0, 0)],
                                "#A0A0A0",
                                "right")
        self.enemy_right = Enemy(self,
                                 [((WIDTH - 3) * SQUARE, (HEIGHT - 1) * SQUARE),
                                  ((WIDTH - 2) * SQUARE, (HEIGHT - 1) * SQUARE),
                                  ((WIDTH - 1) * SQUARE, (HEIGHT - 1) * SQUARE)],
                                 "#F0D011",
                                 "left")

        self.score = 0
        self.canvas.create_text((WIDTH - 1) * SQUARE, SQUARE,
                                fill="#FFFFFF",
                                font=("Old English Text MT", f"{SQUARE}"),
                                text=f"{self.score}",
                                tag="score")

        self.refresh_time = perf_counter()
        self.canvas.create_text(SQUARE + SQUARE//2, SQUARE,
                                fill="#FFFFFF",
                                font=("Old English Text MT", f"{SQUARE}"),
                                text=f"{round(TIME,1)}",
                                tag="timer")

    def next_turn(self):
        self.is_paused()

        self.move_head()

        if Food.eat_food(self):
            self.score = self.score + 1
            self.print_score()
        elif self.check_enemy_kill(self.enemy_left):
            self.score = self.score + len(self.enemy_left.coordinates)
            self.print_score()
            self.enemy_left.kill()
            self.enemy_left = Enemy(self,
                                    [(SQUARE * 2, 0), (SQUARE, 0), (0, 0)],
                                    "#A0A0A0",
                                    "right")
        elif self.check_enemy_kill(self.enemy_right):
            self.score = self.score + len(self.enemy_right.coordinates)
            self.print_score()
            self.enemy_right.kill()
            self.enemy_right = Enemy(self,
                                     [((WIDTH - 3) * SQUARE, (HEIGHT - 1) * SQUARE),
                                      ((WIDTH - 2) * SQUARE,
                                       (HEIGHT - 1) * SQUARE),
                                         ((WIDTH - 1) * SQUARE, (HEIGHT - 1) * SQUARE)],
                                     "#F0D011",
                                     "left")
        else:
            self.delete_tail()

        self.enemy_left.moves()
        self.enemy_right.moves()

        if len(self.food_list) == 0:
            self.update_food_lists()

        self.timer()

        if len(self.coordinates) == 0 or self.check_collision():
            self.game_over()
        else:
            self.canvas.after(SPEED, self.next_turn)

    def timer(self):
        self.canvas.delete("timer")
        current_timer = round(TIME - (perf_counter() - self.refresh_time), 1)

        if current_timer <= 0:
            self.delete_tail()
            current_timer = TIME
            self.refresh_time = perf_counter()
            
        self.canvas.create_text(SQUARE + SQUARE//2, SQUARE,
                                fill="#FFFFFF",
                                font=("Old English Text MT", f"{SQUARE}"),
                                text=f"{round(current_timer,1)}",
                                tag="timer")

    def check_enemy_kill(self, enemy):
        if self.coordinates[0] in enemy.coordinates:
            if self.direction == "left" and enemy.direction != "right":
                return True
            if self.direction == "right" and enemy.direction != "left":
                return True
            if self.direction == "up" and enemy.direction != "down":
                return True
            if self.direction == "down" and enemy.direction != "up":
                return True
        else:
            return False

    def update_food_lists(self):
        self.food_list = Food.get_food(self)
        self.enemy_left.food_list = self.food_list
        self.enemy_right.food_list = self.food_list

    def print_score(self):
        self.canvas.delete("score")
        self.canvas.create_text((WIDTH - 1) * SQUARE, SQUARE,
                                fill="#FFFFFF",
                                font=("Old English Text MT", f"{SQUARE}"),
                                text=f"{self.score}",
                                tag="score")

    def is_paused(self):
        if self.pause.get():
            self.canvas.wait_variable(self.pause)

    def press_space(self):

        self.pause.set(not self.pause.get())

    def draw(self):
        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + SQUARE, y + SQUARE, fill="#99e0ff")
            self.ids.append(square)

    def set_direction(self, new_direction):
        if not self.pause.get():
            if new_direction == "left":
                if self.direction != "right":
                    self.direction = "left"
            elif new_direction == "right":
                if self.direction != "left":
                    self.direction = "right"
            elif new_direction == "up":
                if self.direction != "down":
                    self.direction = "up"
            elif new_direction == "down":
                if self.direction != "up":
                    self.direction = "down"

    def move_head(self):
        x, y = self.coordinates[0]

        if self.direction == "left":
            x = x - SQUARE
        elif self.direction == "right":
            x = x + SQUARE
        elif self.direction == "down":
            y = y + SQUARE
        elif self.direction == "up":
            y = y - SQUARE

        self.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(
            x, y, x + SQUARE, y + SQUARE, fill="#99e0ff")
        self.ids.insert(0, square)

    def delete_tail(self):
        del self.coordinates[-1]
        self.canvas.delete(self.ids[-1])
        del self.ids[-1]

    def game_over(self):
        self.window.destroy()

    def check_collision(self):
        x, y = self.coordinates[0]
        if x < 0 or x >= WIDTH*SQUARE or y < 0 or y >= HEIGHT*SQUARE:
            return True

        for body_part in self.coordinates[1:]:
            if (x, y) == body_part:
                return True

        for body_part in self.coordinates:
            if body_part in self.enemy_left.coordinates or body_part in self.enemy_right.coordinates:
                return True

        return False
