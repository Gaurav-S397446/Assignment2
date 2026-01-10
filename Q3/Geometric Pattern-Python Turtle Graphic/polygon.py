import turtle
from recursive_edge import draw_edge

# Make a shape with many sides using the above line
def draw_polygon(sides, length, depth):
    angle = 360 / sides  # how much to turn after each side
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)  # turn to start next side





