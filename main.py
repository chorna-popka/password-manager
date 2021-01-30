from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+' ]

LABEL_FONT = ("Open Sans", 14, "normal")


def is_valid(*input_str):
    for string in input_str:
        if len(string) == 0:
            lbl_04.config(text=f"Please provide all values", fg="#ab0000")
            return False
    return True


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    p1 = [ random.choice(letters) for _ in range(nr_letters) ]
    p2 = [ random.choice(symbols) for _ in range(nr_symbols) ]
    p3 = [ random.choice(numbers) for _ in range(nr_numbers) ]

    pwd_list = p1 + p2 + p3
    random.shuffle(pwd_list)

    password = "".join(pwd_list)

    input_pwd.delete(0, END)
    input_pwd.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = input_site.get()
    user = input_email.get()
    pwd = input_pwd.get()

    if is_valid(site, user, pwd):
        is_ok = messagebox.askokcancel(title="Please confirm",
                                       message=f"You entered: \n Site: {site} \n Login: {user} \n "
                                               f"Password: {pwd} \n Do you want to save?")
        if is_ok:
            str_save = f"{site} | {user} | {pwd} \n"
            with open("data.txt", "a") as data_txt:
                data_txt.write(str_save)

            input_site.delete(0, END)
            input_pwd.delete(0, END)
            lbl_04.config(text="Entry successfully saved!", fg="#298701")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=50)

img_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)

lbl_01 = Label(text="Website", font=LABEL_FONT)
lbl_01.grid(column=0, row=1, sticky=E)
lbl_02 = Label(text="Email/Username", font=LABEL_FONT)
lbl_02.grid(column=0, row=2, sticky=E)
lbl_03 = Label(text="Password", font=LABEL_FONT)
lbl_03.grid(column=0, row=3, sticky=E)
lbl_04 = Label(text="", font=LABEL_FONT, fg="#298701")
lbl_04.grid(column=0, row=5, columnspan=3, pady=10)

input_site = Entry(width=35)
input_site.grid(column=1, row=1, columnspan=2)
input_site.focus()
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "kalbust@gmail.com")
input_pwd = Entry(width=21)
input_pwd.grid(column=1, row=3)

btn_generate = Button(text="Generate password", command=gen_pwd)
btn_generate.grid(column=2, row=3)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)
window.mainloop()
