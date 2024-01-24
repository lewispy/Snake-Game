from turtle import Turtle, colormode
import random as r


class Snake:
	snakes = []

	@staticmethod
	def __gen_colors():
		c = r.randint(0, 255)
		g = r.randint(0, 255)
		b = r.randint(0, 255)
		return c, g, b

	# Create four instances of snake sections
	def create_sections(self):
		for i in range(3):
			colormode(255)
			color1 = self.__gen_colors()
			s = Turtle(shape="square")
			s.color(color1)
			s.penup()
			Snake.snakes.append(s)
		for j in range(1, len(Snake.snakes)):  # Join the snake sections together
			Snake.snakes[j].setx(Snake.snakes[j - 1].xcor() - 20)

	# Set condition for stopping the game
	@staticmethod
	def forbidden():
		if Snake.snakes[0].xcor() > 290 or Snake.snakes[0].xcor() < -290 or\
				Snake.snakes[0].ycor() > 290 or Snake.snakes[0].ycor() < -290:
			return True

	# Set condition for when the snake bites itself
	@staticmethod
	def bite():
		if any(snake.distance(Snake.snakes[0]) < 10 for snake in Snake.snakes[2:]):
			return True

	# A method to detect collision with food
	@staticmethod
	def collide(food):
		if Snake.snakes[0].distance(food) < 15:
			return True

	# Let the snake grow when it eats food
	def grow(self):
		colormode(255)
		color2 = self.__gen_colors()
		new_s = Turtle(shape="square")
		new_s.color(color2)
		new_s.penup()
		Snake.snakes.append(new_s)
		Snake.snakes[-1].goto(Snake.snakes[-2].xcor(), Snake.snakes[-2].ycor())
	
	# Define a method for moving snake parts
	@staticmethod
	def move():
		for i in range(len(Snake.snakes) - 1, 0, -1):
			sx = Snake.snakes[i - 1].xcor()
			sy = Snake.snakes[i - 1].ycor()
			Snake.snakes[i].goto(sx, sy)
		Snake.snakes[0].forward(20)

	# Define a method for snake to face north
	@staticmethod
	def up():
		if Snake.snakes[0].heading() != 90 and Snake.snakes[0].heading() != 270:
			Snake.snakes[0].setheading(90)

	# Define a method for the snake to turn left/west
	@staticmethod
	def left():
		if Snake.snakes[0].heading() != 0 and Snake.snakes[0].heading() != 180:
			Snake.snakes[0].setheading(180)

	# Define a method for the snake to face down/south
	@staticmethod
	def down():
		if Snake.snakes[0].heading() != 90 and Snake.snakes[0].heading() != 270:
			Snake.snakes[0].setheading(270)

	# Define a method for the snake to turn right/east
	@staticmethod
	def right():
		if Snake.snakes[0].heading() != 0 and Snake.snakes[0].heading() != 180:
			Snake.snakes[0].setheading(0)
