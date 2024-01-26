from snake import Snake
from food import Food
from listener import Listener
from scoreboard import Scoreboard
import time

# create snake and screen objects
sc = Listener()
sn = Snake()
fd = Food()
sb = Scoreboard()

# First create snake sections
sn.create_sections()

# Let the listener start listening
sc.listening()

# Define global variable for starting game loop
movement = True

# Start the game loop
while movement:
	sc.updater()  # The screen should update and refresh
	time.sleep(0.25)  # The timer should activate every 0.25 seconds
	sb.write_scores()
	sn.move()
	if sn.collide(food=fd):
		fd.relocate()
		sn.grow()
		sb.update_scores()
		sb.update_max_scores()
	if sn.forbidden() or sn.bite():
		sb.game_over()
		movement = False

sc.exit_screen()
