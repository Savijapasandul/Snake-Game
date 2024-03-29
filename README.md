# Snake Game
This code is a simple implementation of the classic Snake game using the Pygame library in Python. Here's a brief description of the code:

1. The code sets up the Pygame environment, defines constants such as colors, screen dimensions, block sizes, and game speeds.

2. Functions are defined for drawing text, adding walls, and the main game loop.

3. In the game loop, the snake's movement is controlled by arrow keys. The snake grows when it eats food, and the player earns points. Walls are introduced as the player's score increases.

4. The game checks for collisions with the walls or itself, triggering a game over if such collisions occur.

5. Sound effects are played when the snake eats food or the game ends.

6. The snake's speed increases as the player's score progresses.


To run the code:

1. Make sure you have Python installed on your system along with the Pygame library.
2. Save the code in a file with a .py extension.
3. Make sure you have sound files named eat.wav and game_over.wav located in a folder named "src" in the same directory as your script (or adjust the paths accordingly).
4. Run the script, and the game window should appear. Use arrow keys to control the snake.
5. When the game is over, you can press 'C' to play again or 'Q' to quit.
