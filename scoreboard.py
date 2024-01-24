from turtle import Turtle
import os

file = "max_scores.txt"


# Create class scoreboard to track scores of the snake as it eats
class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(-20, 260)
		self.scores = 0
		self.max_scores = 0
		self.access_scores()  # Let this method be instantiated with the class call

	# Create a method to increase scores as turtle eats
	def update_scores(self):
		self.scores += 1

	# Create a method to write the scores to the screen
	def write_scores(self):
		self.clear()
		self.write(
			f"Score: {self.scores} - Highest Score: {self.max_scores}",
			align="center",
			font=("Arial", 20, "normal")
		)

	# Create a method to print "GAME OVER!" when forbidden condition is activated
	def game_over(self):
		self.goto(0, 0)
		self.color("red")
		self.write(
			"GAME OVER!",
			align="center",
			font=("Arial", 20, "normal")
		)

	# Create a method to access and store the highest score during the game's history
	def access_scores(self):
		if os.path.isfile(file):
			file_size = os.path.getsize(file)
			if file_size == 0:
				with open(file, "w") as f:
					f.write(f"{self.max_scores}")
			else:
				with open(file, "r") as f:
					previous_max = int(f.read())
					if previous_max > self.max_scores:
						self.max_scores = previous_max
					elif previous_max < self.max_scores:
						with open(file, "w") as p:
							p.write(f"{self.max_scores}")
		else:
			with open(file, "x") as f:
				f.write(f"{self.max_scores}")

	# Create a method to update the max score
	def update_max_scores(self):
		if self.scores > self.max_scores:
			self.max_scores = self.scores
			self.access_scores()
	