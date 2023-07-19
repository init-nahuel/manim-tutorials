from manim import *


class AnimatedLinkedList(Scene):
    def construct(self):

        circles: list[Mobject] = list()
        arrows: list[Mobject] = list()
        node_values: list[Text] = list()

        for i in range(-1, 9, 3):
            text = Text(str(i), font_size=48, color=BLUE_D)
            circle = Circle(color=WHITE).shift(i * RIGHT)
            text = text.shift(circle.get_center())
            circle = circle.surround(text)
            circles.append(circle)
            node_values.append(text)
            arrows.append(Arrow(start=circle.get_right(),
                          end=circle.get_right() + RIGHT*2))

        circles_animations = list(map(Create, circles))
        node_values_animations = list(map(Create, node_values))
        arrows_animations = list(map(Create, arrows))

        self.play(*circles_animations, *
                  node_values_animations, *arrows_animations)
