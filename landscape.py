import turtle
from random import random
from math import floor


def getMid(a, b):
    return (a + b) / 2


def drawLine(x1, y1, x2, y2, turtle, degree):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)


def traceLine(x1, y1, x2, y2, turtle, degree):
    turtle.goto(x1, y1)
    turtle.goto(x2, y2)


def tree(treesize, treewidth, treecolor):
    treeTurtle.color(treecolor)
    if treesize > 5:
        treeTurtle.pensize(treewidth)
        treeTurtle.forward(treesize)
        treeTurtle.left(15)
        tree(treesize - (random() * 15), treewidth * 0.75, treecolor)
        treeTurtle.right(30)
        tree(treesize - (random() * 15), treewidth * 0.75, treecolor)
        treeTurtle.left(15)
        treeTurtle.backward(treesize)


def drawTerrain(treesize, treewidth, treecolor, x1, y1, x2, y2, degree):
    if degree > 0:
        if degree == 1:
            drawLine(x1, y1, x2, y2, list[degree - 1], degree)
            e = floor(random() * 0.25 * (2 ** n))
            if e == 0:
                treeTurtle.up()
                treeTurtle.goto(x2, y2)
                treeTurtle.down()
                f = random() * 30 - 15
                treeTurtle.right(f)
                tree(treesize, treewidth, treecolor)
                treeTurtle.left(f)
        else:
            traceLine(x1, y1, x2, y2, list[degree - 1], degree)
        c = 2 ** (n - degree)
        d = (random() * (500 / c)) - (250 / c)
        drawTerrain(treesize, treewidth, treecolor, x1, y1,
                    getMid(x1, x2), getMid(y1, y2) + d, degree - 1)
        drawTerrain(treesize, treewidth, treecolor, getMid(
            x1, x2), getMid(y1, y2) + d, x2, y2, degree - 1)


def layer(height, color, treesize, treewidth, treecolor):
    for turtle in list:
        turtle.color(color)
    list[0].begin_fill()
    a = random() * 40 - 20 + height
    b = random() * 40 - 20 + height
    drawTerrain(treesize, treewidth, treecolor, -720, a, 720, b, n)
    list[0].right(90)
    list[0].forward(400 + b)
    list[0].right(90)
    list[0].forward(1440)
    list[0].right(90)
    list[0].forward(400 + a)
    list[0].end_fill()
    list[0].right(90)


n = int(input())
myWin = turtle.Screen()
treeTurtle = turtle.Turtle()
treeTurtle.speed(0)
treeTurtle.left(90)
treeTurtle.color("#6dd0f7")
treeTurtle.up()
treeTurtle.goto(-730, -400)
treeTurtle.down()
treeTurtle.begin_fill()
treeTurtle.goto(-730, 400)
treeTurtle.goto(730, 400)
treeTurtle.goto(730, -400)
treeTurtle.goto(-730, -400)
treeTurtle.end_fill()
treeTurtle.color("#ffff9c")
treeTurtle.up()
sun_x = random() * 600 - 300
sun_y = random() * 50 + 300
sun_size = random() * 10 + 30
treeTurtle.goto(sun_x, sun_y)
treeTurtle.down()
treeTurtle.begin_fill()
treeTurtle.circle(sun_size)
treeTurtle.end_fill()
list = []
for i in range(n):
    list.append(turtle.Turtle())
for turtle in list:
    turtle.color("white")
for turtle in list[1:]:
    turtle.up()
for turtle in list:
    turtle.speed(0)
    turtle.hideturtle()
treeTurtle.hideturtle()
color1 = random() * 0.4 + 0.6
color2 = random() * 0.4 + 0.6
color3 = random() * 0.4 + 0.6
layer(100, "white", 10, 3, "#ffffff")
layer(0, (color1, color2, color3), 20, 4, "#ffce7a")
layer(-100, (color1 / 2, color2 / 2, color3 / 2), 30, 8, "brown")
layer(-200, "#636363", 40, 9, "#5e493d")
for turtle in list[1:]:
    turtle.clear()
myWin.exitonclick()
