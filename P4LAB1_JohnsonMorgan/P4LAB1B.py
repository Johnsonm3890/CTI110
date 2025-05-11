# Morgan Johnson
# 4/05/2025
# P4LAB1B
# Turtle Program to draw  MJ (initials)


import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()       # Create a turtle, assign to t

# add some display options
t.pensize(3)              # increase pensize (takes integer)
t.pencolor("hotpink")     # set pencolor (takes string)
t.shape("arrow")

#Draw the M
t.left(90)
t.forward(90)
t.right(150)
t.forward(45)
t.left(150)
t.right(30)
t.forward(45)
t.right(150)
t.forward(90)
t.left(90)

# M complete

# Position for next letter
t.penup()
t.forward(45)
t.left(90)
t.forward(90)
t.right(90)
# Position complete

# draw J
t.pendown()
t.forward(45)
t.backward(45/2)
t.right(90)
t.forward(87)
t.right(45)

for i in range(15):
    t.forward(2)
    t.right(7.5)

#j Complete


# Hide turtle to view drawing better
t.hideturtle()



# end commands
wn.mainloop()             # Wait for user to close window
