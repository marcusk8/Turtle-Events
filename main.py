import turtle



turtle.title("Drawing Turtle")
turtle.bgcolor("Blue")
turtle.setup(600,600)



screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(0)


def pattern():
  for i in range(36):
    bob.circle(100)
    bob.right(10)



screen.onkey(pattern, "space")
# screen.onclick(bob.goto)
screen.listen()