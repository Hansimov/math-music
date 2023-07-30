from manim import *
import numpy as np


def calc_centroid(objs):
    """calculates the centroid of objects"""
    if len(objs) == 0:
        return np.array([0, 0, 0])
    return sum([obj.get_center() for obj in objs]) / len(objs)
