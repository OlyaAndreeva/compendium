import tkinter

class Snake:
  def __init__(self, canvas):
    self.coordinates = [(420, 60), (420, 30), (420, 0)]
    self.squares = []
    self.canvas = canvas
    self.direction = "down"

  def draw(self):
    for x, y in self.coordinates:
      square = self.canvas.create_rectangle(x, y, x + 30, y + 30, fill = "#99e0ff"  )                            
      self.squares.append(square)

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


    if y <= 600:
      self.canvas.after(500, self.next_turn)

window = tkinter.Tk()
window.title('Snake game')
canvas = tkinter.Canvas(window, width=900, height=600, bg='#000000')
canvas.pack()

my_snake = Snake(canvas)
my_snake.draw()

my_snake.next_turn()

window.mainloop()

