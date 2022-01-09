from turtle import Screen
from states_manager import StatesManager
screen = Screen()
screen.title("US States Game")
screen.tracer(0)
screen.bgpic("blank_states_img.gif")
states_manager = StatesManager()
on = True
while on:
    screen.update()
    answer = screen.textinput(f"{len(states_manager.answers)}/50", "Write another State")
    states_manager.check(answer)
    if len(states_manager.answers) == 50:
        on = False
    if answer == "Exit":
        states_manager.exit()
        break
screen.exitonclick()