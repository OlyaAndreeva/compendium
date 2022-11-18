# write a function that reverses an integer
import math

def reverse(value):
    result = 0
    while value > 0:
        remain = value % 10
        value = math.floor(value / 10) # 12.3
        result = result * 10
        result = result + remain
     
    return result 

print(reverse(123)) 