import turtle
import time
import random
import sys  # Import the sys module for exiting the program

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off-screen updates

# Define grid size
grid_size = 20

# Snake head
head = turtle.Turtle()
head.speed(0)  # Set animation speed to fastest
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# Score
score = 0
delay = 0.1


# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Function to move to a grid position
def move_to_grid(x, y):
    new_x = (round(x, 1) // grid_size) * grid_size
    new_y = (round(y, 1) // grid_size) * grid_size
    head.goto(new_x, new_y)


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Main game loop
game_over = False
while not game_over:
    screen.update()

    # Move the snake
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    # Border checking
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_over = True

    # Check for collisions with food
    if food.xcor() - 10 <= head.xcor() <= food.xcor() + 10 and \
            food.ycor() - 10 <= head.ycor() <= food.ycor() + 10:
        # Move the food to a random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Increase score
        score += 10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

        # Increase game speed
        delay *= 0.9

    # Indentation fix
    time.sleep(delay)

    # End game routine
if game_over:
    pen.clear()  # Clear any existing text on the screen
    pen.goto(0, 0)  # Move pen to the center

    # Display final score and "Game Over" message
    pen.write("Game Over!\nYour Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

    # Wait for 5 seconds and exit
    time.sleep(5)
    sys.exit()  # Quit the program

# Close the screen after the delay (optional)
screen.exitonclick()

# NOTES SECTION

# try to fix the fact that the game over screen is not working rn
# try to implement a grid based system that the food and snake move on for more consistency
# make it so that when you eat food you grow
#
