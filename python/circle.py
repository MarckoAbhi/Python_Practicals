import turtle as t
import colorsys
t.tracer(500)
t.bgcolor('black')
h = 0.1
t.width(3)
t.up()
t.goto(0, 400)
t.down()
for i in range(310):
	color = colorsys.hsv_to_rgb(h, 1, 1)
	t.color(color)
	for j in range(4):
		t.rt(121)
		t.circle(80, 220)
		t.rt(121)
		h += 0.002
		t.ht()

t.done()