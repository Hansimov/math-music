from manim import *
from math import pow


def create_glow_for_dot(
    dot,
    circles_num=60,
    glow_radius_ratio=10,
    color=None,
    decay_func=lambda i: 0.8 / (pow(i, 1) + 0.001),
):
    glow = VGroup()
    max_glow_radius = dot.radius * glow_radius_ratio
    for i in range(circles_num):
        circle = Circle(
            radius=i / circles_num * max_glow_radius,
            fill_opacity=decay_func(i),
            fill_color=dot.color if color is None else color,
            stroke_opacity=0,
        )
        glow.add(circle)
    return glow


class GlowingDot(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.dot = Dot3D(color=YELLOW)
        self.add(self.dot)
        self.glow = create_glow_for_dot(self.dot)
        self.add(self.glow)


class SpeedTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        glowing_dot = GlowingDot()
        self.play(FadeIn(glowing_dot))
        self.wait()


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
