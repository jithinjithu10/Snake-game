
# Snake Game with Hand Gesture Control

This is a Python-based Snake Game where you control the snake using your hand gestures, specifically the index finger. The game uses a webcam to detect hand movements, and the snake moves in the direction of the index finger.

## Requirements

- Python 3.x
- OpenCV
- cvzone

You can install the required packages using the following:

```bash
pip install opencv-python cvzone
```

## Project Description

This project is a fun and interactive Python-based implementation of the classic Snake Game, where you control the snake using your hand gestures. By detecting the movement of your index finger, the game dynamically adjusts the snake’s direction. The game utilizes a webcam to track your hand's position and OpenCV for image processing.

### Features:
- **Hand Gesture Control**: Move the snake up, down, left, or right by using your index finger.
- **Random Food Generation**: Food spawns at random locations, and the snake must eat it to grow.
- **Score Tracker**: Displays the score based on the food eaten by the snake.
- **Game Over Condition**: The game ends if the snake collides with the wall or itself.

### Technologies Used:
- **Python**: Programming language for the game logic.
- **OpenCV**: Used to capture the webcam feed and process images for hand gesture recognition.
- **cvzone**: A library for hand tracking and gesture recognition.

## How to Run the Game

1. Clone or download the repository to your local machine.
2. Install the necessary dependencies by running the following command in your terminal:

    ```bash
    pip install opencv-python cvzone
    ```

3. Run the game by executing the Python script:

    ```bash
    python snake_game.py
    ```

4. The game window will appear, and you can control the snake using your index finger detected by the webcam.

## How to Close the Game

To exit the game, press the 'q' key while the game window is open. The game will close, and the program will terminate.

## Troubleshooting

- **Webcam not detected**: Ensure that the webcam is properly connected and accessible. You can check if the camera works in other applications.
- **Hand gestures not detected properly**: Adjust the position and distance of your hand from the camera for better recognition.

## License

This project is licensed under the MIT License.
