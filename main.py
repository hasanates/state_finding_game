import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
all_coordinates = df.to_dict()

counter = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state {counter}/50", prompt="Name a state")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        position = df[df.state == answer_state]

        writer.goto(int(position.x), int(position.y))
        writer.color("black")
        writer.write(position.state.item())
        counter += 1

screen.exitonclick()
