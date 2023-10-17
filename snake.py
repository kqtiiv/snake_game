from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_part = []
        self.create_snake()
        self.head = self.snake_part[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setposition(position)
        self.snake_part.append(snake)

    def extend(self):
        self.add_segment(self.snake_part[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_part)-1, 0, -1):
            new_x = self.snake_part[seg_num-1].xcor()
            new_y = self.snake_part[seg_num-1].ycor()
            self.snake_part[seg_num].goto(new_x, new_y)
        self.snake_part[0].forward(DISTANCE)

    def reset(self):
        for snake in self.snake_part:
            snake.goto(1000, 1000)
        self.snake_part.clear()
        self.create_snake()
        self.head = self.snake_part[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

