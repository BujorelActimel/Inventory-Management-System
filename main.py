import tkinter as tk
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
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("750x600")

# Create a label for the main menu
label = tk.Label(root, text="Inventory Management System", font=("Helvetica", 16))
label.place(relx=0.5, rely=0.05, anchor="center")

# Create a function for displaying the inventory
def view_inventory():
    if len(inventory) == 0:
        messagebox.showinfo("Inventory", "The inventory is currently empty.")
    else:
        # Create a new window to display the inventory
        view_window = tk.Toplevel(root)
        view_window.title("View Inventory")
        view_window.geometry("500x500")
        
        # Create a Listbox widget to display the inventory items
        inventory_listbox = tk.Listbox(view_window)
        inventory_listbox.pack(expand=True, fill='both')
        inventory_listbox.config(selectmode="extended")
        
        # Insert the inventory items into the Listbox
        for i in inventory:
            inventory_listbox.insert(tk.END, "VIN: " + i['vin'])
            inventory_listbox.insert(tk.END, "Make and Model: " + i['make_model'])
            inventory_listbox.insert(tk.END, "Year: " + i['year'])
            inventory_listbox.insert(tk.END, "Price: " + i['price'])
            inventory_listbox.insert(tk.END, "Stock Number: " + i['stock_number'])
            inventory_listbox.insert(tk.END, "")
        scrollbar = tk.Scrollbar(view_window, orient="vertical")
        inventory_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=inventory_listbox.yview)
        scrollbar.pack(side="right", fill="y")


# Create a button for viewing the inventory
view_button = tk.Button(root, text="View Inventory", command=view_inventory)
view_button.config(width=30, height=5)
view_button.place(relx=0.2, rely=0.24, anchor="sw")

# # Create a function for adding a vehicle to the inventory
# # add_button.place(relx=0.8, rely=0.24, anchor="se")
def add_vehicle():
    # Create variables to store the input
    vin_var = tk.StringVar()
    make_model_var = tk.StringVar()
    year_var = tk.StringVar()
    price_var = tk.StringVar()
    stock_number_var = tk.StringVar()

    # Create labels and Entry widgets for the input
    vin_label = tk.Label(root, text="Enter the vehicle VIN: ")
    vin_entry = tk.Entry(root, textvariable=vin_var)

    make_model_label = tk.Label(root, text="Enter the vehicle make and model: ")
    make_model_entry = tk.Entry(root, textvariable=make_model_var)

    year_label = tk.Label(root, text="Enter the vehicle year: ")
    year_entry = tk.Entry(root, textvariable=year_var)

    price_label = tk.Label(root, text="Enter the vehicle price: ")
    price_entry = tk.Entry(root, textvariable=price_var)

    stock_number_label = tk.Label(root, text="Enter the vehicle stock number: ")
    stock_number_entry = tk.Entry(root, textvariable=stock_number_var)

    # Position the labels and the Entry widgets in the window
    vin_label.place(relx=0.3, rely=0.5, anchor="center")
    vin_entry.place(relx=0.5, rely=0.5, anchor="center")

    make_model_label.place(relx=0.3, rely=0.55, anchor="center")
    make_model_entry.place(relx=0.5, rely=0.55, anchor="center")

    year_label.place(relx=0.3, rely=0.6, anchor="center")
    year_entry.place(relx=0.5, rely=0.6, anchor="center")

    price_label.place(relx=0.3, rely=0.65, anchor="center")
    price_entry.place(relx=0.5, rely=0.65, anchor="center")

    stock_number_label.place(relx=0.3, rely=0.7, anchor="center")
    stock_number_entry.place(relx=0.5, rely=0.7, anchor="center")

    # Create a submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_vehicle(vin_var, make_model_var, year_var, price_var, stock_number_var, vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button))
    submit_button.place(relx=0.75, rely=0.6, anchor="w")

def submit_vehicle(vin_var, make_model_var, year_var, price_var, stock_number_var, vin_label, vin_entry, make_model_label, make_model_entry, year_label, year_entry, price_label, price_entry, stock_number_label, stock_number_entry, submit_button):
    vin = vin_var.get()
    make_model = make_model_var.get()
    year = year_var.get()
    # while not year.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the year.")
    #     year = year_var.get()

    price = price_var.get()
    # while not price.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the price.")
    #     price = price_var.get()

    stock_number = stock_number_var.get()
    # while not stock_number.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the stock number.")
    #     stock_number = stock_number_var.get()

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
    save_inventory(inventory, 'inventory.json')


# Create a button for adding a vehicle
add_button = tk.Button(root, text="Add Vehicle", command=add_vehicle)
add_button.config(width=30, height=5)
add_button.place(relx=0.8, rely=0.24, anchor="se")

def remove_vehicle():
    # Create a variable to store the stock_number
    stock_number_var = tk.StringVar()
    # Create a label and an Entry widget for the stock_number
    stock_number_label = tk.Label(root, text="Enter the stock number of the vehicle to be removed: ")
    stock_number_entry = tk.Entry(root, textvariable=stock_number_var)
    # Position the label and the Entry widget in the window
    stock_number_label.place(relx=0.3, rely=0.6, anchor="center")
    stock_number_entry.place(relx=0.6, rely=0.6, anchor="center")

    # Create a submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_stock_number(stock_number_var, stock_number_label, stock_number_entry, submit_button))
    submit_button.place(relx=0.75, rely=0.6, anchor="center")

def submit_stock_number(stock_number_var, stock_number_label, stock_number_entry, submit_button):
    stock_number = stock_number_var.get()
    # while not stock_number.isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the stock number.")
    #     stock_number = stock_number_var.get()

    # Search for the vehicle in the inventory
    for i in inventory:
        if i['stock_number'] == stock_number:
            inventory.remove(i)
            messagebox.showinfo("Inventory", "Vehicle removed from the inventory.")
            stock_number_label.destroy()
            stock_number_entry.destroy()
            submit_button.destroy()
            save_inventory(inventory, 'inventory.json')
            return
    messagebox.showinfo("Inventory", "Vehicle not found.")
    stock_number_label.destroy()
    stock_number_entry.destroy()
    submit_button.destroy()
    save_inventory(inventory, 'inventory.json')

# Create a button for removing a vehicle
remove_button = tk.Button(root, text="Remove Vehicle", command=remove_vehicle)
remove_button.config(width=30, height=5)
remove_button.place(relx=0.2, rely=0.4, anchor="sw")

# Create a function for searching a vehicle in the inventory
def search_vehicle():
    make_model_var = tk.StringVar()
    year_var = tk.StringVar()
    make_model_label = tk.Label(root, text="Enter the make and model of the vehicle: ")
    make_model_label.place(relx=0.5, rely=0.50, anchor="center")
    make_model_entry = tk.Entry(root, textvariable=make_model_var)
    make_model_entry.place(relx=0.5, rely=0.55, anchor="center")
    year_label = tk.Label(root, text="Enter the year of the vehicle: ")
    year_label.place(relx=0.5, rely=0.60, anchor="center")
    year_entry = tk.Entry(root, textvariable=year_var)
    year_entry.place(relx=0.5, rely=0.65, anchor="center")
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_search(make_model_var, year_var, make_model_label, year_label, make_model_entry, year_entry, submit_button))
    submit_button.place(relx=0.75, rely=0.6, anchor="center")

def submit_search(make_model_var, year_var, make_model_label, year_label, make_model_entry, year_entry, submit_button):
    make_model = make_model_var.get()
    # while not year_var.get().isnumeric():
    #     messagebox.showerror("Invalid input", "Please enter a valid number for the year.")
    #     year_var.set('')
    year = year_var.get()
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

# Create a button for searching a vehicle
search_button = tk.Button(root, text="Search Vehicle", command=search_vehicle)
search_button.config(width=30, height=5)
search_button.place(relx=0.8, rely=0.4, anchor="se")

# Create a button for exiting the program
exit_button = tk.Button(root, text="Exit", command=root.destroy)
# exit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
exit_button.config(width=20, height=5)
exit_button.place(relx=0.5, rely=0.9, anchor="s")


# Run the main loop
root.mainloop()
