import numpy as np
import cv2 as cv
from scipy.spatial.transform import Rotation

def line_intersection(line1, line2, descale=True, parallel=False):
    '''
    This function finds the intersection point of two lines in 2D space.

    Args:
    line1: A list of three numbers representing the coefficients of the first line equation (a, b, c) in the form ax + by + c = 0.
    line2: A list of three numbers representing the coefficients of the second line equation (a, b, c) in the form ax + by + c = 0.
    descale: A boolean flag indicating whether to normalize the intersection point by dividing by the third coefficient.
    parallel: A boolean flag indicating whether you want a result for parallel lines.

    Returns:
    A tuple of three numbers representing the intersection point (x, y, 1) if the lines intersect, or None if the lines are parallel or coincident.
    '''
    point_vector = np.cross(line1, line2)
    if point_vector[2] != 0 and descale:
        (x,y) = point_vector[0:2]/point_vector[2]
        return (x,y,1)
    elif point_vector[2] != 0 and not descale and not parallel:
        return (point_vector[0], point_vector[1], point_vector[2])
    elif point_vector[2] == 0 and parallel:
        return (point_vector[0], point_vector[1], point_vector[2])
    else:
        return None

def point_intersection(point1, point2):
    '''
    This function finds the line intersecting two points in 2D space.

    Args:
    line1: A list of three numbers representing the homogeneous coordinates of a point (zx, zy, z) from ax + by + c = 0.
    line2: A list of three numbers representing the homogeneous coordinates of the second point (zx, zy, z) from ax + by + c = 0.
    
    Returns:
    A tuple of three numbers representing the coeeficients of the line equation (a, b, c).
    '''
    (a,b,c) = np.cross(point1, point2)
    return (a,b,c)