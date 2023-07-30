from manim import Circle, Dot
from manim import FadeIn, ThreeDScene, Scene, VGroup
from manim import RIGHT, YELLOW, DEGREES
from manim import config
from pathlib import Path

config.media_width = "25%"


from manim import Circle, Dot, FadeIn, ThreeDScene, VGroup, YELLOW


def create_glow(vmobject, rad=1, col=YELLOW):
    """Create a glowing effect around a given vmobject."""
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(
            radius=rad * (1.002 ** (idx**2)) / 400,
            stroke_opacity=0,
            fill_color=col,
            fill_opacity=0.2 - idx / 300,
        ).move_to(vmobject)
        glow_group.add(new_circle)
    return glow_group


class GlowingPoints(ThreeDScene):
    """A 3D scene that shows the evolution of glowing points.

    [1] A glowing point appears in the dark.
    [2] Then a new glowing point appears next to the previous point.
    [3] More glowing points appear, equally spaced, with increasing speed.
    """

    def construct(self):
        # Set the camera position and orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # [1] a glowing point, in dark
        point = Dot()
        self.add(create_glow(point))
        self.wait(1)

        # [2] then a new glowing point appear next to the previous point
        new_point = Dot().next_to(point, RIGHT)
        self.play(FadeIn(new_point))
        self.add(create_glow(new_point))
        self.wait(1)

        # [3] More glowing points appear, equally spaced, with increasing speed
        points = [point, new_point]
        for i in range(30):
            new_point = Dot().next_to(points[-1], RIGHT)
            self.play(FadeIn(new_point), run_time=1 / (i + 1))
            self.add(create_glow(new_point))
            points.append(new_point)

            # Adjust the camera position and orientation to keep all points in view
            self.set_camera_orientation(
                phi=75 * DEGREES, theta=-45 * DEGREES - i * 5 * DEGREES
            )


# To render the scene and output a video file:

scene = GlowingPoints()
scene.render()
