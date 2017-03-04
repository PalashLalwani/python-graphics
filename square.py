import turtle

def draw_square(var):
    for i in range(1,5):
      var.forward(100)
      var.right(90)


def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    #create the turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    brad.right(10)

    for i in range(1,37):
      draw_square(brad)
      brad.right(10)
      
    #create the turtle an
    an = turtle.Turtle()
    an.shape("arrow")
    an.color("yellow")
    an.circle(100)

    window.exitonclick()
draw()
    
  
