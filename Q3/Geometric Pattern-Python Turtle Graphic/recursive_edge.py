import turtle

# These numbers help to know how far turtle goes so we can put drawing in center
min_x = max_x = min_y = max_y = 0

def update_bounds():
    """
    This function below checks where the turtle is right now.
    It saves the left, right, top, and bottom limits of the drawing.
    This helps us later to move the drawing to the center.
    """
    global min_x, max_x, min_y, max_y
    x, y = turtle.position()
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
# This is the main drawing line that can make itself smaller and repeat
def draw_edge(length, depth):
    """
    This function below will draw one side of the shape.
    If depth is 0, it draws a simple straight line.
    If depth is more than 0, it breaks the line into smaller parts
    and draws them again and again.
    """
    if depth == 0:
        turtle.forward(length)  # just draw straight line
        update_bounds()  # remember where we are
        return
    length /= 3  # make the line shorter for next step

    draw_edge(length, depth - 1)  # draw first small line
    turtle.right(60)  # turn a little
    draw_edge(length, depth - 1)  # draw second line
    turtle.left(120)  # turn other way
    draw_edge(length, depth - 1)  # draw third line
    turtle.right(60)  # turn back
    draw_edge(length, depth - 1)  # draw last line