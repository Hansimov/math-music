from manim import *
from math import pow
from utils import calc_centroid
import numpy as np


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
config.disable_caching = True


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
    def create_dots(self):
        glow_dots = []
        dot_texts = []
        dots_num = 11
        for i in range(dots_num):
            dot = Dot3D(color=YELLOW, point=[i, 0, 0])
            # text = Text(str(i), color=YELLOW)
            # text.next_to(dot, DOWN)
            decimal = Integer(i, color=YELLOW)
            decimal.next_to(dot, DOWN)
            glow_dot = GlowDot(dot)
            glow_dots.append(glow_dot)
            dot_texts.append(decimal)

        init_wait_time_value_space = [1, 1, 0.5, 0.5]
        wait_time_value_space = (
            init_wait_time_value_space
            + np.linspace(
                0.5, 0.02, dots_num - len(init_wait_time_value_space)
            ).tolist()
        )
        for idx, glow_dot in enumerate(glow_dots):
            self.play(
                FadeIn(glow_dot),
                FadeIn(dot_texts[idx]),
                self.camera.frame.animate.move_to(calc_centroid(glow_dots[: idx + 1])),
                run_time=wait_time_value_space[idx],
            )
            self.wait(wait_time_value_space[idx])

    def set_camera_options(self):
        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=30 * DEGREES,
        )

    def construct(self):
        # self.set_camera_options()
        self.create_dots()
        # self.camera.frame_center = calc_centroid(self.mobjects)
        # self.camera.frame.scale(1.5)


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
