import turtle

turt = turtle.Turtle()

# Your drawing code here

turt.forward(100)  
turt.right(90)
turt.forward(200)
turt.left(90)
turt.forward(50)

turt.penup() 	
turt.goto(-100, 100)
turt.pendown() 
turt.color('red')

for i in range(4):  # loop 4 times
    turt.forward(50)
    turt.right(90)




# Keeps the window open
turtle.done()