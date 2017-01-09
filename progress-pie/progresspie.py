#!/bin/python
"""
Python v2.7.12
@author: Kunal Baweja
Facebook Hackercup 2017 - Qualification Round
Progress-Pie: https://www.facebook.com/hackercup/problem/1254819954559001/
"""

from math import hypot, acos, pi

def in_circle(point, center, radius):
    """
    check if point (x,y) lies in a circle of radius
    'radius' around 'center'
    point = (x, y)
    center = (cx, cy)
    radius = r
    """
    distance = hypot(center[0] - point[0], center[1] - point[1])

    """
    Whenever a point (X, Y) is queried, it's guaranteed that all points within
    a distance of 10-6 of (X, Y) are the same color as (X, Y).
    """
    distance = round(distance, 6) - (10 ** -6)

    return radius >= 0 and distance <= radius


def get_angle(a, b, center=(0.0, 0.0)):
    """
    get clockwise angle between two points
    a and b

    returns angle in 360 degree measure but
    clockwise direction
    """
    a = (a[0] - center[0], a[1] - center[1])
    b = (b[0] - center[0], b[1] - center[1])

    #dot product
    _angle = (a[0] * b[0]) + (a[1] * b[1])

    #divide by vector lengths
    _angle /= hypot(a[0], a[1])
    _angle /= hypot(b[0], b[1])

    #get angle in radians from cos(_angle)
    _angle = acos(_angle)

    #convert to 360 deg scale clockwise
    _angle = _angle * 180 / pi
    _determinant = (a[0] * b[1]) - (a[1] * b[0])

    if _determinant < 0:
        _angle = _angle
    else:
        _angle = 360 - _angle

    return _angle


def main():
    """
    check point black or white
    """
    CENTER = (50.0, 50.0)
    RADIUS = 50.0
    TOP = (50.0, 100.0)
    P = X = Y = None
    result = None

    T = int(raw_input().strip())

    for test in xrange(1, T + 1):
        P, X, Y = map(float, raw_input().strip().split())
        point = (X, Y)
        result = 'Case #' + str(test) +': '

        if P == 0 or not in_circle(point, CENTER, RADIUS):
            result += 'white'

        else:
            sector_angle = P * (360 / 100.0) #percentage
            point_angle = get_angle(TOP, point, CENTER) #actual angle

            if point_angle <= sector_angle:
                result += 'black'
            else:
                result += 'white'

        print result

if __name__ == '__main__':
    main()
