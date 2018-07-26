import turtle


def draw_shapes():
    window = turtle.Screen() # Make an environment for Tom
    window.bgcolor('white')

    tom = turtle.Turtle()
    tom.shape('turtle')
    tom.color('green')
    tom.speed(1.5)

    for i in range(4): # This loop makes the square
        tom.forward(100)
        tom.right(90)

    amy = turtle.Turtle() # Second Turtle, to make a circle
    amy.shape('arrow')
    amy.color('blue')
    amy.circle(100)

    window.exitonclick()
#
# draw_shapes()


# DRAW A CIRCLE WITH SQUARES
def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    canvas = turtle.Screen()
    canvas.bgcolor('white')
    rob = turtle.Turtle()
    rob.shape('turtle')
    rob.color('green')
    rob.speed(10)
    for i in range(1,37):
        draw_square(rob)
        rob.right(10)

    canvas.exitonclick()


draw_circle()
