from manim import *
import numpy as np


def create_ll(coords: list[np.array], node_scale=1, text_scale=1, arrow_scale=1) -> VGroup:
    """Create a linked list composed of mobjects (`Circle`, `Text` and `Arrow`) for the animation, it links
    the nodes sequentially. Returns a `VGroup` containing the mobjects.
    """
    
    vgroup = VGroup()

    if (len(coords) == 1): # Case one node -> arrow not req
        pos = coords[0]
        circle = Circle(color=WHITE).shift(pos).scale(node_scale)
        value = Text(str(abs(int(pos[0]))), color=BLUE_D).shift(pos).scale(text_scale)
        vgroup.add(circle, value)
        return vgroup
    
    # Adding first node to group
    prev_coord = coords[0]
    circle = Circle(color=WHITE).shift(prev_coord).scale(node_scale)
    value = Text(str(abs(int(prev_coord[0]))), color=BLUE_D).shift(prev_coord).scale(text_scale)
    vgroup.add(circle, value)

    for c in coords[1:]:
        arrow_len = abs(c - prev_coord) - 2*np.array((node_scale, 0, 0))
        arrow = Arrow(start=circle.get_right(), end=circle.get_right()+arrow_len).scale(arrow_scale)
        circle = Circle(color=WHITE).shift(c).scale(node_scale)
        value = Text(str(abs(int(c[0]))), color=BLUE_D).shift(c).scale(text_scale)
        prev_coord = c
        vgroup.add(circle, value, arrow)
    
    return vgroup

class AnimatedAddNode(Scene):
    def construct(self):
        coords = [(0, 0, 0), (3, 0, 0), (6, 0, 0), (9, 0, 0)]
        coords = list(map(np.array, coords))
        ll_vgroup = create_ll(coords, node_scale=0.8)

        # Show linked list before insertion
        self.play(Create(ll_vgroup, lag_ratio=0))

        new_node_coords = [np.array((-3, 0, 0))]
        new_node_vgroup = create_ll(new_node_coords, node_scale=0.8)

        arrow_len = abs(coords[0] - new_node_coords[0]) - 2 * \
            np.array((0.8, 0, 0))
        new_arrow = Arrow(start=new_node_vgroup.get_right(),
                          end=new_node_vgroup.get_right()+arrow_len)

        # Show new node added
        self.wait(1)
        self.play(Create(Text("addNode(3)", font_size=48,
                              color=BLUE_D).shift(new_node_coords + DOWN*2)))
        self.wait(1)
        self.play(Create(new_node_vgroup, lag_ratio=0), Create(new_arrow))
        self.wait(2)

class AnimatedRemoveNode(Scene):
    def construct(self):
        coords = [(-6, 0, 0), (-3, 0, 0), (0, 0, 0), (3, 0, 0), (6, 0, 0)]
        coords = list(map(np.array, coords))
        ll_vgroup = create_ll(coords, node_scale=0.8)

        # Show linked list before removing operation
        self.play(Create(ll_vgroup, lag_ratio=0))
        
        # Show operation's name: removeNode(0)
        txt = Text("removeNode(0)", font_size=48, color=BLUE_D).shift(DOWN*3)
        self.play(Create(txt))

        # Show pointer for guiding operation
        ptr = Arrow(start=DOWN*2, end=DOWN, color=YELLOW).scale(1.5).shift(coords[0])
        self.play(Create(ptr))
        

        target = np.array((0, 0, 0))
        shift = np.array((3, 0, 0))
        for c in coords[1:]:
            if np.array_equal(target, c):
                self.wait(1)
                self.play(ptr.animate.shift(shift))
                self.wait(1)
                break
            self.wait(1)
            self.play(ptr.animate.shift(shift))