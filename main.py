import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("blue")
turtle.setup(600,600)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("white")

screen.onclick(bob.goto)
#bob.ondrag(bob.goto)
screen.listen()

#The pattern above consists of circles drawn repeatedly at different angles - 
#Declare a function to draw a circle - Use a while loop to draw a circle and turn repeatedly

