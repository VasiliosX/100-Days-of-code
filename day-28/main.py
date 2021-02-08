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
reps=0
check_mark_text=''
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global check_mark_text

    window.after_cancel(timer)
    label_timer.config(text='Timer', fg=GREEN)
    reps=0
    check_mark_text =''
    label_check_mark.config(text=check_mark_text)
    canvas.itemconfig(timer_text, text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    time_length=0

    if reps%2==0:
        time_length=25
        label_timer.config(text='Work', fg=GREEN)
    elif reps%2!=0 and reps%7!=0:
        time_length = 5
        label_timer.config(text='Short break', fg=PINK)
    elif reps%7==0:
        time_length = 20
        label_timer.config(text='Long break', fg=RED)
    count_down(time_length)
    print(reps)
    reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global check_mark_text
    global reps
    count_minutes = math.floor(count/60)
    count_seconds = count % 60


    if count_seconds<10:
        count_seconds=f'0{count % 60}'

    canvas.itemconfig(timer_text,text=f'{count_minutes}:{count_seconds}')

    if count>0:
     timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            check_mark_text+='✓'
            label_check_mark.config(text=check_mark_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)





canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato)

timer_text=canvas.create_text(100,130,text='00:00',fill='white', font=(FONT_NAME,35,'bold'))

canvas.grid(column=1,row=1)



label_timer=Label(text='Timer',fg=GREEN, bg=YELLOW,font=('Arial',30,'bold'))
label_timer.grid(column=1, row=0)



label_check_mark=Label(text=check_mark_text)
label_check_mark.grid(column=1,row=5)

button_reset=Button(text='Reset',command=reset_timer)
button_reset.grid(column=2,row=4)

button_start=Button(text='Start',command=start_timer)
button_start.grid(column=0,row=4)

window.mainloop()