import time
import turtle as t
import pandas as pd

screen = t.Screen()
screen.title('US States Game')
screen.bgpic('blank_states_img.gif')
screen.tracer(2)
time.sleep(0.1)
data = pd.read_csv('50_states.csv')
print(data)

all_states = data['state'].to_list()
x_cor = data['x'].to_list()
y_cor = data['y'].to_list()
final_list = []
guessed_states = []
g = 0
while g <= 50:
    user_guess = screen.textinput(f'{g}/50 States Correct', 'Name a state:')
    if user_guess == 'Exit':
        final_list = [n for n in all_states if n not in guessed_states]
        final_result = pd.DataFrame(final_list)
        final_result.to_csv('unknown_states')
        break
    if user_guess in all_states:
        for i in range(len(all_states)):
            if all_states[i] == user_guess:
                guessed_states.append(all_states[i])
                turtle = t.Turtle()
                turtle.hideturtle()
                turtle.speed(900)
                turtle.penup()
                turtle.goto(x_cor[i], y_cor[i])
                turtle.write(f'{all_states[i]}', move=False, font=('Arial', 11, 'normal'))
                g += 1
                break














