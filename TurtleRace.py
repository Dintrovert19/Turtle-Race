#Do you think you can guess which turtle will win the race?
import turtle
import time
import random

WIDTH, HEIGHT=500,500   #https://www.programiz.com/python-programming/variables-constants-literals

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_racers():
    while True:
        try:                                                    #https://www.w3schools.com/python/python_try_except.asp
            racers=int(input('Enter the number of Turtles (2 - 10): '))
        except:
            print('Input is not numeric...Please try again!')
            continue
        if (2<=racers<=10):
            return racers
        else:
            print('Please enter the number in range 2 to 10!')

def set_screen():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Race!')

def create_turtles(colors):
    turtles=[]
    x=WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)              #changes the color of the turtle
        racer.shape('turtle')           #changes the shape of the turtle
        racer.left(90)                  #changes the angle of the turtle to 90 degree to the left
        racer.penup()                   #stops the turtle to leave the track marks
        racer.setpos(-WIDTH//2 + (i+1)*x,-HEIGHT//2 + 20)   #to set the position of the turtle
        turtles.append(racer)
    return turtles

def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]

racers=get_racers()
set_screen()
random.shuffle(COLORS)
colors=COLORS[:racers]
winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)