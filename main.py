from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from order import Order
from database import DatabaseManager


db = DatabaseManager()

window = Tk()
window.title("FoodieExpress Order Management System")
window.geometry("550x600")
window.configure(bg="#eef2f7")
window.resizable(False, False)


# Title
Label(
    window,
    text="FoodieExpress Order Management System",
    font=("Arial", 16, "bold"),
    bg="#3f51b5",
    fg="white",
    pady=15
).pack(fill="x")


# Main Form
form = Frame(
    window,
    bg="white",
    padx=25,
    pady=20
)
form.pack(padx=30, pady=20, fill="x")


# Customer Name
Label(
    form,
    text="Customer Name",
    bg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, sticky="w", pady=8)

entry_name = Entry(form, width=32)
entry_name.grid(row=0, column=1, pady=8)


# Order Type
Label(
    form,
    text="Order Type",
    bg="white",
    font=("Arial", 10, "bold")
).grid(row=1, column=0, sticky="w", pady=8)

combo_order_type = ttk.Combobox(
    form,
    values=["Regular", "Premium", "VIP"],
    width=30,
    state="readonly"
)
combo_order_type.grid(row=1, column=1, pady=8)
combo_order_type.current(0)


# Number of Items
Label(
    form,
    text="Number of Items",
    bg="white",
    font=("Arial", 10, "bold")
).grid(row=2, column=0, sticky="w", pady=8)

entry_items = Entry(form, width=32)
entry_items.grid(row=2, column=1, pady=8)


# Price
Label(
    form,
    text="Price Per Item",
    bg="white",
    font=("Arial", 10, "bold")
).grid(row=3, column=0, sticky="w", pady=8)

entry_price = Entry(form, width=32)
entry_price.grid(row=3, column=1, pady=8)


# Distance
Label(
    form,
    text="Delivery Distance (KM)",
    bg="white",
    font=("Arial", 10, "bold")
).grid(row=4, column=0, sticky="w", pady=8)

entry_distance = Entry(form, width=32)
entry_distance.grid(row=4, column=1, pady=8)


# Discount
discount_var = IntVar()

Checkbutton(
    form,
    text="Discount Eligible",
    variable=discount_var,
    bg="white"
).grid(
    row=5,
    column=1,
    sticky="w",
    pady=8
)


# Variables
food_cost = 0
delivery_fee = 0
discount = 0
total_amount = 0


# Calculate Function
def calculate():

    global food_cost
    global delivery_fee
    global discount
    global total_amount

    try:

        name = entry_name.get()

        if name == "":
            raise ValueError("Customer name required")

        items = int(entry_items.get())
        price = float(entry_price.get())
        distance = float(entry_distance.get())

        if items <= 0:
            raise ValueError("Items must be positive")

        if price <= 0:
            raise ValueError("Price must be positive")

        if distance < 0 or distance > 20:
            raise ValueError(
                "Distance must be between 0 and 20 km"
            )

        order_type = combo_order_type.get()

        order = Order(
            name,
            order_type,
            items,
            price,
            distance
        )

        (
            food_cost,
            delivery_fee,
            discount,
            total_amount
        ) = order.calculate_total()

        result_text.delete(1.0, END)

        result_text.insert(
            END,
            f"Customer Name : {name}\n\n"
        )

        result_text.insert(
            END,
            f"Food Cost     : Rs.{food_cost:.2f}\n"
        )

        result_text.insert(
            END,
            f"Delivery Fee  : Rs.{delivery_fee:.2f}\n"
        )

        result_text.insert(
            END,
            f"Discount      : Rs.{discount:.2f}\n"
        )

        result_text.insert(
            END,
            f"Total Amount  : Rs.{total_amount:.2f}"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# Save Function
def save_order():

    try:

        db.save_order(
            entry_name.get(),
            combo_order_type.get(),
            int(entry_items.get()),
            float(entry_price.get()),
            float(entry_distance.get()),
            food_cost,
            discount,
            delivery_fee,
            total_amount
        )

        messagebox.showinfo(
            "Success",
            "Order Saved Successfully"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# Clear Function
def clear_fields():

    entry_name.delete(0, END)
    entry_items.delete(0, END)
    entry_price.delete(0, END)
    entry_distance.delete(0, END)

    result_text.delete(
        1.0,
        END
    )


# Result
result_text = Text(
    window,
    height=7,
    width=55,
    font=("Arial", 10),
    bg="white",
    fg="#333333"
)

result_text.pack(
    padx=30,
    pady=5
)


# Buttons
button_frame = Frame(
    window,
    bg="#eef2f7"
)

button_frame.pack(pady=15)


Button(
    button_frame,
    text="Calculate",
    command=calculate,
    bg="#2196F3",
    fg="white",
    width=12,
    font=("Arial", 10, "bold")
).grid(row=0, column=0, padx=5)


Button(
    button_frame,
    text="Save Order",
    command=save_order,
    bg="#4CAF50",
    fg="white",
    width=12,
    font=("Arial", 10, "bold")
).grid(row=0, column=1, padx=5)


Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#FF9800",
    fg="white",
    width=12,
    font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=5)


Button(
    button_frame,
    text="Exit",
    command=window.destroy,
    bg="#F44336",
    fg="white",
    width=12,
    font=("Arial", 10, "bold")
).grid(row=0, column=3, padx=5)


window.mainloop()