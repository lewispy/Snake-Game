from turtle import Turtle
import random as r


# Create food class for snake to eat and grow
class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.turtlesize(stretch_len=0.5, stretch_wid=0.5)
		self.shape("circle")
		self.color("blue")
		self.penup()
		self.speed("fastest")
		self.relocate()

	# Let the food relocate to a random position each time snake eats it
	def relocate(self):
		x = r.randint(-280, 280)
		y = r.randint(-280, 280)
		self.goto(x, y)
