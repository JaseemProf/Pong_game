from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.new_ycor = None
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.shape("square")
        self.goto(position)

    def upward(self):
        self.new_ycor = self.ycor() + 20
        self.goto(self.xcor(), self.new_ycor)

    def backward(self):
        self.new_ycor = self.ycor() - 20
        self.goto(self.xcor(), self.new_ycor)
