from manim import *


class AnimatedLinkedList(Scene):
    def construct(self):
        circles = [Create(Circle(color=WHITE).scale(0.5).shift(i * RIGHT).shift(UP))
                   for i in range(-8, 9, 3)]

        arrows = [Create(Arrow(start=c.get_right(), end=RIGHT))
                  for c in circles[0:len(circles)-1]]

        self.play(*circles, )
