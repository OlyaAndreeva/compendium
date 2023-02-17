class Snake:
  def __init__(self, window, canvas):
      self.coordinates = [(420, 210), (420, 180), (420, 150), (420, 120), (420, 90), (420, 60), (420, 30), (420, 0)]
      self.squares = []
      self.window = window
      self.canvas = canvas
      self.direction = "down"
      self.draw()

  def draw(self):
    for x, y in self.coordinates:
        square = self.canvas.create_rectangle(x, y, x + 30, y + 30, fill = "#99e0ff")                            
        self.squares.append(square)

  def set_direction(self, new_direction):
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

    
  def next_turn(self):
    x, y = self.coordinates[0]

    if self.direction == "left":
        x = x - 30
    elif self.direction == "right":
        x = x + 30
    elif self.direction == "down":
        y = y + 30
    elif self.direction == "up":
      y = y - 30

    self.coordinates.insert(0, (x, y))
    square = self.canvas.create_rectangle(x, y,x +30, y + 30, fill = "#99e0ff")
    self.squares.insert(0, square)
    
    del self.coordinates[-1]
    self.canvas.delete(self.squares[-1])
    del self.squares[-1]


    if self.check_collision():
        self.game_over()
    else:
        self.canvas.after(50, self.next_turn)

  def game_over(self):
    self.window.destroy()

  def check_collision(self):
    x, y = self.coordinates[0]
    if x < 0 or x >= 900 or y < 0 or y >= 600:
        return True
        
    for body_part in self.coordinates[1:]:
        if (x, y) == body_part:
            return True

    return False
        
