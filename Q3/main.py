import turtle
import recursive_edge # handles the recursive edge drawing and stores boundary values
from polygon import draw_polygon  # draws the complete polygon

def main():
    # Take input from the user
    sides = int(input("Enter the number of sides: "))  # number of sides for the polygon
    length = int(input("Enter the side length: "))     # length of each side
    depth = int(input("Enter the recursion depth: ")) # how detailed the edges should be

    turtle.speed()          # make drawing as fast as possible
    turtle.shape("turtle")  # show turtle cursor
    turtle.tracer(0, 0)    # turn off animation for faster drawing

    # ---- First draw (hidden) to figure out the size ----
    turtle.hideturtle()      # hide turtle during first pass
    turtle.penup()         # move without drawing
    turtle.goto(0, 0)      # start from the center
    turtle.setheading(0)    # face to the right
    turtle.pendown()       # start tracking movement

    draw_polygon(sides, length, depth)  # draw once to get min/max positions

    # Work out the center of the drawing
    center_x = (recursive_edge.min_x + recursive_edge.max_x) / 2
    center_y = (recursive_edge.min_y + recursive_edge.max_y) / 2

    # ---- Second draw (visible and centered) ----
    turtle.clear()    # clear the first invisible drawing
    turtle.penup()     # pick the pen up so it doesn’t draw while moving
    turtle.goto(-center_x, -center_y)  # shift drawing so it appears centered
    turtle.setheading(0)    # reset direction to the right
    turtle.pendown()  # put the pen back down to start drawing

    turtle.showturtle()         # show turtle for final drawing
    turtle.tracer(1)            # turn animation back on

    draw_polygon(sides, length, depth)  # draw the final polygon

    turtle.mainloop()           # keep the window open

main()
