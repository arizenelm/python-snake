import time
from graphics import *
from pynput.keyboard import Listener
import random

class Segment(Polygon) :
    #def __init__(self, p1, p2, p3, p4) :
    #    super().__init__(self, p1, p2, p3, p4)
    def x(self) :
        points = super().getPoints()
        return points[0].getX() + 5
    def y(self) :
        points = super().getPoints()
        return points[0].getY() + 5


score = 0

win = GraphWin("Snake", 650, 600, autoflush = False)
win.setCoords(0, 0, 600, 650)
win.setBackground("blue")

status_line = Line(Point(0, 0), Point(600, 0))
status_line.setOutline("black")
status_line.setWidth(50)
status_line.draw(win)

status_text = Text(Point(300, 10), "")
status_text.setText("Score: {}".format(score))
status_text.setTextColor("white")
status_text.setFace("helvetica")
status_text.draw(win)

c = Segment(Point(300, 300), Point(300, 310), Point(310, 310), Point(310, 300))
c.setFill("white")
c.draw(win)




dx = 0
dy = 0   

while True:
    x = c.x() - 5 
    y = c.y() - 5
    if c.x() <= 0 or c.x() >= 600 or c.y() <= 36 or c.y() >= 650 :
        status_text.undraw()
        status_text.setText("You lost. Press any key...")
        status_text.draw(win)
        win.getKey()
        x = 300
        y = 300
    c.undraw()
    c = Segment(Point(x + dx, y + dy), Point(x + dx, y + 10 + dy), Point(x + 10 + dx, y + 10 + dy), Point(x + 10 + dx, y + dy))
    c.setFill("white")
    c.draw(win)
    key = win.checkKey()
    if key == "Up" :
        dy = 5 
        dx = 0
    elif key == "Down" :
        dy = -5
        dx = 0
    elif key == "Right" :
        dy = 0
        dx = 5
    elif key == "Left" :
        dy = 0
        dx = -5 # чтобы не было задержки надо в этих if-ах отрисовывать
    score += 1
    status_text.undraw()
    status_text.setText("Score {}".format(score))
    status_text.draw(win)
    update(15)
    



    
