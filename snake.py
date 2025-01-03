from turtle import Turtle,Screen
position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP=90
DOWN=270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
    def createsnake(self):
        for pos in position:
            self.add_segment(pos)

    def add_segment(self,pos):
        segment = Turtle(shape='square')
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
