import turtle
import pandas

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


screen.exitonclick()