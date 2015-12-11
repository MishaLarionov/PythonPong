from graphics import *
import time
import math
import gmcode
window = GraphWin("Pong", 600, 600)
window.setBackground("black")
background = Image(Point(0, 0), "background.png")
background.draw(window)

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
    p2 = Text(Point(300, 550), "Press any key to continue")
    p2.setFace("helvetica")
    p2.setSize(11)
    p2.setTextColor("white")
    p2.draw(window)
    window.getKey()
    h1.undraw()
    h2.undraw()
    p.undraw()
    p2.undraw()
    background.undraw()
    
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
    moveX = 1
    moveY = 0
    while True and moveX != 0:
        # Input functions and logic
        time.sleep(0.02)
        key = window.checkKey()
        lpaddleY = lpaddle.getCenter().getY()
        rpaddleY = rpaddle.getCenter().getY()
        if key == "w" and lpaddleY > 50:
            lpaddle.move(0, -6)
        elif key == "s" and lpaddleY < 550:
            lpaddle.move(0, 6)
        elif key == "i" and rpaddleY > 50:
            rpaddle.move(0, -6)
        elif key == "k" and rpaddleY < 550:
            rpaddle.move(0, 6)
        # Direction switch and boundaries
        # TODO: Let the ball move vertically
        if ball.getCenter().getX() >= 560:
            if rpaddleY + 60 > ball.getCenter().getY() > rpaddleY - 60:
                moveX = -moveX
            else:
                # TODO: End round here
                moveX = 0
        if ball.getCenter().getX() <= 40:
            if lpaddleY + 60 > ball.getCenter().getY() > lpaddleY - 60:
                moveX = -moveX
            else:
                # TODO: End round here
                moveX = 0
        if not 10 < ball.getCenter().getY() < 590:
            moveY = -moveY
        ballmove(ball, moveX, moveY)

def ballmove(ball, moveX, moveY):
    ball.move(moveX * 2, moveY * 2)
        
splashUX()
gameUX()
