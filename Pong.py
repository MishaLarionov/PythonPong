from graphics import *
import time
import math
import gmcode
window = GraphWin("Pong", 600, 600)
window.setBackground("black")

def splashUX():
    h1 = Text(Point(300, 50), "Welcome to PythonPong")
    h1.setFace("helvetica")
    h1.setSize(36)
    h1.setTextColor("white")
    h1.draw(window)
    h2 = Text(Point(300, 150), "Controls")
    h2.setFace("helvetica")
    h2.setSize(18)
    h2.setTextColor("white")
    h2.draw(window)
    p = Text(Point(300, 200), "Left: w = up, s = down; Right: i = up, k = down")
    p.setFace("helvetica")
    p.setSize(11)
    p.setTextColor("white")
    p.draw(window)
    p2 = Text(Point(300, 550), "Click anywhere to continue")
    p2.setFace("helvetica")
    p2.setSize(11)
    p2.setTextColor("white")
    p2.draw(window)
    window.getMouse()
    h1.undraw()
    h2.undraw()
    p.undraw()
    p2.undraw()
    
def gameUX():
    lpaddle = Rectangle(Point(10, 250), Point(30, 350))
    lpaddle.setFill("white")
    lpaddle.draw(window)
    rpaddle = Rectangle(Point(570, 250), Point(590, 350))
    rpaddle.setFill("white")
    rpaddle.draw(window)
    ball = Circle(Point(300, 300), 10)
    ball.setFill("grey")
    ball.draw(window)
    movedir = 1
    while True:
        # Put input functions here
        time.sleep(0.05)
        ballmove(ball, movedir)

def ballmove(ball, movedir):
    ball.move(movedir*4,0)
        
splashUX()
gameUX()
