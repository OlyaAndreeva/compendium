WIDTH = 90
HEIGHT = 60
SQUARE = 15
SPEED = 25
FOOD_NUMBER = 10

def center_window(window):
    window.update()
    x = (window.winfo_screenwidth() - window.winfo_width())//2
    y = (window.winfo_screenheight() - window.winfo_height())//4
    window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")