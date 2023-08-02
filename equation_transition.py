from manim import *


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
                    "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} {{ \\vec{e_\\alpha} }} ) {{ = }} {{ \\vec{0} }}",
                    "{{ \\mathrm{d}_\\tau }} ( {{ v^\\alpha }} ) {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ \\mathrm{d}_\\tau }} ( {{ \\vec{e_\\mu} }} ) {{ = }} {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} \,{{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} )\, {{ \\mathrm{d}_\\tau }} {{ x^\\nu }} {{=}} {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }}  {{ v^\\nu }} {{ \\mathrm{d}_{x^\\nu} }} ( {{ \\vec{e_\\mu} }} ) {{=}} {{ \\vec{0} }}",
                    "{{ a^\\alpha }} {{ \\vec{e_\\alpha} }} + {{ v^\\mu }} {{ v^\\nu }} ( {{ \Gamma }} ^ {{ \\beta }} _{{ {\\mu\\nu} }}\\vec{e_\\beta}) {{=}} {{ \\vec{0} }} ",
                    "{{ a^\\alpha }} + {{ v^\\mu }} {{ v^\\nu }} {{ \Gamma }}^ {{ \\alpha }} _ {{ {\\mu\nu} }} {{=}} {{ 0 }}",
                ],
                "animation": "each",
            },
            {
                "texts": ["牛顿万有引力定律"],
                "equations": [
                    "{{ \\frac{\\vec{F} }{m} }} {{=}} - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                    "- {{ \\nabla\\phi }} {{=}} - {{ \\frac{GM}{r^2} }} {{ \\vec{e_r} }}",
                    "{{ \\nabla\\phi }} {{=}} {{ \\frac{GM}{r^2} }}{{ \\vec{e_r} }}",
                    "\\nabla\\cdot({{ \\nabla\\phi }}) {{=}} {{ \\frac{GM}{r^2} }}{{ \\frac{4\\pi r^2}{V} }}",
                ],
                "animation": "each",
            },
            {
                "texts": [
                    "里奇张量 <sub>(Ricci tensor)</sub>",
                    "里奇曲率 <sub>(Ricci scalar)</sub>",
                    "(合体)",
                ],
                "equations": [
                    "R_{\\mu \\nu }",
                    "R",
                    "{{ R_{\\mu \\nu } }} - {\\frac {1}{2}}g_{\\mu \\nu } {{ R }}",
                ],
                "animation": "combine",
            },
        ]

        equation_groups = [
            {
                "texts": [self.process_text(text) for text in equation_group["texts"]],
                "equations": [
                    self.process_equation(equation)
                    for equation in equation_group["equations"]
                ],
                "animation": equation_group["animation"],
            }
            for equation_group in equation_groups
        ]

        for equation_group in equation_groups:
            texts = equation_group["texts"]
            equations = equation_group["equations"]
            animation_type = equation_group["animation"]

            if animation_type == "each":
                texts = [text.move_to(UP * 2.5) for text in texts]
                self.play(Write(texts[0]), run_time=1.2)
                for i in range(len(texts) - 1):
                    self.play(
                        TransformMatchingShapes(
                            texts[i],
                            texts[i + 1],
                        ),
                        run_time=1,
                        transform_mismatches=False,
                        fade_transform_mismatches=False,
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
            else:  # animation_type == "combine":
                single_equations_group = VGroup()
                for i in range(len(texts) - 1):
                    single_equations_group.add(*(texts[i], equations[i]))
                    single_equations_group.arrange(DOWN, buff=0.5)
                single_equations_group.move_to(LEFT * 3)

                for obj in single_equations_group:
                    self.play(Write(obj), run_time=1.2)

                single_equations = [
                    obj
                    for obj in single_equations_group.submobjects
                    if isinstance(obj, MathTex)
                ]

                single_equations = Group(*equations[:-1]).copy()
                combined_equation = equations[-1]
                combined_equation.move_to(RIGHT * 3)
                self.wait(0.5)
                self.play(
                    TransformMatchingShapes(
                        single_equations,
                        combined_equation,
                    ),
                    run_time=1.5,
                )

            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

    def process_equation(self, equation):
        equation = MathTex(equation)
        equation = self.colorize_symbols(equation, ["\\mathrm{d}"])
        return equation

    def process_text(self, text):
        text = MarkupText(text)
        return text

    def colorize_symbols(self, equation, symbols, color=YELLOW):
        if type(symbols) == str:
            symbols = [symbols]
        for symbol in symbols:
            equation.set_color_by_tex(symbol, color)
        return equation


def main():
    equation_transition = EquationTransition()
    equation_transition.render()


if __name__ == "__main__":
    main()
