import tkinter as tk

cal = tk.Tk()

cal.geometry("300x500")

expenses = {}
y_position = 200


def add():

    global y_position

    Expense = str(expense_entry.get())
    amount = int(Amount_entry.get())

    expenses.update({Expense: amount})

    expense_label = tk.Label(cal, text=Expense)
    expense_label.place(x=50, y=y_position)

    amount_label = tk.Label(cal, text=amount)
    amount_label.place(x=150, y=y_position)

    y_position += 30

    expense_entry.delete(0, tk.END)
    Amount_entry.delete(0, tk.END)


lb = tk.Label(
    cal,
    text="Expense Calculator"
)

lb.place(relx=0.5, y=20, anchor="center")


Expense = tk.Label(
    cal,
    text="Expense:"
)

Amount = tk.Label(
    cal,
    text="Amount:"
)

Expense.place(x=50, y=70)
Amount.place(x=48, y=90)


expense_entry = tk.Entry(cal)
Amount_entry = tk.Entry(cal)

expense_entry.place(x=120, y=70)
Amount_entry.place(x=120, y=93)


btn = tk.Button(
    cal,
    text="Add",
    command=add
)

btn.place(relx=0.5, y=150, anchor="center")


cal.mainloop()