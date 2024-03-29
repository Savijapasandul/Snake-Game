# Snake Game
This code is a simple implementation of the classic Snake game using the Pygame library in Python. Here's a brief description of the code:

The code sets up the Pygame environment, defines constants such as colors, screen dimensions, block sizes, and game speeds.

Functions are defined for drawing text, adding walls, and the main game loop.

In the game loop, the snake's movement is controlled by arrow keys. The snake grows when it eats food, and the player earns points. Walls are introduced as the player's score increases.

The game checks for collisions with the walls or itself, triggering a game over if such collisions occur.

Sound effects are played when the snake eats food or the game ends.

The snake's speed increases as the player's score progresses.


To run the code:

Make sure you have Python installed on your system along with the Pygame library.
Save the code in a file with a .py extension.
Make sure you have sound files named eat.wav and game_over.wav located in a folder named "src" in the same directory as your script (or adjust the paths accordingly).
Run the script, and the game window should appear. Use arrow keys to control the snake.
When the game is over, you can press 'C' to play again or 'Q' to quit.
