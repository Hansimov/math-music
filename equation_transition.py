from manim import *
from utils import colorize_symbols


class EquationTransition(MovingCameraScene):
    def construct(self):
        equation_groups = [
            {
                "texts": [
                    "万恶的爱因斯坦求和约定",
                    "<s>万恶的</s>爱因斯坦求和约定",
                    "爱因斯坦求和约定",
                ],
                "equations": [
                    "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} {{ \\vec{e_\\alpha} }} )= {{ \\vec{0} }}",
                    "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} ) {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ \\mathrm{d}_\\tau }} ( {{ \\vec{e_\\mu} }} )= {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} \,{{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} )\, {{ \\mathrm{d}_\\tau }} {{ x^\\nu }} = {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }}  {{ v^\\nu }} {{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} )= {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ v^\\nu }} ( {{ \Gamma }} ^ {{ \\beta }} _{{ {\\mu\\nu} }}\\vec{e_\\beta}) = {{ \\vec{0} }} ",
                    "{{ a^\\alpha }} + {{ v^\\mu }} {{ v^\\nu }} {{ \Gamma }}^ {{ \\alpha }} _ {{ {\\mu\nu} }} = {{ 0 }}",
                ],
            },
            {
                "texts": ["牛顿万有引力定律"],
                "equations": [
                    "{{ \\frac{\\vec{F} }{m} }} = - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                    "- {{ \\nabla\\phi }}= - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                    "{{ \\nabla\\phi }} = {{ \\frac{GM}{r^2} }}{{ \\vec{e_r} }}",
                    "\\nabla\\cdot({{ \\nabla\\phi }})={{ \\frac{GM}{r^2} }}{{ \\frac{4\\pi r^2}{V} }}",
                ],
            },
        ]

        equation_groups = [
            {
                "texts": [self.process_text(text) for text in equation_group["texts"]],
                "equations": [
                    self.process_equation(equation)
                    for equation in equation_group["equations"]
                ],
            }
            for equation_group in equation_groups
        ]

        for equation_group in equation_groups:
            equations = equation_group["equations"]
            texts = equation_group["texts"]

            self.play(Write(texts[0]), run_time=1.2)
            for i in range(len(texts) - 1):
                self.play(
                    TransformMatchingShapes(
                        texts[i],
                        texts[i + 1],
                    ),
                    run_time=1,
                    transform_mismatches=False,
                    fade_transform_mismatches=True,
                )

            self.wait(0.5)

            self.play(FadeIn(equations[0]), run_time=1)
            self.wait(0.8)
            for i in range(len(equations) - 1):
                eq_old = equations[i]
                eq_new = equations[i + 1]
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
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

    def process_equation(self, equation):
        equation = MathTex(equation)
        equation = colorize_symbols(equation, ["\\mathrm{d}"])
        return equation

    def process_text(self, text):
        text = MarkupText(text).move_to(UP * 2.5)
        return text


def main():
    equation_transition = EquationTransition()
    equation_transition.render()


if __name__ == "__main__":
    main()
