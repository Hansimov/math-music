from manim import *
from utils import colorize_symbols


class EquationTransition(MovingCameraScene):
    def construct(self):
        equation_groups = [
            [
                "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} {{ \\vec{e_\\alpha} }} )= {{ \\vec{0} }}",
                "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} ) {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ \\mathrm{d}_\\tau }} ( {{ \\vec{e_\\mu} }} )= {{ \\vec{0} }}",
                "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} \,{{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} )\, {{ \\mathrm{d}_\\tau }} {{ x^\\nu }} = {{ \\vec{0} }}",
                "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }}  {{ v^\\nu }} {{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} )= {{ \\vec{0} }}",
                "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ v^\\nu }} ( {{ \Gamma }} ^ {{ \\beta }} _{{ {\\mu\\nu} }}\\vec{e_\\beta}) = {{ \\vec{0} }} ",
                "{{ a^\\alpha }} + {{ v^\\mu }} {{ v^\\nu }} {{ \Gamma }}^ {{ \\alpha }} _ {{ {\\mu\nu} }} = {{ 0 }}",
            ],
            # [
            #     "{{ \\frac{\\vec{F} }{m} }} = - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
            #     "- {{ \\nabla\\phi }}= - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
            #     "{{ \\nabla\\phi }} = {{ \\frac{GM}{r^2} }}{{ \\vec{e_r} }}",
            #     "\\nabla\\cdot({{ \\nabla\\phi }})={{ \\frac{GM}{r^2} }}{{ \\frac{4\\pi r^2}{V} }}",
            # ],
        ]

        equation_groups = [
            [self.process_equation(equation) for equation in equation_group]
            for equation_group in equation_groups
        ]

        for equation_group in equation_groups:
            for equation in equation_group:
                colorize_symbols(equation, ["\\mathrm{d}"])

        for equation_group in equation_groups:
            self.play(FadeIn(equation_group[0]), run_time=1)
            self.wait(0.8)
            for i in range(len(equation_group) - 1):
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
                self.wait(0.8)
            # self.clear()
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

    def process_equation(self, equation):
        equation = MathTex(equation)
        return equation


def main():
    equation_transition = EquationTransition()
    equation_transition.render()


if __name__ == "__main__":
    main()
