from manim import *

class TuringMachine(Scene):
    def construct(self):
        # Create a tape with 10 cells
        tape_length = 10
        cell_width = 1
        tape = VGroup(*[Square(side_length=cell_width) for _ in range(tape_length)])
        tape.arrange(RIGHT, buff=0)
        
        # Add labels to the tape cells
        tape_labels = VGroup()
        for i, cell in enumerate(tape):
            label = Text("B", font_size=24).move_to(cell.get_center())
            tape_labels.add(label)
            cell.set_fill(BLACK, opacity=1)
            cell.set_stroke(WHITE, width=1)
        
        # Position the tape in the scene
        tape.move_to(ORIGIN)
        tape_labels.move_to(tape)

        self.play(FadeIn(tape), FadeIn(tape_labels))

        # Create a head and position it at the first cell
        head = Triangle(color=RED, fill_opacity=1).scale(0.2).rotate(PI)
        head.next_to(tape[0], UP)

        self.play(FadeIn(head))

        # Define a function to move the head and update the tape
        def move_head(position, write_value=None):
            nonlocal head
            self.play(head.animate.next_to(tape[position], UP))
            if write_value is not None:
                tape_labels[position].become(Text(str(write_value), font_size=24).move_to(tape[position].get_center()))

        # Move the head across the tape and update the values
        move_head(1, 1)
        move_head(2, 0)
        move_head(3, 1)
        move_head(4, 1)
        move_head(5, 0)
        move_head(6, 0)
        move_head(7, 1)
        move_head(8, 1)
        move_head(9, 0)

        # End the scene
        self.wait(2)

# To render this scene, use the following command in the terminal:
# manim -pql your_script_name.py TuringMachine

