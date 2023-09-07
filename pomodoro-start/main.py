import tkinter as tk

# # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None
# # ---------------------------- TIMER RESET ------------------------------- # 

# # ---------------------------- TIMER MECHANISM ------------------------------- # 

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# # ---------------------------- UI SETUP ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 2:
        time_sec = work_sec
        timer_label.config(fg=PINK,text="WORK")
    else: 
        if reps == 8: 
            time_sec = long_break_sec
            timer_label.config(fg=RED,text="LONG BREAK") 
        else: 
            time_sec = short_break_sec  
            timer_label.config(fg=GREEN,text="BREAK")

    click_start(time_sec)

def click_start(count):
    minute = count//60
    second = count%60
    # if second < 10: second = f"0{second}" 가능
    # dynamic typing 
    canvas.itemconfig(my_text,text="{0:02d}:{1:02d}".format(minute,second))

    if count>0:
        global timer
        timer = window.after(1000,click_start, count-1)
    else: 
        if reps % 2==0:
            check_count = reps // 2
            check_label.config(text="✔"*check_count)
        start_timer()

def click_reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(my_text,text="00:00")
    check_label.config(text="")
    timer_label.config(fg=GREEN,text="Timer")

window = tk.Tk()
window.title("Pamodoro timer")
window.config(padx=100,pady=50,bg=YELLOW)

# def say_something(h,e,l,o):
#     print(h,e,l,o)

# window.after(1000, say_something, "h","e","l","o")

# canvas 만들기
canvas = tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

tomato_image = tk.PhotoImage(file="/Users/user/OneDrive/바탕 화면/language/python 학습자료/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomato_image)
my_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# Label
timer_label = tk.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
timer_label.grid(column=1,row=0)

check_label = tk.Label(fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)


#button
start_button = tk.Button(text="Start",command=start_timer,highlightthickness=0)
reset_button = tk.Button(text="Reset",command=click_reset,highlightthickness=0)

start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

window.mainloop()
