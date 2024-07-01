import turtle

# Create a turtle named "duck"
duck = turtle.Turtle()

# Function to draw a basic duck outline
def draw_duck():
    # Body
    duck.forward(50)
    duck.right(90)
    duck.forward(30)
    duck.right(90)
    duck.forward(50)
    duck.right(90)
    duck.forward(30)
    duck.right(90)

    # Head
    duck.right(90)
    duck.forward(20)
    duck.left(90)
    duck.circle(20, -180)  # Draw a semicircle for the head
    duck.left(90)
    duck.forward(20)

    # Beak
    duck.right(90)
    duck.forward(10)
    duck.left(45)
    duck.forward(10)
    duck.left(90)
    duck.forward(10)
    duck.left(45)
    duck.forward(10)

    # Tail
    duck.right(90)
    duck.forward(20)
    duck.right(90)
    duck.forward(10)
    duck.left(90)
    duck.forward(20)

# Set up the turtle
duck.speed(2)  # Set the turtle speed (1 to 10, 10 being the fastest)

# Call the draw_duck function to draw a basic duck outline
draw_duck()

# Close the turtle graphics window when clicked
turtle.exitonclick()
