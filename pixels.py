import numpy as np


def is_input_valid(data):
    '''
    Checks if the JSON object passed to the route valid
    '''
    if 'dimensions' not in data or 'corner_points' not in data:
        print('error here')
        return False
    
    # Check dimensions
    m, n = data['dimensions']
    if type(m) != int or type(n) != int:
        print('dance')
        return False
    if m < 2 or n < 2:
        print('hello')
        return False

    # Check corner points
    corner_points = data['corner_points']
    if len(corner_points) != 4:
        print('nachle')
        return False
    for coordinates in corner_points:
        if len(coordinates) != 2:
            print('yaar')
            return False
    return True
    

def determine_corner_order(corner_points):
    '''
    Finds the correct order of corner points: left_top, left_bottom, right_top, right_bottom
    '''
    x = [el[0] for el in corner_points]
    y = [el[1] for el in corner_points]

    left_top = (min(x), max(y))
    left_bottom = (min(x), min(y))
    right_top = (max(x), max(y))
    right_bottom = (max(x), min(y))

    return left_top, left_bottom, right_top, right_bottom



def generate_pixels(m, n, corner_points):
    '''
    Generates the image pixels for m * n grid according to the specifications
    '''
    left_top, left_bottom, right_top, right_bottom = determine_corner_order(corner_points)
    
    # Create evenly spaced X values on top and bottom row of the rectangle
    x_top_sequence = np.linspace(left_top[0], right_top[0], n)
    x_bottom_sequence = np.linspace(left_bottom[0], right_bottom[0], n)
    all_x = np.linspace(x_top_sequence, x_bottom_sequence, m)

    # Create evenly spaced Y values on top and bottom row of the rectangle
    y_top_sequence = np.linspace(left_top[1], right_top[1], n)
    y_bottom_sequence = np.linspace(left_bottom[1], right_bottom[1], n)
    all_y = np.linspace(y_top_sequence, y_bottom_sequence, m)

    # Combine X and Y values to get grid of coordinates in the rectangle
    pixels = np.stack((all_x, all_y), axis=2)
    return pixels.tolist()
