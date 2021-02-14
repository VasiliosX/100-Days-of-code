import tkinter
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_list=[random.choice(letters) for _ in range(nr_letters)]

    password_list+=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list+=[random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(index=0, string=password)




# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    web = entry_web.get()
    password = entry_password.get()
    mail = entry_mail.get()

    if mail=='' or password=='':
        messagebox.showinfo(title='Warning', message='Please do not leave any of the fields empty.')
    else:

        answer= messagebox.askokcancel(title=web, message=f'These are the details entered, Email: {mail}\n, Password:{password}\n Are you sure you want to save?')

        if answer:
            with open('mydata.txt', 'a') as data:

                data.write(f'{web} | {mail} | {password}\n')
                entry_password.delete(first=0,last=len(password))

                entry_web.delete(first=0, last=len(web))




# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()

window.title('Password Manager')

window.config(padx=30,pady=30, bg='#fefefa')

canvas = tkinter.Canvas(height=200,width=200, bg='#fefefa',highlightthickness=0 )

logo = tkinter.PhotoImage(file='logo.png')



canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

label_web=tkinter.Label(text='Website:', highlightthickness=0 ,bg='#fefefa')
label_web.grid(row=1,column=0)

label_mail=tkinter.Label(text='Email/Username:',highlightthickness=0 ,bg='#fefefa' )
label_mail.grid(row=2,column=0)


label_password=tkinter.Label(text='Password:' ,highlightthickness=0 ,bg='#fefefa' )
label_password.grid(row=3,column=0)


entry_web=tkinter.Entry(width=52 )
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.focus()

entry_mail=tkinter.Entry(width=52)
entry_mail.grid(row=2, column=1, columnspan=2)



entry_password=tkinter.Entry(width=52)
entry_password.grid(row=3, column=1, columnspan=2)

button_generate=tkinter.Button(text='Generate Password', command=generate_password)
button_generate.grid(row=3,column=2)

button_add=tkinter.Button(text='Add', width=44,command=save_data)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()