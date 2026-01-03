from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    if timer:
        window.after_cancel(timer)
    canva.itemconfig(timer_text, text = "00:00")
    checkmark_label.config(text = "")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = 5
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="PRZERWA", fg= RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="PRZERWA", fg = PINK)
    else:
        countdown(work_sec)
        label.config(text="PRACUJ", fg = GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    mins, secs = divmod(count, 60)
    if secs < 10:
        secs = f"0{secs}" 
    canva.itemconfig(timer_text, text = f"{mins}:{secs}")
    
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        sesje = int(reps/2)
        for n in range(sesje):
            marks += "✓"
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodorro app")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_tomato = PhotoImage(file= "tomato.png")
canva.create_image(102, 112, image = photo_tomato)
canva.grid(row=1, column=1)

timer_text = canva.create_text(102, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))

checkmark_label = Label(text=f"", font=(FONT_NAME, 12, "bold"), fg = GREEN, bg= YELLOW)
checkmark_label.grid(row=2, column=1)

reset_button = Button(text="RESET", width=5, height=1, font=(FONT_NAME, 8, "bold"), command=reset_timer)
reset_button.grid(row=2, column=0)

start_button = Button(text="START", width=5, height=1, font=(FONT_NAME, 8, "bold"), command=start_timer)
start_button.grid(row=2, column=2)


window.mainloop()
