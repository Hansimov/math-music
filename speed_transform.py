from manim import *
from math import pow, gcd
from utils import calc_centroid
import numpy as np
from fractions import Fraction
from utils import (
    next_color,
    next_text_position,
    is_reduced,
    count_reduced_fractions,
    next_play_time_for_dots_creation,
)


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
    dot_creation_idx = 0

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
            if frac == 1:
                numbers.append(
                    {
                        "frac": i,
                        "float": i,
                        "tex": f"{i}",
                    }
                )
            else:
                if is_reduced(i, frac):
                    fraction_value = Fraction(i, frac)
                    numbers.append(
                        {
                            "frac": fraction_value,
                            "float": float(fraction_value),
                            "tex": f"\\frac{{{i}}}{{{frac}}}" if frac > 1 else f"{i}",
                        }
                    )

        glow_dots = []
        dot_texts = []
        tmp_color = next_color(frac - 1)
        text_pos = next_text_position(frac - 1)
        for idx, number in enumerate(numbers):
            dot = Dot3D(
                radius=0.1 / frac,
                color=tmp_color,
                point=[number["float"], 0, 0],
            )
            tex_text = MathTex(
                number["tex"],
                color=tmp_color,
                font_size=int(48 / frac),
            )
            tex_text.next_to(dot, text_pos)

            glow_dot = GlowDot(dot)
            glow_dots.append(glow_dot)
            dot_texts.append(tex_text)

        start_reduced_idx = 0
        for i in range(self.MAX_INTEGER):
            play_time = next_play_time_for_dots_creation(
                i, start_idx=self.dot_creation_idx
            )
            self.dot_creation_idx += 1

            if frac == 1:
                glow_dot_chunk = [glow_dots[i]]
                dot_text_chunk = [dot_texts[i]]
            else:
                reduced_fractions_count = count_reduced_fractions(i, i + 1, frac)
                glow_dot_chunk = glow_dots[
                    start_reduced_idx : start_reduced_idx + reduced_fractions_count
                ]
                dot_text_chunk = dot_texts[
                    start_reduced_idx : start_reduced_idx + reduced_fractions_count
                ]
                start_reduced_idx += reduced_fractions_count

            glow_dot_anims = [FadeIn(glow_dot) for glow_dot in glow_dot_chunk]
            dot_text_anims = [FadeIn(dot_text) for dot_text in dot_text_chunk]
            self.play(
                *glow_dot_anims,
                # self.camera.frame.animate.move_to(glow_dot_chunk[-1]),
                run_time=play_time,
            )
            self.play(*dot_text_anims, run_time=play_time)

    def construct(self):
        for i in range(1, 5):
            self.create_fractions(axis="x", frac=i)
        # self.create_integers(axis="y")


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
