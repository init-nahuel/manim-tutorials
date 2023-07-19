from manim import *


class CreateCircle(Scene):
    """Animation for create a circle"""

    def construct(self):
        circle = Circle()  # Create a circle

        # Set the color for the circle and opacity
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(circle))  # Show animation


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=1)
        self.play(Create(circle), Create(square))


class AnimatedSquareToCircle(Scene):
    """Tutorial for create a scene and make animations on changes to mobjects."""

    def construct(self):
        circle = Circle()  # Create a circle
        square = Square()  # Create a square

        self.play(Create(square))  # Show square animation on screen

        # Show square's rotation on screen
        self.play(square.animate.rotate(PI/4))

        # Show transformation from square to circle
        self.play(ReplacementTransform(square, circle))

        # Show circle's coloring
        self.play(circle.animate.set_fill(PINK, opacity=0.5))


class DifferentRotations(Scene):
    """Showing the interpretations in animate and Rotate functions for certain animations.
    When making rotation the interpretations of rotations are very different."""

    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)

        self.play(left_square.animate.rotate(PI), Rotate(
            right_square, angle=PI), run_time=2)
        self.wait()
