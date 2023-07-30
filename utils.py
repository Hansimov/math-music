from manim import *
import itertools
import numpy as np


def calc_centroid(objs):
    """calculates the centroid of objects"""
    if len(objs) == 0:
        return np.array([0, 0, 0])
    return sum([obj.get_center() for obj in objs]) / len(objs)


def next_color(i):
    """
    * Colors - Manim Community v0.17.3
      * https://docs.manim.community/en/stable/reference/manim.utils.color.Colors.html
    """
    colors = [YELLOW, BLUE, RED, GREEN, PURPLE, ORANGE, PINK, TEAL, MAROON, GOLD]
    return colors[i % len(colors)]
