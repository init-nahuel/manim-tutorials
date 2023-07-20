from manim import *
import numpy as np


def create_ll_animation(coords: list[np.ndarray], nodes_scale=1, text_scale=1, arrows_scale=1) -> tuple[list[Circle], list[Text], list[Arrow]]:
    """Create the linked list mobjects and positioning on the given coordinates.
    Returns a tuple with each list containing the mobjects for nodes,
    node's value and arrows."""

    nodes: list[Mobject] = list()
    node_values: list[Text] = list()
    arrows: list[Mobject] = list()

    if (len(coords) == 1):
        pos = coords[0]
        nodes.append(Circle(color=WHITE).shift(pos).scale(nodes_scale))
        node_values.append(Text(str(abs(int(pos[0]))), color=BLUE_D, font_size=48).shift(
            pos).scale(text_scale))
        return (nodes, node_values, None)

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


class AnimatedAddNode(Scene):
    def construct(self):
        coords = [(0, 0, 0), (3, 0, 0), (6, 0, 0), (9, 0, 0)]
        coords = list(map(np.array, coords))
        nodes, node_values, arrows = create_ll_animation(
            coords, nodes_scale=0.8)

        # Show linked list before insertion
        nodes_animations = list(map(Create, nodes))
        node_value_animations = list(map(Create, node_values))
        arrows_animations = list(map(Create, arrows))
        self.play(*nodes_animations,
                  *node_value_animations,
                  *arrows_animations)

        new_node_coords = list([np.array((-3, 0, 0))])
        new_node, new_node_val, _ = create_ll_animation(
            new_node_coords, nodes_scale=0.8)
        new_node = new_node[0]
        new_node_val = new_node_val[0]

        arrows_len = abs(coords[1] - coords[0]) - 2 * \
            np.array((0.8, 0, 0))
        new_arrow = Arrow(start=new_node.get_right(),
                          end=new_node.get_right()+arrows_len)

        # Show new node added
        self.wait(1)
        self.play(Create(Text("addNode(3)", font_size=48,
                              color=BLUE_D).shift(new_node_coords + DOWN*2)))
        self.wait(1)
        self.play(Create(new_node), Create(new_node_val), Create(new_arrow))
        self.wait(2)
