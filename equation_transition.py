from manim import *


class EquationTransition(MovingCameraScene):
    def construct(self):
        eq1 = MathTex("\\frac{\\vec{F}}{m}", "=-\\frac{GM}{r^2}\\vec{e_r}")
        eq2 = MathTex("-\\nabla\\phi", "=-\\frac{GM}{r^2}\\vec{e_r}")
        eq3 = MathTex("\\nabla\\phi", "=\\frac{GM}{r^2}\\vec{e_r}")
        equations = [eq1, eq2, eq3]
        for i in range(len(equations) - 1):
            self.wait(0.5)
            eq_old = equations[i]
            eq_new = equations[i + 1]
            self.play(
                TransformMatchingTex(
                    eq_old,
                    eq_new,
                    transform_mismatches=True,
                    fade_transform_mismatches=True,
                ),
                run_time=1,
            )

        self.wait(0.5)


def main():
    equation_transition = EquationTransition()
    equation_transition.render()


if __name__ == "__main__":
    main()
