from manim import *
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1].resolve()))
from utils import calc_centroid


class TestAxisRotate(MovingCameraScene):
    def construct(self):
        x_dots = [Dot3D(point=[i, 0, 0]) for i in range(5)]
        y_dots = [Dot3D(point=[0.707 * i, 0.707 * i, 0]) for i in range(5)]
        z_dots = [Dot3D(point=[0, i, 0]) for i in range(5)]
        self.add(*x_dots, *y_dots, *z_dots)
        self.camera.frame.move_to(calc_centroid(x_dots + y_dots + z_dots))


if __name__ == "__main__":
    test_axis_rotate = TestAxisRotate()
    test_axis_rotate.render()
