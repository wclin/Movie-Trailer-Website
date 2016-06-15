import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)
    step = 10
    while step < 500:
        brad.forward(step)
        brad.right(90)
        step *= 1.2
    window.exitonclick()

draw_square()
