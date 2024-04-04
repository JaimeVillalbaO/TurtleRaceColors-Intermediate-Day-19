from turtle import Turtle, Screen
import random 

screen = Screen()

screen.setup(width=1300,height= 500)
# colormode(255)

bet_user = screen.textinput(title='MAKE YOU BET', prompt='Which turtle will win the race? Enter a color...')

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "purple"
]

all_new_turtle = []
y_movement = [230, 160, 90, 20, -50, -120, -190]

for turtle in range(0, 7):

    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-630, y=y_movement[turtle])
    new_turtle.color(colors[turtle])
    all_new_turtle.append(new_turtle)

game_over = False
while not game_over:
    for turtle in all_new_turtle:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 630:
            winning_Color = turtle.pencolor()
            if winning_Color == bet_user.lower():
                screen.textinput('You win!!! ', 'You win!!!')
            else:
                screen.textinput('YOU LOSED', f'You losed. The winning was {turtle.pencolor()}')
            game_over = True

screen.exitonclick()
