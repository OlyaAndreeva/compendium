from tkinter import Tk, Canvas
from snake import Snake

window = Tk()
window.title('Snake game')
canvas = Canvas(window, width=900, height=600, bg='#000000')
canvas.pack()


my_snake = Snake(window, canvas)
my_snake.next_turn()

window.bind('<Left>', lambda event: my_snake.set_direction('left'))
window.bind('<Right>', lambda event: my_snake.set_direction('right'))
window.bind('<Up>', lambda event: my_snake.set_direction('up'))
window.bind('<Down>', lambda event: my_snake.set_direction('down'))

window.mainloop()
