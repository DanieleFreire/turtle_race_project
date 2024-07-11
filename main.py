from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour(red, orange, "
                                                          "yellow, green, blue or purple): ")

turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-200, y_positions[turtle_index])
    #appending the range of multiple turtle created
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:
    #looping through the multiple turtles to make them move
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)



screen.exitonclick()
