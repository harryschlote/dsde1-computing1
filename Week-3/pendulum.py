'''doc'''
import math
def period(length, grav):
    '''doc'''
    if grav == 0:
        raise ValueError('cant divide by 0')
    return math.sqrt(length / grav) * 2  * 3.141592653
    