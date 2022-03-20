import cv2, cvzone, math, random, numpy

class SnakeGameClass:
    def __init__(self, food_path):
        # Snake variable stuffs
        self.points = [] # all points of the snake
        self.lengths = [] # distance between each point
        self.current_length = 0 # current length of the snake
        self.allowed_length = 200 # max allowed length of the snake
        self.previous_head = 0, 0 # previous head point

        # Food variable stuffs
        self.img_food = cv2.imread(food_path, cv2.IMREAD_UNCHANGED)
        self.food_height_position, self.food_weight_position, _  = self.img_food.shape
        self.food_point = 0, 0
        self.image = None
        self.randomize_food_location()

        self.score = 0
        self.game_over = False

    def randomize_food_location(self):
        self.food_point = random.randint(100, 1000), random.randint(100, 600)

    def update(self, image, current_head):
        # Check if the snake is dead
        print(self.points)
        if self.game_over:
            cvzone.putTextRect(image, "Game Over", [300, 400],scale = 7, thickness = 5, offset = 20)
            cvzone.putTextRect(image, f"Your Score: {self.score}", [300, 550],scale = 7, thickness = 5, offset = 20)
        else:
            previous_x, previous_y = self.previous_head
            current_x, current_y = current_head

            self.points.append([current_x, current_y])
            distance = math.hypot(current_x - previous_x, current_y - previous_y)
            self.lengths.append(distance)
            self.current_length += distance
            self.previous_head = current_x, current_y

            # Length reduction
            if self.current_length > self.allowed_length:
                for i, length in enumerate(self.lengths):
                    self.current_length -= length
                    self.lengths.pop(i)
                    self.points.pop(i)

                    if self.current_length < self.allowed_length:
                        break
            
            # Food detection
            random_x, random_y = self.food_point
            if random_x - self.food_weight_position // 2 < current_x < random_x + self.food_weight_position // 2 and\
                random_y - self.food_height_position // 2 < current_y < random_y + self.food_height_position // 2:
                print("Ate!")
                self.randomize_food_location()
                self.allowed_length += 50
                self.score += 1

            # Draw the snake
            if self.points:
                for j, point in enumerate(self.points):
                    if j != 0:
                        cv2.line(image, self.points[j-1], self.points[j], (0, 0, 255), 20)

                cv2.circle(image, self.points[-1], 20, (200, 0, 200), cv2.FILLED)
            
            # Draw the food
            image = cvzone.overlayPNG(image, 
                self.img_food, 
                (random_x - self.food_weight_position // 2, random_y - self.food_height_position // 2)
            )

            cvzone.putTextRect(image, f"Your Score: {self.score}", [50, 80],scale = 3, thickness = 3, offset = 10)

            # Check for collision
            pts = numpy.array(self.points[:-2], numpy.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], False, (0, 200, 0), 3)
            min_dist = cv2.pointPolygonTest(pts, (current_x, current_y), True)
            # print(min_dist)

            if -1 <= min_dist <= 1:
                print("Hit!")
                self.game_over = True
                self.points = []
                self.lengths = []
                self.current_length = 0
                self.previous_head = 0, 0
                self.allowed_length = 200
                self.randomize_food_location()


        return image