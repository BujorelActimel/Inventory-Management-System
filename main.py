import tkinter, customtkinter as tk
from tkinter import messagebox
import json

# read the json file
with open('inventory.json', 'r') as f:
    inventory_json = f.read()

# convert the json object to a list
inventory = json.loads(inventory_json)

def save_inventory(inventory, file_name):
    with open(file_name, 'w') as f:
        json.dump(inventory, f, indent=4)

# Create the main window
root_VD = tk.CTk()
root_VD.title("Inventory Management System")
root_VD.geometry("750x600")

# Create a label for the main menu
label = tk.CTkLabel(root_VD, text="Inventory Management System", font=("Helvetica", 16))
label.place(relx=0.5, rely=0.05, anchor="center")

# Create a dark mode toggle
switch_var = tk.StringVar(value="on")

def switch_event():
    print("switch toggled, current value:", switch_var.get())
    if switch_var.get() == "on":
        tk.set_appearance_mode("dark")
    else:
        tk.set_appearance_mode("light")

switch_1 = tk.CTkSwitch(master=root_VD, text="Dark Mode", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
# switch_1.pack(padx=20, pady=10)
switch_1.place(relx=0.1, rely=0.95, anchor="center")


# Create a function for displaying the inventory
def view_inventory():
    if len(inventory) == 0:
        messagebox.showinfo("Inventory", "The inventory is currently empty.")
    else:
        # Create a new window to display the inventory
        view_window_VD = tk.CTkToplevel(root_VD)
        view_window_VD.title("View Inventory")
        view_window_VD.geometry("500x500")
        
        # Create a Listbox widget to display the inventory items
        inventory_listbox_VD = tkinter.Listbox(view_window_VD)
        inventory_listbox_VD.pack(expand=True, fill='both')
        inventory_listbox_VD.configure(selectmode="extended")
        
        # Insert the inventory items into the Listbox
        for i in inventory:
            inventory_listbox_VD.insert(tk.END, "VIN: " + i['vin'])
            inventory_listbox_VD.insert(tk.END, "Make and Model: " + i['make_model'])
            inventory_listbox_VD.insert(tk.END, "Year: " + i['year'])
            inventory_listbox_VD.insert(tk.END, "Price: " + i['price'])
            inventory_listbox_VD.insert(tk.END, "Stock Number: " + i['stock_number'])
            inventory_listbox_VD.insert(tk.END, "")
        scrollbar = tkinter.Scrollbar(view_window_VD, orient="vertical")
        inventory_listbox_VD.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=inventory_listbox_VD.yview)
        scrollbar.pack(side="right", fill="y")


# Create a button for viewing the inventory
view_button_VD = tk.CTkButton(root_VD, text="View Inventory", command=view_inventory)
view_button_VD.configure(width=160, height=60)
view_button_VD.place(relx=0.25, rely=0.24, anchor="sw")

# # Create a function for adding a vehicle to the inventory
# # add_button.place(relx=0.8, rely=0.24, anchor="se")
def add_vehicle():
    # Create variables to store the input
    vin_var_VD = tk.StringVar()
    make_model_var_VD = tk.StringVar()
    year_var_VD = tk.StringVar()
    price_var_VD = tk.StringVar()
    stock_number_var_VD = tk.StringVar()

    # Create labels and Entry widgets for the input
    vin_label = tk.CTkLabel(root_VD, text="Enter the vehicle VIN: ")
    vin_entry = tk.CTkEntry(root_VD, textvariable=vin_var_VD)

    make_model_label = tk.CTkLabel(root_VD, text="Enter the vehicle make and model: ")
    make_model_entry = tk.CTkEntry(root_VD, textvariable=make_model_var_VD)

    year_label = tk.CTkLabel(root_VD, text="Enter the vehicle year: ")
    year_entry = tk.CTkEntry(root_VD, textvariable=year_var_VD)

    price_label = tk.CTkLabel(root_VD, text="Enter the vehicle price: ")
    price_entry = tk.CTkEntry(root_VD, textvariable=price_var_VD)

    stock_number_label = tk.CTkLabel(root_VD, text="Enter the vehicle stock number: ")
    stock_number_entry = tk.CTkEntry(root_VD, textvariable=stock_number_var_VD)

    # Position the labels and the Entry widgets in the window
    vin_label.place(relx=0.3, rely=0.5, anchor="center")
    vin_entry.place(relx=0.55, rely=0.5, anchor="center")

    make_model_label.place(relx=0.3, rely=0.55, anchor="center")
    make_model_entry.place(relx=0.55, rely=0.55, anchor="center")

    year_label.place(relx=0.3, rely=0.6, anchor="center")
    year_entry.place(relx=0.55, rely=0.6, anchor="center")

    price_label.place(relx=0.3, rely=0.65, anchor="center")
    price_entry.place(relx=0.55, rely=0.65, anchor="center")

    stock_number_label.place(relx=0.3, rely=0.7, anchor="center")
    stock_number_entry.place(relx=0.55, rely=0.7, anchor="center")

    # Create a submit button
    submit_button = tk.CTkButton(root_VD, text="Submit", command=lambda: submit_vehicle(vin_var_VD, make_model_var_VD, year_var_VD, price_var_VD, stock_number_var_VD, vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button, clear_button))
    submit_button.place(relx=0.75, rely=0.6, anchor="w")

    # Create a clear window button
    clear_button = tk.CTkButton(root_VD, text="Clear", command=lambda: clear_add(vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button, clear_button))
    clear_button.place(relx=0.75, rely=0.65, anchor="w")

def submit_vehicle(vin_var_VD, make_model_var_VD, year_var_VD, price_var_VD, stock_number_var_VD, vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button, clear_button):
    vin = vin_var_VD.get()
    make_model = make_model_var_VD.get()
    year = year_var_VD.get()
    # while not year.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the year.")
    #     year = year_var_VD.get()

    price = price_var_VD.get()
    # while not price.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the price.")
    #     price = price_var_VD.get()

    stock_number = stock_number_var_VD.get()
    # while not stock_number.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the stock number.")
    #     stock_number = stock_number_var_VD.get()

    # Add the vehicle to the inventory
    inventory.append({
        'vin': vin,
        'make_model': make_model,
        'year': year,
        'price': price,
        'stock_number': stock_number
    })

    messagebox.showinfo("Inventory", "Vehicle added to the inventory.")
    vin_label.destroy()
    vin_entry.destroy()
    make_model_label.destroy()
    make_model_entry.destroy()
    year_label.destroy()
    year_entry.destroy()
    price_label.destroy()
    price_entry.destroy()
    stock_number_label.destroy()
    stock_number_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()
    save_inventory(inventory, 'inventory.json')


def clear_add(vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button, clear_button):
    vin_label.destroy()
    vin_entry.destroy()
    make_model_label.destroy()
    make_model_entry.destroy()
    year_label.destroy()
    year_entry.destroy()
    price_label.destroy()
    price_entry.destroy()
    stock_number_label.destroy()
    stock_number_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()

# Create a button for adding a vehicle
add_button = tk.CTkButton(root_VD, text="Add Vehicle", command=add_vehicle)
add_button.configure(width=160, height=60)
add_button.place(relx=0.75, rely=0.24, anchor="se")

def remove_vehicle():
    # Create a variable to store the stock_number
    stock_number_var_VD = tk.StringVar()
    # Create a label and an Entry widget for the stock_number
    stock_number_label = tk.CTkLabel(root_VD, text="Enter the stock number of the vehicle to be removed: ")
    stock_number_entry = tk.CTkEntry(root_VD, textvariable=stock_number_var_VD)
    # Position the label and the Entry widget in the window
    stock_number_label.place(relx=0.3, rely=0.625, anchor="center")
    stock_number_entry.place(relx=0.6, rely=0.625, anchor="center")

    # Create a submit button
    submit_button = tk.CTkButton(root_VD, text="Submit", command=lambda: submit_stock_number(stock_number_var_VD, stock_number_label, stock_number_entry, submit_button, clear_button))
    submit_button.place(relx=0.85, rely=0.6, anchor="center")

    # Create a clear window button
    clear_button = tk.CTkButton(root_VD, text="Clear", command=lambda: clear_remove(stock_number_label, stock_number_entry, submit_button, clear_button))
    clear_button.place(relx=0.85, rely=0.65, anchor="center")

def submit_stock_number(stock_number_var_VD, stock_number_label, stock_number_entry, submit_button, clear_button):
    stock_number = stock_number_var_VD.get()
    # while not stock_number.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the stock number.")
    #     stock_number = stock_number_var_VD.get()

    # Search for the vehicle in the inventory
    for i in inventory:
        if i['stock_number'] == stock_number:
            inventory.remove(i)
            messagebox.showinfo("Inventory", "Vehicle removed from the inventory.")
            stock_number_label.destroy()
            stock_number_entry.destroy()
            submit_button.destroy()
            clear_button.destroy()
            save_inventory(inventory, 'inventory.json')
            return
    messagebox.showinfo("Inventory", "Vehicle not found.")
    stock_number_label.destroy()
    stock_number_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()
    save_inventory(inventory, 'inventory.json')

def clear_remove(stock_number_label, stock_number_entry, submit_button, clear_button):
    stock_number_label.destroy()
    stock_number_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()

# Create a button for removing a vehicle
remove_button = tk.CTkButton(root_VD, text="Remove Vehicle", command=remove_vehicle)
remove_button.configure(width=160, height=60)
remove_button.place(relx=0.25, rely=0.4, anchor="sw")

# Create a function for searching a vehicle in the inventory
def search_vehicle():
    make_model_var_VD = tk.StringVar()
    year_var_VD = tk.StringVar()
    make_model_label = tk.CTkLabel(root_VD, text="Enter the make and model of the vehicle: ")
    make_model_label.place(relx=0.5, rely=0.50, anchor="center")
    make_model_entry = tk.CTkEntry(root_VD, textvariable=make_model_var_VD)
    make_model_entry.place(relx=0.5, rely=0.55, anchor="center")
    year_label = tk.CTkLabel(root_VD, text="Enter the year of the vehicle: ")
    year_label.place(relx=0.5, rely=0.60, anchor="center")
    year_entry = tk.CTkEntry(root_VD, textvariable=year_var_VD)
    year_entry.place(relx=0.5, rely=0.65, anchor="center")
    submit_button = tk.CTkButton(root_VD, text="Submit", command=lambda: submit_search(make_model_var_VD, year_var_VD, make_model_label, year_label, make_model_entry, year_entry, submit_button, clear_button))
    submit_button.place(relx=0.75, rely=0.57, anchor="center")
    clear_button = tk.CTkButton(root_VD, text="Clear", command=lambda: clear_search(make_model_label, year_label, make_model_entry, year_entry, submit_button, clear_button))
    clear_button.place(relx=0.75, rely=0.62, anchor="center")

def submit_search(make_model_var_VD, year_var_VD, make_model_label, year_label, make_model_entry, year_entry, submit_button, clear_button):
    make_model = make_model_var_VD.get()
    # while not year_var_VD.get().isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the year.")
    #     year_var_VD.set('')
    year = year_var_VD.get()
    found = False
    for i in inventory:
        if i['make_model'] == make_model and i['year'] == year:
            search_string = "Vehicle found.\n"
            search_string += "VIN: " + i['vin'] + "\n"
            search_string += "Make and Model: " + i['make_model'] + "\n"
            search_string += "Year: " + i['year'] + "\n"
            search_string += "Price: " + i['price'] + "\n"
            search_string += "Stock Number: " + i['stock_number'] + "\n\n"
            messagebox.showinfo("Inventory", search_string)
            found = True
    if not found:
        messagebox.showinfo("Inventory", "Vehicle not found.")
    make_model_label.destroy()
    year_label.destroy()
    make_model_entry.destroy()
    year_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()

def clear_search(make_model_label, year_label, make_model_entry, year_entry, submit_button, clear_button):
    make_model_label.destroy()
    year_label.destroy()
    make_model_entry.destroy()
    year_entry.destroy()
    submit_button.destroy()
    clear_button.destroy()

# Create a button for searching a vehicle
search_button = tk.CTkButton(root_VD, text="Search Vehicle", command=search_vehicle)
search_button.configure(width=160, height=60)
search_button.place(relx=0.75, rely=0.4, anchor="se")

# Create a button for exiting the program
exit_button = tk.CTkButton(root_VD, text="Exit", command=root_VD.destroy)
# exit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
exit_button.configure(width=160, height=60)
exit_button.place(relx=0.5, rely=0.9, anchor="s")


# Run the main loop
root_VD.mainloop()
