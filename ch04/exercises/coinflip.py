import turtle
import random


window = turtle.Screen()
window.bgcolor("dimgray")

myturtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("mistyrose")
turtle.up()
turtle.goto(0,0)
turtle.delay(150)

while True: 
  i = random.randint(1,2)
  if i==1:
    print("heads")
    myturtle.left(90)
    myturtle.fd(50)
  else:
    print("tails")
    myturtle.right(90)
    myturtle.fd(50)


window.exitonclick()