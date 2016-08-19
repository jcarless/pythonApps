import turtle

def draw_square(some_turtle):
	num = 1

	while num <= 4:
		some_turtle.forward(100)
		some_turtle.right(90)
		num += 1



def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("white")
	brad.shape("arrow")
	brad.speed(5)

	for i in range (1, 37):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()




# def draw_circle():
# 	angie = turtle.Turtle()
# 	angie.shape("turtle")
# 	angie.color("green")
# 	angie.circle(100)

# def draw_triangle():
# 	john = turtle.Turtle()
# 	john.color("blue")
# 	john.speed(8)

# 	john.forward(50)
# 	john.left(90)
# 	john.forward(100)
# 	john.left(40)
# 	john.forward(45)
# 	john.left(100)

draw_art()