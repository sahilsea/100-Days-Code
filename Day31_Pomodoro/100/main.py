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
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= f"00:00")
    title_label.config(text="Timer", fg= GREEN)
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=RED )
    else:
        count_down(work_sec)
        title_label.config(text= "WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_count = math.floor(count/60)
    sec_count = count%60
    if sec_count  < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks =""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔️"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 90, pady=45, bg= YELLOW)

# Label - Timer text
title_label = Label(text="Timer",font= (FONT_NAME, 35), fg=GREEN,bg= YELLOW)
title_label.grid(column=1, row= 0)

# Canvas for the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img )
timer_text = canvas.create_text(103, 130, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Start Button
start_button = Button(text="Start", highlightthickness=0, command= start_timer,)
start_button.grid(column=0, row= 2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0,command= reset_timer)
reset_button.grid(column=2, row= 2 )

# Tick Button
tick_label = Label(highlightthickness=0,)
tick_label.grid(column=1, row= 3)







window.mainloop()