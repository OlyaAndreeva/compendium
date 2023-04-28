from tkinter import Tk, Canvas
from snake import Snake
from config import WIDTH, HEIGHT, SQUARE, center_window

def new_game():
    my_snake = Snake(window, canvas)
    my_snake.next_turn()

    window.bind('<Left>', lambda event: my_snake.set_direction('left'))
    window.bind('<Right>', lambda event: my_snake.set_direction('right'))
    window.bind('<Up>', lambda event: my_snake.set_direction('up'))
    window.bind('<Down>', lambda event: my_snake.set_direction('down'))
    window.bind('<space>', lambda event: my_snake.press_space())

#################################################################################################################################

window = Tk()
window.title('Snake game')
canvas = Canvas(window, width=WIDTH*SQUARE, height=HEIGHT*SQUARE, bg='#000000')
canvas.pack()

center_window(window)
new_game()

window.mainloop()
