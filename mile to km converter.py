import tkinter as tk

def calculate():
    mile_value = float(my_entry.get())
    km_value  = mile_value*1.6
    second_label.config(text=f"{km_value}")

# window setting
window = tk.Tk()
# window.minsize(width=400, height=150)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

# entry
my_entry = tk.Entry(width=7)
my_entry.grid(column=1, row=0)


# label
first_label = tk.Label(text="is equal to",font=("Arial",20,"normal"))
second_label = tk.Label(text="0",font=("Arial",20,"normal"))

mile_label = tk.Label(text="Miles",font=("Arial",20,"normal"))
km_label = tk.Label(text="Km",font=("Arial",20,"normal"))

first_label.grid(column=0,row=1)
second_label.grid(column=1, row=1)
mile_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)

#button
calculate_button = tk.Button(text="Calculate",font=("Arial",20,"normal"),width=8,command=calculate)
calculate_button.grid(column=1,row=2)


window.mainloop()