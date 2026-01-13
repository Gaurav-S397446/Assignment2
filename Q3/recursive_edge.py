import turtle

# These variables keep track of how far the turtle moves in each direction
min_x = max_x = min_y = max_y = 0

def update_bounds():
    # Check the turtle’s current position and update the limits if needed
    global min_x, max_x, min_y, max_y
    x, y = turtle.position()
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# This function draws one edge using recursion
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)   # draw a straight line when recursion ends
        update_bounds()          # store the current position
        return

    length /= 3                  # reduce the length for smaller segments

    draw_edge(length, depth - 1)  # draw the first part
    turtle.right(60)              # turn right
    draw_edge(length, depth - 1)  # draw the second part
    turtle.left(120)              # turn left
    draw_edge(length, depth - 1)  # draw the third part
    turtle.right(60)              # turn back to original direction
    draw_edge(length, depth - 1)  # draw the last part
