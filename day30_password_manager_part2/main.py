from _ast import mod
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    ppp = password_entry.get()

    if len(ppp) > 0:
        password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    aa = [choice(letters) for _ in range(1, 9)]
    ss = [choice(symbols) for _ in range(1, 5)]
    dd = [choice(numbers) for _ in range(1, 5)]
    password_list = aa + ss + dd
    shuffle(password_list)
    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    name = name_entry.get()
    email = email_entry.get()

    new_data = {
        name: {
            'email': email,
            'password': password,
        },
    }

    if len(name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="make sure name and password field not empty")

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            name_entry.delete(0, END)


# ---------------------------- find detail ------------------------------- #
def find_detail():
    name = name_entry.get()
    try:
        with open('data.json',mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="file not found !")
    else:
        if name in data:
            email = data[name]['email']
            password = data[name]['password']
            messagebox.showinfo(title="result",message=f" the email: {email}\n the password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"no detail exists for ' {name} ' !")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string='password Manager')
window.config(pady=20, padx=20, )
img = PhotoImage(file='logo.png')
canvas = Canvas(width=250, height=250, )
canvas.create_image(125, 125, image=img)
canvas.grid(row=0, column=1, columnspan=2)

name_label = Label(text="name :")
email_label = Label(text="email :")
password_label = Label(text="password :")

name_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

name_entry = Entry(width=21)
name_entry.focus()
email_entry = Entry(width=41)
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=21)

name_entry.grid(row=1, column=1, )
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, )

search_btn = Button(text="search",width=15,command=find_detail)
search_btn.grid(row=1, column=2)
password_btn = Button(text="generate password", width=15, command=generate)
password_btn.grid(row=3, column=2)

add_btn = Button(text="add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
