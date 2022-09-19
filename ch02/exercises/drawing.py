import turtle
my_turtle = turtle.Turtle()

turtle.delay(75)
my_turtle.shape("turtle")
my_turtle.color("#f47b7b")

sides = int(input("Enter the number of sides:"))
length = int(input("Enter the length of the sides:"))

turn = ((sides-2)*180/sides)
if turn > 90:
  turn = turn % 90
  turn= 90 - turn

n = 0
for n in range (0, sides):
  my_turtle.fd(length)
  my_turtle.right(turn)
  n + 1