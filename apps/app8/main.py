from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    email = email_username_input.get()
    password = password_input.get()
    website = website_input.get()


    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Day29_End\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website = Label(text="Website:")
website.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=35)
website_input.focus( )
website_input.grid(column=1, row=1, columnspan=2)
person_website_input = website_input.get()

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_username_input = Entry()
email_username_input.config(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "kalle.pohjanjoki@gmail.com")
person_email_username_input = email_username_input.get()

password = Label(text="Password:")
password.grid(column=0, row=3)


password_input = Entry()
password_input.config(width=17)
password_input.grid(column=1, row=3,)
person_password_input = password_input.get()


generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)


add = Button(text="Add", command=save_password)
add.config(width=30)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()