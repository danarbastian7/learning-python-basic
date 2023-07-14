from turtle import Turtle, Screen
import random
#
timy_turtle = Turtle()
# # timy_the_turtle.shape("turtle")
# # timy_the_turtle.color("red")
# # timy_the_turtle.forward(100)
# # timy_the_turtle.right(90)
# # timy_the_turtle.forward(100)
# #Make the turtle draw square shape
# for _ in range(4):
#     timy_turtle.forward(100)
#     timy_turtle.right(90)
#
#
# screen = Screen()
# screen.exitonclick()
#
# ==========================
# Aliasing Modul
# import turtle as t
# tim = t.Turtle()


# Draw Dashed Line using Turtle

# timy_turtle.fillcolor("blue")
# timy_turtle.pencolor("red")
# for t in range (15):
#     timy_turtle.forward(10)
#     timy_turtle.penup()
#     timy_turtle.forward(10)
#     timy_turtle.pendown()


colours = ["blue", "red", "gray", "brown", "purple", "green", "black"]
def draw_shape(num_sides):
    for t in range(num_sides):
        angle = 360 / num_sides
        timy_turtle.forward(100)
        timy_turtle.right(angle)

for shape_side_n in range(3, 11):
    timy_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()