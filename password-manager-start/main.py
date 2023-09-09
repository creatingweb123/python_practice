import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# # ---------------------------- SAVE PASSWORD ------------------------------- #

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '`', '~']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def save_data():
    website = entry_1.get()
    username = entry_2.get()
    password = entry_3.get()
    new_data={
         website:{
         "email":username,
         "password":password,
    }}
    if website and username and password:
        # is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?")
        # if is_ok:
            # with open("data.json","w") as f:
            #     json.dump(new_data,f,indent=4)

            # with open("data.json","r") as f:
            #     data = json.load(f)
        try:
            with open("data.json","r") as f:
                data = json.load(f)
                data.update(new_data)         
        except FileNotFoundError:  
            with open("data.json","w") as f:
                json.dump(new_data,f,indent=4) 
        else:
            with open("data.json","w") as f:
                json.dump(data,f,indent=4) 
        finally:
            entry_1.delete(0,tk.END)
            entry_3.delete(0,tk.END)


    else: 
        messagebox.showinfo(title="Wrong",message="Write every detail")

def random_password():
    entry_3.delete(0,tk.END)
    my_letter = [random.choice(letters) for _ in range(random.randint(8,9))]
    my_number = [random.choice(numbers) for _ in range(random.randint(2,4))]
    my_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]
    new_password = my_letter + my_number + my_symbol
    random.shuffle(new_password)
    
    entry_3.insert(0,string = "".join(new_password))
    pyperclip.copy("".join(new_password))

def search_json():
    website = entry_1.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website,message="There is no data about your password")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword: {password}")
            pyperclip.copy("password")
        else:
            messagebox.showinfo(title=website,message="There is no password about the website")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


password_image = tk.PhotoImage(file="/Users/user/OneDrive/바탕 화면/language/python_practice/password-manager-start/logo.png")
canvas = tk.Canvas(width=200,height=200)
canvas.create_image(100,100,image=password_image)
canvas.grid(column=1,row=0)

#label
label_1 = tk.Label(text="Website:")
label_2 = tk.Label(text="Email/Username:")
label_3 = tk.Label(text="Password:")

label_1.grid(column= 0,row=1)
label_2.grid(column= 0,row=2)
label_3.grid(column= 0,row=3)

#entry
entry_1 = tk.Entry(width=28)
entry_2 = tk.Entry(width=45)
entry_2.insert(tk.END, string="dlalsgud@gmail.com")
entry_3 = tk.Entry(width=28)

entry_1.focus()
entry_1.grid(row=1,column=1)
entry_2.grid(row=2,column=1,columnspan=2)
entry_3.grid(row=3,column=1)

#button
p_button = tk.Button(text="Generate Password",width=15,command=random_password)
search_button = tk.Button(text="search",width=15,command=search_json)
add_button = tk.Button(text="Add",width=45,command=save_data)

p_button.grid(row=3,column= 2)
search_button.grid(row=1,column= 2)
add_button.grid(column= 1,row=4,columnspan=2)


window.mainloop()
