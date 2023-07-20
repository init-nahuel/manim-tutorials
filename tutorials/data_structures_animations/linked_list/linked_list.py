from manim import *
import numpy as np


def create_ll_animation(coords: list[np.ndarray], nodes_scale=1, text_scale=1, arrows_scale=1) -> tuple[list[Mobject]]:
    """Create the linked list mobjects and positioning on the given coordinates.
    Returns a tuple with each list containing the mobjects for nodes,
    node's value and arrows."""

    nodes: list[Mobject] = list()
    node_values: list[Text] = list()
    arrows: list[Mobject] = list()

    if (len(coords) == 1):
        nodes.append(Circle(color=WHITE).shift(coords[0]).scale(nodes_scale))
        node_values.append(Text(str(abs(int(i[0])))).scale(text_scale))
        return (nodes, node_values, arrow)

    arrows_len = abs(coords[1] - coords[0]) - 2*np.array((nodes_scale, 0, 0))

    for i in coords:
        text = Text(str(abs(int(i[0]))), font_size=48,
                    color=BLUE_D).shift(i).scale(text_scale)
        node_values.append(text)

        node = Circle(color=WHITE).shift(i).scale(nodes_scale)
        nodes.append(node)

        arrow = Arrow(start=node.get_right(),
                      end=node.get_right() + arrows_len).scale(arrows_scale)
        arrows.append(arrow)

    # deleting last arrow
    arrows.pop()

    return (nodes, node_values, arrows)


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
        arrows.pop()

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
        self.play(Create(Text("addNode(9)", font_size=48,
                  color=BLUE_D).shift(new_node_pos + DOWN)))
        self.wait(1)
        self.play(Create(new_node), Create(
            Arrow(start=new_node.get_right(), end=new_node.get_right() + RIGHT*2)),
            Create(new_node_value))
        self.wait(2)
