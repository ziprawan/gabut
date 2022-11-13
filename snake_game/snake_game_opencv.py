import cv2
from cvzone.HandTrackingModule import HandDetector

try:
    from game_class import SnakeGameClass
except:
    exit("Please run it inside snake_game folder :)")

# Setting up variable
video_capture = cv2.VideoCapture(0) # Main camera. You can edit here to change camera
video_capture.set(3, 1280)
video_capture.set(4, 720)

detector = HandDetector(
    detectionCon = 0.8, # set detection confidence threshold
    maxHands = 1 # Set one because this is a single hand game
)

game = SnakeGameClass("donut.png")

while True:
    _, img = video_capture.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType = False)

    if hands != []:
        lm_list = hands[0]['lmList']
        # For thumb finger, set to 4
        # For forefinger set to 8
        # For middle finger set to 12
        # For ring finger set to 16
        # For little finger set to 20
        # Default is forefinger for easier play
        point_index = lm_list[8][0:2]
        img = game.update(img, point_index)

    cv2.imshow("Snake game window", img)
    key = cv2.waitKey(1)

    # Press 'q' to exit, and 'r' to restart if you lose the game

    if key == ord('r'):
        game.gameOver = False
        game.isNewGame = True
    elif key == ord('q'):
        break