import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals? (2-6)", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?",6))

    
for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for x in range(number_of_circles):
        t.pendown()
        t.circle(100)
        t.left(360/number_of_circles)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
