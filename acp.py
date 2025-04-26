import turtle

# Creating canvas
turtle.Screen().bgcolor("Blue")
turtle.title("Welcome to Turtle Window")
sc = turtle.Screen()
sc.setup(900, 600)

# Turtle object creation
board = turtle.Turtle()

# Equilateral Triangle
board.penup()
board.goto(-300, 0)
board.pendown()
for i in range(3):
    board.forward(100)
    board.left(120)

# Reset heading before drawing the rectangle
board.setheading(0)  

# Rectangle 
board.penup()
board.goto(-50, 0)
board.pendown()
for i in range(2):
    board.forward(150)
    board.left(90)
    board.forward(100)
    board.left(90)

board.setheading(0) 

# Hexagon
board.penup()
board.goto(300, 0)
board.pendown()
for i in range(6):
    board.forward(60)
    board.left(60)

turtle.done()