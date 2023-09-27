from turtle import *
from random import randrange

# Define constants for screen boundaries
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400


# Define constants for snake speed and movement
SNAKE_SPEED = 100  # Increase or decrease for faster/slower snake
SNAKE_MOVE_DISTANCE = 10

# Define the initial snake direction
snake_direction = vector(SNAKE_MOVE_DISTANCE, 0)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(SNAKE_MOVE_DISTANCE, 0)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -SCREEN_WIDTH/2 < head.x < SCREEN_WIDTH/2 - 10 and -SCREEN_HEIGHT/2 < head.y < SCREEN_HEIGHT/2 - 10

def move_food():
    "Move the food to a random position."
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

    setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
