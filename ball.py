from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcor_move = 10
        self.ycor_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.xcor_move
        y_cor = self.ycor() + self.ycor_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.ycor_move *= -1

    def bounce_x(self):
        self.xcor_move *= -1
        self.move_speed *= 0.9
        print(float(self.move_speed))

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
