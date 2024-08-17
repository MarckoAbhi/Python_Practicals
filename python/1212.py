import turtle 
g = 1
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
while True:
    t.forward(g)
    t.color('red')
    t.left(100*30)
    t.left(1)
    g += 1
    t.forward(g)
    t.color('greenyellow')
    t.right(350)
    t.radians()
    t.color('purple')
    t.right(30)
turtle.done()