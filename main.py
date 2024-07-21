from tkinter import *
from tkinter import messagebox
from Password_Generator import Generator
import json

#--------------------------------Find Password-------------------------------#

def find_password():
    try:
        with open("data.json") as data:
            data_dict = json.load(data)
            website_data = data_dict[website_input.get()]
            messagebox.showinfo(website_input.get(), f"Email: {website_data["email"]}\nPassword: {website_data["password"]}")
    except KeyError:
        messagebox.showinfo("Not Found!", "The requested website was not found!")
    except FileNotFoundError:
         messagebox.showinfo("Not Found!", "The requested website was not found!")

#------------------------------Generate Password-----------------------------#
password_generator = Generator
def generate_password():
    password = password_generator.generate()
    password_input.delete(0, END)
    password_input.insert(0, password)

#-------------------------------Save Password--------------------------------#

def save_data():
    if len(website_input.get()) == 0 or len(username_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo("Oops!", "Please make sure all fields are full!")
    else:
        data = ""
        website_ = website_input.get()
        email_ = username_input.get()
        password_ = password_input.get()
        data = {
            website_: {
                "email": email_,
                "password": password_,
            }
        }
        def confirmed():
            try:
                with open("data.json", mode="r") as data_file:
                    data_ = json.load(data_file)
            except FileNotFoundError:
                file = open("data.json", mode="a")
                json.dump(data, file, indent=4)
                file.close()
            else:
                data_.update(data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data_, data_file, indent=4)
                    website_input.delete(0, END)
                    password_input.delete(0, END)

        answer = messagebox.askyesno(title="Conformation!", message=f"These are the details entered {data}, do you wish to continue?")

        if answer:
            confirmed()

#----------------------------------UI Setup----------------------------------#
window = Tk()
window.title("MyPASS")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

website = Label(text="Website:")
username = Label(text="Email/Username:")
password = Label(text="Password:")

website_input = Entry(width=30)
username_input = Entry(width=30)
password_input = Entry(width=30)

generate_password = Button(text="Generate Password", command=generate_password,width=30)
add = Button(text="Add", width=60, command=save_data)
search = Button(text="Find", command=find_password, width=30)


canvas.grid(row=1, column=2)
website.grid(row=2, column=1)
username.grid(row=3, column=1)
password.grid(row=4, column=1)

website_input.grid(row=2, column=2)
username_input.grid(row=3, column=2)
password_input.grid(row=4, column=2)
generate_password.grid(row=4, column=3)
add.grid(row=5, column=2, columnspan=2)
search.grid(row=2, column=3)

username_input.insert(END, "@gmail.com")
website_input.focus()

window.mainloop()
