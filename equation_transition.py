from manim import *
from utils import colorize_symbols


class EquationTransition(MovingCameraScene):
    def construct(self):
        equation_groups = [
            [
                "{{ \\frac{\\vec{F} }{m} }} = - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                "- {{ \\nabla\\phi }}= - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                "{{ \\nabla\\phi }} = {{ \\frac{GM}{r^2} }}{{ \\vec{e_r} }}",
                "\\nabla\\cdot({{ \\nabla\\phi }})={{ \\frac{GM}{r^2} }}{{ \\frac{4\\pi r^2}{V} }}",
            ],
        ]

        equation_groups = [
            [MathTex(equation) for equation in equation_group]
            for equation_group in equation_groups
        ]

        for equation_group in equation_groups:
            for i in range(len(equation_group) - 1):
                # self.wait(0.5)
                eq_old = equation_group[i]
                eq_new = equation_group[i + 1]
                self.play(
                    TransformMatchingTex(
                        eq_old,
                        eq_new,
                        transform_mismatches=True,
                        fade_transform_mismatches=False,
                    ),
                    run_time=1,
                )
            self.wait(0.5)


def main():
    equation_transition = EquationTransition()
    equation_transition.render()


if __name__ == "__main__":
    main()
