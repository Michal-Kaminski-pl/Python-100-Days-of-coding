import turtle
import pandas as pd 
import time
timer_turtle = turtle.Turtle()
timer_turtle.ht()
timer_turtle.up()
timer_turtle.goto(200,240)
def countdown(t):
    timer_turtle.clear()
    mins, secs = divmod(t, 60)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    timer_turtle.write(f"Time: {time_format}", font=("Courier", 20, "bold"))
def create_state(name):

    state_data = df[df.state == name.capitalize()]
    cord_x = int(state_data.x.item())
    cord_y = int(state_data.y.item())
    coordinates = (cord_x, cord_y)
    state = turtle.Turtle()
    state.ht()
    state.up()
    state.goto(coordinates)
    state.write(name, font=("Arial", 8, "normal"))

df = pd.read_csv("50_states.csv")
states = df.state.to_list()

screen = turtle.Screen()
screen.title("USA guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_score = 0
t = 600
start_time = time.time()
guessed_states = []
while len(guessed_states) < 50:
    uplyniety_czas = int(time.time() - start_time)
    pozostaly_czas = t - uplyniety_czas
    if pozostaly_czas <= 0:
        timer_turtle.clear()
        timer_turtle.write("TIME'S UP!", font=("Courier", 20, "bold"))
        break
    countdown(pozostaly_czas)

    user_answer = screen.textinput(f"guess the state {user_score}/50", "What's another state?")
    
    if user_answer.capitalize() in states and user_answer.capitalize() not in guessed_states:
        guessed_states.append(user_answer)
        create_state(user_answer)
        user_score += 1

if user_score == 50:
    timer_turtle.write("WYGRAŁEŚ!", align="center", font=("Courier", 30, "bold"))

states_to_learn = [state for state in states if state not in guessed_states]

states_to_learn_df = pd.DataFrame(states_to_learn)
states_to_learn_df.to_csv("stany_do_nauczenia.csv")

screen.exitonclick()