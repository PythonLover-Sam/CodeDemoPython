import turtle
from random import randint
turtle.color('light green')
turtle.screensize(800,600, "black")
turtle.speed(1000)
turtle.pensize(3)

turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
times = 63
while times>=0:
	turtle.fillcolor((randint(0, 100)/100, randint(0, 100)/100, randint(0, 100)/100))
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(60)
		turtle.right(90)
	turtle.end_fill()
	if times % 8 != 0:
		turtle.forward(60)
	else:
		turtle.penup()
		turtle.goto(-300, 200-60*((64-times)//8))
		turtle.pendown()
	times -= 1

turtle.mainloop()