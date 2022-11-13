### Snake Game using cvzone

Make sure you have installed python3 (Version 3.7 - 3.10)

Run it with:

1. ```git clone https://github.com/ridhwan-aziz/gabut.git```
2. ```cd gabut/snake_game```
3. ```pip(3) install -Uvr requirements.txt```
4. ```python(3) snake_game_opencv.py```

How to play

- Move your index finger in front of the camera towards the donut image
- If you want to change camera, find ```video_capture = cv2.VideoCapture(0)``` at snake_game_opencv.py then change '0' to index of your camera
- If you want to change the donut image, replace the donut.png file or change ```game = SnakeGameClass("donut.png")``` at snake_game_opencv.py to your image path
- Press 'r' to restart the game and 'q' to quit the program