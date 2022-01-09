from turtle import Turtle
import pandas
class StatesManager(Turtle):
    def __init__(self):
        super().__init__()
        self.states = {}
        self.ht()
        self.pu()
        self.answers = []
        states_data = pandas.read_csv("50_states.csv")
        states_list = states_data.state.to_list()
        x_list = states_data.x.to_list()
        y_list = states_data.y.to_list()
        for s in range(len(states_list)):
            state = Turtle()
            state.pu()
            state.ht()
            self.states[states_list[s]] = [state, (x_list[s], y_list[s])]
    def check(self, answer):
        for state in self.states:
            if answer.lower() == state.lower() and not answer.lower() in self.answers:
                self.states[state][0].goto(self.states[state][1])
                self.states[state][0].write(arg=state, font=("Courier", 10, "normal"), align="Center")
                self.answers.append(answer.lower())
                return True
    def exit(self):
        for state in self.states:
            if not state.lower() in self.answers:
                self.states[state][0].goto(self.states[state][1])
                self.states[state][0].color("red")
                self.states[state][0].write(arg=state, font=("Courier", 10, "normal"), align="Center")
