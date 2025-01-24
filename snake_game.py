import cv2
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize webcam with DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Game variables
width, height = 640, 480
food_size = 20
score = 0
snake = [(100, 100)]  # Snake starts with one segment
direction = (20, 0)  # Moving right initially
food_pos = (random.randint(0, width // 20) * 20, random.randint(0, height // 20) * 20)
game_over = False

# Delay for movement control
last_move_time = time.time()
move_delay = 0.15  # Adjust to control speed

# Set the window to full screen
cv2.namedWindow("Snake Game", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Snake Game", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    success, img = cap.read()

    # Ensure frame is captured
    if not success or img is None:
        print("Warning: Skipping frame, no image captured.")
        continue

    # Flip the image horizontally for natural movement
    img = cv2.flip(img, 1)

    # Detect hands
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lm_list = hands[0]['lmList']  # Get landmark list of first detected hand
        index_finger_tip = lm_list[8]  # Tip of the index finger
        finger_x, finger_y = index_finger_tip[0], index_finger_tip[1]

        # Change direction based on finger position
        if finger_x < snake[0][0]:  # Move left
            direction = (-20, 0)
        elif finger_x > snake[0][0]:  # Move right
            direction = (20, 0)
        elif finger_y < snake[0][1]:  # Move up
            direction = (0, -20)
        elif finger_y > snake[0][1]:  # Move down
            direction = (0, 20)

    # Move the snake at set intervals
    if time.time() - last_move_time > move_delay:
        last_move_time = time.time()

        # Move the snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Check for collision with food
        if abs(new_head[0] - food_pos[0]) < food_size and abs(new_head[1] - food_pos[1]) < food_size:
            score += 1
            food_pos = (random.randint(0, width // 20) * 20, random.randint(0, height // 20) * 20)  # Spawn new food
        else:
            snake.pop()  # Remove last segment if no food eaten

        # Check for collision with wall
        if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
            game_over = True

        # Check for collision with itself
        if new_head in snake[1:]:
            game_over = True

    # Draw game elements
    img = cv2.resize(img, (width, height))

    # Draw food
    cv2.rectangle(img, food_pos, (food_pos[0] + food_size, food_pos[1] + food_size), (0, 0, 255), -1)

    # Draw snake
    for segment in snake:
        cv2.rectangle(img, segment, (segment[0] + 20, segment[1] + 20), (0, 255, 0), -1)

    # Display score
    cv2.putText(img, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if game_over:
        cv2.putText(img, "Game Over!", (width // 3, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Snake Game", img)
        cv2.waitKey(3000)  # Show game over screen for 3 seconds
        break

    # Show the game frame
    cv2.imshow("Snake Game", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
