import turtle
import pandas

FONT = FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# print(all_states)

answer_state = screen.textinput(title="Guess the State", prompt="Give another state's name.").capitalize()

if answer_state in all_states:
    guessed_state = data[data.state == answer_state]
    x_position = int(guessed_state.x)
    y_position = int(guessed_state.x)
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x_position, y_position)
    new_turtle.color("black")
    new_turtle.write(f"{answer_state}", align="center", font=FONT)
    


screen.exitonclick()