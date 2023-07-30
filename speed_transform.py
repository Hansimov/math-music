from manim import *


def create_glow(
    obj,
    num_circles=60,
    max_radius=0.6,
    color=YELLOW,
    decay_func=lambda i: 1 / i * i,
):
    glow = VGroup()
    for i in range(1, num_circles):
        circle = Circle(
            radius=i * max_radius / num_circles,
            fill_opacity=decay_func(i),
            fill_color=color,
            stroke_opacity=0,
        )
        glow.add(circle)
    return glow


class SpeedTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        dot = Dot3D()
        glow = create_glow()
        # self.add_fixed_in_frame_mobjects(glow)
        glowed_dot = VGroup(dot, glow)
        self.play(FadeIn(glowed_dot))
        # self.play(FadeIn(glow))
        self.wait()


def main():
    speed_transform = SpeedTransform()
    speed_transform.render()


if __name__ == "__main__":
    main()
