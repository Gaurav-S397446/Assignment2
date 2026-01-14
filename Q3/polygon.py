import turtle
from recursive_edge import draw_edge

# Make a shape with many sides using the above line
def draw_polygon(sides, length, depth):
    """ 
    This function draws a full shape (polygon).
    It uses the draw edge function to draw each side.
    After drawing one side, the turtle turns to start the next side.
     
     Parameters:
        sides : int
            The total number of sides of the polygon
        length : float
            The length of each side before any recursive fractal subdivision.
        depth : int
            The recursion depth for each edge.
    """
    angle = 360 / sides  # how much to turn after each side
    count = 0
    while count < sides:
        draw_edge(length, depth, 0, -60, 120, -60)
        turtle.right(angle)  # turn to start next side
        count += 1
    





