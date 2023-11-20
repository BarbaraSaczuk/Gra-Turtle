import turtle
from random import choice
from time import time

screen = turtle.Screen()
turtle.bgcolor('lightblue')
screen.setup(1000, 1000)
t = turtle.Turtle('turtle')

t.color('pink')
t.fillcolor('grey')

# zasady gry
t.pencolor('black')
t.hideturtle()
t.penup()
t.left(90)
t.forward(300)
t.write('ODRYSOWYWANIE FIGURY', False, align="center", font=('Arial', 20, 'normal'))

t.left(180)
t.fd(50)
t.right(90)
t.fd(400)
t.write('Zasady gry:', font=('Arial', 15, 'normal'))
t.left(90)
t.fd(20)
t.write('Za pomocą strzałek odrysuj wylosowaną figurę i naciśnij spację', font=('Arial', 10, 'normal'))
t.fd(20)
t.write('Aby zresetować figurę naciśnij R')
t.left(90)
t.fd(500)
t.left(90)
t.fd(40)
t.write('Sterowanie:', font=('Arial', 15, 'normal'))
t.left(180)
t.fd(20)
t.write('Do góry - strzałka skierowana w górę')
t.fd(20)
t.write('Do dołu - strzałka skierowana w dół')
t.fd(20)
t.write('W prawo - strzałka skierowana w prawo')
t.fd(20)
t.write('W lewo - strzałka skierowana w lewo')
t.fd(20)
t.write('Aby rozpocząć - przycisk R')
t.fd(20)
t.write('Aby wyświetlić fraktal - przycisk F')
t.fd(100)
t.seth(90)
t.showturtle()
t.pendown()


# figury możliwe do wylosowania
def figura1():
    t.forward(150)
    t.left(90)
    for i in range(3):
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
    t.left(180)
    t.fd(150)


def figura2():
    for i in range(4):
        t.forward(200)
        t.left(90)


def figura3():
    for i in range(4):
        for j in range(2):
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.left(90)
        t.forward(50)
        t.left(90)


def figura4():
    t.left(90)
    t.forward(500)
    t.right(90)
    t.forward(50)
    for i in range(5):
        t.forward((5 - i) * 50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward((5 - i) * 50)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.right(180)
    t.forward(50)


# opis przycisków
def gora():
    t.seth(90)
    t.fd(50)


def prawo():
    t.seth(0)
    t.fd(50)


def dol():
    t.seth(270)
    t.fd(50)


def lewo():
    t.seth(180)
    t.fd(50)


def koniec():
    t2 = time()
    print(t2 - t1)


def reset():
    t.clear()
    losujfigure()


def losujfigure():
    t.seth(90)
    t.penup()
    t.goto(-25, 100)
    t.pendown()

    t.begin_fill()
    figury = [figura1, figura2, figura3, figura4]
    choice(figury)()
    t.end_fill()

    t.penup()
    t.goto(-25, -250)
    t.pendown()
    global t1
    t1 = time()


def fraktal():
    t.speed(0)
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.seth(90)
    t.pendown()
    for i in range(150):
        colors = ['darkred', 'olive', 'seagreen', 'indigo', 'navy', 'crimson']
        for j in range(4):
            color = choice(colors)
            t.pencolor(color)
            t.forward(150 - i)
            t.left(90)
        t.left(5)


turtle.listen()
turtle.onkey(fraktal, 'f')
turtle.onkey(gora, 'Up')
turtle.onkey(dol, 'Down')
turtle.onkey(lewo, 'Left')
turtle.onkey(prawo, 'Right')
turtle.onkey(reset, 'r')
turtle.onkey(koniec, 'space')
turtle.mainloop()
