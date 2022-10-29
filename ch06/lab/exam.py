import turtle
import random

window = turtle.Screen()

window.bgcolor("#3F3F3F")

bejewel = turtle.Turtle()
bejewel.shape("turtle")
turtle.delay(10)

def circle(radius, extent):
  for i in range(1):
    bejewel.circle(10, 360)

def round_rectangle(length, high, cor_angle, cor_rad):
  for i in range(2):
    bejewel.fd(high)
    bejewel.circle(cor_rad,cor_angle)
    bejewel.fd(length)
    bejewel.circle(cor_rad, cor_angle)

def main():
#pizzabox
  bejewel.up()
  bejewel.ht()
  bejewel.goto(-125,145)
  bejewel.st()
  bejewel.down()

  bejewel.color("#F9F8F3")
  bejewel.fillcolor("#F9F8F3")
  bejewel.begin_fill()

  for i in range(4):
    bejewel.fd(250)
    bejewel.right(90)

  bejewel.end_fill()

  #pizzacrust
  bejewel.up()
  bejewel.ht()
  bejewel.goto(0,-70)
  bejewel.st()
  bejewel.down()

  bejewel.color("#D1A869")
  bejewel.fillcolor("#D1A869")
  bejewel.begin_fill()
  bejewel.circle(100,360)
  bejewel.end_fill()

  #pizzasauce
  bejewel.ht()
  bejewel.goto(0,-60)
  bejewel.st()

  bejewel.color("#DE4622")
  bejewel.fillcolor("#DE4622")
  bejewel.begin_fill()
  bejewel.circle(90,360)
  bejewel.end_fill()

  #cheese
  bejewel.ht()
  bejewel.goto(0,-55)
  bejewel.st()

  bejewel.color("#F6DF82")
  bejewel.fillcolor("#F6DF82")
  bejewel.begin_fill()
  bejewel.circle(85,360)
  bejewel.end_fill()
  

  #pepperoni
  for i in range(10):
    x = random.randrange(-50,70)
    y = random.randrange(-40,80)
    bejewel.color("#A63D12")
    bejewel.fillcolor("#A63D12")
    bejewel.up()
    bejewel.goto(x,y)
    bejewel.begin_fill()
    circle(5,360)
    bejewel.end_fill()

    #pineapple
  for i in range(10):
    x = random.randrange(-50,70)
    y = random.randrange(-40,80)
    bejewel.color("#cccc00")
    bejewel.fillcolor("#cccc00")
    bejewel.up()
    bejewel.goto(x,y)
    bejewel.begin_fill()
    round_rectangle(10,5,90,5)
    bejewel.end_fill()

main()
window.exitonclick()
