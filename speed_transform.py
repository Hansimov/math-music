from manim import *
from math import pow
from utils import calc_centroid
import numpy as np
from fractions import Fraction


def set_render_config(quality="low"):
    if quality == "low":
        pixel_ratio = 0.25

        config.frame_rate = 30
    elif quality == "medium":
        pixel_ratio = 0.5
        config.frame_rate = 30
    else:
        pixel_ratio = 1
        config.frame_rate = 60

    config.pixel_width = int(1920 * pixel_ratio)
    config.pixel_height = int(1080 * pixel_ratio)


set_render_config("high")
# config.disable_caching = True


def create_glow_for_dot(
    dot,
    circles_num=60,
    glow_radius_ratio=10,
    color=None,
    decay_func=lambda i: 0.8 / (pow(i, 1.2) + 0.001),
):
    glow = VGroup()
    max_glow_radius = dot.radius * glow_radius_ratio
    for i in range(circles_num):
        circle = Circle(
            arc_center=dot.get_center(),
            radius=i / circles_num * max_glow_radius,
            fill_opacity=decay_func(i),
            fill_color=dot.color if color is None else color,
            stroke_opacity=0,
        )
        glow.add(circle)
    return glow


class GlowDot(VGroup):
    def __init__(
        self,
        dot,
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.dot = dot
        self.glow = create_glow_for_dot(dot)
        self.add(self.dot, self.glow)


class SpeedTransform(MovingCameraScene):
    MAX_INTEGER = 4

    def create_integers(self, axis="x"):
        glow_dots = []
        dot_texts = []
        dots_num = self.MAX_INTEGER
        for i in range(dots_num):
            decimal = Integer(i, color=YELLOW)
            wait_time_value_space = np.linspace(0.1, 0.02, dots_num).tolist()
            if axis == "x":
                dot = Dot3D(color=YELLOW, point=[i, 0, 0])
                decimal.next_to(dot, DOWN)
                init_wait_time_value_space = [0.75, 0.5, 0.25]
                wait_time_value_space = (
                    init_wait_time_value_space
                    + np.linspace(
                        init_wait_time_value_space[-1],
                        0.02,
                        dots_num - len(init_wait_time_value_space),
                    ).tolist()
                )
            elif axis == "y":
                dot = Dot3D(color=YELLOW, point=[0, i, 0])
                decimal.next_to(dot, LEFT)
            else:
                dot = Dot3D(color=YELLOW, point=[0, 0, i])
                decimal.next_to(dot, RIGHT)

            glow_dot = GlowDot(dot)
            glow_dots.append(glow_dot)
            dot_texts.append(decimal)

        for idx, glow_dot in enumerate(glow_dots):
            self.play(
                FadeIn(glow_dot),
                FadeIn(dot_texts[idx]),
                self.camera.frame.animate.move_to(calc_centroid(glow_dots[: idx + 1])),
                run_time=wait_time_value_space[idx],
            )
            self.wait(wait_time_value_space[idx])

    def create_fractions(self, axis="x", frac=2):
        numbers = []
        for i in range(1, self.MAX_INTEGER * frac + 1):
            if i % frac != 0:
                fraction_value = Fraction(i, frac)
                numbers.append(
                    {
                        "frac": fraction_value,
                        "float": float(fraction_value),
                        "tex": f"\\frac{{{i}}}{{{frac}}}",
                    }
                )
        dots_num = len(numbers)

        glow_dots = []
        dot_texts = []
        for idx, number in enumerate(numbers):
            dot = Dot3D(color=BLUE, point=[number["float"], 0, 0])
            tex_text = MathTex(number["tex"], color=BLUE, font_size=int(48 / frac))
            tex_text.next_to(dot, DOWN)

            glow_dot = GlowDot(dot)
            glow_dots.append(glow_dot)
            dot_texts.append(tex_text)

        for idx, glow_dot in enumerate(glow_dots):
            self.play(
                FadeIn(glow_dot),
                FadeIn(dot_texts[idx]),
                self.camera.frame.animate.move_to(calc_centroid(glow_dots[: idx + 1])),
                run_time=0.1,
            )
            self.wait(0.1)

    def set_camera_options(self):
        self.camera.frame.rotate(75 * DEGREES, axis=[1, 1, 0])

    def construct(self):
        self.set_camera_options()
        self.create_integers(axis="x")
        self.create_fractions(axis="x", frac=2)
        self.create_fractions(axis="x", frac=3)
        self.create_fractions(axis="x", frac=4)
        # self.create_dots(axis="y")


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
