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
    
     # ---------- FIRST PASS (measure size, invisible) ----------
    turtle.hideturtle()  # hide the turtle so we don't see first pass
    turtle.penup()  # lift pen so we don't draw yet
    turtle.goto(0, 0)  # start at the center
    turtle.setheading(0)  # face right
    turtle.pendown()  # put pen down to start drawing

    draw_polygon(sides, length, depth)  # draw once invisibly to measure bounds

