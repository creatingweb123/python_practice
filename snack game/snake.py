
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self,screen,Turtle):
        self.snake_list = []
        self.screen = screen
        self.Turtle = Turtle
        self.create_snake()
        self.main_snake = self.snake_list[0]

    def create_snake(self):
        start_position = ((0,0),(-20,0),(-40,0))
        for position in start_position:
            self.add_snake(position)

    def plus_snake(self):
        self.add_snake(self.snake_list[-1].position())

    def add_snake(self, position):
        new_snake = self.Turtle(shape = "square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.setposition(position)
        self.snake_list.append(new_snake)
        

    def move_main_snake(self):
        self.screen.listen()
        # move forward
        self.screen.onkey(key="w",fun=self.move_forward)
        # move backward
        self.screen.onkey(key="s",fun=self.move_backward)
        # move right
        self.screen.onkey(key="a",fun=self.move_left)
        # move left
        self.screen.onkey(key="d",fun=self.move_right)
    def move_forward(self):
        if int(self.main_snake.heading()) != DOWN:
            self.main_snake.setheading(UP)
    def move_backward(self):
        if int(self.main_snake.heading()) != UP:
            self.main_snake.setheading(DOWN)
    def move_right(self):
        if int(self.main_snake.heading()) != LEFT:
            self.main_snake.setheading(RIGHT)
    def move_left(self):
        if int(self.main_snake.heading()) != RIGHT:
            self.main_snake.setheading(LEFT)

    def move_snake(self):
        self.screen.update()
        self.move_main_snake()
        for i in range(len(self.snake_list)-1,0,-1):
            next_snake_pos = self.snake_list[i-1].position()
            self.snake_list[i].goto(next_snake_pos)
        self.main_snake.forward(MOVE_DISTANCE)
        

    def check_out(self,width,height):
        if self.main_snake.xcor() < -width/2 or self.main_snake.xcor() > width/2 or self.main_snake.ycor() < -height/2 or self.main_snake.ycor() > height/2:
            return False
        
        for tail in self.snake_list[1:]:
            if self.main_snake.distance(tail.position())<20:
                return False
        return True