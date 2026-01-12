import turtle
import recursive_edge  # this has our drawing function and keeps track of min/max positions
from polygon import draw_polygon  # this draws the whole polygon using recursive edges
def main():
    # Ask user for input
    sides = int(input("Enter the number of sides: "))  # how many sides the polygon will have
    length = int(input("Enter the side length: "))  # how long each side is
    depth = int(input("Enter the recursion depth: "))  # how detailed the edges should be

    turtle.speed()  # make the turtle draw fast
    turtle.shape("turtle")  # show the turtle icon
    turtle.tracer(0, 0)  # stop animation for first invisible pass (faster) 
