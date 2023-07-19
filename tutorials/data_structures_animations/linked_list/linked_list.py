from manim import *


class AnimatedAddNodeToLinkedList(Scene):
    def construct(self):

        nodes: list[Mobject] = list()
        arrows: list[Mobject] = list()
        node_values: list[Text] = list()

        for i in range(-1, 9, 3):
            text = Text(str(abs(i)), font_size=48, color=BLUE_D)
            circle = Circle(color=WHITE).shift(i * RIGHT)
            text = text.shift(circle.get_center())
            circle = circle.surround(text).scale(1.5)
            nodes.append(circle)
            node_values.append(text)
            arrows.append(Arrow(start=circle.get_right(),
                          end=circle.get_right() + RIGHT*2))

        nodes_animations = list(map(Create, nodes))
        node_values_animations = list(map(Create, node_values))
        arrows_animations = list(map(Create, arrows))

        # Show linked list before insertion
        self.play(*nodes_animations,
                  *node_values_animations,
                  *arrows_animations)

        new_node_pos = nodes[0].get_center() - RIGHT*3
        new_node_value = Text(str(9), font_size=48,
                              color=BLUE_D).shift(new_node_pos)
        new_node = Circle(color=WHITE).shift(new_node_pos).surround(
            new_node_value).scale(1.5)

        # Show new node added
        self.wait(1)
        self.play(Create(new_node), Create(
            Arrow(start=new_node.get_right(), end=new_node.get_right() + RIGHT*2)),
            Create(new_node_value))
