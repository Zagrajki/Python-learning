from turtle import *
import math

bok = 80

def kwadrat():
    for i in range(4):
        fd(bok)
        left(90)

def plansza():
    for i in range(3):
        for j in range(3):
            pd()
            kwadrat()
            pu()
            fd(bok)
        bk(3*bok)
        left(90)
        fd(bok)
        right(90)

def krzyzyk(a, b):
    pu()
    setx(a*bok+bok/2)
    sety(b*bok+bok/2)
    pd()
    left(45)
    for i in range(4):
        fd(bok/4)
        bk(bok/4)
        left(90)
    right(45)
    pu()

def kolko(a, b):
    pu()
    setx(a*bok+bok/2)
    sety(b*bok+bok/2-54/math.pi)
    pd()
    circle(bok/4)
    pu()

tura = "x"
pole = [[False, False, False], [False, False, False], [False, False, False]]
def postaw(a, b):
    global tura
    global pole
    if pole[a][b]==False:
        pole[a][b]=True
        if tura=="x":
            krzyzyk(a, b)
            tura="o"
        else:
            kolko(a, b)
            tura="x"
            
