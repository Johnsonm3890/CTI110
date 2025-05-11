# Morgan Johnson
# 4/05/2025
# P4LAB1A
# Turtle Program to draw a triangle & Square

import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()    # Create a turtle, assign to alex

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")


# Draw Square
for i in range(4):
    t.forward(50)
    t.left(90)
# Square complete

#move turtle to better position for triangle
t.left(90)
t.forward(50)
t.right(90)
#position complete

#draw triangle
for j in range(4):
    t.forward(50)
    t.left(120)
#triangle complete

# Hide turtle to view drawing better

t.hideturtle()

# end commands
wn.mainloop()             # Wait for user to close window
