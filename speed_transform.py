from manim import *
from math import pow


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


class SpeedTransform(ThreeDScene):
    def create_dots(self):
        for i in range(5):
            fadein_time = 2 - i / 5
            dot = Dot3D(color=YELLOW, point=[i, 0, 0])
            glow_dot = GlowDot(dot)
            self.play(FadeIn(glow_dot), run_time=fadein_time)
            # self.wait()

    def set_camera_options(self):
        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=30 * DEGREES,
        )

    def construct(self):
        self.set_camera_options()
        self.create_dots()


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
