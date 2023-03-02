import turtle
import pandas
print("test")
FONT = FONT = ("Arial", 9, "normal")

# setting the screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get data from csv
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} States Correct", prompt="Give another state's name.").title()
    if answer_state == "Exit":
        states_missing = [ state for state in all_states if state not in guessed_states]
        print(states_missing)
        new_data = pandas.DataFrame(states_missing)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_position = int(state.x)
        y_position = int(state.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_position, y_position)
        t.write(f"{answer_state}", align="center", font=FONT)


