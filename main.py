import turtle 
import pandas 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct" , prompt="What's another state's name?").title()
    if answer_state == "Exit" :
        missed_states = []
        for state in all_states :
            if state not in guessed_states :
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states :
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == answer_state]
        t.goto(data_state.x.item(), data_state.y.item())
        t.write(data_state.state.item())
        guessed_states.append(answer_state)








