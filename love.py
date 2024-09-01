import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # Set speed to maximum (fastest speed is 0)
bgcolor("black")
color("red")

penup()  # Lift the pen to move without drawing
goto(0, 0)  # Go to the center of the screen
pendown()  # Start drawing

for i in range(6000):
    x = hearta(i / 100) * 20  # Scale the heart by dividing i
    y = heartb(i / 100) * 20  # Scale the heart by dividing i
    goto(x, y)

done()
