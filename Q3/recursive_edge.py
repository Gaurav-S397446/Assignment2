import turtle

# These numbers help to know how far turtle goes so we can align drawing in center
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
def draw_edge(length, depth, *turns):
    """
    This function recursively draws a fractal using turtle graphic library.
    If depth is 0, it draws a simple straight line.
    If depth is more than 0, it breaks the line into smaller parts
    and draws them again and again.
    
     Parameters:
        length  (float): The length of the line segment to draw at current recursion level.
        depth  (int): The recursion depth. A value of 0 draws a straight line. Higher values 
                        recursively subdivide the line.
        **turns (int) :A variable number of angles (in degrees) to turn the turtle at each step. 
    """
    if depth == 0:
        turtle.forward(length)  # just draw straight line
        update_bounds()  # remember where we are
        return
    length /= 3  # make the line shorter for next step
    
    for turn in turns:
        turtle.left(turn)
        draw_edge(length, depth - 1, *turns)
    