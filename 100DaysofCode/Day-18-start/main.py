import turtle as t
import random
#
timmy_turtle = t.Turtle()
t.colormode(255)

# timmy_turtle.shape("turtle")
# timmy_turtle.color("DarkMagenta")
#
# # Create a square
# for _ in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)

#Create a dashline

# for _ in range(15):
#
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()

# Creating different shape
colors = ["chartreuse", "medium turquoise", "cyan", "dark slate gray", "tan", "deep pink", "orange red", "sienna"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)

for shape_side_n in range(3, 11):
    timmy_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

# Draw a random walk
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# timmy_turtle.speed("fastest")

# direction = [0, 90, 180, 270]
# timmy_turtle.pensize(15)
#
# for _ in range(200):
#     timmy_turtle.color(random_color())
#     timmy_turtle.forward(30)
#     timmy_turtle.setheading(random.choice(direction))


# Draw Spirograph

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# timmy_turtle.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy_turtle.color(random_color())
#         timmy_turtle.circle(100)
#         timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)
#
#
# draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

