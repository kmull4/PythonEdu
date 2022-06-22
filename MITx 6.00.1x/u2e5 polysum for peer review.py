'''
Regular Polygons: polysum

A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon

Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. This
function should sum the area and square of the perimeter of the regular
polygon. The function returns the sum, rounded to 4 decimal places.

+++ IMPORTANT NOTE +++
You must upload a .py file. Any code you enter in the box will have its
spacing removed, so will be unreadable by your peers. In the box type in
anything, for example, "attached".
'''
# import math to use tangent function and pi constant
import math

def polysum(n, s):
    '''
    Parameters
    ----------
    n : int
        number of sides
    s : int
        side length
    Returns
    -------
    sum of the area and square of the preimeter of the regular
        polygon
    '''
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    perim = n * s
    return round(area + perim**2, 4)