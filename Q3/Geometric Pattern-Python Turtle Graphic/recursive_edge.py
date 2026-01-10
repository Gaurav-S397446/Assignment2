import turtle

# These numbers help to know how far turtle goes so we can put drawing in center
min_x = max_x = min_y = max_y = 0

def update_bounds():
    # Check turtle's place and save the farthest points
    global min_x, max_x, min_y, max_y
    x, y = turtle.position()
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
