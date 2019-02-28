import turtle  # 1. import the modules
import random
import time

def draw_game():

    wn = turtle.Screen()  # 2. Create a screen
    wn.setup(width=420, height=420, startx=0, starty=0)
    wn.bgcolor('skyblue')

    # Setup Landscape
    landscape = turtle.Turtle()
    landscape.speed(10) # Speed
    landscape.pensize(1)
    landscape.ht()  # I dont want people see what I'm using to draw (my own turtle)
    landscape.up()

    # Road setup
    draw_road(landscape)

    draw_gray_box(landscape)

    draw_road_lines(landscape)

    draw_red_lines(landscape)

    draw_finish_lines(landscape)

    draw_sun(landscape)

    draw_hill(landscape)

    # Draw the racer
    lance = add_racer('turtle', 'Olive', -190, -95)
    andy = add_racer('turtle', 'SaddleBrown', -190, -125)
    luis = add_racer('turtle', 'ForestGreen', -190, -155)
    michael = add_racer('turtle', 'DarkOliveGreen', -190, -185)

    # Starting the race
    lance_winner = 0
    andy_winner = 0
    luis_winner = 0
    michael_winner = 0

    draw_circle(landscape)

    winners_flag = 0
    for i in range(51):
        winners_flag, lance_winner = move_racer(lance, lance_winner, winners_flag)
        winners_flag, andy_winner = move_racer(andy, andy_winner, winners_flag)
        winners_flag, luis_winner = move_racer(luis, luis_winner, winners_flag)
        winners_flag, michael_winner = move_racer(michael, michael_winner, winners_flag)

    print("Lance is the first place: {}".format(lance_winner))
    print("andy is the first place: {}".format(andy_winner))
    print("luis is the first place: {}".format(luis_winner))
    print("michael is the first place: {}".format(michael_winner))

    wn.exitonclick()

def draw_road(landscape):
    landscape.setpos(-200, -200)
    landscape.down()
    landscape.color("White", "DarkGray")

def draw_gray_box(landscape):
    # Draw gray road
    landscape.begin_fill()  # landscape.fill(True)
    for square in range(2):
        landscape.forward(400)
        landscape.left(90)
        landscape.forward(120)
        landscape.left(90)
    landscape.end_fill()  # landscape.fill(False)
    landscape.up()

def draw_road_lines(landscape):
    landscape.setpos(-200, -200)
    for line in range(4):
        landscape.left(90)
        landscape.forward(30)
        landscape.right(90)
        for lot_of_paint in range(10):
            landscape.down()
            landscape.forward(20)
            landscape.up()
            landscape.forward(20)
        landscape.backward(400)

    landscape.setpos(-200, -200)
    landscape.pensize(5)

def draw_red_lines(landscape):
    for line in range(2):
        landscape.down()
        for lot_of_paint in range(20):
            landscape.color("red")
            landscape.forward(10)
            landscape.color("white")
            landscape.forward(10)
        landscape.up()
        landscape.backward(400)
        landscape.setpos(-200, -80)

def draw_finish_lines(landscape):
    landscape.setpos(180, -80)
    landscape.pensize(8)
    landscape.seth(270)
    landscape.shape("square")

    flag1 = 1
    for line in range(4):
        landscape.down()
        if ((flag1 % 2) != 1):
            for lot_of_paint in range(10):
                landscape.color("black")
                landscape.forward(6)
                landscape.color("white")
                landscape.forward(6)
        else:
            for lot_of_paint in range(10):
                landscape.color("white")
                landscape.forward(6)
                landscape.color("black")
                landscape.forward(6)
        flag1 = flag1 + 1
        landscape.up()
        landscape.backward(120)
        landscape.left(90)
        landscape.forward(6)
        landscape.right(90)

def draw_sun(landscape):
    landscape.backward(120)
    landscape.left(90)
    landscape.forward(6)
    landscape.right(90)
    landscape.speed(7)
    landscape.up()
    landscape.goto(-100, 100)
    landscape.color("yellow")
    landscape.pensize(3)
    landscape.speed(0)
    for number_of_positions in range(1, 47, 1):
        landscape.forward(60)
        landscape.up()
        landscape.forward(-60)
        landscape.down()
        landscape.right(8)
    landscape.up()

def draw_hill(landscape):
    landscape.setpos(-90, -77)
    landscape.pensize(1)
    landscape.shape("arrow")
    landscape.color("black", "green")

    landscape.begin_fill()  # landscape.fill(True)
    landscape.seth(45)
    landscape.down()
    landscape.forward(100)
    for degree in range(135):  # 90 degrees + 45 degrees
        landscape.right(1)
        landscape.forward(1)
    landscape.forward(30)
    landscape.end_fill()  # landscape.fill(False)

    landscape.begin_fill()  # landscape.fill(True)
    landscape.seth(90)
    landscape.forward(200)
    for degree in range(180):  # 90 degrees + 45 degrees
        landscape.right(1)
        landscape.forward(1)
    landscape.forward(200)
    landscape.end_fill()  # landscape.fill(False)
    landscape.penup()

def draw_circle(landscape):
    landscape.shape("circle")
    landscape.color("red")
    landscape.setpos(-188, -60)
    landscape.seth(0)

    for countdown in range(3):
        landscape.st()
        time.sleep(0.5)
        landscape.ht()
        time.sleep(0.5)

    landscape.color("LawnGreen")
    landscape.st()
    time.sleep(1.5)
    landscape.ht()

def add_racer(shape, color, x, y):
    racer = turtle.Turtle()
    racer.ht()
    racer.shape(shape)
    racer.color(color)
    racer.st()
    racer.up()
    racer.goto(x, y)
    return racer

def move_racer(racer, place, count):
    if (racer.xcor() < 200):
        racer.forward(random.randrange(1, 50))
    elif place == 0:
        count = count + 1
        place = count

    return count, place

draw_game()
