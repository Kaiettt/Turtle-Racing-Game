#  input number of turtles
# creating the screen
#  creating turle
#  handle turtles action
#  check wining
import turtle
import time
import random


HEIGHT = 500
WIDTH = 500

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "orange"]

def generate_number_of_turtle():
    while True:
        size = input("What is number of turtles: 2 - 10 ")
        if(size.isdigit):
            if(2 > int(size) or  int(size) > 10):
                print("The number of turles is 2 to 10")
            else:
                break
        else:
            print("please enter a number")
    return int(size)

def create_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)

def create_turtles(colors):
    turtles = []
    pos_x_left = -25
    pos_x_right =25
    for i,color in enumerate(colors):
        tur_tle = turtle.Turtle()
        tur_tle.shape("turtle")
        tur_tle.color(color)
        tur_tle.left(90)
        if(i%2==0):
            tur_tle.penup()
            tur_tle.goto(pos_x_left, -220)
            tur_tle.pendown()
            pos_x_left -= 50
        else:
            tur_tle.penup()
            tur_tle.goto(pos_x_right, -220)
            tur_tle.pendown()
            pos_x_right += 50
        turtles.append(tur_tle)
    return turtles

def race(turtles):
    Winner = None
    Done = True
    while Done:
        for turtle in turtles:
            distance = random.randint(1, 20)
            turtle.forward(distance)
            x, y = turtle.position()
            if(y>=250):
                Winner = str(turtle.pencolor())
                Done = False
                break

    return Winner

while True:
    choice = input("Press P to play Or Q to Quit: ")
    if(choice == "P"):
        numberOfTurtles = generate_number_of_turtle()
        create_screen()
        Color = colors[:numberOfTurtles]
        turtles = create_turtles(Color)
        winner = race(turtles)
        print(f"Turtle {winner} won the race")
        turtle.done()
    else:
        break