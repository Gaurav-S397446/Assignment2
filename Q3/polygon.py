import turtle
from recursive_edge import draw_edge

# This function draws a polygon by repeating one edge multiple times
def draw_polygon(sides, length, depth):
    angle = 360 / sides        # calculate the turn angle based on number of sides
    for _ in range(sides):
        draw_edge(length, depth)  # draw one side using recursion
        turtle.right(angle)       # turn to draw the next side
