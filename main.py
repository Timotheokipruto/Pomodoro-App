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
    checkmark_label.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
        
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
        

        
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <10:
        count_sec = (f"0{count_sec}")
    if count_min==0:
        countdown_text = (f"00:{count_sec}")
    else:
        countdown_text = (f"{count_min}:{count_sec}")

    canvas.itemconfig(timer_text,text=countdown_text)
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions= reps//2
        for _ in range(work_sessions):
            marks+= "✅︎"
        
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas_width = 200
canvas_height = 224
canvas = Canvas(width=canvas_width, height=canvas_height,bg=YELLOW,highlightthickness=0)
canvas_image = PhotoImage(file="tomato.png")
canvas.create_image(canvas_width//2,canvas_height//2, image=canvas_image)
timer_text = canvas.create_text(102,130,text="00:00",font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1,column=1)


   



title_label = Label(text="Timer",font=(FONT_NAME, 40, "normal"),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)

start_button = Button(text="start",highlightbackground=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="reset",highlightbackground=YELLOW,command=reset_timer)
reset_button.grid(row=2,column=2)

checkmark_label = Label(fg=GREEN,bg=YELLOW)
checkmark_label.grid(row=3,column=1)





window.mainloop()