from manim import YELLOW, BLUE, RED, GREEN, PURPLE, ORANGE, PINK, TEAL, MAROON, GOLD
from manim import LEFT, RIGHT, UP, DOWN

from math import gcd
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


def next_text_position(i):
    positions = [DOWN, UP]
    return positions[i % len(positions)]


def next_play_time_for_dots_creation(
    i,
    start_idx=0,
    init_play_times=[1, 1, 0.75, 0.5, 0.5],
    mid_val=0.5,
    mid_num=5,
    min_val=0.15,
):
    i += start_idx
    if i >= len(init_play_times) + mid_num:
        return min_val
    if i >= len(init_play_times):
        return mid_val

    return init_play_times[i]


def is_reduced(numerator, denominator):
    return gcd(numerator, denominator) == 1


def count_reduced_fractions(m, n, frac):
    if m > n or n <= 0:
        return 0

    count = 0
    for i in range(m * frac, n * frac + 1):
        if is_reduced(i, frac):
            count += 1

    return count


def colorize_symbols(equation, symbols, color=YELLOW):
    if type(symbols) == str:
        symbols = [symbols]
    for symbol in symbols:
        equation.set_color_by_tex(symbol, color)
    return equation
