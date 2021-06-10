from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    label_heading.config(text="Timer")
    label_tick.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_heading.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_heading.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_heading.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        working_session = math.floor(reps/2)
        for _ in range(working_session):
            marks += "✔"
        label_tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label for heading
label_heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
label_heading.grid(column=2, row=1)
label_tick = Label(fg=GREEN, bg=YELLOW)
label_tick.grid(column=2, row=4)

# canvas widget
canvas = Canvas(width=210, height=227, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
timer_txt = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# button for start and stop
start_button = Button(text="Start", bg="white", highlightthickness=0, borderwidth=0.1, command=start_timer)
start_button.config(padx=8, pady=5)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", bg="white", highlightthickness=0, borderwidth=0.1, command=reset_timer)
reset_button.config(padx=8, pady=5)
reset_button.grid(column=3, row=3)

window.mainloop()
