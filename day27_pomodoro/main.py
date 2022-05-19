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
    window.after_cancel(timer)
    lb.config(text="TIMER",foreground=GREEN)
    lb2.config(text="",)
    canvas.itemconfig(title_num , text="00:00")
    global reps
    reps = 0 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        lb.config(text="WORK", foreground=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        lb.config(text="BREAk", foreground=PINK)
    else:
        count_down(20 * 60)
        lb.config(text="BREAk", foreground=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(title_num, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        r = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            r += "✔"
        lb2.config(text=r, foreground=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string='pormodoro', )
window.config(padx=20, pady=20, bg=YELLOW)
lb = Label(text="TIMER", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
lb.grid(row=0, column=1)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=img)
title_num = canvas.create_text(150, 160, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="start", width=10, highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="reset", width=10, highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

lb2 = Label(text="", foreground=GREEN)
lb2.grid(row=3, column=1)
window.mainloop()
