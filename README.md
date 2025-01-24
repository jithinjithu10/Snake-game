# Snake Game with Hand Gesture Control

This is a Python-based Snake Game where you control the snake using your hand gestures, specifically the index finger. The game uses a webcam to detect hand movements, and the snake moves in the direction of the index finger.

## Requirements

- Python 3.x
- OpenCV
- cvzone

You can install the required packages using the following:

```bash
pip install opencv-python cvzone



This project is a fun and interactive Python-based implementation of the classic Snake Game, where you control the snake using your hand gestures. By detecting the movement of your index finger, the game dynamically adjusts the snake’s direction. The game utilizes a webcam to track your hand's position and OpenCV for image processing.

Features:
Hand Gesture Control: Move the snake up, down, left, or right by using your index finger.
Random Food Generation: Food spawns at random locations, and the snake must eat it to grow.
Score Tracker: Displays the score based on the food eaten by the snake.
Game Over Condition: The game ends if the snake collides with the wall or itself.
Technologies Used:
Python: Programming language for the game logic.
OpenCV: Used to capture the webcam feed and process images for hand gesture recognition.
cvzone: A library for hand tracking and gesture recognition.
