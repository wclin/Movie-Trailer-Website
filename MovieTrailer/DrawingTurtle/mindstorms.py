import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    
    t = turtle.Turtle()
    t.speed(20)
    step = 200
    while step > 1:
        t.forward(step)
        t.right(179)
        step -= 1
        t.forward(step)
        t.left(179)
        step -= 1
    window.exitonclick()

draw_art()

