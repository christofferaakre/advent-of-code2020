import numpy as np


def rotate_vector(v, theta):
    x, y = v
    magnitude = np.sqrt(x ** 2 + y ** 2)
    angle = np.arctan2(y, x)

    new_angle = angle + theta
    return magnitude * np.array([
            np.cos(new_angle),
            np.sin(new_angle)
            ])
