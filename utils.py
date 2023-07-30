from manim import *


def calc_centroid(objs):
    """calculates the centroid of objects"""
    return sum([obj.get_center() for obj in objs]) / len(objs)
