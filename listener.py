from snake import Snake
from turtle import Screen


# Create class listener
class Listener:
	def __init__(self):
		self.sc = Screen()
		self.sc.setup(width=600, height=600)
		self.sc.bgcolor("black")
		self.sc.title("Snake Game")
		self.sc.tracer(0)
		self.snake = Snake()

	# Let the screen listen for key prompt
	def listening(self):
		self.sc.listen()
		self.sc.onkey(fun=self.snake.up, key="Up")
		self.sc.onkey(fun=self.snake.down, key="Down")
		self.sc.onkey(fun=self.snake.left, key="Left")
		self.sc.onkey(fun=self.snake.right, key="Right")

	# Set an updater to update screen
	def updater(self):
		self.sc.update()

	# Exit the screen on click
	def exit_screen(self):
		self.sc.exitonclick()
